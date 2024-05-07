import numpy as np
from itertools import zip_longest

def f_1022(l1, l2,THRESHOLD = 0.5):
    """
    Alternates elements from two numeric lists, calculates the absolute difference of each 
    element from a predefined threshold, and returns the element closest to this threshold.
    
    Parameters:
    l1 (list): The first input list containing numeric values.
    l2 (list): The second input list containing numeric values.
    THRESHOLD (float): The predefined constant representing a numeric value used as a reference point for comparison. Default to 0.5. 
    
    Returns:
    float: The element from the combined list that is closest to the threshold of 0.5.
    
    Requirements:
    - numpy
    - itertools.zip_longest

    Notes:
    - If l1 and l2 are of different lengths, elements from the longer list without a corresponding 
      pair in the shorter list will not be paired with 'None'. Only existing numeric elements are considered.
    - The threshold is fixed at 0.5. Adjustments to the threshold require changes to the THRESHOLD constant.
    
    Example:
    >>> l1 = [0.3, 1, 2, 3]
    >>> l2 = [0.7, 11, 12, 13]
    >>> closest = f_1022(l1, l2)
    >>> print(closest)
    0.7
    """
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    differences = np.abs(np.array(combined) - THRESHOLD)
    closest_index = np.argmin(differences)
    return combined[closest_index]

import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Test with two lists of equal length where one element exactly matches the threshold.
        l1 = [0, 0.5, 2, 3, 4]
        l2 = [10, 11, 12, 13, 14]
        self.assertEqual(f_1022(l1, l2), 0.5)

    def test_case_2(self):
        # Test with the first list longer than the second, where the closest value is below the threshold.
        l1 = [0, 0.4, 0.6, 3, 4, 5]
        l2 = [10, 11, 12]
        self.assertEqual(f_1022(l1, l2), 0.4)
        
    def test_case_3(self):
        # Test with the second list longer than the first, where the closest value is just above the threshold.
        l1 = [0, 0.51]
        l2 = [10, 11, 12, 13]
        self.assertEqual(f_1022(l1, l2), 0.51)
        
    def test_case_4(self):
        # Test where one list is empty and the function must choose the closest value from a single non-empty list.
        l1 = []
        l2 = [10, 11, 12, 13]
        self.assertEqual(f_1022(l1, l2), 10)
        
    def test_case_5(self):
        # Test with negative and positive numbers where the closest value to the threshold is zero.
        l1 = [-10, -5, 0, 5, 10]
        l2 = [-1, 0, 1]
        self.assertEqual(f_1022(l1, l2), 0)

    def test_empty_lists(self):
        # Test with both lists empty to check function's behavior in absence of any elements.
        with self.assertRaises(ValueError):
            f_1022([], [])
                    
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()