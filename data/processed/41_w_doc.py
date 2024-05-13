import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew


def task_func(data_matrix):
    """
    Calculate the skew of each row in a 2D data matrix and plot the distribution.

    Parameters:
    - data_matrix (numpy.array): The 2D data matrix.

    Returns:
    pandas.DataFrame: A DataFrame containing the skewness of each row. The skweness is stored in a new column which name is 'Skewness'.
    matplotlib.axes.Axes: The Axes object of the plotted distribution.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - scipy.stats.skew

    Example:
    >>> import numpy as np
    >>> data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
    >>> df, ax = task_func(data)
    >>> print(df)
       Skewness
    0  0.122440
    1  0.403407
    """

    skewness = skew(data_matrix, axis=1)
    df = pd.DataFrame(skewness, columns=["Skewness"])
    plt.figure(figsize=(10, 5))
    df["Skewness"].plot(kind="hist", title="Distribution of Skewness")
    return df, plt.gca()

import unittest
import os
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_dir = "data/task_func"
        os.makedirs(self.test_dir, exist_ok=True)
    def test_case_1(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        df, ax = task_func(data)
        self.verify_output(df, ax, data.shape[0], data)
    def test_case_2(self):
        data = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        df, ax = task_func(data)
        self.verify_output(df, ax, data.shape[0], data)
    def test_case_3(self):
        data = np.array([[3, 5, 7, 1000], [200, 5, 7, 1], [1, -9, 14, 700]])
        df, ax = task_func(data)
        self.verify_output(df, ax, data.shape[0], data)
    def test_case_4(self):
        data = np.array(
            [
                [1, 2, 3, 4, 5, 4, 3, 2, 1],
            ]
        )
        df, ax = task_func(data)
        self.verify_output(df, ax, data.shape[0], data)
    def test_case_5(self):
        data = np.array([[1, 1], [1, 1], [1, 1]])
        df, ax = task_func(data)
        # Check if DataFrame is returned with correct values
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 1))
        self.assertIn("Skewness", df.columns)
        # Check if Axes object is returned for the plot
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Distribution of Skewness")
    def verify_output(self, df, ax, expected_rows, data):
        # Check if DataFrame is returned with correct values
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (expected_rows, 1))
        self.assertIn("Skewness", df.columns)
        # Check if Axes object is returned for the plot
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Distribution of Skewness")
        # Check skewness values
        skewness = skew(data, axis=1)
        self.assertListEqual(df["Skewness"].tolist(), list(skewness))
