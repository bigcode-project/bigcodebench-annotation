import pandas as pd
import seaborn as sns


def f_68(array):
    """Generates a DataFrame and heatmap from a 2D list.

    This function takes a 2D list and returns a pandas DataFrame and a seaborn heatmap
    representing the correlation matrix of the DataFrame. Assumes sublists of length 5.
    Also assumes DataFrame columns: 'A', 'B', 'C', 'D', 'E'.

    Parameters:
    - array (list of list of int): 2D list with sublists of length 5. Must not be empty.

    Returns:
    - DataFrame: Constructed from the input 2D list.
    - heatmap: Seaborn heatmap of the DataFrame's correlation matrix.

    Requirements:
    - pandas
    - seaborn

    Example:
    >>> df, ax = f_68([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
    >>> df
       A  B  C  D  E
    0  1  2  3  4  5
    1  5  4  3  2  1
    >>> ax
    <Axes: >
    """
    COLUMNS = ["A", "B", "C", "D", "E"]

    if not array or any(len(sublist) != 5 for sublist in array):
        raise ValueError("array must be non-empty and all sublists must have a length of 5.")

    df = pd.DataFrame(array, columns=COLUMNS)
    heatmap = sns.heatmap(df.corr(), annot=True)
    return df, heatmap

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        random.seed(42)
        cls.mock_data = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
    def test_case_1(self):
        # Test dataframe creation with valid input
        df, _ = f_68(self.mock_data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (5, 5))
    def test_case_2(self):
        # Test heatmap creation with valid input
        _, heatmap = f_68(self.mock_data)
        self.assertIsNotNone(heatmap)
    def test_case_3(self):
        # Test correlation accuracy with known data
        correlated_data = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
        df, _ = f_68(correlated_data)
        corr_matrix = df.corr()
        np.testing.assert_array_almost_equal(
            corr_matrix, np.corrcoef(correlated_data, rowvar=False)
        )
    def test_case_4(self):
        # Test handling of non-numeric data
        with self.assertRaises(ValueError):
            f_68([["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5]])
    def test_case_5(self):
        # Test with empty list
        with self.assertRaises(ValueError):
            f_68([])
    def test_case_6(self):
        # Test with single sublist
        single_sublist = [[1, 2, 3, 4, 5]]
        df, _ = f_68(single_sublist)
        self.assertEqual(df.shape, (1, 5))
    def test_case_7(self):
        # Test handling sublists of varying lengths
        with self.assertRaises(ValueError):
            f_68([[1, 2, 3], [4, 5, 6, 7, 8]])
    def tearDown(self):
        plt.close("all")
