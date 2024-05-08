import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def f_951(mean=123456.908, std_dev=1.2, save_plots=False):
    """
    Generate a random sample from a normal distribution, analyze its skewness and kurtosis,
    and create a histogram and a QQ plot to visualize the distribution.

    Parameters:
    - mean (float, optional): Mean of the normal distribution. Defaults to 123456.908.
    - std_dev (float, optional): Standard deviation of the normal distribution. Defaults to 1.2.
    - save_plots (bool, optional): If True, saves the plots to files. Defaults to False.

    Returns:
    - float: Skewness of the sample.
    - float: Kurtosis of the sample.
    - list: Paths to the saved plot files, empty if save_plots is False.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.stats

    Example:
    >>> np.random.seed(0)
    >>> skewness, kurtosis, plot_paths = f_951(123456.908, 1.2, True)
    >>> print(f'Skewness: {skewness}, Kurtosis: {kurtosis}, Plots: {plot_paths}')
    Skewness: 0.03385895323538189, Kurtosis: -0.04676632447765128, Plots: ['histogram_plot.png', 'qq_plot.png']

    """
    sample = np.random.normal(mean, std_dev, 1000)
    plot_paths = []
    plt.figure()
    plt.hist(sample, bins=50)
    if save_plots:
        hist_path = "histogram_plot.png"
        plt.savefig(hist_path)
        plt.close()
        plot_paths.append(hist_path)
    plt.figure()
    stats.probplot(sample, plot=plt)
    if save_plots:
        qq_path = "qq_plot.png"
        plt.savefig(qq_path)
        plt.close()
        plot_paths.append(qq_path)
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)
    return skewness, kurtosis, plot_paths

import unittest
import os
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for f_951."""
    def test_default_parameters(self):
        """
        Test f_951 with default parameters.
        """
        np.random.seed(0)
        skewness, kurtosis, plot_paths = f_951()
        self.assertAlmostEqual(skewness, 0, delta=0.5)
        self.assertAlmostEqual(kurtosis, 0, delta=0.5)
        self.assertEqual(len(plot_paths), 0)
    def test_save_plots_true(self):
        """
        Test f_951 with save_plots set to True.
        """
        np.random.seed(1)
        _, _, plot_paths = f_951(save_plots=True)
        self.assertEqual(len(plot_paths), 2)
        for path in plot_paths:
            self.assertTrue(os.path.exists(path))
            os.remove(path)  # Clean up: remove created files
    def test_custom_mean_std_dev(self):
        """
        Test f_951 with custom mean and standard deviation.
        """
        np.random.seed(2)
        mean = 100
        std_dev = 10
        skewness, kurtosis, _ = f_951(mean, std_dev)
        self.assertAlmostEqual(skewness, 0, delta=1)
        self.assertAlmostEqual(kurtosis, 0, delta=1)
    def test_negative_std_dev(self):
        """
        Test f_951 with a negative standard deviation.
        """
        np.random.seed(3)
        with self.assertRaises(ValueError):
            f_951(std_dev=-1)
    def test_large_sample(self):
        """
        Test f_951 with a larger sample size.
        """
        np.random.seed(4)
        _, _, plot_paths = f_951(mean=1000, std_dev=50, save_plots=True)
        self.assertEqual(len(plot_paths), 2)
        for path in plot_paths:
            self.assertTrue(os.path.exists(path))
            os.remove(path)  # Clean up: remove created files
