import re
import os
from pathlib import Path
import glob


def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    """
    Extracts matches from all text files in a specified directory based on a regular expression pattern. 
    It captures whatever is between parentheses as a single match, and any character outside the parentheses 
    as individual matches in the string.

    Parameters:
    - directory_path (str): The path to the directory containing the text files.
    - regex_pattern (str): The regular expression pattern to use for matching. Defaults to REGEX_PATTERN.

    Returns:
    - dict: A dictionary where keys are file names (without path) and values are lists of matches extracted from the files.

    Requirements:
    - Utilizes libraries: re, os, pathlib.Path, and glob.glob

    Example:
    >>> matches = task_func('/path/to/directory') # Test with fictional directory path
    >>> print(matches)
    {}
    """
    FILE_PATTERN = '*.txt'
    match_dict = {}
    file_paths = glob.glob(os.path.join(directory_path, FILE_PATTERN))
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            matches = re.findall(regex_pattern, content)
            match_dict[Path(file_path).name] = matches
    return match_dict

import unittest
import shutil
import doctest
import tempfile
class TestCases(unittest.TestCase):
    regex_pattern = r'\(.+?\)'
    def setUp(self) -> None:
        self.base_tmp_dir = tempfile.mkdtemp()
        self.temp_dir = f"{self.base_tmp_dir}/test"
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)
    def tearDown(self) -> None:
        if os.path.exists(self.base_tmp_dir):
            shutil.rmtree(self.base_tmp_dir)
    def test_case_1(self):
        # Test with the first sample directory
        input_text = {
            "file1.txt": ['world', 'H', 'e', 'l', 'l', 'o', ' ', '!', ' '],
            "file2.txt": ['Greetings', ' ', 'e', 'v', 'e', 'r', 'y', 'o', 'n', 'e', '.'],
            "file3.txt": ['test', 'S', 'i', 'm', 'p', 'l', 'e', ' ', ' ', 'f', 'i', 'l', 'e', '.']
        }
        expected = {
            "file1.txt": [],
            "file2.txt": [],
            "file3.txt": []
        }
        for file_name, content in input_text.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(''.join(content))
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, expected)
    def test_case_2(self):
        # Test with an empty directory
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, {})
    def test_case_3(self):
        # Test with a directory containing a text file with no matches
        with open(os.path.join(self.temp_dir, "file4.txt"), "w") as file:
            file.write("No matches here!")
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, {'file4.txt': []})
    
    def test_case_4(self):
        # Test with a directory containing a text file with multiple matches
        with open(os.path.join(self.temp_dir, "file5.txt"), "w") as file:
            file.write("(A)(B)(C)(D)")
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, {"file5.txt": ['(A)', '(B)', '(C)', '(D)']})
    
    def test_case_5(self):
        # Test with a directory containing a text file with special characters
        with open(os.path.join(self.temp_dir, "file6.txt"), "w") as file:
            file.write("Special (characters) like #, $, %")
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, {"file6.txt": ['(characters)']})
