import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def f_811(df):
    """
    Creates and return a heatmap of the cumulative sum of each column in a pandas DataFrame.

    Parameters:
    - df (pandas.DataFrame): A DataFrame with numerical values.

    Returns:
    - matplotlib.axes._axes.Axes: The Axes object of the Seaborn heatmap.

    Raises:
    - ValueError: If the DataFrame is empty or if no numeric columns are present.

    Requirements:
    - pandas
    - matplotlib
    - seaborn

    Notes:
    - Only numeric columns are considered for the heatmap. Non-numeric columns are ignored.

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    >>> ax = f_811(df)
    """
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        raise ValueError("No numeric columns present")

    df_cumsum = numeric_df.cumsum()
    ax = sns.heatmap(df_cumsum)
    return ax

import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def tearDown(self):
        plt.close("all")
    def test_cumsum_correctness(self):
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        ax = f_811(df)
        result_cumsum = df.cumsum().values.flatten()
        heatmap_data = ax.collections[0].get_array().data.flatten()
        np.testing.assert_array_equal(
            result_cumsum, heatmap_data, "Cumulative sum calculation is incorrect"
        )
    def test_non_numeric_columns_ignored(self):
        df = pd.DataFrame({"A": [1, 2, 3], "B": ["one", "two", "three"]})
        ax = f_811(df)
        self.assertIsInstance(
            ax, plt.Axes, "The result should be a matplotlib Axes object"
        )
        self.assertEqual(
            len(ax.get_xticklabels()), 1, "Non-numeric columns should be ignored"
        )
    def test_with_positive_numbers(self):
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        result = f_811(df)
        self.assertIsInstance(
            result, plt.Axes, "The result should be a matplotlib Axes object"
        )
    def test_with_negative_numbers(self):
        df = pd.DataFrame({"A": [-1, -2, -3], "B": [-4, -5, -6]})
        result = f_811(df)
        self.assertIsInstance(
            result, plt.Axes, "The result should be a matplotlib Axes object"
        )
    def test_with_mixed_numbers(self):
        df = pd.DataFrame({"A": [1, -2, 3], "B": [-4, 5, -6]})
        result = f_811(df)
        self.assertIsInstance(
            result, plt.Axes, "The result should be a matplotlib Axes object"
        )
    def test_with_zeroes(self):
        df = pd.DataFrame({"A": [0, 0, 0], "B": [0, 0, 0]})
        result = f_811(df)
        self.assertIsInstance(
            result, plt.Axes, "The result should be a matplotlib Axes object"
        )
    def test_with_empty_dataframe(self):
        df = pd.DataFrame({"A": [], "B": []})
        with self.assertRaises(ValueError):
            f_811(df)
    def test_no_numeric_columns(self):
        df = pd.DataFrame({"A": ["one", "two", "three"], "B": ["four", "five", "six"]})
        with self.assertRaises(ValueError):
            f_811(df)
