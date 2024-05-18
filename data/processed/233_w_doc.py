import random
import matplotlib.pyplot as plt


# Sample data
class Object:
    value = 0

    def __init__(self, value=None):
        if value is None:
            self.value = random.gauss(0, 1)
        else:
            self.value = value


def task_func(obj_list, attr, num_bins=30, seed=0):
    """
    Create a histogram of the specified attribute from a list of objects and return the histogram plot.

    Parameters:
    obj_list (list): The list of objects containing the attribute.
    attr (str): The attribute to generate a histogram for.
    num_bins (int, Optional): The number of bins to use in the histogram. Defaults to 30.
    seed (int, Optional): The seed for the random number generator. Defaults to 0.

    Returns:
    matplotlib.axes._axes.Axes: The histogram plot of the attribute values, with the title 'Histogram of attribute values', x-axis labeled 'Attribute Value', and y-axis labeled 'Count'.

    Requirements:
    - random (used for default object generation)
    - numpy (used for numerical computations)
    - matplotlib (used for plotting)

    Constants:
    - NUM_BINS (int): Number of bins to use in the histogram, set to 30 by default.

    Example:
    >>> obj_list = [Object(value=i) for i in range(10)]
    >>> ax = task_func(obj_list, 'value')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    random.seed(seed)
    attr_values = [getattr(obj, attr) for obj in obj_list]
    fig, ax = plt.subplots()
    ax.hist(attr_values, bins=num_bins, alpha=0.5)
    ax.set_title('Histogram of attribute values')
    ax.set_xlabel('Attribute Value')
    ax.set_ylabel('Count')
    return ax

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: Simple list of objects with integer values from 0 to 9
        random.seed(1)
        obj_list = [Object(value=i) for i in range(10)]
        ax = task_func(obj_list, 'value')
        
        # Assertions
        self.assertIsInstance(ax, plt.Axes, "Returned object is not a valid Axes object.")
        self.assertEqual(ax.get_title(), 'Histogram of attribute values', "Histogram title is incorrect.")
        self.assertEqual(ax.get_xlabel(), 'Attribute Value', "X-axis label is incorrect.")
        self.assertEqual(ax.get_ylabel(), 'Count', "Y-axis label is incorrect.")
        self.assertEqual(sum([p.get_height() for p in ax.patches]), len(obj_list), "Histogram data points do not match input list size.")
    def test_case_2(self):
        # Input 2: List of objects with random Gaussian values
        random.seed(2)
        obj_list = [Object() for _ in range(100)]
        ax = task_func(obj_list, 'value', seed=77)
        
        # Assertions
        self.assertIsInstance(ax, plt.Axes, "Returned object is not a valid Axes object.")
        self.assertEqual(ax.get_title(), 'Histogram of attribute values', "Histogram title is incorrect.")
        self.assertEqual(ax.get_xlabel(), 'Attribute Value', "X-axis label is incorrect.")
        self.assertEqual(ax.get_ylabel(), 'Count', "Y-axis label is incorrect.")
        self.assertEqual(sum([p.get_height() for p in ax.patches]), len(obj_list), "Histogram data points do not match input list size.")
        # Check axis data
        self.assertAlmostEqual(ax.get_xlim()[0], -3.933336166652307, delta=0.1, msg="X-axis lower limit is incorrect.")
        
    def test_case_3(self):
        # Input 3: List of objects with fixed value
        random.seed(3)
        obj_list = [Object(value=5) for _ in range(50)]
        ax = task_func(obj_list, 'value', seed=4)
        
        # Assertions
        self.assertIsInstance(ax, plt.Axes, "Returned object is not a valid Axes object.")
        self.assertEqual(ax.get_title(), 'Histogram of attribute values', "Histogram title is incorrect.")
        self.assertEqual(ax.get_xlabel(), 'Attribute Value', "X-axis label is incorrect.")
        self.assertEqual(ax.get_ylabel(), 'Count', "Y-axis label is incorrect.")
        self.assertEqual(sum([p.get_height() for p in ax.patches]), len(obj_list), "Histogram data points do not match input list size.")
    def test_case_4(self):
        # Input 4: Empty list
        obj_list = []
        ax = task_func(obj_list, 'value')
        
        # Assertions
        self.assertIsInstance(ax, plt.Axes, "Returned object is not a valid Axes object.")
        self.assertEqual(ax.get_title(), 'Histogram of attribute values', "Histogram title is incorrect.")
        self.assertEqual(ax.get_xlabel(), 'Attribute Value', "X-axis label is incorrect.")
        self.assertEqual(ax.get_ylabel(), 'Count', "Y-axis label is incorrect.")
        self.assertEqual(sum([p.get_height() for p in ax.patches]), 0, "Histogram data points do not match input list size.")
        # Check axis data
        self.assertAlmostEqual(ax.get_xlim()[0], -0.05, msg="X-axis limits are incorrect.", delta=0.01)
        self.assertAlmostEqual(ax.get_xlim()[1], 1.05, msg="X-axis limits are incorrect.", delta=0.01)
        self.assertAlmostEqual(ax.get_ylim()[0], -0.05, msg="Y-axis limits are incorrect.", delta=0.01)
        self.assertAlmostEqual(ax.get_ylim()[1], 0.05, msg="Y-axis limits are incorrect.", delta=0.01)
    def test_case_5(self):
        # Input 5: Large list of objects
        random.seed(5)
        obj_list = [Object(value=random.gauss(0, 5)) for _ in range(1000)]
        ax = task_func(obj_list, 'value')
        
        # Assertions
        self.assertIsInstance(ax, plt.Axes, "Returned object is not a valid Axes object.")
        self.assertEqual(ax.get_title(), 'Histogram of attribute values', "Histogram title is incorrect.")
        self.assertEqual(ax.get_xlabel(), 'Attribute Value', "X-axis label is incorrect.")
        self.assertEqual(ax.get_ylabel(), 'Count', "Y-axis label is incorrect.")
        self.assertEqual(sum([p.get_height() for p in ax.patches]), len(obj_list), "Histogram data points do not match input list size.")
