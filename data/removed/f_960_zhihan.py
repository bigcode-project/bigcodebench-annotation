import os
import sys
import json
import re

def f_960(file_path='File.txt'):
    """
    Converts a text file to a JSON string format. This function fetches each line from the file, 
    splits it into words using regex, and stores the words in a list. The list is then converted 
    to a JSON string format.
    
    Parameters:
    - file_path (str): The path to the text file. Defaults to 'File.txt'.
    
    Returns:
    - str: The JSON string in the format '[["word1", "word2", ...], ...]'. 
           Returns an error message if the file is not found.
    
    Required Libraries:
    - os
    - json
    - re
    
    Example:
    >>> f_960('sample.txt')
    '[["This", "is", "a", "sample"], ["Another", "line"]]'
    """
    if not os.path.isfile(file_path):
        return f"Error: File not found: {file_path}"

    lines = []

    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\\b\\w+\\b', line)
            lines.append(words)

    return json.dumps(lines)

import unittest
import json

class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_960('/mnt/data/sample1.txt')
        expected = '[["This", "is", "a", "sample", "line"], ["Another", "sample", "line"], ["Third", "line", "in", "the", "file"]]'
        self.assertEqual(result, expected)

    def test_case_2(self):
        result = f_960('/mnt/data/sample2.txt')
        expected = '[["Just", "one", "line", "in", "this", "file"]]'
        self.assertEqual(result, expected)

    def test_case_3(self):
        result = f_960('/mnt/data/sample3.txt')
        expected = '[["Mixed", "numbers", "123", "and", "words"], ["Special", "characters", "are", "not", "words"]]'
        self.assertEqual(result, expected)

    def test_case_4(self):
        result = f_960('non_existent_file.txt')
        expected = "Error: File not found: non_existent_file.txt"
        self.assertEqual(result, expected)

    def test_case_5(self):
        result = f_960('/mnt/data/sample1.txt')
        self.assertTrue(isinstance(result, str))
        json_output = json.loads(result)
        self.assertTrue(isinstance(json_output, list))

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()