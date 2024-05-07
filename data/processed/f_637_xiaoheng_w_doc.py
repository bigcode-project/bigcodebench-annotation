import numpy as np
from itertools import chain

def f_272(L):
    """
    Calculate the mean and variance of all elements in a nested list 'L'.
    
    Parameters:
    - L (list): The nested list.
    
    Returns:
    - dict: A dictionary containing the mean and variance.
    
    Requirements:
    - numpy
    - itertools.chain

    Example:
    >>> f_272([[1,2,3],[4,5,6]])
    {'mean': 3.5, 'variance': 2.9166666666666665}
    """
    flattened = list(chain.from_iterable(L))
    mean = np.mean(flattened)
    variance = np.var(flattened)
    return {'mean': mean, 'variance': variance}

import unittest
import numpy as np
from itertools import chain
class TestCases(unittest.TestCase):
    
    def test_1(self):
        L = [[1, 2, 3], [4, 5, 6]]
        result = f_272(L)
        flattened = list(chain.from_iterable(L))
        expected_mean = np.mean(flattened)
        expected_variance = np.var(flattened)
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['variance'], expected_variance)
    def test_2(self):
        L = [[10, 20], [30, 40], [50, 60]]
        result = f_272(L)
        flattened = list(chain.from_iterable(L))
        expected_mean = np.mean(flattened)
        expected_variance = np.var(flattened)
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['variance'], expected_variance)
    def test_3(self):
        L = [[5]]
        result = f_272(L)
        flattened = list(chain.from_iterable(L))
        expected_mean = np.mean(flattened)
        expected_variance = np.var(flattened)
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['variance'], expected_variance)
    def test_4(self):
        L = [[1, 2, 3], [3, 2, 1], [4, 5, 6], [6, 5, 4]]
        result = f_272(L)
        flattened = list(chain.from_iterable(L))
        expected_mean = np.mean(flattened)
        expected_variance = np.var(flattened)
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['variance'], expected_variance)
    def test_5(self):
        L = [[10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
        result = f_272(L)
        flattened = list(chain.from_iterable(L))
        expected_mean = np.mean(flattened)
        expected_variance = np.var(flattened)
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['variance'], expected_variance)
