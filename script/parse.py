import os
import sys
import re
import ast
import json
import zipfile
import base64
import shutil
from glob import glob
from pprint import pprint
from tqdm import tqdm

def extract_apis(code):
    tree = ast.parse(code)
    api_list = []
    imported_modules = {}

    class ApiExtractor(ast.NodeVisitor):
        def visit_Import(self, node):
            for alias in node.names:
                module_name = alias.name
                alias_name = alias.asname or alias.name
                imported_modules[alias_name] = module_name
                # Add submodule and top-level module
                submodule_parts = module_name.split('.')
                for i in range(1, len(submodule_parts) + 1):
                    submodule = '.'.join(submodule_parts[:i])
                    imported_modules[submodule] = submodule
            self.generic_visit(node)

        def visit_ImportFrom(self, node):
            module = node.module
            if module:
                for alias in node.names:
                    full_name = f'{module}.{alias.name}'
                    alias_name = alias.asname or alias.name
                    imported_modules[alias_name] = full_name
            self.generic_visit(node)

        def visit_Attribute(self, node):
            if isinstance(node.value, ast.Name) and node.value.id in imported_modules:
                base_module = imported_modules[node.value.id]
                api_call = f"{base_module}.{node.attr}"
                if api_call not in api_list:
                    api_list.append(api_call)
            self.generic_visit(node)

        def visit_Call(self, node):
            if isinstance(node.func, ast.Attribute):
                attr_parts = []
                current = node.func
                while isinstance(current, ast.Attribute):
                    attr_parts.append(current.attr)
                    current = current.value

                if isinstance(current, ast.Name) and current.id in imported_modules:
                    base_module = imported_modules[current.id]
                    attr_parts.append(base_module)
                    attr_parts.reverse()
                    api_call = '.'.join(attr_parts)
                    if api_call not in api_list:
                        api_list.append(api_call)
            elif isinstance(node.func, ast.Name) and node.func.id in imported_modules:
                api_call = imported_modules[node.func.id]
                if api_call not in api_list:
                    api_list.append(api_call)

            self.generic_visit(node)

    ApiExtractor().visit(tree)
    return list(set(api_list))  # Remove duplicates

def remove_trailing_comments(text):
    """
    Removes all trailing lines starting with '#' from the given text.

    Parameters:
    text (str): The text from which to remove trailing comment lines.

    Returns:
    str: The text with trailing comments removed.
    """
    lines = text.splitlines()  # Split the text into individual lines
    # Find the last non-comment line from the end; i.e., the first line from the end that doesn't start with '#'
    for i in range(len(lines) - 1, -1, -1):
        if not lines[i].strip().startswith('#'):
            break  # Found the last non-comment line
    # Return the text up to and including the last non-comment line, joined back into a single string
    return '\n'.join(lines[:i+1])

def extract_test(file_contents, function_name):
    """
    Extracts the content after a specified function in a given Python script using the ast module,
    excludes a function named 'run_tests' if it exists, and excludes content after "__main__".

    Parameters:
    file_contents (str): The contents of the Python script.
    function_name (str): The name of the function after which the content is to be extracted.

    Returns:
    str: The content of the script after the specified function excluding 'run_tests' function
         and anything after "__main__", or a message if the main function is not found.
    """
    try:
        # Parsing the file contents into an AST
        tree = ast.parse(file_contents)

        # Finding the end line number of the specified function and '__main__'
        function_end_line = None
        main_block_start_line = None

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == function_name:
                function_end_line = node.end_lineno  # End line of the target function
            if isinstance(node, ast.If):
                # Check if the 'if' condition is exactly "__name__ == '__main__'"
                if (isinstance(node.test, ast.Compare) and
                    isinstance(node.test.left, ast.Name) and node.test.left.id == '__name__' and
                    isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == '__main__'):
                    main_block_start_line = node.lineno - 1  # Start line of the '__main__' block
                    break

        if function_end_line is not None:
            # Splitting the file contents into lines
            lines = file_contents.splitlines()

            # Determine end line for content extraction
            if main_block_start_line is not None and main_block_start_line < len(lines):
                function_end_end_line = main_block_start_line
            else:
                function_end_end_line = len(lines)

            # Initial content extraction
            content_after_function = lines[function_end_line:function_end_end_line]

            # Removing 'run_tests' function if present
            run_tests_tree = ast.parse("\n".join(content_after_function))
            filtered_lines = content_after_function[:]
            
            for node in ast.walk(run_tests_tree):
                if isinstance(node, ast.FunctionDef) and node.name == "run_tests":
                    start = node.lineno - 1  # Adjust index to be 0-based
                    end = node.end_lineno
                    for i in range(start, end):
                        filtered_lines[i] = ""  # Clearing out lines of 'run_tests'
            content = "\n".join([line for line in filtered_lines if line])
            
            return remove_trailing_comments("\n".join(line for line in content.split("\n") if "run_tests" not in line))

        else:
            return "Function not found in the script."
    except Exception as e:
        return f"Error processing the script: {e}"


def extract_content(file_path):
    data = {}
    with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('def'):
                    # Extract the function name
                    start = line.find('def') + 4  # 'def ' has 4 characters
                    end = line.find('(')
                    if end != -1:
                        function_name = line[start:end].strip()
                        if function_name.startswith("f_"):
                            data["task_id"] = function_name
                            break
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip("\n").replace("AxesSubplot", "Axes").replace("matplotlib.axes._subplots", "matplotlib.axes._axes")

        # Extracting the docstring if present
        docstring_start = content.find('"""')
        docstring_end = content.find('"""', docstring_start + 3)
        if docstring_start == -1 and docstring_end == -1:
            docstring_start = content.find("'''")
            docstring_end = content.find("'''", docstring_start + 3)
        data["prompt"] = content[:docstring_end + 3]
        tree = ast.parse(content)
        function_end_line = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == function_name:
                function_end_line = node.end_lineno
                break

        if function_end_line is not None:
            lines = content.splitlines()
            function_start_line = content[:docstring_end + 3].count('\n') + 1
            data["canonical_solution"] = "\n".join(lines[function_start_line:function_end_line])
        else:
            data["canonical_solution"] = ""
    data["test"] = extract_test(content,function_name).strip()
    data["apis"] = extract_apis(data["prompt"] + "\n" + data["canonical_solution"])
    data["libs"] = list(set([api.split(".")[0] for api in data["apis"]]))
    
    docs = re.search(r'\"\"\"(.*?)\"\"\"', data["prompt"], re.DOTALL)
    if not docs:
        docs = re.search(r"'''(.*?)'''", data["prompt"], re.DOTALL)
    data['doc'] = parse_docstring(docs.group(1))
    return data

def count_return_values(function_code):
    # Parse the function code into an AST
    parsed_code = ast.parse(function_code)
    
    # Function to recursively find return statements
    def find_returns(node):
        if isinstance(node, ast.Return):
            # Count the number of items in a tuple return, or 1 for a single return
            return [len(node.value.elts) if isinstance(node.value, ast.Tuple) else 1] if node.value else [0]
        elif hasattr(node, 'body') and isinstance(node.body, list):
            # Check body of node if it's a list (e.g., function or if statement)
            return [count for child in node.body for count in find_returns(child)]
        return []

    # Analyze the first function definition found in the AST
    for node in ast.walk(parsed_code):
        if isinstance(node, ast.FunctionDef):
            return find_returns(node)

    return []

def parse_docstring(docstring):
    sections = {
        'description': [],
        'note': [],
        'params': [],
        'returns': [],
        'reqs': [],
        'raises': [],
        'example': []
    }
    # Split the docstring into lines and strip whitespace
    lines = [line.strip() for line in docstring.strip().split('\n')]

    current_section = None
    replace_word = ""
    
    for line in lines:
        if line.startswith('Note:'):
            current_section = 'note'
            replace_word = 'Note:'
        elif line.startswith('Parameters:'):
            current_section = 'params'
            replace_word = 'Parameters:'
        elif line.startswith('Returns:'):
            current_section = 'returns'
            replace_word = 'Returns:'
        elif line.startswith('Requirements:'):
            current_section = 'reqs'
            replace_word = 'Requirements:'
        elif line.startswith('Raises:'):
            current_section = 'raises'
            replace_word = 'Raises:'
        elif line.startswith('Example:') or line.startswith('Examples:'):
            current_section = 'example'
            replace_word = 'Example:'
        elif line and not current_section:
            current_section = 'description'
        elif not line:
            current_section = None

        if current_section and current_section != 'description':
            reformat_line = line.replace(replace_word, '')
            if reformat_line:
                if current_section != 'example':
                    reformat_line = reformat_line.strip('- ')
                sections[current_section].append(reformat_line)
        elif current_section and current_section == 'description':
            sections[current_section].append(line)

    # Cleaning empty entries
    for key in sections:
        sections[key] = [item for item in sections[key] if item]

    return sections

def reconstruct_problem(data):
    return data["prompt"] + "\n" + data["canonical_solution"] + "\n\n" + data["test"] + "\n"

def check_test_wo_doc(data):
    "Check if the problem is related to file system, network requests and database"
    
    if any([lib in data["libs"] for lib in ["shutil", "requests", "django", "sqlite3", "datetime", "flask", "turtle"]]):
        return True
    elif any([kw in data["prompt"] for kw in ["url"]]):
        return True
    elif any([api in data["apis"] for api in ["os.path"]]):
        return True
    # check any file suffixes are inside data["prompt"]
    elif any([suffix in data["prompt"] for suffix in [".txt", ".csv", ".json", ".xml", ".html", ".log", ".zip", ".tar", ".gz", ".pdf", ".png"]]):
        return True
    # check path like patterns are inside data["prompt"]
    elif any([re.search(r"[\w\-.]+\/[\w\-.]+", data["prompt"])]):
        return True
    else:
        return False

def validate_lib_num(data):
    if len(data["libs"]) < 2:
        return False
    return True

def validate_doc_example(data):
    if not data["doc"]["example"]:
        return False
    return True

if __name__ == "__main__":
    shutil.rmtree("data/processed", ignore_errors=True)
    os.makedirs("data/processed")
    with open("data/open-eval.jsonl", "w") as f:
        for file in tqdm(glob("data/clean/*.py")):
            data = extract_content(file)
            # assert validate_lib_num(data), f"Less than 2 libraries are used in {file.replace('clean/', 'raw/')}"
            # assert validate_doc_example(data), f"Example is missing in {file.replace('clean/', 'raw/')}"
            if not validate_lib_num(data):
                print(file.replace('clean/', 'raw/'), "Less than 2 libraries are used")
            if not validate_doc_example(data):
                print(file.replace('clean/', 'raw/'), "Example is missing")
            f.write(json.dumps(data) + "\n")
            file_name = file.split("/")[-1].split(".")[0]
            file_name = file_name + "_wo_doc" if check_test_wo_doc(data) else file_name + "_w_doc"
            with open(f"data/processed/{file_name}.py", "w") as f2:
                f2.write(reconstruct_problem(data))