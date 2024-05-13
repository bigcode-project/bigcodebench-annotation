import math
import numpy as np
import matplotlib.pyplot as plt


def task_func(list_input):
    """
    Sort the given list in ascending order based on the degree value of its elements, calculate the cumulative sum of 
    the sorted list, and draw a line chart of the cumulative sum.

    Parameters:
    list_input (list): The list to be sorted.

    Returns:
    tuple: A tuple containing:
           - numpy array: The cumulative sum of the sorted list.
           - matplotlib.axes._axes.Axes: The Axes object of the plotted line chart.

    Requirements:
    - math
    - numpy
    - matplotlib.pyplot

    Example:
    >>> cumsum, ax = task_func([10, 20, 30])
    >>> print(cumsum)
    [10 30 60]
    >>> ax.get_title()
    'Cumulative Sum Plot'
    """

    sorted_list = sorted(list_input, key=lambda x: (math.degrees(x), x))
    cumsum = np.cumsum(sorted_list)
    ax = plt.plot(cumsum)[0].axes
    ax.set_title("Cumulative Sum Plot")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Sum")
    return cumsum, ax

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        cumsum, ax = task_func([10, 20, 30])
        self.assertListEqual(list(cumsum), [10, 30, 60])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_2(self):
        cumsum, ax = task_func([5, 15, 25])
        self.assertListEqual(list(cumsum), [5, 20, 45])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_3(self):
        cumsum, ax = task_func([])
        self.assertListEqual(list(cumsum), [])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_4(self):
        cumsum, ax = task_func([1, 2, 3, 4, 5])
        self.assertListEqual(list(cumsum), [1, 3, 6, 10, 15])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_5(self):
        cumsum, ax = task_func([5])
        self.assertListEqual(list(cumsum), [5])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
