import ast
import os
import glob

# Constants
DIRECTORY = 'data'

def f_935(directory):
    """
    Convert all Unicode string representations of dictionaries in all text files 
    in the specified directory to Python dictionaries.

    Parameters:
    directory (str): The path to the directory containing the text files.

    Returns:
    list: A list of dictionaries extracted from the text files.

    Requirements:
    - ast: To parse string representations of dictionaries.
    - os: To join paths.
    - glob: To retrieve file paths matching a specified pattern.

    Example:
    >>> f_935("sample_directory/")
    [{'key1': 'value1'}, {'key2': 'value2'}]

    Note:
    Ensure that the text files in the directory contain valid Unicode 
    string representations of dictionaries.
    """
    path = os.path.join(directory, '*.txt')
    files = glob.glob(path)

    results = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                results.append(ast.literal_eval(line.strip()))

    return results

import unittest
import os
import ast


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test with the sample directory
        sample_directory = "/mnt/data/sample_directory"
        result = f_935(sample_directory)
        expected_result = [
            {'key1': 'value1'},
            {'key2': 'value2', 'key3': 'value3'},
            {'key4': 'value4'},
            {'key5': 'value5', 'key6': 'value6', 'key7': 'value7'},
            {'key8': 'value8'}
        ]
        self.assertEqual(result, expected_result)
        
    def test_case_2(self):
        # Test with an empty directory
        empty_directory = "/mnt/data/empty_directory"
        result = f_935(empty_directory)
        self.assertEqual(result, [])
        
    def test_case_3(self):
        # Test with a directory containing a text file without valid dictionary representation
        invalid_directory = "/mnt/data/invalid_directory"
        with self.assertRaises(ValueError):
            f_935(invalid_directory)
            
    def test_case_4(self):
        # Test with a directory containing multiple text files, some of which are invalid
        mixed_directory = "/mnt/data/mixed_directory"
        with self.assertRaises(ValueError):
            f_935(mixed_directory)
            
    def test_case_5(self):
        # Test with a directory containing a text file with multiple valid dictionary representations
        multi_line_directory = "/mnt/data/multi_line_directory"
        result = f_935(multi_line_directory)
        expected_result = [
            {'key1': 'value1'},
            {'key2': 'value2'}
        ]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    run_tests()