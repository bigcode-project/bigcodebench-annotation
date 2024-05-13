import matplotlib.pyplot as plt
from collections import Counter


FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']

def task_func(fruit_dict):
    """
    Given a constant list of fruits in FRUITS, and a dictionary 'fruit_dict' with keys as people's names and values 
    as their favorite fruit names, record the frequency of each fruits' occurence. Return a bar chart of the number 
    of fruits for each fruit type and return the dictionary with fruit names as keys and their counts as values. 

    Parameters:
    fruit_dict (dict): The dictionary with keys as people's names and values as fruit names.

    Returns:
    dict: A dictionary with fruit names as keys and their counts as values.
    matplotlib.axes.Axes: The axes object of the plot.

    Requirements:
    - collections
    - random
    - matplotlib

    Example:
    >>> fruit_dict = {'John': 'Apple', 'Alice': 'Banana', 'Bob': 'Cherry', 'Charlie': 'Date', 'David': 'Apple'}
    >>> freq, ax = task_func(fruit_dict)
    >>> dict(freq)
    {'Apple': 2, 'Banana': 1, 'Cherry': 1, 'Date': 1}
    """
    fruit_list = [item for item in fruit_dict.values() if isinstance(item, str) and item in FRUITS]
    fruit_counter = Counter(fruit_list)
    plt.bar(fruit_counter.keys(), fruit_counter.values())
    return Counter([item for item in fruit_dict.values() if isinstance(item, str)]), plt.gca()

import unittest
import matplotlib.axes
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        fruit_dict = {'John': 'Apple', 'Alice': 'Banana', 'Bob': 'Cherry'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 1, 'Banana': 1, 'Cherry': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_2(self):
        fruit_dict = {'John': 'Apple', 'Alice': 'Banana', 'Bob': 'Apple'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 2, 'Banana': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_3(self):
        fruit_dict = {}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_4(self):
        fruit_dict = {'John': 'Apple'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_5(self):
        fruit_dict = {'John': 123, 'Alice': None, 'Bob': 'Apple'}
        count_dict, ax = task_func(fruit_dict)
        self.assertEqual(count_dict, {'Apple': 1})
        self.assertIsInstance(ax, matplotlib.axes.Axes)
