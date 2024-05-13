import seaborn as sns
import matplotlib.pyplot as plt


def task_func(df, target_values=[1, 3, 4]):
    """
    Replace all elements in DataFrame columns that do not exist in the target_values array with zeros, and then output the distribution of each column after replacing.
    - label each plot as the name of the column it corresponds to.

    Parameters:
    - df (DataFrame): The input pandas DataFrame.
    - target_values (list) : Array of values not to replace by zero.

    Returns:
    - matplotlib.axes.Axes: The Axes object of the plotted data.

    Requirements:
    - seaborn
    - matplotlib.pyplot

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.randint(0,10,size=(100, 5)), columns=list('ABCDE'))
    >>> print(df.head(2))
       A  B  C  D  E
    0  6  3  7  4  6
    1  9  2  6  7  4
    >>> df1, ax = task_func(df)
    >>> print(ax)
    Axes(0.125,0.11;0.775x0.77)
    """

    df = df.applymap(lambda x: x if x in target_values else 0)
    plt.figure(figsize=(10, 5))
    for column in df.columns:
        sns.kdeplot(df[column], label=column, warn_singular=False)
    plt.legend()
    return df, plt.gca()

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        df = pd.DataFrame({"A": [1, 4, 7, 6, 7, 3, 4, 4]})
        df1, ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [7, 4, 3, 3, 1]})
        df1, ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)
    def test_case_3(self):
        df = pd.DataFrame({"A": [5, 6, 2, 9, 7, 3, 2, 2, 8, 1]})
        target_values = [1, 2, 3, 4, 5]
        df1, ax = task_func(df, target_values=target_values)
        mask = df1.isin(target_values) | (df1 == 0)
        self.assertTrue(mask.all().all())
        self.assertIsInstance(ax, plt.Axes)
    def test_case_4(self):
        df = pd.DataFrame({"A": [10, 20, 30, 40, 50], "B": [50, 40, 10, 10, 30]})
        target_values = [10, 20, 30]
        df1, ax = task_func(df, target_values=target_values)
        mask = df1.isin(target_values) | (df1 == 0)
        self.assertTrue(mask.all().all())
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)
    def test_case_5(self):
        df = pd.DataFrame({"A": [5, 6, 2, 9, 7, 3, 2, 2, 8, 1]})
        df1, ax = task_func(df, target_values=[])
        self.assertTrue(df1.eq(0).all().all())
        self.assertIsInstance(ax, plt.Axes)
    def test_case_7(self):
        df = pd.DataFrame({"A": [5, 6, 2, 9, 7, 3, 2, 2, 8, 1]})
        df1, ax = task_func(df, target_values=[5, 6, 2, 9, 7, 3, 8, 1])
        self.assertTrue(df1.equals(df))
        self.assertIsInstance(ax, plt.Axes)
