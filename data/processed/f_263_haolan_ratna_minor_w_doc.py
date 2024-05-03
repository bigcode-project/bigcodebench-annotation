import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def f_691(n_keys, n_values):
    """
    Create a Python dictionary with a specified number of keys and values. 

    Parameters:
    n_keys (int): The number of keys to generate.
    n_values (int): The number of values for each key (consecutive integers starting from 1).

    Returns:
    dict: A Python dictionary with keys as strings and values as lists of integers.

    Note: 
    - Keys are randomly selected from a predefined list of letters, and values are consecutive integers starting from 1.
    - Due to the randomness in key selection, the actual keys in the dictionary may vary in each execution.

    Requirements:
    - collections
    - random

    Example:
    >>> random.seed(0)
    >>> f_691(3, 5)
    {'g': [1, 2, 3, 4, 5], 'a': [1, 2, 3, 4, 5]}
    >>> result = f_691(1, 5)
    >>> list(result)[0] in LETTERS
    True
    """

    keys = [random.choice(LETTERS) for _ in range(n_keys)]
    values = list(range(1, n_values + 1))
    return dict(collections.OrderedDict((k, values) for k in keys))

import unittest
import random
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
class TestCases(unittest.TestCase):
    def test_basic_functionality(self):
        random.seed(0)
        result = f_691(3, 5)
        self.assertLessEqual(len(result), 3)
        for key in result:
            self.assertIn(key, LETTERS)
            self.assertEqual(result[key], [1, 2, 3, 4, 5])
    def test_no_keys(self):
        random.seed(0)
        result = f_691(0, 5)
        self.assertEqual(result, {})
    def test_no_values(self):
        random.seed(0)
        result = f_691(3, 0)
        for key in result:
            self.assertEqual(result[key], [])
    def test_large_input(self):
        random.seed(0)
        result = f_691(10, 1000)
        for key in result:
            self.assertIn(key, LETTERS)
            self.assertEqual(len(result[key]), 1000)
    def test_max_keys(self):
        random.seed(0)
        result = f_691(len(LETTERS), 5)
        for key in result:
            self.assertIn(key, LETTERS)
            self.assertEqual(result[key], [1, 2, 3, 4, 5])
