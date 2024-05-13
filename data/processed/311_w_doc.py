import numpy as np
import random
from scipy import stats


def task_func(list_of_lists, size=5, seed=0):
    """
    Calculate the mean, median, and mode of values in a list of lists.
    If a list is empty, fill it with SIZE (default: 5) random integers between 0 and 100, 
    and then calculate the statistics.
    
    Parameters:
    list_of_lists (list): The list of lists.
    size (int, Optional): The number of random integers to generate. Default is 5.
    seed (int, Optional): Seed value for random number generation. Default is 0.
    
    Returns:
    dict: A dictionary with the mean, median, and mode of the values.
    
    Requirements:
    - numpy
    - random
    - scipy.stats
    
    Example:
    >>> task_func([[1, 2, 3], [], [4, 5, 6]])
    {'mean': 23.454545454545453, 'median': 5.0, 'mode': array([5])}
    """
    random.seed(seed)
    data = []
    for list_ in list_of_lists:
        if list_:
            data += list_
        else:
            data += [random.randint(0, 100) for _ in range(size)]
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': stats.mode(data)[0]
    }

import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test with a mix of non-empty and empty lists.
        input_data = [[1, 2, 3], [], [4, 5, 6]]
        result = task_func(input_data)
        self.assertTrue(result["mean"] < 100)
        self.assertTrue(result["median"] < 100)
        self.assertTrue(result["mode"] < 100)
    def test_case_2(self):
        # Test with all non-empty lists.
        input_data = [[7, 8, 9], [10, 11, 12], [13, 14, 15]]
        result = task_func(input_data, 4)
        combined_data = [7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(result["mean"], np.mean(combined_data))
        self.assertEqual(result["median"], np.median(combined_data))
        self.assertEqual(result["mode"], stats.mode(combined_data).mode)
    def test_case_3(self):
        # Test with all empty lists.
        input_data = [[], [], []]
        result = task_func(input_data)
        self.assertTrue(result["mean"] < 100)
        self.assertTrue(result["median"] < 100)
        self.assertTrue(result["mode"] < 100)
    def test_case_4(self):
        # Test with lists containing both negative and positive integers.
        input_data = [[-1, -2, -3], [4, 5, 6], [-7, -8, -9]]
        result = task_func(input_data, 2)
        combined_data = [-1, -2, -3, 4, 5, 6, -7, -8, -9]
        self.assertEqual(result["mean"], np.mean(combined_data))
        self.assertEqual(result["median"], np.median(combined_data))
        self.assertEqual(result["mode"], stats.mode(combined_data).mode)
    def test_case_5(self):
        # Test with a single list.
        input_data = [[1, 2, 3, 4, 5]]
        result = task_func(input_data)
        self.assertEqual(result["mean"], np.mean(input_data[0]))
        self.assertEqual(result["median"], np.median(input_data[0]))
        self.assertEqual(result["mode"], stats.mode(input_data[0]).mode)
