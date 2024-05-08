from collections import Counter
import heapq

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def f_603(my_dict):
    """
    Create a dictionary in which the keys are letters and the values are random integers.
    Find the 3 most common letters in the dictionary.

    Parameters:
    - my_dict (dict): The dictionary to process.

    Returns:
    - most_common_letters (list): The 3 most common letters.

    Requirements:
    - collections
    - heapq

    Example:
    >>> random.seed(43)
    >>> my_dict = {letter: random.randint(1, 100) for letter in LETTERS}
    >>> most_common_letters = f_603(my_dict)
    >>> print(most_common_letters)
    ['d', 'v', 'c']
    """
    letter_counter = Counter(my_dict)
    most_common_letters = heapq.nlargest(3, letter_counter, key=letter_counter.get)
    return most_common_letters

import unittest
import random
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
def generate_random_dict(size=26, min_val=1, max_val=100):
    """Generate a random dictionary with letters as keys and random integers as values."""
    letters = random.sample(LETTERS, size)
    return {letter: random.randint(min_val, max_val) for letter in letters}
class TestCases(unittest.TestCase):
    def test_basic(self):
        # Basic Test
        test_dict = generate_random_dict()
        result = f_603(test_dict)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(letter, str) for letter in result))
    def test_few_letters(self):
        # Edge Case: Fewer than 3 letters
        test_dict = {'a': 10, 'b': 20}
        result = f_603(test_dict)
        self.assertEqual(result, ['b', 'a'])
    def test_empty_dict(self):
        # Edge Case: Empty dictionary
        test_dict = {}
        result = f_603(test_dict)
        self.assertEqual(result, [])
    def test_specific_letters(self):
        # Specific Test: Known output
        test_dict = {'a': 100, 'b': 90, 'c': 80, 'd': 70}
        result = f_603(test_dict)
        self.assertEqual(result, ['a', 'b', 'c'])
    def test_general(self):
        # General Test: Check top 3 values
        test_dict = generate_random_dict()
        result = f_603(test_dict)
        sorted_values = sorted(test_dict.values(), reverse=True)[:3]
        sorted_keys = [k for k, v in sorted(test_dict.items(), key=lambda item: item[1], reverse=True)][:3]
        self.assertEqual(result, sorted_keys)
        self.assertEqual([test_dict[key] for key in result], sorted_values)
