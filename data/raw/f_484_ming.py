import numpy as np
from itertools import chain
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def f_484(L):
    """
    Convert a list of lists into a list of integers, apply the KMeans clustering, 
    and return a scatter plot with data points color-coded by their cluster.
    
    This function utilizes the following libraries/modules:
    - numpy (for data reshaping)
    - itertools.chain (for list conversion)
    - sklearn.cluster.KMeans (for clustering)
    - matplotlib.pyplot (for plotting)

    Parameters:
    L (list of lists): A list of lists where each sublist contains integers.

    Returns:
    matplotlib.axes.Axes: An Axes object representing the scatter plot.

    Example:
    >>> ax = f_484([[1, 2, 3], [50, 60, 70], [100, 110, 120]])
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """
    # Constants
    N_CLUSTERS = 3

    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)

    kmeans = KMeans(n_clusters=N_CLUSTERS).fit(data)

    fig, ax = plt.subplots()
    ax.scatter(data, [0]*len(data), c=kmeans.labels_.astype(float))
    
    return ax

import unittest
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FunctionTests))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class FunctionTests(unittest.TestCase):
    def test_case_1(self):
        ax = f_484([[1, 2, 3], [50, 60, 70], [100, 110, 120]])
        self.assertIsInstance(ax, plt.Axes)

    def test_case_2(self):
        ax = f_484([[1, 5], [2, 6], [3, 7]])
        self.assertIsInstance(ax, plt.Axes)

    def test_case_3(self):
        ax = f_484([[10, 20, 30, 40], [15, 25, 35, 45]])
        self.assertIsInstance(ax, plt.Axes)

    def test_case_4(self):
        ax = f_484([[1000, 2000], [3000, 4000], [5000, 6000]])
        self.assertIsInstance(ax, plt.Axes)

    def test_case_5(self):
        ax = f_484([[-1, -2, -3], [-50, -60, -70], [-100, -110, -120]])
        self.assertIsInstance(ax, plt.Axes)

if __name__ == "__main__":
    run_tests()