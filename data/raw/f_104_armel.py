import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def f_104(df, target_values=np.array([1, 3, 4])):
    """
    Replace all elements in DataFrame columns that do not exist in the target_values array with zeros, and then output the distribution of each column after replacing.
    - label each plot as the name of the column it corresponds to.

    Parameters:
    - df (DataFrame): The input pandas DataFrame.
    - target_values (numpy.ndarray) : Array of values not to replace by zero.

    Returns:
    - matplotlib.axes.Axes: The Axes object of the plotted data.

    Requirements:
    - numpy
    - pandas
    - seaborn
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame(np.random.randint(0,10,size=(100, 5)), columns=list('ABCDE'))
    >>> f_104(df)
    """
    df = df.applymap(lambda x: x if x in target_values else 0)
    plt.figure(figsize=(10, 5))
    for column in df.columns:
        sns.kdeplot(df[column], label=column)
    plt.legend()
    return plt.gca()


import unittest


class TestCases(unittest.TestCase):
    """Test cases for the f_104 function."""

    def test_case_1(self):
        df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [7, 4, 3, 3, 1]})
        ax = f_104(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)

    def test_case_2(self):
        df = pd.DataFrame({"A": [10, 20, 30, 40, 50], "B": [50, 40, 10, 10, 30]})
        ax = f_104(df, target_values=np.array([10, 20, 30]))
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)

    def test_case_3(self):
        df = pd.DataFrame({"A": [5, 6, 2, 9, 7, 3, 2, 2, 8, 1]})
        ax = f_104(df, target_values=np.array([1, 2, 3, 4, 5]))
        self.assertIsInstance(ax, plt.Axes)

    def test_case_4(self):
        df = pd.DataFrame({"A": [1, 4, 7, 6, 7, 3, 4, 4]})
        ax = f_104(df)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_5(self):
        df = pd.DataFrame({"A": [1, 3, 5, 3, 1]})
        ax = f_104(df)
        self.assertIsInstance(ax, plt.Axes)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
