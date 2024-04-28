import numpy as np
from scipy.linalg import svd

def f_484(rows=3, columns=2, seed=0):
    """
    Generate a matrix of random values with specified dimensions and perform Singular Value Decomposition (SVD) on it.

    Requirements:
    - numpy
    - scipy.linalg.svd

    Parameters:
    - rows (int): Number of rows for the random matrix. Default is 3.
    - columns (int): Number of columns for the random matrix. Default is 2.
    - seed (int, optional): Seed for the random number generator to ensure reproducibility. Default is None.

    Returns:
    tuple: A tuple containing three elements:
        - U (ndarray): The unitary matrix U.
        - s (ndarray): The singular values, sorted in descending order.
        - Vh (ndarray): The conjugate transpose of the unitary matrix V.

    Example:
    >>> U, s, Vh = f_484(3, 2, seed=42)
    >>> print('U shape:', U.shape)
    U shape: (3, 3)
    >>> print('s shape:', s.shape)
    s shape: (2,)
    >>> print('Vh shape:', Vh.shape)
    Vh shape: (2, 2)
    """
    np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    U, s, Vh = svd(matrix)

    return U, s, Vh

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test with default 3x2 matrix
        U, s, Vh = f_484(seed=3)
        self.assertEqual(U.shape, (3, 3))
        self.assertEqual(s.shape, (2,))
        self.assertEqual(Vh.shape, (2, 2))
        self.assertTrue(np.all(s >= 0))
        
    def test_case_2(self):
        # Test with a 5x5 square matrix
        U, s, Vh = f_484(5, 5, seed=42)
        self.assertEqual(U.shape, (5, 5))
        self.assertEqual(s.shape, (5,))
        self.assertEqual(Vh.shape, (5, 5))
        self.assertTrue(np.all(s >= 0))
    
    def test_case_3(self):
        # Test with a 2x3 matrix (more columns than rows)
        U, s, Vh = f_484(2, 3, seed=12)
        self.assertEqual(U.shape, (2, 2))
        self.assertEqual(s.shape, (2,))
        self.assertEqual(Vh.shape, (3, 3))
        self.assertTrue(np.all(s >= 0))
        
    def test_case_4(self):
        # Test with a 1x1 matrix (a scalar)
        U, s, Vh = f_484(1, 1, seed=0)
        self.assertEqual(U.shape, (1, 1))
        self.assertEqual(s.shape, (1,))
        self.assertEqual(Vh.shape, (1, 1))
        self.assertTrue(np.all(s >= 0))
        
    def test_case_5(self):
        # Test with a 4x3 matrix
        U, s, Vh = f_484(4, 3, seed=1)
        self.assertEqual(U.shape, (4, 4))
        self.assertEqual(s.shape, (3,))
        self.assertEqual(Vh.shape, (3, 3))
        self.assertTrue(np.all(s >= 0))
