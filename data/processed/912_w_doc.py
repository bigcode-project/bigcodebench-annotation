from collections import Counter
import itertools

def task_func(letters: list, repetitions: int) -> dict:
    """
    Count the frequency of each letter in a list after repeating it a given number of times.

    Parameters:
    - letters (list): A list of single-character strings representing letters.
    - repetitions (int): The number of times to repeat the list.

    Returns:
    Returns a dictionary where the keys are the letters and the values are their frequencies.

    Requirements:
    - collections.Counter
    - itertools

    Example:
    >>> task_func(['A', 'B', 'C'], 2)
    {'A': 2, 'B': 2, 'C': 2}
    >>> task_func(['A', 'B'], 3)
    {'A': 3, 'B': 3}
    """

    flattened_list = list(itertools.chain(*[letters for _ in range(repetitions)]))
    counts = dict(Counter(flattened_list))
    return counts

import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        result = task_func(['A', 'B', 'C'], 2)
        expected = {'A': 2, 'B': 2, 'C': 2}
        self.assertEqual(result, expected)
        
    def test_case_2(self):
        result = task_func(['A', 'B'], 3)
        expected = {'A': 3, 'B': 3}
        self.assertEqual(result, expected)
        
    def test_case_3(self):
        result = task_func([], 2)
        expected = {}
        self.assertEqual(result, expected)
        
    def test_case_4(self):
        result = task_func(['A', 'B', 'A'], 2)
        expected = {'A': 4, 'B': 2}
        self.assertEqual(result, expected)
        
    def test_case_5(self):
        result = task_func(['A'], 0)
        expected = {}
        self.assertEqual(result, expected)
