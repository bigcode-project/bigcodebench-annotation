import numpy as np
import math

def f_639(L):
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
    >>> f_639([[1,2,3],[4,5,6]])
    3.5
    """
    # Recursive function to flatten the list
    def flatten(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list
    
    flattened = flatten(L)
    
    if len(flattened) == 0:
        raise ValueError("List is empty")
    
    median = np.median(flattened)
    
    return median

import unittest
import numpy as np

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_median_odd_elements(self):
        result = f_639([[1, 2, 3], [4, 5, 6], [7]])
        self.assertEqual(result, 4.0)

    def test_median_even_elements(self):
        result = f_639([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(result, 3.5)
        
    def test_median_single_element(self):
        result = f_639([[5]])
        self.assertEqual(result, 5.0)
        
    def test_median_deep_nesting(self):
        result = f_639([1, [2, [3, 4, [5, 6], 7], 8], 9])
        self.assertEqual(result, 5.0)
        
    def test_median_empty_list(self):
        with self.assertRaises(ValueError):
            f_639([])

if __name__ == "__main__":
    run_tests()