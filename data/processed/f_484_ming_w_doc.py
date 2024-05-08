from itertools import chain
import numpy as np
from sklearn.cluster import KMeans


def f_486(L):
    """
    Convert a list of lists into a list of integers, apply the KMeans clustering, 
    and return a scatter plot 'matplotlib.axes.Axes' with data points color-coded by their cluster.

    Requirements:
    - itertools.chain
    - numpy
    - sklearn.cluster

    Parameters:
    L (list of lists): A list of lists where each sublist contains integers.

    Returns:
    matplotlib.axes.Axes: An Axes object representing the scatter plot.

    Example:
    >>> ax = f_486([[1, 2, 3], [50, 60, 70], [100, 110, 120]])
    """
    N_CLUSTERS = 3
    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)
    kmeans = KMeans(n_clusters=N_CLUSTERS).fit(data)
    fig, ax = plt.subplots()
    ax.scatter(data, [0]*len(data), c=kmeans.labels_.astype(float))
    return ax

import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = f_486([[1, 2, 3], [50, 60, 70], [100, 110, 120]])
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        ax = f_486([[1, 5], [2, 6], [3, 7]])
        self.assertIsInstance(ax, plt.Axes)
    def test_case_3(self):
        ax = f_486([[10, 20, 30, 40], [15, 25, 35, 45]])
        self.assertIsInstance(ax, plt.Axes)
    def test_case_4(self):
        ax = f_486([[1000, 2000], [3000, 4000], [5000, 6000]])
        self.assertIsInstance(ax, plt.Axes)
    def test_case_5(self):
        ax = f_486([[-1, -2, -3], [-50, -60, -70], [-100, -110, -120]])
        self.assertIsInstance(ax, plt.Axes)
