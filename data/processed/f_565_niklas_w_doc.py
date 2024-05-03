import numpy as np
from sklearn.decomposition import PCA

def f_501(tuples_list, n_components):
    """
    Perform Principal Component Analysis (PCA) on a list of tuples.
    
    Parameters:
    - tuples_list (list): The list of tuples.
    
    Returns:
    - transformed_data (ndarray): The transformed data.

    Requirements:
    - numpy
    - sklearn
    
    Example:
    >>> data = f_501([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], 2)
    >>> print(data)
    [[ 8.00000000e+00  3.84592537e-16]
     [ 0.00000000e+00  0.00000000e+00]
     [-8.00000000e+00  3.84592537e-16]]
    """
    data = np.array(tuples_list)
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    return transformed_data

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        transformed_data = f_501([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], 2)
        self.assertEqual(transformed_data.shape, (3, 2))
    def test_case_2(self):
        transformed_data = f_501([(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 2)
        self.assertEqual(transformed_data.shape, (3, 2))
        self.assertTrue(np.all(transformed_data == 0))
    def test_case_3(self):
        transformed_data = f_501([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], 3)
        self.assertEqual(transformed_data.shape, (3, 3))
    def test_case_4(self):
        transformed_data = f_501([(0, 1)], 1)
        self.assertEqual(transformed_data.shape, (1, 1))
        self.assertTrue(np.all(transformed_data == 0))
    def test_case_5(self):
        transformed_data = f_501([(-1, -1, -1), (0, 0, 0), (1, 1, 1)], 1)
        self.assertEqual(transformed_data.shape, (3, 1))
        self.assertTrue(transformed_data[0][0] < 0)
        self.assertTrue(transformed_data[1][0] == 0)
        self.assertTrue(transformed_data[2][0] > 0)
