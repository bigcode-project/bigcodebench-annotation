import numpy as np
import math
import matplotlib.pyplot as plt


def f_242(range_start=0, range_end=10, step=0.1):
    """
    Create a generator object that generates a sequence of tuples.
    Each tuple contains x and e^x values. Plot the exponential function using these values.

    Returns:
    tuple: 
        - A generator object that yields tuples of (x, e^x).
        - The plotted Axes object of the exponential function.

    Requirements:
    - numpy
    - math
    - matplotlib.pyplot

    Example:
    >>> data, ax = f_242()
    >>> print(next(data))
    (0.0, 1.0)
    >>> ax.get_title()  # Returns the title of the plot
    'Exponential Function Plot'
    """
    x_values = np.arange(range_start, range_end, step)
    data = ((x, math.exp(x)) for x in x_values)
    _, ax = plt.subplots()
    for x, exp_x in data:
        ax.scatter(x, exp_x, color='b')
    ax.set_title("Exponential Function Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("e^x")
    data = ((x, math.exp(x)) for x in x_values)
    return data, ax


import unittest
import doctest
from matplotlib.axes import Axes


class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data, ax = f_242()
        # Check the first data point
        first_point = next(data)
        self.assertEqual(first_point, (0.0, 1.0))
        # Check plot title and labels
        self.assertEqual(ax.get_title(), "Exponential Function Plot")
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "e^x")
        # Check if ax is an instance of Axes
        self.assertIsInstance(ax, Axes)

    # For brevity, similar test cases will be written for test_case_2 to test_case_5
    # These will test various attributes of the plotted data and generator object.

    def test_case_2(self):
        data, ax = f_242(11.4, 17.9, 0.2)
        self.assertIsInstance(ax, Axes)
        # Check the first data point
        first_point = next(data)
        self.assertEqual(first_point, (11.4, math.exp(11.4)))

    def test_case_3(self):
        data, ax = f_242(9.6, 15.2, 0.3)
        self.assertIsInstance(ax, Axes)
        # Check the last data point
        for point in data:
            pass
        self.assertAlmostEqual(point[0], 15.0, places=2)
        self.assertAlmostEqual(point[1], math.exp(15.0), places=2)
        
    def test_case_4(self):
        data, ax = f_242()
        self.assertIsInstance(ax, Axes)
        # Check the data in the axis object
        for point in data:
            ax.scatter(point[0], point[1], color='r')
        self.assertEqual(len(ax.get_children()), 210)
        
    def test_case_5(self):
        data, ax = f_242(89.0, 100.0, 0.1)
        self.assertIsInstance(ax, Axes)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
