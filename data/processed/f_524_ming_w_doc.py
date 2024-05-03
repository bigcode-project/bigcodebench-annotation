import numpy as np
from scipy.optimize import curve_fit


def f_22(x, y, labels):
    """
    Fit an exponential curve to given data points and plot the curves with labels.

    This function fits an exponential curve of the form: f(x) = a * exp(-b * x) + c
    to the provided x and y data points for each set of data and plots the fitted curves
    with the corresponding labels on a single matplotlib figure.

    Parameters:
    - x (list of np.ndarray): List of numpy arrays, each representing the x-values of the data points for a dataset.
    - y (list of np.ndarray): List of numpy arrays, each representing the y-values of the data points for a dataset.
    - labels (list of str): List of strings, each representing the label for a dataset.

    Returns:
    - matplotlib.figure.Figure: The figure object that contains the plotted curves.

    Requirements:
    - numpy
    - scipy.optimize

    Example:
    >>> x_data = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
    >>> y_data = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
    >>> labels = ['H2O', 'O2', 'CO2']
    """

    if not x or not y or not labels:
        raise ValueError("Empty data lists provided.")

    def exponential_func(x, a, b, c):
        """Exponential function model for curve fitting."""
        return a * np.exp(-b * x) + c

    fig, ax = plt.subplots()

    for i in range(len(x)):
        # Fit the exponential model to the data
        popt, _ = curve_fit(exponential_func, x[i], y[i])

        # Plot the fitted curve
        ax.plot(x[i], exponential_func(x[i], *popt), label=labels[i])

    ax.legend()

    return fig

import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Example data for all tests
        self.x = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([1, 3, 5])]
        self.y = [np.array([2, 3, 5]), np.array([5, 7, 10]), np.array([2.5, 3.5, 5.5])]
        self.labels = ["Test 1", "Test 2", "Test 3"]
    def test_plot_labels(self):
        """Ensure the plot includes all specified labels."""
        fig = f_22(self.x, self.y, self.labels)
        ax = fig.gca()
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertListEqual(legend_labels, self.labels, "Legend labels do not match input labels.")
    def test_curve_fit_success(self):
        """Verify that curve_fit successfully fits the data."""
        for x_arr, y_arr in zip(self.x, self.y):
            with self.subTest(x=x_arr, y=y_arr):
                popt, _ = curve_fit(lambda x, a, b, c: a * np.exp(-b * x) + c, x_arr, y_arr)
                self.assertTrue(len(popt) == 3, "Optimal parameters not found for the exponential fit.")
    def test_output_type(self):
        """Check the output type to be a matplotlib figure."""
        fig = f_22(self.x, self.y, self.labels)
        self.assertIsInstance(fig, plt.Figure, "Output is not a matplotlib figure.")
    def test_no_data(self):
        """Test the function with no data provided."""
        with self.assertRaises(ValueError, msg="Empty data lists should raise a ValueError."):
            f_22([], [], [])
    def test_non_numeric_data(self):
        """Ensure non-numeric data raises a ValueError during fitting."""
        x = [np.array(["a", "b", "c"])]
        y = [np.array(["d", "e", "f"])]
        labels = ["Invalid Data"]
        with self.assertRaises(ValueError, msg="Non-numeric data should raise a ValueError."):
            f_22(x, y, labels)
