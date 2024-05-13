import numpy as np
import matplotlib.pyplot as plt


def task_func(data: np.ndarray) -> plt.Axes:
    """
    Plots the cumulative probability distribution of a given NumPy array of numbers,
    representing how the cumulative probability increases with the sorted data indexes.

    Parameters:
    - data (numpy.ndarray): The input NumPy array of non-negative numbers.

    Returns:
    - matplotlib.pyplot.Axes: The plot of cumulative probabilities.

    Requirements:
    - numpy
    - matplotlib

    Raises:
    - ValueError: If the input array contains negative numbers or NaNs.
    - TypeError: If the input array contains non-numeric inputs.

    Note:
    - In case of an all-zeros input, the cumulative probability remains at 0 across all indexes.
    - The plot uses marker ('o') and a solid line ('-') for the cumulative probability curve.
    - The plot is titled "Cumulative Probability Plot", with "Index" on the x-axis and
      "Cumulative Probability" on the y-axis.

    Example:
    >>> ax = task_func(np.array([1, 2, 3, 4, 5]))
    >>> ax.get_title()
    'Cumulative Probability Plot'
    """

    if np.any(data < 0) or np.isnan(data).any():
        raise ValueError("Input array contains negative numbers or NaNs.")
    if not np.issubdtype(data.dtype, np.number):
        raise TypeError("Input array contains non-numeric values.")
    data_sorted = np.sort(data)
    cumulative_prob = (
        np.cumsum(data_sorted) / np.sum(data_sorted)
        if np.sum(data_sorted) != 0
        else np.zeros_like(data_sorted)
    )
    fig, ax = plt.subplots()
    ax.plot(cumulative_prob, marker="o", linestyle="-")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Probability")
    ax.set_title("Cumulative Probability Plot")
    return ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
class TestCases(unittest.TestCase):
    def tearDown(self):
        plt.close("all")
    def helper_assert_plot_attributes(self, ax):
        self.assertIsInstance(ax, plt.Axes)
        self.assertIn("Cumulative Probability Plot", ax.get_title())
        self.assertIn("Index", ax.get_xlabel())
        self.assertIn("Cumulative Probability", ax.get_ylabel())
        lines = ax.get_lines()
        self.assertIsInstance(
            lines[0], Line2D, "The plot should contain a Line2D object."
        )
        self.assertEqual(lines[0].get_marker(), "o", "The marker should be 'o'.")
        self.assertEqual(lines[0].get_linestyle(), "-", "The linestyle should be '-'.")
    def helper_assert_cumulative_probability_correctness(
        self, ax, expected_cumulative_prob
    ):
        line = ax.get_lines()[0]
        np.testing.assert_array_almost_equal(
            line.get_ydata(),
            expected_cumulative_prob,
            decimal=2,
            err_msg="Cumulative probability calculation is incorrect.",
        )
    def test_negative_numbers(self):
        data = np.array([-1, 0, 1, 2, 3])
        with self.assertRaises(ValueError):
            task_func(data)
    def test_nan_values(self):
        data = np.array([1, 2, 3, np.nan, 5])
        with self.assertRaises(ValueError):
            task_func(data)
    def test_non_numeric_values(self):
        data = np.array([1, 2, 3, "hello", 5])
        with self.assertRaises(TypeError):
            task_func(data)
    def test_increasing_array(self):
        data = np.array([1, 2, 3])
        ax = task_func(data)
        expected_cumulative_prob = np.array([1 / 6, 1 / 2, 1])
        self.helper_assert_plot_attributes(ax=ax)
        self.helper_assert_cumulative_probability_correctness(
            ax=ax, expected_cumulative_prob=expected_cumulative_prob
        )
    def test_constant_array(self):
        data = np.array([1, 1, 1, 1, 1])
        ax = task_func(data)
        self.helper_assert_plot_attributes(ax)
        expected_cumulative_prob = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
        self.helper_assert_cumulative_probability_correctness(
            ax=ax, expected_cumulative_prob=expected_cumulative_prob
        )
    def test_zeros_array(self):
        data = np.array([0, 0, 0, 0, 0])
        ax = task_func(data)
        self.helper_assert_plot_attributes(ax)
        expected_cumulative_prob = np.array([0, 0, 0, 0, 0])
        self.helper_assert_cumulative_probability_correctness(
            ax=ax, expected_cumulative_prob=expected_cumulative_prob
        )
    def test_single_element_array(self):
        data = np.array([7])
        ax = task_func(data)
        self.helper_assert_plot_attributes(ax)
        expected_cumulative_prob = np.array([1])
        self.helper_assert_cumulative_probability_correctness(
            ax=ax, expected_cumulative_prob=expected_cumulative_prob
        )
