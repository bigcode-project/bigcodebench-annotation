import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 1000

def f_193(mean, standard_deviation):
    """
    Generate a histogram plot of a random normal distribution with a specified mean and a standard deviation. The number of samples is stored in the constant NUM_SAMPLES.
    
    Parameters:
    - mean (float): The mean of the distribution.
    - standard_deviation (float): The standard deviation of the distribution.

    Returns:
    - AxesSubplot: A histogram plot of the normal distribution.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib

    Example:
    >>> ax = f_193(0, 1)
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """
    # Generate random normal distribution data
    data = np.random.normal(loc=mean, scale=standard_deviation, size=NUM_SAMPLES)
    # Plot histogram
    ax = plt.hist(data, bins=30, density=True)[1]
    # Plot normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    print(f"mean = {np.mean(x)}, std = {np.std(x)}")
    p = norm.pdf(x, mean, standard_deviation)
    plt.plot(x, p, 'k', linewidth=2)
    return ax

import unittest

class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = f_193(0, 1)
        self.assertIsInstance(ax, np.ndarray)

    def test_case_2(self):
        ax = f_193(5, 0.5)
        self.assertIsInstance(ax, np.ndarray)

    def test_case_3(self):
        ax = f_193(-3, 2)
        self.assertIsInstance(ax, np.ndarray)

    def test_case_4(self):
        ax = f_193(10, 10)
        self.assertIsInstance(ax, np.ndarray)

    def test_case_5(self):
        ax = f_193(-5, 0.1)
        self.assertIsInstance(ax, np.ndarray)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__" :
    run_tests()