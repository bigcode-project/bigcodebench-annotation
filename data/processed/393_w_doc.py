import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def task_func(mu, sigma, num_samples=1000, seed=77):
    """
    Generate a normal distribution with the given mean and standard deviation. 
    Creates a figure containing a histogram and a Q-Q plot of the generated samples.

    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    num_samples (int, Optional): The number of samples to generate. Default is 1000.
    seed (int, Optional): The seed for the random number generator. Default is 77.

    Returns:
    matplotlib.figure.Figure: A matplotlib figure containing the histogram and Q-Q plot.

    Requirements:
    - numpy for generating the samples.
    - matplotlib.pyplot for plotting.
    - scipy.stats for the Q-Q plot.

    Example:
    >>> fig = task_func(0, 1)
    >>> type(fig)
    <class 'matplotlib.figure.Figure'>
    """
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)
    fig = plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    plt.subplot(1, 2, 2)
    stats.probplot(samples, dist="norm", plot=plt)
    return fig

import unittest
from matplotlib import colors as mcolors
from matplotlib.figure import Figure
import doctest
class TestCases(unittest.TestCase):
    def test_standard_normal_distribution(self):
        """Test with standard normal distribution parameters (mu=0, sigma=1)."""
        fig = task_func(0, 1)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)  # Should contain two subplots
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def test_nonzero_mean(self):
        """Test with a nonzero mean."""
        mu = 5
        sigma = 1
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def test_different_standard_deviation(self):
        """Test with a different standard deviation."""
        mu = 0
        sigma = 2
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def test_negative_mean(self):
        """Test with a negative mean."""
        mu = -5
        sigma = 1
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def test_large_standard_deviation(self):
        """Test with a large standard deviation."""
        mu = 0
        sigma = 5
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def _test_histogram_attributes(self, ax, expected_bins, color):
        """Helper function to test histogram attributes."""
        n, bins, patches = ax.hist([], bins=expected_bins, color=color)  # Dummy histogram to get attributes
        self.assertEqual(expected_bins, len(patches))  # The number of bars should match the number of bins
        self.assertEqual(patches[0].get_facecolor(), mcolors.to_rgba(color))  # Checking the color of the bars
    def _test_qq_plot_attributes(self, ax):
        """Helper function to test Q-Q plot attributes."""
        self.assertTrue(len(ax.get_lines()) > 0)  # Check if there are lines in the Q-Q plot
