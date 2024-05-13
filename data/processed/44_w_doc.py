from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


def task_func(df):
    """
    Normalize numeric columns in a DataFrame and draw a box plot for each column. Missing values are replaced by column's average.

    Parameters:
    df (DataFrame): The pandas DataFrame.

    Returns:
    DataFrame: A pandas DataFrame after normalization.
    Axes: A matplotlib Axes displaying a box plot for each column.

    Requirements:
    - pandas
    - numpy
    - sklearn.preprocessing.MinMaxScaler
    - matplotlib.pyplot

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> df = pd.DataFrame([[1,2,3],[4,5,6],[7.0,np.nan,9.0]], columns=["c1","c2","c3"])
    >>> df, ax = task_func(df)
    >>> print(df)
        c1   c2   c3
    0  0.0  0.0  0.0
    1  0.5  1.0  0.5
    2  1.0  0.5  1.0
    """

    df = df.fillna(df.mean(axis=0))
    scaler = MinMaxScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])
    plt.figure(figsize=(10, 5))
    df.boxplot(grid=False, vert=False, fontsize=15)
    return df, plt.gca()

import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        df = pd.DataFrame(
            [[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"]
        )
        normalized_df, ax = task_func(df)
        self.assertTrue(np.allclose(normalized_df["c1"].tolist(), [0.0, 0.5, 1.0]))
        self.assertTrue(np.allclose(normalized_df["c2"].tolist(), [0.0, 1.0, 0.5]))
        self.assertTrue(np.allclose(normalized_df["c3"].tolist(), [0.0, 0.5, 1.0]))
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["c1", "c2", "c3"])
        normalized_df, ax = task_func(df)
        self.assertTrue(np.allclose(normalized_df["c1"].tolist(), [0.0, 0.5, 1.0]))
        self.assertTrue(np.allclose(normalized_df["c2"].tolist(), [0.0, 0.5, 1.0]))
        self.assertTrue(np.allclose(normalized_df["c3"].tolist(), [0.0, 0.5, 1.0]))
        self.assertIsInstance(ax, plt.Axes)
    def test_case_3(self):
        df = pd.DataFrame(
            [[1, 2, 3, 4, 5], [None, None, None, None, None]],
            columns=["c1", "c2", "c3", "c4", "c5"],
        )
        normalized_df, ax = task_func(df)
        for col in df.columns:
            self.assertTrue(normalized_df[col].max() <= 1.0)
            self.assertTrue(normalized_df[col].min() >= 0.0)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_4(self):
        df = pd.DataFrame(
            [[11, 2, 13, 7], [1, 5, 6, 16], [15, 3, 14, 9], [8, 10, 4, 12]],
            columns=["c1", "c2", "c3", "c4"],
        )
        normalized_df, ax = task_func(df)
        for col in df.columns:
            self.assertTrue(normalized_df[col].max() <= 1.0)
            self.assertTrue(normalized_df[col].min() >= 0.0)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_5(self):
        df = pd.DataFrame(
            [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], columns=["c1", "c2"]
        )
        normalized_df, ax = task_func(df)
        for col in df.columns:
            self.assertTrue(np.isclose(normalized_df[col].max(), 1.0, atol=1e-5))
            self.assertTrue(normalized_df[col].min() >= 0.0)
        self.assertListEqual(
            normalized_df.loc[:, "c1"].tolist(), [0.0, 0.25, 0.5, 0.75, 1.0]
        )
        self.assertListEqual(
            normalized_df.loc[:, "c2"].tolist(), [0.0, 0.25, 0.5, 0.75, 1.0]
        )
        self.assertIsInstance(ax, plt.Axes)
