import urllib.request
import os
import re

# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'

def task_func(url):
    """
    Download a text file from the specified url and search for occurrences of the word "ERROR."

    Parameters:
    - url (str): The url of the text file to be downloaded.

    Returns:
    - occurrences (int): The number of occurrences of the word 'ERROR'.

    Requirements:
    - urllib
    - os
    - re

    Example:
    >>> task_func('http://example.com/log.txt')
    5 # Assuming there are 5 occurrences of 'ERROR' in the file
    """

    TARGET_FILE = 'downloaded_file.txt'
    SEARCH_PATTERN = r'\bERROR\b'
    urllib.request.urlretrieve(url, TARGET_FILE)
    with open(TARGET_FILE, 'r') as f:
        data = f.read()
    occurrences = len(re.findall(SEARCH_PATTERN, data))
    os.remove(TARGET_FILE)
    return occurrences

import unittest
from unittest.mock import patch, mock_open
class TestCases(unittest.TestCase):
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open, read_data='ERROR\nOK\nERROR')
    @patch('os.remove')
    def test_sample1(self, mock_remove, mock_file, mock_urlretrieve):
        mock_urlretrieve.return_value = ('mock/path/to/file.txt', {'mock': 'headers'})
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 2)  # Expecting 2 occurrences of 'ERROR'
    
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open, read_data='OK\nFINE\nGOOD')
    @patch('os.remove')
    def test_sample2(self, mock_remove, mock_file, mock_urlretrieve):
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 0)  # Expecting 0 occurrences of 'ERROR'
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.remove')
    def test_sample3(self, mock_remove, mock_file, mock_urlretrieve):
        mock_file.return_value.read.return_value = "ERROR\nERROR\nERROR\nERROR\nERROR"
        mock_urlretrieve.return_value = ('mock/path/to/file.txt', {'mock': 'headers'})
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 5)  # Expecting 5 occurrences of 'ERROR'
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.remove')
    def test_mixed_case_errors(self, mock_remove, mock_file, mock_urlretrieve):
        mock_file.return_value.read.return_value = "Error\nerror\nERROR"
        mock_urlretrieve.return_value = ('mock/path/to/file.txt', {'mock': 'headers'})
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 1)  # Expecting 1 occurrence of 'ERROR' (case-sensitive)
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.remove')
    def test_large_file(self, mock_remove, mock_file, mock_urlretrieve):
        mock_file.return_value.read.return_value = "ERROR\n" * 5001
        mock_urlretrieve.return_value = ('mock/path/to/file.txt', {'mock': 'headers'})
        result = task_func('http://example.com/log.txt')
        self.assertEqual(result, 5001)  # Expecting 5001 occurrences of 'ERROR'
