import re
import os
import glob

def f_621(directory, word):
    """
    Count the number of files in a directory that contain a specific word.
    
    Parameters:
    - directory (str): The directory path.
    - word (str): The word to search for.
    
    Returns:
    - count (int): The number of files that contain the given word.
    
    Requirements:
    - re
    - os
    - glob
    
    Example:
    >>> f_621('./documents', 'word')
    2
    >>> f_621('./documents', 'apple')
    3
    """
    count = 0
    for filename in glob.glob(os.path.join(directory, '*')):
        with open(filename, 'r') as f:
            text = f.read()
            if re.search(r'\b' + word + r'\b', text):
                count += 1
    return count

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_1(self):
        result = f_621('/mnt/data/documents', 'apple')
        self.assertEqual(result, 5)  # 5 files contain the word "apple"

    def test_2(self):
        result = f_621('/mnt/data/documents', 'word')
        self.assertEqual(result, 3)  # 3 files contain the word "word"

    def test_3(self):
        result = f_621('/mnt/data/documents', 'banana')
        self.assertEqual(result, 3)  # 3 files contain the word "banana"

    def test_4(self):
        result = f_621('/mnt/data/documents', 'orange')
        self.assertEqual(result, 1)  # 1 file contains the word "orange"

    def test_5(self):
        result = f_621('/mnt/data/documents', 'grape')
        self.assertEqual(result, 1)  # 1 file contains the word "grape"
        
if __name__ == "__main__":
    run_tests()