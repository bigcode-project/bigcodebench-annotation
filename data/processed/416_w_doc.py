import pandas as pd
import seaborn as sns


def task_func(data, column="c"):
    """
    Removes a column from a given data dictionary and creates a heatmap
    of the correlation matrix of the remaining data. Non-numeric columns are
    excluded from the heatmap. If the data is empty or has no numeric columns,
    the function returns None.

    Parameters:
    - data: The input data dictionary.
    - column (str): Name of column to remove. Defaults to "c".

    Returns:
    - matplotlib.axes._axes.Axes or None: The Axes object of the heatmap
      or None if the heatmap is not generated.

    Requirements:
    - pandas
    - seaborn

    Example:
    >>> task_func({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    <Axes: >
    >>> task_func(pd.DataFrame({'a': ["foo", "bar"]}))
    """

    df = pd.DataFrame(data)
    if column in df.columns:
        df = df.drop(columns=column)
    df = df.select_dtypes(include=["number"])
    if df.empty:
        return None
    return sns.heatmap(df.corr())

import unittest
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
class TestCases(unittest.TestCase):
    def _assert_heatmap_matches_corr(self, ax, corr):
        # Helper function to assert that the heatmap matches the correlation matrix
        heatmap_data = ax.collections[0].get_array().data
        np.testing.assert_array_almost_equal(
            heatmap_data, corr.values.flatten(), decimal=2
        )
    def test_case_1(self):
        # Input: DataFrame with column "c".
        data = {
                "a": list(range(10)),
                "b": list(range(10)),
                "c": list(range(10)),
            }
        df = pd.DataFrame(
            data
        )
        ax = task_func(data)
        # Assert that column "c" is not in the heatmap
        self.assertNotIn("c", [col.get_text() for col in ax.get_xticklabels()])
        # Check plotted value correctness
        self._assert_heatmap_matches_corr(ax, df.drop(columns=["c"]).corr())
    def test_case_2(self):
        # Input: DataFrame without column "c".
        data = {"a": list(range(10)), "b": list(range(10))}
        df = pd.DataFrame(data)
        ax = task_func(data)
        # Assert that columns "a" and "b" are in the heatmap
        self.assertIn("a", [col.get_text() for col in ax.get_xticklabels()])
        self.assertIn("b", [col.get_text() for col in ax.get_xticklabels()])
        # Check plotted value correctness
        self._assert_heatmap_matches_corr(ax, df.corr())
    def test_case_3(self):
        # Input: DataFrame with column "c", but we specify another column to remove
        data = {
                "a": list(range(10)),
                "b": list(range(10)),
                "c": list(range(10)),
            }
        df = pd.DataFrame(
            data
        )
        ax = task_func(data, column="b")
        # Assert that column "b" is not in the heatmap
        self.assertNotIn("b", [col.get_text() for col in ax.get_xticklabels()])
        # Assert that other columns are in the heatmap
        self.assertIn("a", [col.get_text() for col in ax.get_xticklabels()])
        self.assertIn("c", [col.get_text() for col in ax.get_xticklabels()])
        # Check plotted value correctness
        self._assert_heatmap_matches_corr(ax, df.drop(columns=["b"]).corr())
    def test_case_4(self):
        # Input: DataFrame with non-numeric columns and column "c".
        data = {
                "a": list(range(4)),
                "b": ["low", "medium", "high", "medium"],
                "c": ["apple", "banana", "cherry", "dates"],
            }
        df = pd.DataFrame(
            data
        )
        ax = task_func(data)
        # Assert that only numeric column "a" is in the heatmap
        self.assertIn("a", [col.get_text() for col in ax.get_xticklabels()])
        self.assertNotIn("b", [col.get_text() for col in ax.get_xticklabels()])
        self.assertNotIn("c", [col.get_text() for col in ax.get_xticklabels()])
    def test_case_5(self):
        # Input: DataFrame with missing values and column "c".
        np.random.seed(0)
        data = {
                "a": np.random.choice([1, np.nan], 100),
                "b": np.random.choice([2, np.nan], 100),
                "c": np.random.choice([3, np.nan], 100),
            }
        df = pd.DataFrame(
            data
        )
        ax = task_func(data)
        # Assert that columns "a" and "b" are in the heatmap and column "c" is not
        self.assertIn("a", [col.get_text() for col in ax.get_xticklabels()])
        self.assertIn("b", [col.get_text() for col in ax.get_xticklabels()])
        self.assertNotIn("c", [col.get_text() for col in ax.get_xticklabels()])
    def test_case_6(self):
        # Input: Empty DataFrame.
        data = {}
        df = pd.DataFrame(data)
        ax = task_func(data)
        # Assert that the function returns None for an empty DataFrame
        self.assertIsNone(ax)
    def tearDown(self):
        plt.close("all")
