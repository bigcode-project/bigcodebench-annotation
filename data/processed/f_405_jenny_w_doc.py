import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


def f_66(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    """
    Converts a 2D list into a pandas DataFrame and applies PCA for dimensionality reduction.

    This function creates a DataFrame from the provided 2D list and then applies PCA to reduce the dataset
    to its two main components. The function uses a fixed random seed to ensure reproducibility.

    Parameters:
    - array (list of list of int): A 2D list representing data rows and columns.
    - random_seed (int, optional): The seed for the random number generator. Default is 42.

    Returns:
    - pd.DataFrame: The original data in DataFrame format.
    - np.ndarray: The data after PCA transformation.

    Requirements:
    - pandas
    - numpy
    - sklearn.decomposition.PCA

    Examples:
    >>> data = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
    >>> df, transformed = f_66(data)
    >>> print(df)
        0   1   2   3   4
    0   1   2   3   4   5
    1   6   7   8   9  10
    2  11  12  13  14  15
    >>> print(transformed[:, 0])
    [ 11.18033989  -0.         -11.18033989]
    """
    df = pd.DataFrame(array)

    pca = PCA(n_components=2, random_state=random_seed)
    transformed_data = pca.fit_transform(df)

    return df, transformed_data

import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic 2-row dataset
        data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        df, transformed_data = f_66(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (2, 2))
    def test_case_2(self):
        # Test basic 3-row dataset
        data = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]]
        df, transformed_data = f_66(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (3, 2))
    def test_case_3(self):
        # Test mix of positive, negative, zero values
        data = [[-1, -2, -3, -4, -5], [5, 6, 7, 8, 9], [0, 0, 0, 0, 0]]
        df, transformed_data = f_66(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (3, 2))
    def test_case_4(self):
        # Test 4-row dataset with incremental pattern
        data = [
            [5, 15, 25, 35, 45],
            [55, 65, 75, 85, 95],
            [105, 115, 125, 135, 145],
            [155, 165, 175, 185, 195],
        ]
        df, transformed_data = f_66(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (4, 2))
    def test_case_5(self):
        # Test uniform rows
        data = [[10, 10, 10, 10, 10], [20, 20, 20, 20, 20], [30, 30, 30, 30, 30]]
        df, transformed_data = f_66(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (3, 2))
    def test_case_6(self):
        # Test single row (should fail since it's < n_components)
        with self.assertRaises(ValueError):
            data = [[1, 2, 3, 4, 5]]
            f_66(data)
    def test_case_7(self):
        # Test large numbers
        data = [[1000000000, 2000000000], [-1000000000, -2000000000]]
        df, transformed_data = f_66(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (2, 2))
    def test_case_8(self):
        # Test correctness of PCA
        data = [[2, 3], [3, 4], [5, 6]]
        _, transformed_data = f_66(data)
        # Using the sklearn PCA output as the expected transformation
        expected_transformation = np.array(
            [
                [-1.88561808e00, 1.93816421e-16],
                [-4.71404521e-01, 3.32511118e-16],
                [2.35702260e00, 2.21555360e-16],
            ]
        )
        np.testing.assert_almost_equal(
            transformed_data, expected_transformation, decimal=5
        )
    def test_case_9(self):
        # Test floats
        data = [[1.5, 2.5], [3.5, 4.5], [5.5, 6.5]]
        df, transformed_data = f_66(data)
        expected_df = pd.DataFrame(data)
        self.assertTrue(df.equals(expected_df))
        self.assertEqual(transformed_data.shape, (3, 2))
