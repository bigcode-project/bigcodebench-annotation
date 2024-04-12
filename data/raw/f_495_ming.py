from typing import Any
import numpy as np
import itertools
from scipy import stats

def f_495(input_list: list, repetitions: int) -> Any:
    """
    Calculate the mode of a list of elements with multiple repetitions of the original list.
    
    Functionality: 
    - Takes a list and a repetition count as input.
    - Flattens the list with multiple repetitions.
    - Calculates the mode of the flattened list.
    
    Input:
    - input_list (list): A list containing elements (can be of any hashable type).
    - repetitions (int): The number of times the original list should be repeated.
    
    Output:
    - Returns a ModeResult object from scipy.stats containing the mode(s) and count(s).
    
    Requirements:
    - numpy
    - itertools
    - scipy.stats
    
    Examples:
    >>> f_495(['A', 'B', 'C'], 10)
    ModeResult(mode=array(['A'], dtype='<U1'), count=array([10]))
    
    >>> f_495([1, 2, 3], 5)
    ModeResult(mode=array([1]), count=array([5]))
    """
    # Flattening the list with multiple repetitions
    flattened_list = np.array(list(itertools.chain(*[input_list for _ in range(repetitions)])))
    
    # Calculating the mode
    mode = stats.mode(flattened_list)
    
    return mode

import unittest
import numpy as np

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test with list of integers
        result = f_495([1, 2, 3], 5)
        self.assertEqual(result.mode.tolist(), [1])
        self.assertEqual(result.count.tolist(), [5])
        
    def test_case_2(self):
        # Test with list of strings
        result = f_495(['A', 'B', 'C'], 10)
        self.assertEqual(result.mode.tolist(), ['A'])
        self.assertEqual(result.count.tolist(), [10])
        
    def test_case_3(self):
        # Test with list of floating-point numbers
        result = f_495([1.5, 2.5, 3.5], 4)
        self.assertEqual(result.mode.tolist(), [1.5])
        self.assertEqual(result.count.tolist(), [4])
        
    def test_case_4(self):
        # Test with empty list
        result = f_495([], 10)
        self.assertEqual(result.mode.shape, (0,))
        self.assertEqual(result.count.shape, (0,))
        
    def test_case_5(self):
        # Test with mixed type list
        result = f_495([1, 'A', 1.5], 3)
        self.assertEqual(result.mode.tolist(), ['1'])
        self.assertEqual(result.count.tolist(), [3])


if __name__ == "__main__":
    run_tests()