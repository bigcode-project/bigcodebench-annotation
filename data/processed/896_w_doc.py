from collections import Counter
import random
import itertools

def task_func(length, count, seed=0):
    """
    Generate a number of random strings with a specified length from a fixed set of letters ('a', 'b', 'c', 'd', 'e'),
    and analyze the frequency of each letter in the generated strings.
    
    Parameters:
    - length (int): The length of each string to be generated. Should be a non-negative integer.
    - count (int): The number of random strings to generate. Should be a non-negative integer.
    - seed (int, optional): A seed for the random number generator to ensure reproducibility.
    
    Requirements:
    - collections.Counter
    - random
    - itertools
    
    Returns:
    - Counter: A collections.Counter object containing the frequency of each letter in the generated strings.
    
    Example:
    >>> task_func(5, 2, seed=1)
    Counter({'a': 3, 'd': 3, 'c': 2, 'e': 1, 'b': 1})
    >>> task_func(0, 100, seed=2)
    Counter()
    """

    random.seed(seed)
    strings = [''.join(random.choices(['a', 'b', 'c', 'd', 'e'], k=length)) for _ in range(count)]
    letter_frequency = Counter(itertools.chain(*strings))
    return letter_frequency

import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_length_one_count_ten(self):
        result = task_func(1, 10, seed=0)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 10, "The total count of letters should be 10.")
        
    def test_length_five_count_hundred(self):
        result = task_func(5, 100, seed=1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 500, "The total count of letters should be 500.")
        
    def test_zero_length(self):
        result = task_func(0, 100, seed=2)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 0, "With length 0, there should be no letters.")
        
    def test_zero_count(self):
        result = task_func(5, 0, seed=3)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 0, "With count 0, there should be no letters.")
        
    def test_specific_distribution(self):
        # Assuming the seed value of 4 leads to a specific, known distribution
        result = task_func(5, 2, seed=4)
        # Correct the expected distribution based on actual output
        correct_expected_distribution = Counter({'b': 3, 'a': 3, 'e': 2, 'c': 1, 'd': 1})
        self.assertEqual(result, correct_expected_distribution, "The letter distribution should match the expected distribution.")
