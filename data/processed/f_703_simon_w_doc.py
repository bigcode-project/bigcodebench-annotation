import string
import random
from collections import Counter


def f_288(n, seed=None):
    """
    Generate a number of random lowercase letters and count their occurrences.

    This function takes an integer input to determine how many random letters 
    to generate and an optional seed for consistent randomness. It then creates 
    a list of these letters, chosen from the English lowercase alphabet, and 
    counts each letter's occurrences. The result is returned as a Counter 
    object (from the collections module) which behaves like a dictionary where 
    the keys are the letters, and the values are their counts.

    Parameters:
    n (int): The number of random letters to generate.
    seed (int, optional): A seed for the random number generator for consistent
                         results. Defaults to None.

    Returns:
    Counter: A collections.Counter object with the count of each letter.

    Requirements:
    - collections
    - string
    - random

    Example:
    >>> letter_counts = f_288(1000, seed=123)
    >>> print(letter_counts)
    Counter({'v': 48, 'b': 47, 'n': 46, 'r': 46, 'k': 46, 'z': 46, 'c': 44, 'e': 43, 'q': 43, 'l': 43, 'y': 42, 'm': 42, 'a': 42, 'u': 42, 'd': 36, 'o': 34, 'j': 34, 'g': 34, 'f': 33, 'h': 33, 'p': 32, 'w': 30, 'x': 30, 'i': 29, 't': 28, 's': 27})
    >>> f_288(10, seed=12)
    Counter({'v': 2, 'l': 2, 'p': 1, 'i': 1, 'q': 1, 'e': 1, 'm': 1, 'a': 1})

    Note: 
    The function internally uses a list to store the randomly generated 
    letters before counting them. The randomness of letter selection can be 
    consistent by providing a seed.
    """
    LETTERS = string.ascii_lowercase
    if seed is not None:
        random.seed(seed)
    letters = [random.choice(LETTERS) for _ in range(n)]
    letter_counts = Counter(letters)
    return letter_counts

import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_randomness_with_seed(self):
        # Using a seed should give consistent results
        result1 = f_288(100, seed=1)
        result2 = f_288(100, seed=1)
        self.assertEqual(result1, result2)
    def test_randomness_without_seed(self):
        # Without a seed, the results should be potentially different
        result1 = f_288(100)
        result2 = f_288(100)
        self.assertNotEqual(result1, result2)
    def test_validity_of_counts(self):
        # The total counts should equal the number of letters generated
        num_letters = 200
        result = f_288(num_letters, seed=2)
        self.assertEqual(sum(result.values()), num_letters)
    def test_non_negative_counts(self):
        # All counts should be non-negative
        result = f_288(100, seed=3)
        self.assertTrue(all(count >= 0 for count in result.values()))
    def test_type_of_return_value(self):
        # The return type should be a Counter object
        result = f_288(100, seed=4)
        self.assertIsInstance(result, Counter)
    def test_return_value(self):
        # test specific values
        result = f_288(10, seed=42)
        exp = Counter({'d': 2, 'x': 2, 'h': 2, 'u': 1, 'a': 1, 'i': 1, 'e': 1})
        self.assertEqual(result, exp)
