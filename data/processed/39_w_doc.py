import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

# Constants
ALPHA = 0.05


def task_func(data_matrix):
    """
    Calculate the mean value of each row in a 2D data matrix, run a t-test from a sample against the population value, and record the mean values that differ significantly.
    - Create a lineplot with the mean of rows in red. Its label is 'Means'.
    - Create a line plot with the significant_indices (those with a pvalue less than ALPHA) on the x-axis and the corresponding means on the y-axis. This plot should be blue. Its label is 'Significant Means'.
    - Create an horizontal line which represent the mean computed on the whole 2D matrix. It should be in green. Its label is 'Population Mean'.

    Parameters:
    data_matrix (numpy.array): The 2D data matrix.

    Returns:
    tuple: A tuple containing:
        - list: A list of indices of the means that are significantly different from the population mean.
        - Axes: The plot showing the means and significant means.

    Requirements:
    - numpy
    - scipy.stats.ttest_1samp
    - matplotlib.pyplot

    Example:
    >>> data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
    >>> indices, ax = task_func(data)
    >>> print(indices)
    []

    Example 2:
    >>> data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> indices, ax = task_func(data)
    >>> print(indices)
    []
    """

    means = np.mean(data_matrix, axis=1)
    population_mean = np.mean(data_matrix)
    _, p_value = ttest_1samp(means, population_mean)
    significant_indices = np.where(p_value < ALPHA)[0]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(means, "ro", label="Means")
    ax.plot(
        significant_indices, means[significant_indices], "bo", label="Significant Means"
    )
    ax.axhline(y=population_mean, color="g", linestyle="-", label="Population Mean")
    ax.legend()
    return significant_indices.tolist(), ax

import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self._validate_function(data)
    def test_case_2(self):
        data = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        self._validate_function(data)
    def test_case_3(self):
        data = np.array([[3, 5, 7, 1000], [200, 5, 7, 1], [1, 9, 14, 700]])
        self._validate_function(data)
    def test_case_4(self):
        data = np.array(
            [
                [1, 2, 3, 4, 5, 4, 3, 2, 1],
            ]
        )
        self._validate_function(data)
    def test_case_5(self):
        data = np.array([[1], [1], [1]])
        self._validate_function(data)
    def _validate_function(self, data):
        indices, ax = task_func(data)
        self.assertIsInstance(indices, list)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0].get_color(), "r")
        self.assertEqual(lines[0].get_label(), "Means")
        self.assertEqual(lines[1].get_color(), "b")
        self.assertEqual(lines[1].get_label(), "Significant Means")
        self.assertEqual(lines[2].get_color(), "g")
        self.assertEqual(lines[2].get_label(), "Population Mean")
