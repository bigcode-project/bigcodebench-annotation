import numpy as np
import math

def task_func(L):
    """
    Calculate the median of all elements in a nested list 'L'.
    
    Parameters:
    - L (list): The nested list.
    
    Returns:
    - median (float): The median.
    
    Requirements:
    - numpy
    - math

    Example:
    >>> task_func([[1,2,3],[4,5,6]])
    3.5
    """
    def flatten(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list
    flattened = flatten(L)
    if not flattened:
        raise ValueError("List is empty")
    sorted_flattened = np.sort(flattened)
    n = len(sorted_flattened)
    if n % 2 == 0:
        median_index1 = math.ceil(n / 2) - 1
        median_index2 = median_index1 + 1
        median = (sorted_flattened[median_index1] + sorted_flattened[median_index2]) / 2.0
    else:
        median_index = math.ceil(n / 2) - 1
        median = sorted_flattened[median_index]
    return median

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_median_odd_elements(self):
        result = task_func([[1, 2, 3], [4, 5, 6], [7]])
        self.assertEqual(result, 4.0)
    def test_median_even_elements(self):
        result = task_func([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(result, 3.5)
        
    def test_median_single_element(self):
        result = task_func([[5]])
        self.assertEqual(result, 5.0)
        
    def test_median_deep_nesting(self):
        result = task_func([1, [2, [3, 4, [5, 6], 7], 8], 9])
        self.assertEqual(result, 5.0)
        
    def test_median_empty_list(self):
        with self.assertRaises(ValueError):
            task_func([])
