import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def f_362(l):
    '''
    Draw a histogram of the given array with a Gaussian fit.

    Parameters:
    l (numpy array): The input array.

    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object with the plot.

    Note:
    - This function use "Fit results: mu = {mean},  std = {standard deviation}" as the title of the plot, 
    where the values are rounded to two decimal points.


    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> l = np.array([5, 5, 5, 5, 5])
    >>> ax = f_362(l)
    >>> print(ax.get_title())
    Fit results: mu = 5.00,  std = 0.00
    >>> plt.close()
    '''
    fig, ax = plt.subplots()
    ax.hist(l, bins='auto', density=True, alpha=0.6, color='g')

    mu, std = stats.norm.fit(l)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    ax.set_title(title)
    return ax

import unittest
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        l1 = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        ax1 = f_362(l1)
        mu, std = stats.norm.fit(l1)
        expected_title_1 = f"Fit results: mu = {mu:.2f},  std = {std:.2f}"
        self.assertIsInstance(ax1, plt.Axes, "Return type should be a matplotlib Axes object.")
        self.assertEqual(ax1.get_title(), expected_title_1, "Incorrect title for test case 1.")
    
    def test_case_2(self):
        l2 = np.array([5, 5, 5, 5, 5])
        ax2 = f_362(l2)
        self.assertIsInstance(ax2, plt.Axes, "Return type should be a matplotlib Axes object.")
        self.assertEqual(ax2.get_title(), "Fit results: mu = 5.00,  std = 0.00", "Incorrect title for test case 2.")
    def test_case_3(self):
        l3 = np.array([1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9])
        ax3 = f_362(l3)
        mu, std = stats.norm.fit(l3)
        expected_title_3 = f"Fit results: mu = {mu:.2f},  std = {std:.2f}"
        self.assertIsInstance(ax3, plt.Axes, "Return type should be a matplotlib Axes object.")
        self.assertEqual(ax3.get_title(), expected_title_3, "Incorrect title for test case 3.")
    
    def test_case_4(self):
        l4 = np.array([10, 10, 10, 10, 10])
        ax4 = f_362(l4)
        self.assertIsInstance(ax4, plt.Axes, "Return type should be a matplotlib Axes object.")
        self.assertEqual(ax4.get_title(), "Fit results: mu = 10.00,  std = 0.00", "Incorrect title for test case 4.")
        
    def test_case_5(self):
        l5 = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
        ax5 = f_362(l5)
        mu, std = stats.norm.fit(l5)
        expected_title_5 = f"Fit results: mu = {mu:.2f},  std = {std:.2f}"
        self.assertIsInstance(ax5, plt.Axes, "Return type should be a matplotlib Axes object.")
        self.assertEqual(ax5.get_title(), expected_title_5, "Incorrect title for test case 5.")
