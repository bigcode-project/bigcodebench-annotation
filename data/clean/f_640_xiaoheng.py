import numpy as np
from scipy.stats import iqr

def f_640(L):
    """
    Calculate the interquartile range of all elements in a nested list 'L'.
    
    Parameters:
    - L (list): The nested list.
    
    Returns:
    - iqr_value (float): The interquartile range.
    
    Requirements:
    - numpy
    - scipy.stats

    Example:
    >>> f_640([[1,2,3],[4,5,6]])
    2.5
    """
    flattened = np.array(L).flatten()
    iqr_value = iqr(flattened)
    
    return iqr_value

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_1(self):
        result = f_640([[1,2,3],[4,5,6]])
        expected = 2.5
        self.assertAlmostEqual(result, expected, places=2)

    def test_2(self):
        result = f_640([[1,1,1],[2,2,2]])
        expected = 1.0
        self.assertAlmostEqual(result, expected, places=2)

    def test_3(self):
        result = f_640([[1,5,3]])
        expected = 2.0
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_4(self):
        result = f_640([[1],[2],[3],[4],[5]])
        expected = 2.0
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_5(self):
        result = f_640([[1,-2,3],[-4,5,6]])
        expected = 5.75
        self.assertAlmostEqual(result, expected, places=2)

if __name__ == "__main__":
    run_tests()