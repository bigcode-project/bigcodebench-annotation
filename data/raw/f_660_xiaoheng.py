from string import ascii_lowercase
import re
from collections import Counter

# Constants
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
LETTERS = ascii_lowercase

def f_660(string):
    """
    If a string occurs, divide it the last time "-" occurs and count the frequency of each lowercase letter in the prefix of the string.
    
    Parameters:
    - string (str): The input string.

    Returns:
    - dict: A dictionary with the frequency of each lowercase letter.

    Requirements:
    - string
    - re
    - collections

    Example:
    >>> f_660('abc-def-ghij')
    """
    match = LETTERS_PATTERN.match(string)
    if match is not None:
        prefix = match.group(1)
        letter_counts = Counter(prefix)
        return {letter: letter_counts.get(letter, 0) for letter in LETTERS}

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a string containing multiple hyphens
        result = count_letters_before_last_hyphen('abc-def-ghij')
        expected = {
            'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1,
            'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
            'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
        self.assertEqual(result, expected)

    def test_case_2(self):
        # Test with a string with no hyphen
        result = f_660('abcdefghij')
        expected = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
        self.assertEqual(result, expected)

    def test_case_3(self):
        # Test with a string with single hyphen and repeated letters
        result = f_660('aabbcc-def')
        expected = {
            'a': 2, 'b': 2, 'c': 2, 'd': 0, 'e': 0, 'f': 0,
            'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
            'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
        self.assertEqual(result, expected)

    def test_case_4(self):
        # Test with an empty string
        result = f_660('')
        expected = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
        self.assertEqual(result, expected)

    def test_case_5(self):
        # Test with a string containing letters from the end of the alphabet
        result = f_660('xyz-abc')
        expected = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
            'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
            'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 1,
            'y': 1, 'z': 1
        }
        self.assertEqual(result, expected)

if __name__ == "__main__":
    run_tests()