import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def task_func(mu, sigma, seed=0):
    """
    Draw a normal distribution using a 1000 samples, indicating the mean and standard deviation 
    with a color bar.
    
    Parameters:
    mu (float): The mean of the distribution.
    sigma (float): The standard deviation of the distribution.
    seed (int, Optional): The seed for the random number generator. Defaults to 0.
    
    Returns:
    matplotlib.axes._axes.Axes: The Axes object of the plotted distribution.
    
    Requirements:
    - matplotlib.pyplot
    - numpy
    - seaborn
    
    Example:
    >>> plot = task_func(0, 1)
    >>> type(plot)
    <class 'matplotlib.axes._axes.Axes'>
    """
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, 1000)
    mappable = sns.kdeplot(samples, fill=True)
    plt.colorbar(mappable=mappable.collections[0])
    return mappable

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = task_func(0, 1)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.collections) > 0, "The plot should have data.")
        # Check if the colorbar is present
        self.assertTrue(ax.get_figure().colorbar is not None)
        
    def test_case_2(self):
        ax = task_func(2, 0.5)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.collections) > 0, "The plot should have data.")
        # Test the KDE plot data
        self.assertTrue(len(ax.collections[0].get_offsets()) > 0)
        
    def test_case_3(self):
        ax = task_func(-2, 2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.collections) > 0, "The plot should have data.")
        
    def test_case_4(self):
        ax = task_func(5, 0.1)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.collections) > 0, "The plot should have data.")
        
    def test_case_5(self):
        ax = task_func(-5, 5)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.collections) > 0, "The plot should have data.")
