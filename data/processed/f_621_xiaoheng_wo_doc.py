import re
import os
import glob

def f_582(directory, word):
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
    >>> f_582('./documents', 'word')
    2
    >>> f_582('./documents', 'apple')
    3
    """
    count = 0
    pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    for filename in glob.glob(os.path.join(directory, '*.*')):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            if pattern.search(text):
                count += 1
    return count

import unittest
from pyfakefs.fake_filesystem_unittest import TestCase
class TestCases(TestCase):
    def setUp(self):
        self.setUpPyfakefs()
        self.directory = '/mnt/data/documents'
        self.fs.create_dir(self.directory)
        self.fs.create_file('/mnt/data/documents/apple.txt', contents='Apple is great.')
        self.fs.create_file('/mnt/data/documents/word.txt', contents='This file contains the word. Word is important. Word up!')
        self.fs.create_file('/mnt/data/documents/banana.txt', contents='Banana is yellow.')
        self.fs.create_file('/mnt/data/documents/orange.txt', contents='Orange is sweet.')
        self.fs.create_file('/mnt/data/documents/grape.txt', contents='I like grapes. Grapes are nice.')
    def test_1(self):
        result = f_582(self.directory, 'apple')
        self.assertEqual(result, 1) 
    def test_2(self):
        result = f_582(self.directory, 'word')
        self.assertEqual(result, 1)  # Ensuring 3 files contain the word "word" 
    def test_3(self):
        result = f_582(self.directory, 'banana')
        self.assertEqual(result, 1)  # Should be 1 file that contains "banana" multiple times
    def test_4(self):
        result = f_582(self.directory, 'orange')
        self.assertEqual(result, 1)  # 1 file contains the word "orange"
    def test_5(self):
        result = f_582(self.directory, 'grapes')
        self.assertEqual(result, 1)  # Ensuring 1 file contains the word "grape"
