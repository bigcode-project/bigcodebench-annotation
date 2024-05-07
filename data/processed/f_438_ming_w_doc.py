import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


def f_640(a, b):
    """
    Calculate the Pearson correlation coefficient of two lists, generate a Pandas DataFrame from these lists, and then draw a scatter plot with a regression line.

    Parameters:
    a (list): A list of numbers.
    b (list): Another list of numbers.

    Requirements:
    - numpy
    - pandas
    - scipy
    - matplotlib.pyplot

    Returns:
    - tuple: Contains two elements:
        - float: The Pearson correlation coefficient.
        - matplotlib.axes.Axes: The Axes object of the plotted scatter plot with a regression line.


    Example:
    >>> correlation, ax = f_640([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
    >>> isinstance(correlation, float) and isinstance(ax, matplotlib.axes.Axes)
    True
    >>> round(correlation, 1)
    1.0
    """
    correlation, _ = stats.pearsonr(a, b)
    df = pd.DataFrame({'A': a, 'B': b})
    plt.scatter(df['A'], df['B'])
    plt.plot(np.unique(df['A']), np.poly1d(np.polyfit(df['A'], df['B'], 1))(np.unique(df['A'])), color='red')
    plt.show()
    return correlation, plt.gca()

import unittest
import math
import matplotlib
class TestCases(unittest.TestCase):
    def test_case_1(self):
        correlation, ax = f_640([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        self.assertAlmostEqual(correlation, 1.0)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_2(self):
        correlation, ax = f_640([1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
        self.assertTrue(math.isnan(correlation))
    def test_case_3(self):
        correlation, ax = f_640([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        self.assertAlmostEqual(correlation, -1.0)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_4(self):
        correlation, ax = f_640([2, 4, 6, 8, 10], [1, 2, 3, 4, 5])
        self.assertAlmostEqual(correlation, 1.0)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_5(self):
        correlation, ax = f_640([1, 3, 5, 7, 9], [9, 7, 5, 3, 1])
        self.assertAlmostEqual(correlation, -1.0)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
