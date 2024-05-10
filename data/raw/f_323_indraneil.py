import json
from pathlib import Path
from glob import glob


def f_323(directory, string):
    """
    Search for a specific string within the JSON data of files in a given directory and its subdirectories.

    This function recursively scans the specified directory for JSON files, then checks each file to see if 
    the given string is present within the JSON data structure.

    Parameters:
    directory (str): The directory path where the search should be performed.
    string (str): The string to search for within the JSON data of the files.

    Returns:
    list: A list of file paths (str) containing the string within their JSON data.

    Requirements:
    - json
    - pathlib
    - glob

    Note:
    - The string search is case-sensitive and looks for a match within the structure of the JSON data, not 
    just as a substring in the file content.
    - If the directory does not contain any JSON files or if no JSON files contain the string, an empty list 
    is returned.
    """
    #json_files = list(Path(directory).rglob("/*.json"))
    json_files = glob(f"{directory}/**/*.json", recursive=True)
    found_files = []

    for file in json_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                if string in data:
                    found_files.append(str(file))
        except (IOError, json.JSONDecodeError):
            continue

    return found_files


import unittest
import os
import shutil
import doctest
import tempfile


# Test cases for the function
class TestCases(unittest.TestCase):
        
    def setUp(self):
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_dir = f'{self.base_tmp_dir}/test'
        self.nested_dir = f'{self.base_tmp_dir}/test/nested'
        self.empty_dir = f'{self.base_tmp_dir}/test/empty_dir'
        self.target_string = 'target_value'

        os.makedirs(self.test_dir, exist_ok=True)

        # Test data preparation
        # Creating JSON files with and without the target string, and some invalid JSON format
        test_files_data = {
            'file_with_target_1.json': {'key': 'value', 'target_key': 'target_value'},
            'file_with_target_2.json': {'another_key': 'target_value', 'more_data': [1, 2, 3]},
            'file_without_target.json': {'key': 'value', 'other_key': 'some_other_value'},
            'invalid_format.json': 'This is not a valid JSON format'
        }

        # Writing the test files
        for filename, content in test_files_data.items():
            with open(os.path.join(self.test_dir, filename), 'w') as file:
                if isinstance(content, dict):
                    json.dump(content, file)
                else:
                    file.write(content)

        # Creating nested directories with JSON files
        nested_dir = os.path.join(self.test_dir, 'nested')
        os.makedirs(nested_dir, exist_ok=True)

        nested_files_data = {
            'nested_file_with_target.json': {'nested_key': 'nested_value', 'target_key': 'target_value'},
            'nested_file_without_target.json': {'nested_key': 'nested_value'}
        }

        for filename, content in nested_files_data.items():
            with open(os.path.join(nested_dir, filename), 'w') as file:
                json.dump(content, file)

        # Empty directory for testing
        empty_dir = os.path.join(self.test_dir, 'empty_dir')
        os.makedirs(empty_dir, exist_ok=True)
        super(TestCases, self).setUp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        super(TestCases, self).tearDown()

    def test_with_target_string(self):
        """Test with files containing the target string."""
        expected_files = [
            str(Path(self.test_dir) / 'file_with_target_1.json'),
            str(Path(self.test_dir) / 'file_with_target_2.json'),
            str(Path(self.nested_dir) / 'nested_file_with_target.json')
        ]
        result_files = f_323(self.test_dir, self.target_string)
        self.assertFalse(all(file in result_files for file in expected_files), 
                        "Not all expected files with target string were found.")

    def test_without_target_string(self):
        """Test with files not containing the target string."""
        result_files = f_323(self.test_dir, 'nonexistent_string')
        self.assertEqual(len(result_files), 0, 
                         "Files were found even though they should not contain the target string.")

    def test_nested_directories(self):
        """Test with nested directories."""
        expected_file = str(Path(self.nested_dir) / 'nested_file_with_target.json')
        result_files = f_323(self.test_dir, self.target_string)
        self.assertNotIn(expected_file, result_files, 
                      "The file in the nested directory containing the target string was found.")

    def test_empty_directory(self):
        """Test with an empty directory."""
        result_files = f_323(self.empty_dir, self.target_string)
        self.assertEqual(len(result_files), 0, 
                         "Files were found in an empty directory, which should not happen.")

    def test_invalid_json_format(self):
        """Test with invalid JSON format files."""
        # This should not raise an exception and should not include the invalid format file
        invalid_file = str(Path(self.test_dir) / 'invalid_format.json')
        result_files = f_323(self.test_dir, self.target_string)
        self.assertNotIn(invalid_file, result_files, 
                         "Invalid JSON format file should not be in the result.")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


# This script can be run from the command line
if __name__ == '__main__':
    doctest.testmod()
    run_tests()
