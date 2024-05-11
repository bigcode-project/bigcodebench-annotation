import re
from nltk import word_tokenize
from collections import Counter

def task_func(input_str):
    """
    Remove all special characters, punctuation marks and spaces from a string called "input _ str" using regex and then count the frequency of each word.

    Parameters:
    input_str (str): The input string.

    Returns:
    dict: A dictionary with the frequency of each word.

    Requirements:
    - re
    - nltk.word_tokenize
    - collections.Counter

    Example:
    >>> task_func('Special $#! characters   spaces 888323')
    Counter({'Special': 1, 'characters': 1, 'spaces': 1, '888323': 1})
    """
    cleaned_str = re.sub('[^A-Za-z0-9 ]+', '', input_str)
    words = word_tokenize(cleaned_str)
    freq_dict = Counter(words)
    return freq_dict

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func('Special $#! characters   spaces 888323')
        expected = {'Special': 1, 'characters': 1, 'spaces': 1, '888323': 1}
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = task_func('Hello hello world')
        expected = {'Hello': 1, 'hello': 1, 'world': 1}
        self.assertEqual(result, expected)
    def test_case_3(self):
        result = task_func('')
        expected = {}
        self.assertEqual(result, expected)
    def test_case_4(self):
        result = task_func('123 123 456')
        expected = {'123': 2, '456': 1}
        self.assertEqual(result, expected)
    def test_case_5(self):
        result = task_func('Hello123 #$! 123')
        expected = {'Hello123': 1, '123': 1}
        self.assertEqual(result, expected)
