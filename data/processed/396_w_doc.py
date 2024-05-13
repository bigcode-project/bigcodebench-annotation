import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def task_func(mu, sigma, sample_size, seed=0):
    """
    Create a Gaussian kernel density estimate diagram of a normal distribution with a given mean and a 
    standard deviation using a random sample of a size determined by the sample_size parameter. The density 
    diagram is plotted using default settings in a deterministic matplotlib plot. Return the axes object.
    
    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    sample_size (int): The size of the sample to generate. Must be a positive integer.
    seed (int, Optional): The seed to be used for the random number generator. Default is 0.
    
    Returns:
    matplotlib.axes._axes.Axes: Axes object containing the plot of the normal distribution.
    
    Requirements:
    - numpy
    - matplotlib
    - scipy.stats
    
    Example:
    >>> ax = task_func(0, 1, 1000)
    >>> type(ax) # The result should be a matplotlib.axes._axes.Axes object
    <class 'matplotlib.axes._axes.Axes'>
    """

    if sample_size <= 0:
        raise ValueError('sample_size must be a positive integer.')
    np.random.seed(seed)
    sample = np.random.normal(mu, sigma, sample_size)
    density = stats.gaussian_kde(sample)
    x = np.linspace(min(sample), max(sample), sample_size)
    fig, ax = plt.subplots()
    ax.plot(x, density(x))
    return ax

import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        with self.assertRaises(ValueError):
            ax = task_func(0, 1, 0, 77)        
    def test_case_2(self):
        mu, sigma, sample_size, seed = 0, 1, 10000, 42
        ax = task_func(mu, sigma, sample_size, seed)
        line = ax.lines[0]
        x_data, y_data = line.get_data()
        assert isinstance(ax, matplotlib.axes._axes.Axes)
        assert min(x_data) < mu - 3*sigma and max(x_data) > mu + 3*sigma
    def test_case_3(self):
        ax = task_func(0, 1, 10000, 42)
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        assert xlim[0] < 0 and xlim[1] > 0
        assert ylim[0] < 0 and ylim[1] > 0
    def test_case_4(self):
        ax = task_func(0, 1, 1000, 42)
        assert len(ax.lines) == 1
    def test_case_5(self):
        ax1 = task_func(0, 1, 42)
        ax2 = task_func(0, 1, 42)
        line1 = ax1.lines[0]
        line2 = ax2.lines[0]
        x_data1, y_data1 = line1.get_data()
        x_data2, y_data2 = line2.get_data()
        assert np.array_equal(x_data1, x_data2) and np.array_equal(y_data1, y_data2)
