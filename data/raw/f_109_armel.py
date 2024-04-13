import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore


def f_109(data_matrix):
    """
    Calculate the Z-values of a 2D data matrix, calculate the mean value of each row and then visualize the correlation matrix of the Z-values with a heatmap.

    Parameters:
    data_matrix (numpy.array): The 2D data matrix of shape (m, n) where m is the number of rows and n is the number of columns.

    Returns:
    tuple: A tuple containing:
      - pandas.DataFrame: A DataFrame with columns 'Feature 1', 'Feature 2', ..., 'Feature n' containing the Z-scores (per matrix row).
                      There is also an additional column 'Mean' the mean of z-score per row.
      - matplotlib.axes.Axes: The Axes object of the plotted heatmap.

    Requirements:
    - numpy
    - pandas
    - seaborn
    - scipy.stats.zscore
    - matplotlib.pyplot

    Example:
    >>> data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
    >>> df, ax = f_109(data)
    >>> print(df)
    """
    z_scores = zscore(data_matrix, axis=1)
    feature_columns = ["Feature " + str(i + 1) for i in range(data_matrix.shape[1])]
    df = pd.DataFrame(z_scores, columns=feature_columns)
    df["Mean"] = df.mean(axis=1)
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, fmt=".2f")
    return df, ax

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_109 function."""

    def test_case_1(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        df, ax = f_109(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)

    def test_case_2(self):
        data = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        df, ax = f_109(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)

    def test_case_3(self):
        data = np.array([[3, 5, 7, 1000], [200, 5, 7, 1], [1, -9, 14, 700]])
        df, ax = f_109(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)

    def test_case_4(self):
        data = np.array(
            [
                [1, 2, 3, 4, 5, 4, 3, 2, 1],
            ]
        )
        df, ax = f_109(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)

    def test_case_5(self):
        data = np.array([[1], [1], [1]])
        df, ax = f_109(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
