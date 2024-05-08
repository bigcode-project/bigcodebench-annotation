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

    Requirements:
    - string
    - re
    - collections

    Returns:
    - dict: A dictionary with the frequency of each lowercase letter.

    Example:
    >>> f_660('abc-def-ghij')
    {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    """
    # Match and extract the portion before the last hyphen
    match = re.search(r'^(.*)-', string)
    if match:
        prefix = match.group(1)
    else:
        # If there's no hyphen, the whole string is considered if it is letters only
        prefix = string if string.isalpha() else ""

    # Count each letter in the prefix
    letter_counts = Counter(prefix)
    # Initialize a dictionary with all letters set to zero count
    result = {letter: 0 for letter in ascii_lowercase}
    # Update this dictionary with the actual counts from the prefix
    result.update({letter: letter_counts.get(letter, 0) for letter in letter_counts if letter in result})

    return result

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_660('abc-def-ghij')
        expected = {letter: 1 if letter in 'abcdef' else 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)

    def test_case_2(self):
        result = f_660('abcdefghij')
        expected = {letter: 1 if letter in 'abcdefghij' else 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)

    def test_case_3(self):
        result = f_660('aabbcc-def')
        expected = {letter: 2 if letter in 'aabbcc' else 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)

    def test_case_4(self):
        result = f_660('')
        expected = {letter: 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)

    def test_case_5(self):
        result = f_660('xyz-abc')
        expected = {letter: 1 if letter in 'xyz' else 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)

if __name__ == "__main__":
    run_tests()