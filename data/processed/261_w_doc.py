import matplotlib.pyplot as plt
import numpy as np


def task_func(ax, radius):
    '''
    Draw a circle with a given radius on the polar chart 'ax' and set radial ticks.
    This function manipulates plot data using matplotlib.

    Parameters:
    ax (matplotlib.axes._axes.Axes): The ax to plot on. Must be a polar plot.
    radius (float): The radius of the circle. Must be non-negative.

    Returns:
    matplotlib.axes._axes.Axes: The modified Axes object with the circle plotted.

    Note:
    - If the radius is negative this function will raise ValueError.
    - If 'ax' is not a polar plot this function will raise TypeError.

    Requirements:
    - matplotlib.pyplot
    - numpy

    Example:
    >>> import matplotlib.pyplot as plt
    >>> fig = plt.figure()
    >>> ax = fig.add_subplot(111, polar=True)
    >>> result_ax = task_func(ax, 1.5)
    >>> np.allclose(result_ax.get_lines()[0].get_ydata(), 1.5)
    True
    >>> plt.close()
    '''

    if radius < 0:
        raise ValueError('Radius must be non-negative')
    if not isinstance(ax, plt.PolarAxes):
        raise TypeError('ax must be a polar plot')
    theta = np.linspace(0, 2 * np.pi, 1000)
    ax.plot(theta, radius * np.ones_like(theta))
    ax.set_rlabel_position(radius * 45)
    return ax

import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_polar_plot(self):
        '''Test if the function plots on a polar plot.'''
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        result_ax = task_func(ax, 1.0)
        self.assertIsInstance(result_ax, plt.PolarAxes)
        plt.close()
    def test_circle_radius(self):
        '''Test if the circle is drawn with the correct radius.'''
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        radius = 2.0
        result_ax = task_func(ax, radius)
        for line in result_ax.get_lines():
            self.assertTrue(np.allclose(line.get_ydata(), radius))
        plt.close()
    def test_negative_radius(self):
        '''Test handling of negative radius.'''
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        with self.assertRaises(ValueError):
            task_func(ax, -1.0)
        plt.close()
    def test_non_polar_plot(self):
        '''Test handling of non-polar plot input.'''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        with self.assertRaises(TypeError):
            task_func(ax, 1.0)
        plt.close()
    def test_zero_radius(self):
        '''Test handling of zero radius.'''
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        radius = 0.0
        result_ax = task_func(ax, radius)
        for line in result_ax.get_lines():
            self.assertTrue(np.allclose(line.get_ydata(), radius))
        plt.close()
