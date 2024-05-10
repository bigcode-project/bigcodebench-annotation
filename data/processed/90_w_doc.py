import collections
import string
import random


def task_func(length, seed=0):
    """
    Generate a random string of a given length using ASCII letters and calculate the frequency of each character.​

    Parameters:
    length (int): The length of the random string to be generated.
    seed (int, Optional): The seed to be used for the random number generator. Default is 0.

    Returns:
    dict: A dictionary with the frequency of each character in the generated string.

    Requirements:
    - The function uses the 'collections', 'string', and 'random' modules from the Python standard library.
    - The generated string consists only of ASCII letters.

    Example:
    >>> result = task_func(4)
    >>> isinstance(result, dict)  # The result should be a dictionary
    True
    >>> all(key in string.ascii_letters for key in result.keys())  # All keys should be ASCII letters
    True
    >>> task_func(5, 0)  # The result should be deterministic for a given seed
    {'y': 1, 'W': 1, 'A': 1, 'c': 1, 'q': 1}
    """
    random.seed(seed)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    char_freq = collections.Counter(random_string)
    return dict(char_freq)

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func(0, 77)
        self.assertEquals(result, {})
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)
    def test_case_2(self):
        result = task_func(1)
        self.assertIsInstance(result, dict)
        self.assertEqual(sum(result.values()), 1)
        self.assertEqual(len(result), 1)
    def test_case_3(self):
        length = 10000
        result = task_func(length, 34)
        self.assertIsInstance(result, dict)
        self.assertEqual(sum(result.values()), length)
        self.assertTrue(all(char in string.ascii_letters for char in result))
    def test_case_4(self):
        length = 10
        result = task_func(length, 77)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {'Z': 1, 'q': 1, 'u': 1, 'm': 2, 'p': 1, 'h': 1, 's': 1, 'E': 1, 'J': 1})
        self.assertTrue(all(char in string.ascii_letters for char in result))
    def test_case_5(self):
        length = random.randint(1, 1000)
        result = task_func(length)
        self.assertIsInstance(result, dict)
        self.assertEqual(sum(result.values()), length)
        self.assertTrue(all(char in string.ascii_letters for char in result))
