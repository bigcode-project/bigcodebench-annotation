from sklearn.preprocessing import MinMaxScaler
import numpy as np

def f_281(myList):
    """
    Normalize a list of numeric values to the range [0, 1] using min-max scaling.

    Parameters:
    - myList (list): List of numerical values to normalize.

    Returns:
    - ndarray: An array of normalized values.

    Requirements:
    - sklearn.preprocessing.MinMaxScaler
    - numpy

    Example:
    >>> myList = [10, 20, 30, 40, 50]
    >>> f_281(myList)
    array([0.  , 0.25, 0.5 , 0.75, 1.  ])
    """
    myList = np.array(myList).reshape(-1, 1)
    scaler = MinMaxScaler()
    normalized_list = scaler.fit_transform(myList)
    return normalized_list.flatten()

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_1(self):
        # Testing basic functionality
        input_data = [10, 20, 30, 40, 50]
        expected_output = np.array([0. , 0.25, 0.5 , 0.75, 1. ])
        np.testing.assert_array_almost_equal(f_281(input_data), expected_output, decimal=2)
    def test_2(self):
        # Testing with negative values
        input_data = [-50, -40, -30, -20, -10]
        expected_output = np.array([0. , 0.25, 0.5 , 0.75, 1. ])
        np.testing.assert_array_almost_equal(f_281(input_data), expected_output, decimal=2)
    def test_3(self):
        # Testing with mixed negative and positive values
        input_data = [-50, -25, 0, 25, 50]
        expected_output = np.array([0. , 0.25, 0.5 , 0.75, 1. ])
        np.testing.assert_array_almost_equal(f_281(input_data), expected_output, decimal=2)
    def test_4(self):
        # Testing with single value
        input_data = [100]
        expected_output = np.array([0.])
        np.testing.assert_array_almost_equal(f_281(input_data), expected_output, decimal=2)
    def test_5(self):
        # Testing with all zeros
        input_data = [0, 0, 0, 0, 0]
        expected_output = np.array([0., 0., 0., 0., 0.])
        np.testing.assert_array_almost_equal(f_281(input_data), expected_output, decimal=2)
