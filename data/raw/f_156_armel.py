import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Constants
SAMPLE_SIZE = 5000

def f_156(mu, sigma):
    """
    Generate SAMPLE_SIZE samples from a normal distribution with a given mean and a standard deviation and record its histogram and probability density function.
    - The histogram should have 30 bins.
    - The probability density function should be dashed.

    Parameters:
    mu (float): The mean of the distribution.
    sigma (float): The standard deviation of the distribution.

    Returns:
    sample (numpy.ndarray): The generated sample from the normal distribution.
    density (numpy.ndarray): The probability density function values for the sample.
    fig (matplotlib.figure.Figure): The figure object containing the histogram and PDF plot.
    ax (matplotlib.axes._subplots.AxesSubplot): The axes object containing the histogram and PDF plot.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> sample, density, fig, ax = f_156(0, 1)
    """
    sample = np.random.normal(mu, sigma, SAMPLE_SIZE)
    density = stats.norm(mu, sigma).pdf(sample)
    
    fig, ax = plt.subplots()
    ax.hist(sample, density=True, bins=30, alpha=0.6, color='g')
    ax.plot(sample, density, 'r--')
    plt.close(fig)  # Prevents plt.show()
    
    return sample, density, fig, ax

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_156 function."""
    def test_case_1(self):
        """standard gaussian"""
        mu, sigma = 0, 1
        sample, density, fig, ax = f_156(mu, sigma)
        self._validate_test(sample, density, ax, mu, sigma)
        
    def test_case_2(self):
        mu, sigma = 5, 2
        sample, density, fig, ax = f_156(mu, sigma)
        self._validate_test(sample, density, ax, mu, sigma)
        
    def test_case_3(self):
        """negative mean, small deviation"""
        mu, sigma = -3, 0.5
        sample, density, fig, ax = f_156(mu, sigma)
        self._validate_test(sample, density, ax, mu, sigma)
    
    def test_case_4(self):
        """large mean, large deviation"""
        mu, sigma = 10, 3
        sample, density, fig, ax = f_156(mu, sigma)
        self._validate_test(sample, density, ax, mu, sigma)
        
    def test_case_5(self):
        mu, sigma = -5, 2.5
        sample, density, fig, ax = f_156(mu, sigma)
        self._validate_test(sample, density, ax, mu, sigma)
        
    def _validate_test(self, sample, density, ax, mu, sigma):
        self.assertEqual(len(ax.patches), 30, "The histogram should have 30 bins.")
        self.assertTrue(any(line.get_linestyle() == '--' for line in ax.get_lines()), "The PDF line should be dashed.")
        np.testing.assert_almost_equal(np.mean(sample), mu, decimal=1, err_msg="Sample mean does not match expected mean.")
        np.testing.assert_almost_equal(np.std(sample), sigma, decimal=1, err_msg="Sample standard deviation does not match expected value.")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests() 