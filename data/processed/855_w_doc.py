import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    """
    Generate n random strings of a specified length, count the frequency of each character across all strings, and return the result as a dictionary.

    Parameters:
    - n_strings (int): The number of random strings to generate.
    - string_length (int): The length of each random string.

    Returns:
    - dict: A dictionary containing character counts with characters as keys and their frequencies as values.

    Requirements:
    - random
    - string
    - collections

    Constants:
    - VALID_CHARACTERS: A string containing all valid characters (ASCII letters and digits) that can be used in the random strings.

    Example:
    >>> random.seed(42)
    >>> task_func(2, 3)
    {'O': 1, 'h': 1, 'b': 1, 'V': 1, 'r': 1, 'p': 1}
    """

    strings = [''.join(random.choice(VALID_CHARACTERS) for _ in range(string_length)) for _ in range(n_strings)]
    character_counts = collections.Counter(''.join(strings))
    return dict(character_counts)

import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_single_string_single_character(self):
        # Test when n_strings=1 and string_length=1 (minimal input)
        result = task_func(1, 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(sum(result.values()), 1)
    def test_multiple_strings_single_character(self):
        # Test when n_strings > 1 and string_length=1
        result = task_func(5, 1)
        self.assertTrue(len(result) <= 5)
        self.assertEqual(sum(result.values()), 5)
    def test_single_string_multiple_characters(self):
        # Test when n_strings=1 and string_length > 1
        result = task_func(1, 5)
        self.assertTrue(len(result) <= 5)
        self.assertEqual(sum(result.values()), 5)
    def test_multiple_strings_multiple_characters(self):
        # Test when n_strings > 1 and string_length > 1
        result = task_func(5, 5)
        self.assertTrue(len(result) <= 25)
        self.assertEqual(sum(result.values()), 25)
    def test_valid_characters(self):
        # Test whether the function only uses valid characters as defined in VALID_CHARACTERS
        result = task_func(100, 10)
        all_characters = ''.join(result.keys())
        self.assertTrue(all(char in VALID_CHARACTERS for char in all_characters))
