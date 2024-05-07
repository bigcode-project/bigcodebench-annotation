import os
import re
from collections import Counter

def f_958(file_path):
    """
    Counting the word frequency from a given text file. This function retrieves each line from the file, splits it into words and counts the frequency of each word. Words are normalized to lowercase letters.
    
    Parameters:
    file_path (str): The path to the text file.
    
    Returns:
    dict or str: A dictionary with words as keys and their frequencies as values. If the file is not found, returns an error message.
    
    Requirements:
    - os
    - re
    - collections.Counter
    
    Example:
    >>> f_958('File.txt')
    {'hello': 1, 'world': 1}
    """
    if not os.path.isfile(file_path):
        return f"File not found: {file_path}"

    word_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            word_counter.update(words)

    return dict(word_counter)

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_958('/mnt/data/File1.txt')
        expected = {'hello': 2, 'world': 2, 'is': 1, 'beautiful': 1, 'again': 1}
        self.assertEqual(result, expected)

    def test_case_2(self):
        result = f_958('/mnt/data/File2.txt')
        expected = {'apple': 2, 'banana': 3, 'orange': 2}
        self.assertEqual(result, expected)

    def test_case_3(self):
        result = f_958('/mnt/data/File3.txt')
        expected = {}
        self.assertEqual(result, expected)

    def test_case_4(self):
        result = f_958('/mnt/data/File4.txt')
        expected = {'one': 4, 'two': 3, 'three': 2, 'four': 2}
        self.assertEqual(result, expected)

    def test_case_5(self):
        result = f_958('/mnt/data/File_Not_Exists.txt')
        expected = "File not found: /mnt/data/File_Not_Exists.txt"
        self.assertEqual(result, expected)
if __name__ == "__main__":
    run_tests()