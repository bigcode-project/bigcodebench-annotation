import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

def task_func(length, range_limit=100, seed=0):
    """
    Create a list of random numbers, sort them and record the distribution of the numbers in a histogram using 
    default settings in a deterministic seaborn plot. Return the axes object and the list of random numbers.

    Parameters:
    length (int): The length of the list of random numbers.
    range_limit (int, Optional): The range of the random numbers. Defaults to 100. Must be greater than 1.
    seed (int, Optional): The seed value for the random number generator. Defaults to 0.

    Returns:
    Tuple[matplotlib.axes._axes.Axes, List[int]]: The axes object with the plot and the list of random numbers.

    Requirements:
    - random
    - matplotlib.pyplot
    - seaborn
    - numpy

    Raises:
    ValueError: If range_limit is less than or equal to 1.

    Example:
    >>> import matplotlib.pyplot as plt
    >>> ax, data = task_func(1000, 100, 24) # Generate a list of 1000 random numbers between 1 and 100
    >>> isinstance(ax, plt.Axes)
    True
    """
    if range_limit <= 1:
        raise ValueError("range_limit must be greater than 1")
    random.seed(seed)
    np.random.seed(seed)
    random_numbers = [random.randint(1, range_limit) for _ in range(length)]
    random_numbers.sort()
    plt.figure()
    plot = sns.histplot(random_numbers, kde=False)
    return plot.axes, random_numbers

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        _, data = task_func(1000)
        self.assertEqual(len(data), 1000)
    def test_case_2(self):
        with self.assertRaises(ValueError):
            _, data = task_func(1000, -3, 42)
        
    def test_case_3(self):
        _, data = task_func(20, 75, 77)
        self.assertEqual(data, [1, 4, 15, 19, 23, 25, 25, 26, 31, 31, 33, 36, 38, 42, 61, 64, 65, 65, 72, 72])
        self.assertTrue(all(1 <= num <= 75 for num in data))
    def test_case_4(self):
        ax, data = task_func(1000, 75)
        target = np.array([98, 103, 106, 73, 87, 92, 94, 84, 90, 95, 78])
        self.assertTrue((ax.containers[0].datavalues == target).all()) 
    def test_case_5(self):
        _, data1 = task_func(1000, seed=42)
        _, data2 = task_func(1000, seed=42)
        self.assertEqual(data1, data2)
