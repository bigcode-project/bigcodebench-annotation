import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes


class ValueObject:
    value = 0

    def __init__(self, mu=0, std=1, seed=77):
        random.seed(seed)
        self.value = random.gauss(mu, std)


def f_1235(obj_list) -> Axes:
    '''
    Draw the histogram and the custom normal distribution curve from the mean and standard deviation
    derived from the values of a list of ValueObjects and return the plotted Axes. For an empty list,
    the mean and the standard deviation is 0.
    
    Parameters:
    obj_list (list): The list of objects.
    attr (str): The attribute to plot.

    Returns:
    Axes: The plotted Axes.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib
    - random

    Example:
    >>> obj_list = [ValueObject(mu=23, std=77), ValueObject(mu=23, std=77, seed=222), ValueObject(mu=23, std=77, seed=333)]
    >>> ax = f_1235(obj_list)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    '''
    if len(obj_list) == 0:
        values = [0]
    else:
        values = [obj.value for obj in obj_list]

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Plot histogram
    ax.hist(values, bins=30, density=True, alpha=0.6, color='g')
    mean = np.mean(values)
    std = np.std(values)

    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std)
    ax.plot(x, p, 'k', linewidth=2)

    title = "Fit results: mu = %.2f,  std = %.2f" % (mean, std)
    ax.set_title(title)

    plt.close(fig)  # Close the figure to avoid display during function execution
    return ax
    

import unittest
import doctest


class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Testing with a small number of objects
        obj_list = [ValueObject(mu=23, std=77), ValueObject(mu=23, std=77, seed=222), ValueObject(mu=23, std=77, seed=333)]
        ax = f_1235(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = 10.76,  std = 39.42")

    def test_case_2(self):
        # Testing with a larger number of objects
        obj_list = [ValueObject(mu=23, std=65) for _ in range(1000)]
        ax = f_1235(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = 40.53,  std = 0.00")

    def test_case_3(self):
        # Testing with an even larger number of objects
        obj_list = [ValueObject(mu=23, std=77, seed=88), ValueObject(mu=11, std=99), ValueObject(mu=41, std=77)]
        ax = f_1235(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = 27.52,  std = 32.92")

    def test_case_4(self):
        # Testing with an empty list of objects
        obj_list = []
        ax = f_1235(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = 0.00,  std = 0.00")

    def test_case_5(self):
        # Testing with a single object
        obj_list = [ValueObject(mu=23, std=77, seed=12)]
        ax = f_1235(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = -88.28,  std = 0.00")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
