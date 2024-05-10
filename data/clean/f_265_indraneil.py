import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def f_265(matrix):
    """
    Calculate the distribution of the maximum values of each row in the matrix, 
    record the histogram and the estimate of the core density of the distribution, 
    and return the skew, kurtosis, and the histogram plot of the distribution.
    
    Parameters:
    matrix (list): A list of lists representing a matrix.
    
    Returns:
    tuple: The skewness, the kurtosis of the distribution, and the histogram plot (matplotlib Axes object).
    
    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot
    
    Example:
    >>> skew, kurtosis, ax = f_265([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> round(skew, 2)
    0.0
    >>> round(kurtosis, 2)
    -1.5
    """
    max_values = [max(row) for row in matrix]
    
    fig, ax = plt.subplots()
    ax.hist(max_values, bins=10, density=True, alpha=0.6, color='g')
    
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, np.mean(max_values), np.std(max_values))
    ax.plot(x, p, 'k', linewidth=2)

    skewness = stats.skew(max_values)
    kurtosis = stats.kurtosis(max_values)

    return skewness, kurtosis, ax

import unittest
import doctest


class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Test with a small matrix
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        skew, kurtosis, ax = f_265(matrix)
        
        self.assertEqual(skew, 0.0)
        self.assertEqual(kurtosis, -1.5)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_2(self):
        # Test with negative values
        matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        skew, kurtosis, ax = f_265(matrix)
        
        self.assertEqual(skew, 0.0)
        self.assertEqual(kurtosis, -1.5)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_3(self):
        # Test with larger numbers
        matrix = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
        skew, kurtosis, ax = f_265(matrix)
        
        self.assertEqual(skew, 0.0)
        self.assertEqual(kurtosis, -1.5)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_4(self):
        # Test with identical rows
        matrix = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        skew, kurtosis, ax = f_265(matrix)
        
        self.assertFalse(np.isnan(skew))
        self.assertFalse(np.isnan(kurtosis))
        self.assertIsInstance(ax, plt.Axes)

    def test_case_5(self):
        # Test with a single row
        matrix = [[1, 2, 3]]
        skew, kurtosis, ax = f_265(matrix)
        
        self.assertFalse(np.isnan(skew))  # Skew is defined
        self.assertFalse(np.isnan(kurtosis))  # Kurtosis is defined
        self.assertIsInstance(ax, plt.Axes)


# Define the run_tests function and the test cases
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
