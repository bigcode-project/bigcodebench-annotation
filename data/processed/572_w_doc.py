from itertools import combinations
import math

def task_func(seq, letter_weight_dict):
    """
    Find the subsequence in a string that has the maximum total weight based on the weights given for each character. 
    The weights are assigned randomly and a subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

    Parameters:
    - seq (str): The input string.
    - letter_weight_dict (dict): A dictionary with the weights for each character.

    Returns:
    - str: The subsequence with the highest weight.

    Requirements:
    - itertools
    - math

    Example:
    >>> task_func('abc', {'a': 1, 'b': 2, 'c': 3})
    'abc'
    >>> task_func('aabc', {'a': 10, 'b': -5, 'c': 3})
    'aac'
    """
    max_weight = -math.inf
    max_subseq = ''
    for r in range(1, len(seq) + 1):
        for subseq in combinations(seq, r):
            weight = sum(letter_weight_dict[c] for c in subseq)
            if weight > max_weight:
                max_weight = weight
                max_subseq = ''.join(subseq)
    return max_subseq

import unittest
class TestCases(unittest.TestCase):
    def base(self, seq, letter_weight_dict, correct_seq):
        # Run function
        result = task_func(seq, letter_weight_dict)
        # Check result
        self.assertTrue(isinstance(result, str))
        self.assertEqual(result, correct_seq)
    def test_case_1(self):
        self.base('abc', {'a': 1, 'b': 2, 'c': 3}, 'abc')
    
    def test_case_2(self):
        self.base('aabc', {'a': 10, 'b': -5, 'c': 3}, 'aac')
    def test_case_3(self):
        self.base('zx', {'x': 1, 'z': 2}, 'zx')
    
    def test_case_4(self):
        self.base('lfhah', {'a': 1, 'f': 2, 'h': -1, 'l': 4}, 'lfa')
    
    def test_case_5(self):
        self.base('a', {'a': 1}, 'a')
