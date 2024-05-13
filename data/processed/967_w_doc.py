import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def task_func(func, x_range=(-2, 2), num_points=1000):
    """
    Calculates and plots both a given function and its cumulative integral over a specified range,
    using a linearly spaced range of x-values.

    Parameters:
    func (function): A function of a single variable to integrate and plot.
    x_range (tuple, optional): The range (start, end) over which to evaluate `func`. Defaults to (-2, 2).
    num_points (int, optional): Number of points to generate in `x_range`. Defaults to 1000.

    Returns:
    matplotlib.axes.Axes: The Axes object containing the plots of the function and its integral.

    Requirements:
    - numpy
    - scipy
    - matplotlib

    Note:
    - The plot includes a legend and labels for the x and y axes that include the function's name.

    Example:
    >>> ax = task_func(np.sin)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_legend_handles_labels()[-1]
    ['sin(x)', 'Integral of sin(x)']
    """

    X = np.linspace(x_range[0], x_range[1], num_points)
    y = func(X)
    y_int = integrate.cumulative_trapezoid(y, X, initial=0)
    fig, ax = plt.subplots()
    ax.plot(X, y, label=f"{func.__name__}(x)")
    ax.plot(X, y_int, label=f"Integral of {func.__name__}(x)")
    ax.legend()
    return ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    def tearDown(self):
        plt.close("all")
    def helper_assert_plot_attributes(self, func):
        # Test plot attributes are as expected
        ax = task_func(func)
        function_name = func.__name__
        legend_labels = ax.get_legend_handles_labels()[-1]
        self.assertIsInstance(ax, Axes)
        self.assertIn(function_name, legend_labels[0])
        self.assertIn(function_name, legend_labels[1])
    def test_case_1(self):
        # Test basic case in docstring
        ax = task_func(np.sin)
        self.helper_assert_plot_attributes(np.sin)
    def test_case_2(self):
        # Test other functions - numpy
        for func in [np.cos, np.exp]:
            ax = task_func(func)
            self.helper_assert_plot_attributes(func)
    def test_case_3(self):
        # Test other functions - lambda
        func = lambda x: x ** 2
        ax = task_func(func)
        self.helper_assert_plot_attributes(func)
    def test_case_4(self):
        # Test custom range and points
        ax = task_func(np.cos, x_range=(0, np.pi), num_points=500)
        self.assertEqual(len(ax.lines[0].get_xdata()), 500)
        self.assertEqual(ax.lines[0].get_xdata()[0], 0)
        self.assertEqual(ax.lines[0].get_xdata()[-1], np.pi)
    def test_case_5(self):
        # Test correct integral calculation
        # Test integral of x^2 in the range [0,1], should be close to 1/3
        func = lambda x: x ** 2
        X = np.linspace(0, 1, 1000)
        expected_integral = 1 / 3 * X ** 3  # Analytical integral of x^2
        ax = task_func(func, x_range=(0, 1), num_points=1000)
        computed_integral = ax.lines[1].get_ydata()[
            -1
        ]  # Last value of the computed integral
        self.assertAlmostEqual(computed_integral, expected_integral[-1], places=4)
