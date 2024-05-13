import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    """
    Replace all elements in DataFrame columns that do not exist in the TARGET_VALUES array with zeros, then perform a Box-Cox transformation on each column (if data is not constant, add 1 to account for zeros) and display the resulting KDE plots.

    Parameters:
        - df (pandas.DataFrame): The input pandas DataFrame with positive values.

    Returns:
        - pandas.DataFrame: The transformed DataFrame after Box-Cox transformation.
        - matplotlib.figure.Figure: Figure containing KDE plots of the transformed columns.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.randint(1, 10, size=(100, 5)), columns=list('ABCDE'))  # Values should be positive for Box-Cox
    >>> transformed_df, fig = task_func(df)
    >>> print(transformed_df.head(2))
              A         B    C    D         E
    0  0.000000  0.566735  0.0  0.0  0.000000
    1  0.530493  0.000000  0.0  0.0  0.607007
    """

    if (df <= 0).any().any():
        raise ValueError("Input DataFrame should contain only positive values.")
    df = df.applymap(lambda x: x if x in TARGET_VALUES else 0)
    transformed_df = pd.DataFrame()
    fig, ax = plt.subplots()
    for column in df.columns:
        if df[column].nunique() == 1:
            transformed_df[column] = df[column]
        else:
            transformed_data, _ = stats.boxcox(
                df[column] + 1
            )  # Add 1 since the are some null values
            transformed_df[column] = transformed_data
            kde = stats.gaussian_kde(transformed_df[column])
            x_vals = np.linspace(
                min(transformed_df[column]), max(transformed_df[column]), 1000
            )
            ax.plot(x_vals, kde(x_vals), label=column)
    ax.legend()
    plt.show()
    return transformed_df, fig

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        df = pd.DataFrame(
            {
                "A": [1, 2, 3, 4, 3, 2, 2, 1],
                "B": [7, 8, 9, 1, 2, 3, 5, 6],
                "C": [9, 7, 3, 1, 8, 6, 2, 1],
            }
        )
        transformed_df, fig = task_func(df)
        self.assertEqual(transformed_df.shape, df.shape)
    def test_case_2(self):
        df = pd.DataFrame({"A": [1, 1, 1], "B": [3, 3, 3], "C": [4, 4, 4]})
        transformed_df, fig = task_func(df)
        self.assertEqual(transformed_df.shape, df.shape)
        self.assertEqual(len(fig.axes[0].lines), 0)
        pd.testing.assert_frame_equal(transformed_df, df)
    def test_case_3(self):
        df = pd.DataFrame(
            {
                "A": [1, 7, 5, 4],
                "B": [3, 11, 1, 29],
                "C": [4, 9, 8, 4],
                "D": [16, 12, 20, 8],
            }
        )
        transformed_df, fig = task_func(df)
        self.assertEqual(transformed_df.shape, df.shape)
        self.assertEqual(len(fig.axes[0].lines), 3)
    def test_case_4(self):
        df = pd.DataFrame(
            {
                "E": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "F": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            }
        )
        transformed_df, fig = task_func(df)
        self.assertEqual(transformed_df.shape, df.shape)
        self.assertEqual(len(fig.axes[0].lines), 1)
    def test_case_5(self):
        df = pd.DataFrame(
            {
                "A": [0, 0, 0, 0],
            }
        )
        with self.assertRaises(ValueError):
            transformed_df, _ = task_func(df)
    def test_case_6(self):
        df = pd.DataFrame(
            {
                "A": [1, 2, 3, -4],
            }
        )
        with self.assertRaises(ValueError):
            transformed_df, _ = task_func(df)
