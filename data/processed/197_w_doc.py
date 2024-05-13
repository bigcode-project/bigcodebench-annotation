import heapq
import math
import matplotlib.pyplot as plt


def task_func(l1, l2, N=10):
    """ 
    Find the N biggest differences between the respective elements of the list 'l1' and list 'l2', 
    square the differences, take the square root and return the plotted values as a matplotlib Axes object.

    Parameters:
    l1 (list): A list of numbers.
    l2 (list): A list of numbers.
    N (int): Number of largest differences to consider. Default is 10.

    Returns:
    matplotlib.axes._axes.Axes: A matplotlib Axes object with the plotted differences.

    Requirements:
    - heapq
    - math
    - matplotlib.pyplot

    Example:
    >>> l1 = [99, 86, 90, 70, 86, 95, 56, 98, 80, 81]
    >>> l2 = [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
    >>> ax = task_func(l1, l2)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    largest_diff_indices = heapq.nlargest(N, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))
    largest_diffs = [math.sqrt((l1[i] - l2[i])**2) for i in largest_diff_indices]
    fig, ax = plt.subplots()
    ax.plot(largest_diffs)
    return ax

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        l1 = [99, 86, 90, 70, 86, 95, 56, 98, 80, 81]
        l2 = [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
        ax = task_func(l1, l2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 10)
    def test_case_2(self):
        l1 = [10, 20, 30, 40, 50]
        l2 = [1, 2, 3, 4, 5]
        ax = task_func(l1, l2, 3)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 3)
    def test_case_3(self):
        l1 = [0, 10, 20, 30, 40, 50]
        l2 = [0, 0, 0, 0, 0, 0]
        ax = task_func(l1, l2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 6)
    def test_case_4(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [5, 4, 3, 2, 1]
        ax = task_func(l1, l2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 5)
    def test_case_5(self):
        l1 = [0, 0, 0, 0, 0]
        l2 = [0, 0, 0, 0, 0]
        ax = task_func(l1, l2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 5)
