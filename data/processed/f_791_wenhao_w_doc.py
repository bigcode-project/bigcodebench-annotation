import numpy as np
from sklearn.preprocessing import MinMaxScaler

def f_791(rows=3, columns=2, seed=42):
    """
    Generate a matrix of random values with specified dimensions and scale it between 0 and 1.
    
    Parameters:
    rows (int): The number of rows for the matrix. Default is 3.
    columns (int): The number of columns for the matrix. Default is 2.
    
    Returns:
    ndarray: A numpy ndarray with scaled values between 0 and 1.
    
    Requirements:
    - numpy
    - sklearn.preprocessing.MinMaxScaler
    
    Example:
    >>> f_791(3, 2)
    array([[0.37939383, 1.        ],
           [1.        , 0.55700635],
           [0.        , 0.        ]])
    
    >>> f_791(2, 2)
    array([[0., 1.],
           [1., 0.]])
    """
    np.random.seed(seed) # Ensure reproducibility for consistent outputs across different runs
    matrix = np.random.rand(rows, columns)
    scaler = MinMaxScaler()
    scaled_matrix = scaler.fit_transform(matrix)

    return scaled_matrix

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        result = f_791()
        self.assertEqual(result.shape, (3, 2))
        self.assertTrue(np.all(result >= 0))
    
    def test_case_2(self):
        result = f_791(2, 2)
        self.assertEqual(result.shape, (2, 2))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))
        
    def test_case_3(self):
        result = f_791(4, 3)
        self.assertEqual(result.shape, (4, 3))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))
    
    def test_case_4(self):
        result = f_791(5, 1)
        self.assertEqual(result.shape, (5, 1))
        self.assertTrue(np.all(result >= 0))
        
    def test_case_5(self):
        result = f_791(1, 5)
        self.assertEqual(result.shape, (1, 5))
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))
