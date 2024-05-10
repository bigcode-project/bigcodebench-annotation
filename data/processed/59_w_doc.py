import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    """
    Display a plot showing a normal distribution with a given mean and standard deviation and overlay a histogram of randomly generated samples from this distribution.
    The plot title should be 'Normal Distribution'.

    Parameters:
    mu (float): The mean of the distribution.
    sigma (float): The standard deviation of the distribution.
    num_samples (int): The number of samples to generate.

    Returns:
    fig (matplotlib.figure.Figure): The generated figure. Useful for testing purposes.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> plt = task_func(0, 1, 1000)
    """
    samples = np.random.normal(mu, sigma, num_samples)
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2)
    ax.set_title('Normal Distribution')
    plt.show()
    return fig

import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        np.random.seed(42)
        mu = 0
        sigma = 1
        num_samples = 1000
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)
    def test_case_2(self):
        np.random.seed(42)
        mu = 5
        sigma = 2
        num_samples = 1000
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)
    def test_case_3(self):
        np.random.seed(42)
        mu = 0
        sigma = 1
        num_samples = 10
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)
    def test_case_4(self):
        np.random.seed(42)
        mu = 0
        sigma = 1
        num_samples = 10
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)
    def test_case_5(self):
        np.random.seed(42)
        mu = 0
        sigma = 1
        num_samples = 10
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)
