import random
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def f_451(size=1000, bin_width=100):
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
    >>> fig = f_451(size=500, bin_width=50)
    '''
    data = np.random.randn(size)
    mu, std = stats.norm.fit(data)
    
    # Adjusting bin calculation using numpy's histogram_bin_edges
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

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        fig = f_451()
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
        
    def test_case_2(self):
        fig = f_451(size=500, bin_width=50)
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
        
    def test_case_3(self):
        fig = f_451(size=1500, bin_width=150)
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
        
    def test_case_4(self):
        fig = f_451(size=2000, bin_width=200)
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
        
    def test_case_5(self):
        fig = f_451(size=2500, bin_width=250)
        ax = fig.axes[0]
        self.assertGreaterEqual(len(ax.patches), 5, "Expected at least 5 bars in the histogram")
        self.assertEqual(len(ax.lines), 1, "Expected 1 line for the PDF plot")
if __name__ == "__main__":
    run_tests()