import random
import matplotlib.pyplot as plt

# Constants
DISTRIBUTION_SIZE = 1000

def f_283(bins=30):
    """
    Generate a Gaussian distribution and plot its histogram.

    Parameters:
    - bins (int, optional): Number of bins for the histogram. Default is 30.

    Returns:
    - tuple: A tuple containing the distribution list and the Axes object of the histogram plot.

    Requirements:
    - random
    - matplotlib.pyplot

    Example:
    >>> distribution, ax = f_283()
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    >>> len(distribution)
    1000
    """

    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]
    ax = plt.hist(distribution, bins=bins, edgecolor='black')[2]
    return distribution, ax

import unittest
import matplotlib.pyplot as plt
import numpy as np

class TestCases(unittest.TestCase):
    def test_histogram_axes_type(self):
        _, ax = f_283()
        self.assertTrue(ax, plt.Axes)

    def test_distribution_length(self):
        distribution, _ = f_283()
        self.assertEqual(len(distribution), 1000)

    def test_distribution_type(self):
        distribution, _ = f_283()
        self.assertIsInstance(distribution, list, "Distribution should be a list")
        self.assertTrue(all(isinstance(x, float) for x in distribution))

    def test_histogram_bin_count(self):
        _, ax = f_283(bins=20)
        self.assertEqual(len(ax.patches), 20)

    def test_default_bin_count(self):
        _, ax = f_283()
        self.assertEqual(len(ax.patches), 30)
    
    def test_plot_distribution(self):
        distribution, ax = f_283()
        heights, bins, _ = plt.hist(distribution)
        expected_heights, _ = np.histogram(distribution, bins=bins)
        np.testing.assert_allclose(heights, expected_heights, rtol=0.1, err_msg="Distribution not plotted correctly")



def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_tests()