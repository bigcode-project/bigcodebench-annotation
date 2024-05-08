import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain


def f_485(L):
    '''
    Convert a list of lists 'L' into a flattened list of integers, then fit a normal distribution to the data 
    and plot a histogram with the fitted normal distribution overlay.

    Requirements:
    - numpy
    - itertools.chain
    - scipy.stats.norm
    - matplotlib.pyplot

    Parameters:
    L (list of lists): A nested list where each inner list contains integers.

    Returns:
    matplotlib.axes._axes.Axes: Axes object with the plotted histogram and normal distribution overlay.

    Example:
    >>> ax = f_485([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    '''
    data = list(chain(*L))
    mu, std = norm.fit(data)
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    ax.set_title(title)
    return ax

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ax = f_485(L)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        L = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        ax = f_485(L)
        self.assertIsInstance(ax, plt.Axes)
        # self.assertIn("Fit results:", ax.get_title())
    def test_case_3(self):
        L = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        ax = f_485(L)
        self.assertIsInstance(ax, plt.Axes)
        # self.assertIn("Fit results:", ax.get_title())
    def test_case_4(self):
        L = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ax = f_485(L)
        self.assertIsInstance(ax, plt.Axes)
        # self.assertIn("Fit results:", ax.get_title())
    def test_case_5(self):
        L = [[5, 15, 25], [35, 45, 55], [65, 75, 85]]
        ax = f_485(L)
        self.assertIsInstance(ax, plt.Axes)
