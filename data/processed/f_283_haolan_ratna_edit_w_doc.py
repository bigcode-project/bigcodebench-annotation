import random
import matplotlib.pyplot as plt

# Constants
DISTRIBUTION_SIZE = 1000

def f_215(bins=30):
    """
    Generate a Gaussian distribution and plot its histogram.

    Parameters:
    - bins (int, optional): Number of bins for the histogram. Default is 30.

    Returns:
    - tuple: A tuple containing the distribution list and the Axes patch object of the histogram plot.

    Requirements:
    - random
    - matplotlib.pyplot

    Example:
    >>> random.seed(0)
    >>> distribution, ax = f_215()
    >>> len(ax.patches) == 30
    True
    >>> len(distribution)
    1000
    >>> plt.close()
    """
    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]
    ax = plt.hist(distribution, bins=bins, edgecolor='black')[2]
    return distribution, ax

import unittest
import matplotlib.pyplot as plt
import numpy as np
import random
class TestCases(unittest.TestCase):
    def test_histogram_axes_type(self):
        random.seed(0)
        _, ax = f_215()
        self.assertTrue(ax, plt.Axes)
        plt.close()
    def test_distribution_length(self):
        random.seed(0)
        distribution, _ = f_215()
        self.assertEqual(len(distribution), 1000)
        plt.close()
    def test_distribution_type(self):
        random.seed(0)
        distribution, _ = f_215()
        self.assertIsInstance(distribution, list, "Distribution should be a list")
        self.assertTrue(all(isinstance(x, float) for x in distribution))
        plt.close()
    def test_histogram_bin_count(self):
        random.seed(0)
        _, ax = f_215(bins=20)
        self.assertEqual(len(ax.patches), 20)
        plt.close()
    def test_default_bin_count(self):
        random.seed(0)
        _, ax = f_215()
        self.assertEqual(len(ax.patches), 30)
        plt.close()
    
    def test_plot_distribution(self):
        random.seed(0)
        distribution, ax = f_215()
        heights, bins, _ = plt.hist(distribution)
        expected_heights, _ = np.histogram(distribution, bins=bins)
        np.testing.assert_allclose(heights, expected_heights, rtol=0.1, err_msg="Distribution not plotted correctly")
        plt.close()
