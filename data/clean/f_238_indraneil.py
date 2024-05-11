import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def f_238(mu=0, sigma=1, sample_size=1000, seed=0):
    """
    Generate a sample from a normal distribution with a given mean and a standard deviation and plot the histogram 
    together with the probability density function. Returns the Axes object representing the plot and the empirical
    mean and standard deviation of the sample.

    Parameters:
    - mu (float): The mean of the normal distribution. Default is 0.
    - sigma (float): The standard deviation of the normal distribution. Default is 1.
    - sample_size (int): The size of the sample to generate. Default is 1000.

    Returns:
    - ax (matplotlib.axes._subplots.AxesSubplot): Axes object with the plotted histogram and normal PDF, with the title format of 'Normal Distribution with $\\mu = %0.2f, \\sigma = %0.2f$'.
    - float: The empirical mean of the sample.
    - float: The empirical standard deviation of the sample.

    Requirements:
    - numpy for data generation.
    - scipy.stats for statistical functions.
    - matplotlib.pyplot for plotting.

    Example:
    >>> ax, mean, std = f_238(0, 1, 1000)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> print(round(mean, 3))
    -0.045
    >>> print(round(std, 3))
    0.987
    """
    np.random.seed(seed)
    sample = np.random.normal(mu, sigma, sample_size)
    
    fig, ax = plt.subplots()
    ax.hist(sample, bins=30, density=True, alpha=0.5, label='Sample Histogram')
    
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2, label='Normal PDF')
    
    ax.set_title("Normal Distribution with $\\mu = %0.2f, \\sigma = %0.2f$" % (mu, sigma))
    ax.legend()    
    return ax, np.mean(sample), np.std(sample)


import unittest
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax, _, _ = f_238()
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 0.00, \\sigma = 1.00$")

    def test_case_2(self):
        ax, mean, std = f_238(mu=5, sigma=2, sample_size=500, seed=42)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 5.00, \\sigma = 2.00$")
        self.assertAlmostEqual(mean, 5.0136, places=3)

    def test_case_3(self):
        ax, mean, std = f_238(mu=-3, sigma=5, sample_size=2000, seed=23)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = -3.00, \\sigma = 5.00$")
        self.assertAlmostEqual(std, 4.978, places=3)

    def test_case_4(self):
        ax, _, _ = f_238(mu=1, sigma=0.5, sample_size=100)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 1.00, \\sigma = 0.50$")

    def test_case_5(self):
        ax, mean, std = f_238(mu=10, sigma=0.1, sample_size=1500)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Normal Distribution with $\\mu = 10.00, \\sigma = 0.10$")
        self.assertAlmostEqual(mean, 9.998, places=3)
        self.assertAlmostEqual(std, 0.09804, places=3)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    doctest.testmod()
    run_tests()
