import numpy as np
from scipy import stats
import matplotlib.pyplot as plt



def f_255(size=1000, bin_width=100):
    '''
    Create a list of normally distributed random numbers and plot their histogram and probability density function (PDF).
    
    Parameters:
    - size (int): The number of random numbers to generate. Default is 1000.
    - bin_width (int): Width of the bins for the histogram. Default is 100.
    
    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot
    
    Returns:
    - matplotlib.figure.Figure: A figure object containing the histogram and PDF plot.
    
    Example:
    >>> import matplotlib
    >>> fig = f_255(size=500, bin_width=50)
    >>> isinstance(fig, matplotlib.figure.Figure)  # Check if the output is a matplotlib figure object
    True
    >>> len(fig.axes[0].lines) == 1  # Ensure there is one line plot on the axes for the PDF
    True
    >>> len(fig.axes[0].patches) > 10  # Check if there are histogram bars (patches) present
    True
    '''
    data = np.random.randn(size)
    mu, std = stats.norm.fit(data)
    bin_edges = np.histogram_bin_edges(data, bins='auto')
    number_of_bins = len(bin_edges) - 1
    fig, ax = plt.subplots()
    ax.hist(data, bins=number_of_bins, density=True, alpha=0.6, color='g')
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, size)
    p = stats.norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    return fig

import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        fig = f_255()
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
        
    def test_case_2(self):
        fig = f_255(size=500, bin_width=50)
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
        
    def test_case_3(self):
        fig = f_255(size=1500, bin_width=150)
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
        
    def test_case_4(self):
        fig = f_255(size=2000, bin_width=200)
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
        
    def test_case_5(self):
        fig = f_255(size=2500, bin_width=250)
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
