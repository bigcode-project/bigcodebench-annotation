import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols


def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    '''
    Create a histogram of a normal distribution with a given mean and standard deviation, and overlay the 
    probability density function (PDF) of the normal distribution on the histogram. Additionally, overlay a 
    second order polynomial function on the histogram fitted bin-wise using ordinary least squares (OLS) 
    regression. The random seed is set for reproducibility. The color of the PDF line is red, and the color of the OLS line is green.
    
    Parameters:
    - mu (float): The mean of the distribution.
    - sigma (float): The standard deviation of the distribution.
    - seed (int, Optional): The random seed for reproducibility. Defaults to 0.
    - num_samples (int, Optional): The number of samples to generate from the distribution. Defaults to 1000.
    - num_bins (int, Optional): The number of bins to use in the histogram. Defaults to 30.
    
    Returns:
    - matplotlib.axes.Axes: The Axes object with the histogram and overlaid PDF.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - statsmodels.formula.api
    
    Example:
    >>> ax = task_func(0, 1)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    '''

    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(samples, num_bins, density=True)
    ax.plot(
        bins, 
        1/(sigma * np.sqrt(2 * np.pi)) * \
        np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r'
    )
    bins = (bins[:-1] + bins[1:]) / 2
    model = ols('count ~ bins + np.power(bins, 2)', data={'count': count, 'bins': bins}).fit()
    ax.plot(
        bins, 
        model.params['Intercept'] + model.params['bins'] * bins + \
        model.params['np.power(bins, 2)'] * np.power(bins, 2), linewidth=2, color='g'
    )
    return ax

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = task_func(0, 1)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")
        # Check if the OLS line is plotted
        self.assertEqual(ax.lines[1].get_color(), 'g', "The OLS line color should be green.")
        
    def test_case_2(self):
        ax = task_func(2, 2, 555, 1000, 50)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")
        # Check if the OLS line is plotted
        self.assertEqual(ax.lines[1].get_color(), 'g', "The OLS line color should be green.")
        # Check the axis data
        self.assertAlmostEquals(ax.get_xlim()[0], -5.66, msg="The x-axis limits are incorrect.", places=2)
        self.assertAlmostEquals(ax.get_xlim()[1], 8.54, msg="The x-axis limits are incorrect.", places=2)
        
    def test_case_3(self):
        ax = task_func(-2, 0.5, 77, 50000)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")
        # Check the axis data
        self.assertAlmostEquals(ax.get_ylim()[0], -0.28, msg="The y-axis limits are incorrect.", places=2)
        self.assertAlmostEquals(ax.get_ylim()[1], 0.84, msg="The y-axis limits are incorrect.", places=2)
        # Check the histogram data
        self.assertEqual(len(ax.patches), 30, "The number of histogram bars is incorrect.")
        
    def test_case_4(self):
        ax = task_func(5, 3)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")
        # Test the plot array
        self.assertEqual(len(ax.lines), 2, "The plot should have two lines.")
        
    def test_case_5(self):
        ax = task_func(-5, 1.5)
        self.assertTrue(hasattr(ax, 'lines'), "The plot should have lines representing the PDF.")
        self.assertTrue(hasattr(ax, 'patches'), "The plot should have bars representing the histogram.")
        self.assertEqual(ax.lines[0].get_color(), 'r', "The PDF line color should be red.")
