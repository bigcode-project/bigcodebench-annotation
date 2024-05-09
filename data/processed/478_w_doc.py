from random import randint
import matplotlib.pyplot as plt
import numpy as np


def task_func(array_length=100):
    """
    Generate two arrays of random integers and draw a line diagram with the 
    maximum values of the respective elements of the two arrays. Set 'Maximum Values' on its y-axis.

    Parameters:
    - array_length (int): Length of the random arrays to be generated. Default is 100.

    Returns:
    - matplotlib.axes.Axes: Axes object with the plot.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - random

    Example:
    >>> ax = task_func(100)
    """
    array1 = np.array([randint(1, 100) for _ in range(array_length)])
    array2 = np.array([randint(1, 100) for _ in range(array_length)])
    max_values = np.maximum(array1, array2)
    fig, ax = plt.subplots()
    ax.plot(max_values)
    ax.set_ylabel('Maximum Values')
    return ax

import unittest
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        ax = task_func(50)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 50)
    def test_standard_functionality(self):
        """Test the function with default array length."""
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)
    def test_zero_length_array(self):
        """Test the function with zero array length."""
        ax = task_func(0)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 0)  # Expect no data points in the plot
    def test_non_default_length_array(self):
        """Test the function with non-default array lengths."""
        lengths = [50, 200]
        for length in lengths:
            ax = task_func(length)
            self.assertIsInstance(ax, plt.Axes)
            self.assertEqual(len(ax.lines[0].get_ydata()), length)
    def test_plot_output(self):
        """Verify the plot is generated and is of correct type."""
        ax = task_func()
        self.assertTrue(hasattr(ax, 'figure'), "Plot does not have associated figure attribute")
