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

    >>> f_657("/path/to/directory")
    {'test.txt': 245, 'subdir/test2.txt': 0, 'subdir/sf/test3.txt': 1}
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


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    
    def test_non_existent(self):
        'non existent folder'
        self.assertRaises(
            Exception, f_657, os.path.join("f_657_data_simon", "non_existent")
            )

    def test_case_1(self):
        'empty folder'
        result = f_657(os.path.join("f_657_data_simon", "test_case_1"))
        self.assertEqual(result, {}, "Test Case 1 Failed")
    
    def test_case_2(self):
        'test data 2'
        result = f_657(os.path.join("f_657_data_simon", "test_case_2"))
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = os.path.join('subfolder1', '3.txt')
        expected = {path1: 2, path2: 0, path3: 3}

        self.assertEqual(result, expected, "Test Case 2 Failed")
    
    def test_case_3(self):
        'nested subfolders'
        result = f_657(os.path.join("f_657_data_simon", "test_case_3"))
        path = os.path.join('folder', 'folder', 'folder', 'test.txt')
        expected = {path: 1}
        self.assertEqual(result, expected, "Test Case 3 Failed")
    
    def test_case_4(self):
        'realistic text with error sprinkled in'
        result = f_657(os.path.join("f_657_data_simon", "test_case_4"))
        path1 = os.path.join('sf', 'file2.txt')
        path2 = os.path.join('sf', 'error.txt')

        expected = {"file1.txt": 2, path1: 0, path2: 6}
        self.assertEqual(result, expected, "Test Case 4 Failed")
    
    def test_case_5(self):
        'txt file containes a lot of error'
        result = f_657(os.path.join("f_657_data_simon", "test_case_5"))
        expected = {"many_error.txt": 2650}
        self.assertEqual(result, expected, "Test Case 5 Failed")

    def test_case_6(self):
        'other file extensions'
        result = f_657(os.path.join("f_657_data_simon", "test_case_6"))
        expected = {"1.txt": 0}
        self.assertEqual(result, expected, "Test Case 5 Failed")



if __name__ == "__main__":
    run_tests()
