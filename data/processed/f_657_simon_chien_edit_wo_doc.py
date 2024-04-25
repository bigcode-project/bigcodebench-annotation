import re
import os
import glob


def f_657(dir_path):
    """
    Search for occurrences of the word "error" in all text files within a 
    specified directory and its subdirectories.
    
    Parameters:
    dir_path (str): The path of the directory.
    
    Returns:
    dict: A dictionary with relative file paths as keys and the count of 
            occurrences of the word "error" as values.
    
    Raises:
    - ValueError: If directory in dir_path does not exist.

    Requirements:
    - re: For regex pattern matching.
    - os: For retrieving relative file paths.
    - glob: For fetching all text file paths in the directory.
    
    The function specifically searches for the word "error" in text files
    (with the extension ".txt").
    This function is NOT case sensitive, e.g. also "ERROr" will be counted.
    
    Example:
    >>> f_657("/path/to/directory")
    {'file1.txt': 2, 'subdir/file2.txt': 1}
    """

    if not os.path.isdir(dir_path):
        raise ValueError("Specified directory does not exist.")

    result = {}
    file_paths = glob.glob(f'{dir_path}/**/*.txt', recursive=True)
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
        matches = re.findall(r'\berror\b', content, re.IGNORECASE)
        # Always set the file's count in the result dictionary, even if it's 0
        result[os.path.relpath(file_path, dir_path)] = len(matches)

    return result

import unittest
import os
import shutil
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to simulate test environments
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)
    def create_file(self, sub_path, content=""):
        # Helper method to create a file with given content
        full_path = os.path.join(self.test_dir, sub_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(content)
        # Return normalized path for cross-platform compatibility
        return os.path.normpath(sub_path)
    def test_non_existent(self):
        # Expect ValueError for non-existent directory
        with self.assertRaises(ValueError):
            f_657(os.path.join(self.test_dir, "non_existent"))
    def test_empty_folder(self):
        # Test empty directory
        result = f_657(self.test_dir)
        self.assertEqual(result, {})
    def test_files_with_errors(self):
        # Files with varying counts of 'error'
        files = {
            "1.txt": "error\nERROR\nErrOr",
            "subfolder1/2.txt": "",
            "subfolder2/3.txt": "error\nerror error"
        }
        expected = {
            os.path.normpath("1.txt"): 3,
            os.path.normpath("subfolder1/2.txt"): 0,
            os.path.normpath("subfolder2/3.txt"): 3
        }
        for path, content in files.items():
            self.create_file(path, content)
        result = f_657(self.test_dir)
        self.assertEqual(result, expected)
    def test_case_sensitive_and_realistic_text(self):
        # More complex scenarios, including nested directories
        file_path = self.create_file('nested/folder1/folder2/error_log.txt', 'Error\nerror\nERROR')
        expected = {file_path: 3}
        result = f_657(self.test_dir)
        self.assertEqual(result, expected)
    def test_exact_word_matching(self):
        # Ensure only the exact word 'error' is counted and ignore similar words like 'errors'
        files = {
            "file1.txt": "error error error",  # Should count 3 times
            "subdir/file2.txt": "errors error erro errors",  # Should count 1 time
            "subdir2/nested/file3.txt": "an error occurred",  # Should count 1 time
            "subdir3/file4.txt": "no errors here",  # Should count 0 times
            "subdir3/file5.txt": "Error and ERROR and error"  # Should count 3 times, case insensitive
        }
        expected = {
            os.path.normpath("file1.txt"): 3,
            os.path.normpath("subdir/file2.txt"): 1,
            os.path.normpath("subdir2/nested/file3.txt"): 1,
            os.path.normpath("subdir3/file4.txt"): 0,
            os.path.normpath("subdir3/file5.txt"): 3
        }
        for path, content in files.items():
            self.create_file(path, content)
        result = f_657(self.test_dir)
        self.assertEqual(result, expected)
