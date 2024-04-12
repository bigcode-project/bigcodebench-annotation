import urllib.request
import os
import mmap
import re

# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'

def f_624(url):
    """
    Download a text file from the specified url and search for occurrences of the word "ERROR."

    Parameters:
    - url (str): The url of the text file to be downloaded.

    Returns:
    - occurrences (int): The number of occurrences of the word 'ERROR'.

    Requirements:
    - urllib
    - os
    - mmap
    - re

    Example:
    >>> f_624('http://example.com/log.txt')
    5 # Assuming there are 5 occurrences of 'ERROR' in the file
    """
    urllib.request.urlretrieve(url, TARGET_FILE)

    with open(TARGET_FILE, 'r') as f:
        data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        occurrences = len(re.findall(SEARCH_PATTERN, data))

    os.remove(TARGET_FILE)

    return occurrences

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_sample1(self):
        url = "file:///mnt/data/f_624_data_xiaoheng/sample1.txt"
        result = f_624(url)
        self.assertEqual(result, 2, "Expected 2 occurrences of 'ERROR'")
    
    def test_sample2(self):
        url = "file:///mnt/data/f_624_data_xiaoheng/sample2.txt"
        result = f_624(url)
        self.assertEqual(result, 0, "Expected 0 occurrences of 'ERROR'")
    
    def test_sample3(self):
        url = "file:///mnt/data/f_624_data_xiaoheng/sample3.txt"
        result = f_624(url)
        self.assertEqual(result, 5, "Expected 5 occurrences of 'ERROR'")

    def test_mixed_case_errors(self):
        url = 'file:///mnt/data/f_624_data_xiaoheng/mixed_case_errors.txt'
        result = f_624(url)
        self.assertEqual(result, 2, "Expected 2 occurrences of 'ERROR'")
    
    def test_large_file(self):
        url = 'file:///mnt/data/f_624_data_xiaoheng/large_file.txt'
        result = f_624(url)
        self.assertEqual(result, 5001, "Expected 5001 occurrences of 'ERROR'")
        
if __name__ == "__main__":
    run_tests()