import numpy as np
from scipy import stats

def f_638(L):
    '''
    Calculate the mode of all elements in a nested list 'L'.
    
    Parameters:
    L (list): The nested list.
    
    Returns:
    int: The mode.
    
    Requirements:
    - numpy
    - scipy.stats

    Example:
    >>> f_638([[1,2,3],[4,5,6]])
    1
    '''
    flattened = [item for sublist in L for item in sublist]
    mode = stats.mode(flattened)[0][0]
    return mode
    

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_1(self):
        result = f_638([[1, 2, 3], [4, 5, 6]])
        expected = 1
        self.assertEqual(result, expected)
    
    def test_2(self):
        result = f_638([[1, 2, 3], [4, 5, 6, 6]])
        expected = 6
        self.assertEqual(result, expected)
        
    def test_3(self):
        result = f_638([[1, 1, 2, 2], [3, 4, 5]])
        expected = 1
        self.assertEqual(result, expected)
    
    def test_4(self):
        result = f_638([[1, 1, 2, 2]])
        expected = 1
        self.assertEqual(result, expected)
    
    def test_5(self):
        result = f_638([[-1, -1, -2, -3], [0, 1, 2, 3]])
        expected = -1
        self.assertEqual(result, expected)

if __name__ == "__main__":
    run_tests()