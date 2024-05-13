import math
import statistics
import numpy as np


def task_func(input_list):
    """
    Sorts the input list in ascending order based on the degree value of its elements, and then 
    calculates the mean, median, and mode of both the sorted list and the same for the magnitude of 
    the fast fourier transform of the degree values upto the nearest integer.

    Parameters:
    input_list (list): A list of numbers to be sorted and analyzed.

    Returns:
    tuple: A tuple containing the rounded mean, median and mode of the sorted list along with those 
    for the magnitude of the fast fourier transform of the degree values.

    Requirements:
    - math
    - statistics
    - numpy

    Example:
    >>> input_list = [30, 45, 60, 90, 180]
    >>> stats = task_func(input_list)
    >>> print(stats)
    (81, 60, 30, 10712, 8460, 8460)
    """
    fft = np.abs(np.fft.fft([math.degrees(x) for x in input_list]))
    sorted_list = sorted(input_list, key=lambda x: (math.degrees(x), x))
    mean = statistics.mean(sorted_list)
    median = statistics.median(sorted_list)
    mode = statistics.mode(sorted_list)
    mean_fft = round(statistics.mean(fft))
    median_fft = round(statistics.median(fft))
    mode_fft = round(statistics.mode(fft))
    return (mean, median, mode, mean_fft, median_fft, mode_fft)

import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        input_data = [30, 45, 60, 90, 180]
        result = task_func(input_data)
        self.assertEqual(result, (81, 60, 30, 10712, 8460, 8460))
        
    def test_case_2(self):
        input_data = [0, 90, 180, 270, 360]
        result = task_func(input_data)
        self.assertEqual(result, (180, 180, 0, 24508, 21932, 21932))
        
    def test_case_3(self):
        input_data = [10, 20, 30, 40, 50]
        result = task_func(input_data)
        self.assertEqual(result, (30, 30, 10, 3296, 2437, 2437))
        
    def test_case_4(self):
        input_data = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]
        result = task_func(input_data)
        self.assertEqual(result[:5], (82.5, 82.5, 15, 11366, 6311))
        
    def test_case_5(self):
        input_data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
        result = task_func(input_data)
        self.assertEqual(result, (32.5, 32.5, 5, 4718, 2431, 6641))
