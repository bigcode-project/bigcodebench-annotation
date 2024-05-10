import re
import string
from random import choice

def task_func(n, pattern):
    """
    Generates a random string of a specified length that conforms to a given regular expression pattern.
    The function repeatedly generates random strings, using both uppercase and lowercase ASCII letters,
    of the specified length until one matches the pattern.

    Parameters:
    n (int): The length of the string to be generated.
    pattern (str): A regular expression pattern the generated string must match, including start and end anchors.

    Returns:
    str: A randomly generated string that matches the specified pattern.

    Requirements:
    - re
    - string
    - random.choice

    Examples:
    >>> len(task_func(5, '[a-z]*')) == 5
    True

    >>> bool(re.match('^[A-Z]+$', task_func(3, '^[A-Z]+$')))
    True
    """
    while True:
        s = ''.join(choice(string.ascii_letters) for _ in range(n))
        if re.match(pattern, s):
            return s

import unittest
import re
class TestCases(unittest.TestCase):
    def test_correct_length(self):
        # Ensure the generated string has the requested length
        self.assertEqual(len(task_func(5, '^[a-z]*$')), 5)
    def test_pattern_matching(self):
        # Check if the generated string matches a simple pattern
        self.assertTrue(re.match('^[a-z]+$', task_func(5, '^[a-z]+$')))
    def test_lowercase_letters(self):
        # Verify the function generates a string of only lowercase letters
        self.assertTrue(re.match('^[a-z]{10}$', task_func(10, '^[a-z]{10}$')))
    def test_uppercase_letters(self):
        # Verify the function generates a string of only uppercase letters
        self.assertTrue(re.match('^[A-Z]{10}$', task_func(10, '^[A-Z]{10}$')))
    def test_mixed_case_letters(self):
        # Ensure the function can handle mixed case patterns
        pattern = '^[A-Za-z]{10}$'
        result = task_func(10, pattern)
        self.assertTrue(re.match(pattern, result) and any(c.islower() for c in result) and any(c.isupper() for c in result))
    def test_zero_length_string(self):
        # Test for generating a zero-length string, expecting an empty string as a result
        self.assertEqual(task_func(0, '^$'), '')
