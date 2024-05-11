import itertools
import math
from pandas import Series


def task_func(elements, subset_size, top_n=2):
    """
    Generate all subsets of a given size from a tuple and calculate the product of the sums of the subsets. Additionally, 
    return the top_n sums of the subsets. If the subset size is larger than the tuple length, return 1. If the subset size is 0,
    return 1.

    Parameters:
    - elements (tuple): A tuple of elements to create subsets from.
    - subset_size (int): The size of the subsets to be generated.
    - top_n (int, Optional): The number of top subsets to return. Defaults to None.

    Returns:
    int: The product of the sums of the subsets.
    list: The top_n sums of the subsets as a pandas Series.


    Requirements:
    - itertools
    - math
    
    Example:
    >>> prod, sums = task_func((1, 2, 3), 2)
    >>> prod
    60
    >>> list(sums)
    [5, 4]
    """
    if subset_size > len(elements) or subset_size <= 0:
        return 1, []
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations if len(combination) != 0]
    product = math.prod(sums)
    top_sums = sorted(sums, reverse=True)[:top_n]
    top_sums = Series(top_sums)
    return product, top_sums

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Default values
        result, _ = task_func((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)
        expected = 2781259372192376861719959017613164544000000000
        self.assertEqual(result, expected)
    def test_case_2(self):
        # Custom tuple and subset size
        result, sums = task_func((1, 2, 3), 2)
        expected = 60
        self.assertEqual(result, expected)
        # Test the top sums
        self.assertEqual(list(sums), [5, 4])
        # Test the type of the top sums
        self.assertIsInstance(sums, Series)
    def test_case_3(self):
        # Larger subset size than tuple length
        result, _ = task_func((1, 2, 3), 5)
        expected = 1  # No subset of size 5 can be formed, so the product will be 1
        self.assertEqual(result, expected)
    def test_case_4(self):
        # Subset size of 0
        result, sums = task_func((1, 2, 3), 0)
        expected = 1  # No subset of size 0 can be formed, so the product will be 1
        self.assertEqual(result, expected)
        self.assertEqual(list(sums), [])
    def test_case_5(self):
        # Larger tuple
        result, _ = task_func((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), 4)
        self.assertIsInstance(result, int)  # Ensure the result is an integer
