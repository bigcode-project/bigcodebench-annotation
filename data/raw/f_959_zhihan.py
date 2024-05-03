import glob
import re
from collections import Counter

# Constants
FILE_PATH = '*.txt'

def f_959(file_path=FILE_PATH):
    """
    Count the word frequency from all the text files in a directory. This function retrieves each line from each file, splits it into words and counts the frequency of each word. The words are normalized to lowercase letters.
    
    Parameters:
    file_path (str): The path to the text files. Defaults to '*.txt'.
    
    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    
    Requirements:
    - os
    - glob
    - re
    - collections.Counter
    
    Example:
    
    Example:
    >>> f_959('path_to_text_files/*.txt')
    {'hello': 5, 'world': 3, 'goodbye': 2}
    >>> f_959('another_path/*.txt')
    {'sample': 4, 'test': 6}

    """
    word_counter = Counter()

    for file in glob.glob(file_path):
        with open(file, 'r') as f:
            for line in f:
                words = re.findall(r'\b\w+\b', line.lower())
                word_counter.update(words)

    return dict(word_counter)

import unittest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: Testing with sample1.txt
        result = f_959('/mnt/data/sample1.txt')
        expected = {'hello': 2, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1, 'file': 1, 'again': 1, 'testing': 1, 'word': 1, 'frequencies': 1}
        self.assertEqual(result, expected)

    def test_case_2(self):
        # Input 2: Testing with sample2.txt
        result = f_959('/mnt/data/sample2.txt')
        expected = {'another': 1, 'text': 1, 'file': 1, 'for': 1, 'testing': 1, 'word': 1, 'frequencies': 1, 'are': 1, 'fun': 1, 'to': 1, 'compute': 1, 'hello': 1, 'world': 1}
        self.assertEqual(result, expected)

    def test_case_3(self):
        # Input 3: Testing with both files using wildcard
        result = f_959('/mnt/data/sample*.txt')
        expected = {'hello': 3, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 2, 'file': 2, 'again': 1, 'testing': 2, 'word': 2, 'frequencies': 2, 'another': 1, 'for': 1, 'are': 1, 'fun': 1, 'to': 1, 'compute': 1}
        self.assertEqual(result, expected)

    def test_case_4(self):
        # Input 4: Testing with no matching files
        result = f_959('/mnt/data/non_existent*.txt')
        expected = {}
        self.assertEqual(result, expected)

    def test_case_5(self):
        # Input 5: Testing with default parameter (no files match the default pattern in this environment)
        result = f_959()
        expected = {}
        self.assertEqual(result, expected)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()