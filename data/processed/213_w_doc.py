import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis


def task_func(intervals=100, seed=0):
    """
    Generates a series of random numbers over a specified number of intervals with a delay of 1 second between 
    each interval. It then plots these numbers as a function of elapsed time and returns the Axes object along
    with the kurtosis value of the generated numbers.
    
    Parameters:
    - intervals (int, optional): Number of intervals for generating random numbers. Default is 100.

    Returns:
    - matplotlib.axes.Axes: The Axes object representing the plot.
    - float: The kurtosis value of the generated numbers.

    Requirements:
    - time
    - random
    - matplotlib.pyplot

    Example:
    >>> ax, kurtosis = task_func(5)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    random.seed(seed)
    times = []
    numbers = []
    try:
        for _ in range(intervals):
            time.sleep(1)
            times.append(time.time())
            numbers.append(random.random())
    except KeyboardInterrupt:
        print('Interrupted by user')
    kurtosis_value = kurtosis(numbers, nan_policy='omit')
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(times, numbers)
    return ax, kurtosis_value

import unittest
import doctest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    
    @patch('time.sleep', return_value=None)  # Mocking time.sleep
    def test_case_1(self, mock_sleep):
        ax, kurtosis = task_func(5)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 5)
        self.assertEqual(len(lines[0].get_ydata()), 5)
        self.assertEqual(mock_sleep.call_count, 5)
    @patch('time.sleep', return_value=None)
    def test_case_2(self, mock_sleep):
        ax, kurtosis = task_func(10, 44)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 10)
        self.assertEqual(len(lines[0].get_ydata()), 10)
        self.assertNotAlmostEqual(kurtosis, -0.34024, places=5)
    @patch('time.sleep', return_value=None)
    def test_case_3(self, mock_sleep):
        ax, kurtosis = task_func()  # Default intervals = 100
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 100)
        self.assertEqual(len(lines[0].get_ydata()), 100)
        
    @patch('time.sleep', return_value=None)
    def test_case_4(self, mock_sleep):
        ax, kurtosis = task_func(1)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 1)
        self.assertEqual(len(lines[0].get_ydata()), 1)
    @patch('time.sleep', return_value=None)
    def test_case_5(self, mock_sleep):
        ax, kurtosis = task_func(0)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 0)
        self.assertEqual(len(lines[0].get_ydata()), 0)
