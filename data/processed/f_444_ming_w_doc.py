from random import randint
import matplotlib.pyplot as plt
import numpy as np


def f_434(array_length=100):
    """
    Generate two arrays of random integers and draw a line diagram with the 
    maximum values of the respective elements of the two arrays.

    Args:
    - array_length (int): Length of the random arrays to be generated. Default is 100.

    Returns:
    - matplotlib.axes.Axes: Axes object with the plot.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - random

    Example:
    >>> ax = f_434(100)
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
        ax = f_434(50)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 50)
        
    def test_case_2(self):
        ax = f_434(100)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 100)
        
    def test_case_3(self):
        ax = f_434(150)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 150)
        
    def test_case_4(self):
        ax = f_434(200)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 200)
        
    def test_case_5(self):
        ax = f_434(250)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 250)
