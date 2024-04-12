import pandas as pd
import numpy as np
from scipy import stats

def f_467(matrix):
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
    >>> matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> f_467(matrix)
    """
    df = pd.DataFrame(matrix)
    normalized_df = df.apply(stats.zscore)
    # Handle NaN values by replacing them with 0.0
    normalized_df = normalized_df.fillna(0.0)
    return normalized_df

import unittest
import numpy as np
import pandas as pd
from scipy import stats

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def test_case_1(self):
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = f_467(matrix)
        expected_result = pd.DataFrame({
            0: [-1.224745, 0.0, 1.224745],
            1: [-1.224745, 0.0, 1.224745],
            2: [-1.224745, 0.0, 1.224745]
        })
        pd.testing.assert_frame_equal(result, expected_result)

    def test_case_2(self):
        matrix = np.array([[2, 5], [5, 2]])
        result = f_467(matrix)
        expected_result = pd.DataFrame({
            0: [-1.0, 1.0],
            1: [1.0, -1.0]
        })
        pd.testing.assert_frame_equal(result, expected_result)

    def test_case_3(self):
        matrix = np.array([[5]])
        result = f_467(matrix)
        expected_result = pd.DataFrame({
            0: [0.0]
        })
        pd.testing.assert_frame_equal(result, expected_result)

    def test_case_4(self):
        matrix = np.array([[1, 3], [2, 4], [3, 5]])
        result = f_467(matrix)
        expected_result = pd.DataFrame({
            0: [-1.224745, 0.0, 1.224745],
            1: [-1.224745, 0.0, 1.224745]
        })
        pd.testing.assert_frame_equal(result, expected_result)

    def test_case_5(self):
        matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
        result = f_467(matrix)
        expected_result = pd.DataFrame({
            0: [-1.224745, 0.0, 1.224745],
            1: [-1.224745, 0.0, 1.224745],
            2: [-1.224745, 0.0, 1.224745]
        })
        pd.testing.assert_frame_equal(result, expected_result)
if __name__ == "__main__":
    run_tests()