import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def task_func(X, Y):
    """
    Adjust a quadratic function to the given data (X, Y) and plot the data along with the fit.

    Parameters:
    - X (list or numpy.array): The X data points.
    - Y (list or numpy.array): The Y data points.

    Returns:
    tuple:
    - list: The optimized parameters of the quadratic function (a, b, c).
    - matplotlib.axes.Axes: The plot showing the scatter data points and the quadratic fit.

    Requirements:
    - matplotlib.pyplot
    - scipy.optimize.curve_fit

    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> X = np.linspace(-10, 10, 100)
    >>> Y = 3*X**2 + 2*X + 1 + np.random.normal(0, 20, len(X))
    >>> params, ax = task_func(X, Y)
    >>> params
    [3.0366511660907975, 2.1379326607136035, -2.3233168384548284]
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    def func(x, a, b, c):
        return a * x ** 2 + b * x + c
    popt, pcov = curve_fit(func, X, Y)
    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.plot(X, func(X, *popt), "r-")
    return list(popt), ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
import itertools
class TestCases(unittest.TestCase):
    def setUp(self):
        self.random_seed = 42
        np.random.seed(self.random_seed)
        self.test_data = [
            (
                np.linspace(-10, 10, 100),
                3 * np.linspace(-10, 10, 100) ** 2
                + 2 * np.linspace(-10, 10, 100)
                + 1
                + np.random.normal(0, 20, 100),
            ),
            (
                np.linspace(-5, 5, 100),
                -2 * np.linspace(-5, 5, 100) ** 2
                + 4 * np.linspace(-5, 5, 100)
                - 3
                + np.random.normal(0, 10, 100),
            ),
            (
                np.linspace(-100, 100, 100),
                0.5 * np.linspace(-100, 100, 100) ** 2
                + 1 * np.linspace(-100, 100, 100)
                + 10
                + np.random.normal(0, 50, 100),
            ),
            (
                np.linspace(-1, 1, 100),
                10 * np.linspace(-1, 1, 100) ** 2
                + 5 * np.linspace(-1, 1, 100)
                + 2
                + np.random.normal(0, 1, 100),
            ),
        ]
    def assertDataInPlot(self, X, Y, ax):
        xdata, ydata = ax.collections[0].get_offsets().T  # Access scatter plot data
        self.assertTrue(np.array_equal(X, xdata))
        self.assertTrue(np.array_equal(Y, ydata))
    def test_case_1(self):
        # Test fitting a basic quadratic function with expected params near 3, 2.
        X, Y = self.test_data[0]
        params, ax = task_func(X, Y)
        self.assertTrue(len(params) == 3)
        self.assertDataInPlot(X, Y, ax)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertAlmostEqual(params[0], 3, places=0)
        self.assertAlmostEqual(params[1], 2, places=0)
    def test_case_2(self):
        # Test fitting a basic quadratic function with expected params near -2, 4.
        X, Y = self.test_data[1]
        params, ax = task_func(X, Y)
        self.assertTrue(len(params) == 3)
        self.assertDataInPlot(X, Y, ax)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertAlmostEqual(params[0], -2, places=0)
        self.assertAlmostEqual(params[1], 4, places=0)
    def test_case_3(self):
        # Test fitting a wide parabola with parameters (0.5, 1).
        X, Y = self.test_data[2]
        params, ax = task_func(X, Y)
        self.assertTrue(len(params) == 3)
        self.assertDataInPlot(X, Y, ax)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertAlmostEqual(params[0], 0.5, places=0)
        self.assertAlmostEqual(params[1], 1, places=0)
    def test_case_4(self):
        # Test fitting a steep parabola with high coefficients (10, 5).
        X, Y = self.test_data[3]
        params, ax = task_func(X, Y)
        self.assertTrue(len(params) == 3)
        self.assertDataInPlot(X, Y, ax)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertAlmostEqual(params[0], 10, places=0)
        self.assertAlmostEqual(params[1], 5, places=0)
    def test_case_5(self):
        # Test handling non-numeric data - convertable to int
        string_int_list = ["1", "2", "3"]
        int_list = [1, 2, 3]
        with self.assertRaises(TypeError):
            task_func(string_int_list, int_list)
        with self.assertRaises(TypeError):
            task_func(int_list, string_int_list)
    def test_case_6(self):
        # Test handling non-numeric data
        for X, Y in itertools.product([["a", "b", "c"], [], np.array([])], repeat=2):
            with self.assertRaises(ValueError):
                task_func(X, Y)
    def tearDown(self):
        plt.close("all")
