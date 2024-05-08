import math
import matplotlib.pyplot as plt
import numpy as np
import random
# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi


def f_444(size=SIZE, frequency=1):
    '''
    Create a list of random sinusoidal values and plot them in a graph.
    
    Parameters:
    - size (int): The number of points for the sinusoidal wave. Default is 1000.
    - frequency (float): The frequency of the sinusoidal wave. Default is 1.
    
    Returns:
    - Axes object: The plot of the sinusoidal wave.
    
    Requirements:
    - random
    - math
    - matplotlib.pyplot
    - numpy
    
    Example:
    >>> import matplotlib
    >>> ax = f_444(size=1000, frequency=1)
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    >>> len(ax.lines[0].get_ydata()) == 1000  # Verify the number of data points in the sinusoidal wave
    True
    >>> isinstance(ax.lines[0].get_ydata()[0], float)  # Check if y-values are floating-point numbers
    True
    '''
    x_values = np.arange(0, size)
    y_values = [math.sin((2 * PI / RANGE) * (x + int(RANGE * random.random()) * frequency)) for x in range(size)]
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    return ax

import unittest
class TestCases(unittest.TestCase):
        
    def test_case_4(self):
        ax = f_444(size=1500, frequency=0.5)
        x_data, y_data = ax.lines[0].get_data()
        self.assertEqual(len(x_data), 1500)
        self.assertTrue(min(y_data) >= -1 and max(y_data) <= 1)
    def test_standard_functionality(self):
        """Test the function with default parameters."""
        ax = f_444()
        self.assertIsInstance(ax, plt.Axes)
    def test_varying_sizes(self):
        """Test the function with different array sizes."""
        for size in [0, 10, 500, 1500]:
            ax = f_444(size=size)
            self.assertIsInstance(ax, plt.Axes)
            self.assertEqual(len(ax.lines[0].get_xdata()), size)
    def test_different_frequencies(self):
        """Test the function with different frequencies."""
        for frequency in [0.5, 1, 2]:
            ax = f_444(frequency=frequency)
            self.assertIsInstance(ax, plt.Axes)
    def test_plot_output(self):
        """Verify the plot is generated and is of correct type."""
        ax = f_444()
        self.assertTrue(hasattr(ax, 'figure'), "Plot does not have associated figure attribute")
