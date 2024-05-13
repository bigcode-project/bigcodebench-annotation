from itertools import combinations
import math

def task_func(x, w):
    """
    Find the continuous substring of x, which has the maximum total weight, given a dictionary where the keys are characters and the values are their weights.

    Parameters:
    - x (str): The input string.
    - w (dict): The dictionary of character weights.

    Returns:
    - max_substr (str): The continuous substring with the highest weight.

    Requirements:
    - itertools
    - math

    Example:
    >>> task_func('c', {'a': 1, 'b': 2, 'c': 3})
    'c'
    >>> task_func('abc', {'a': 10, 'b': -5, 'c': 3})
    'a'
    """

    max_weight = -math.inf
    max_substr = ''
    for start, end in combinations(range(len(x) + 1), 2):
        substr = x[start:end]
        weight = sum(w.get(c, 0) for c in substr)
        if weight > max_weight:
            max_weight = weight
            max_substr = substr
    return max_substr

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(task_func('c', {'a': 1, 'b': 2, 'c': 3}), 'c')
    
    def test_case_2(self):
        self.assertEqual(task_func('aabc', {'a': 10, 'b': -5, 'c': 3}), 'aa')
    def test_case_3(self):
        self.assertEqual(task_func('aabc', {'a': 10, 'b': -2, 'c': 3}), 'aabc')
    def test_case_4(self):
        self.assertEqual(task_func('aabc', {'a': 2, 'b': -5, 'c': 3}), 'aa')
    
    def test_case_5(self):
        self.assertEqual(task_func('aabc', {'a': 0, 'b': -1, 'c': 1}), 'c')
