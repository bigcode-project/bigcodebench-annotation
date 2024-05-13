import pandas as pd
from scipy import stats


def task_func(matrix):
    """
    Normalizes a 2D numeric array (matrix) using the Z score.
    
    Parameters:
    matrix (array): The 2D numpy array.
    
    Returns:
    DataFrame: The normalized DataFrame.

    Requirements:
    - pandas
    - numpy
    - scipy

    Example:
    >>> import numpy as np
    >>> matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> normalized_df = task_func(matrix)
    >>> isinstance(normalized_df, pd.DataFrame)
    True
    >>> np.allclose(normalized_df.mean(), 0)
    True
    >>> np.allclose(normalized_df.std(ddof=0), 1)
    True
    """

    df = pd.DataFrame(matrix)
    normalized_df = df.apply(stats.zscore)
    normalized_df = normalized_df.fillna(0.0)
    return normalized_df

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_extreme_values_shape(self):
        """Test the function with extreme values to ensure output shape is correct."""
        matrix = [[1, 2], [10000, 20000]]
        result_df = task_func(matrix)
        # Verify that the shape of the result is the same as the input
        self.assertEqual(result_df.shape, (2, 2))
    def test_case_2(self):
        matrix = np.array([[2, 5], [5, 2]])
        result = task_func(matrix)
        expected_result = pd.DataFrame({
            0: [-1.0, 1.0],
            1: [1.0, -1.0]
        })
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_3(self):
        matrix = np.array([[5]])
        result = task_func(matrix)
        expected_result = pd.DataFrame({
            0: [0.0]
        })
        pd.testing.assert_frame_equal(result, expected_result)
    def test_uniform_data(self):
        """Test a matrix where all elements are the same."""
        matrix = [[1, 1], [1, 1]]
        expected_result = pd.DataFrame({
            0: [0.0, 0.0],
            1: [0.0, 0.0]
        })
        pd.testing.assert_frame_equal(task_func(matrix), expected_result)
    def test_non_numeric_data(self):
        """Test the function with non-numeric data."""
        matrix = [['a', 'b'], ['c', 'd']]
        with self.assertRaises(TypeError):
            task_func(matrix)
