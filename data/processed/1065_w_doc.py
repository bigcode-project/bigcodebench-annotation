from scipy import fftpack
from matplotlib import pyplot as plt


def task_func(arr):
    """
    Performs a Fast Fourier Transform (FFT) on the sum of each row in a 2D array and
    plots the absolute values of the FFT coefficients.

    Parameters:
    arr (numpy.ndarray): A 2D numpy array.

    Returns:
    matplotlib.axes.Axes: An Axes object displaying the plot of the absolute values of the FFT coefficients.

    Requirements:
    - scipy.fftpack
    - matplotlib.pyplot

    Example:
    >>> import numpy as np
    >>> arr = np.array([[i + j for i in range(3)] for j in range(5)])
    >>> ax = task_func(arr)
    >>> ax.get_title()
    'Absolute values of FFT coefficients'
    """
    row_sums = arr.sum(axis=1)
    fft_coefficients = fftpack.fft(row_sums)
    _, ax = plt.subplots()
    ax.plot(np.abs(fft_coefficients))
    ax.set_title("Absolute values of FFT coefficients")
    return ax

import unittest
import numpy as np
from scipy import fftpack
class TestCases(unittest.TestCase):
    """Test cases for the function task_func."""
    def test_plot_title(self):
        """Test that the plot title is correct."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        ax = task_func(arr)
        self.assertEqual(ax.get_title(), "Absolute values of FFT coefficients")
    def test_plot_data(self):
        """Test that the plot data is correct."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        ax = task_func(arr)
        y_data = ax.lines[0].get_ydata()
        row_sums = arr.sum(axis=1)
        fft_coefficients = fftpack.fft(row_sums)
        expected_y_data = np.abs(fft_coefficients)
        np.testing.assert_array_equal(y_data, expected_y_data)
    def test_with_zeros(self):
        """Test that the plot data is correct when the array is all zeros."""
        arr = np.zeros((5, 3))
        ax = task_func(arr)
        y_data = ax.lines[0].get_ydata()
        expected_y_data = np.zeros(5)
        np.testing.assert_array_equal(y_data, expected_y_data)
    def test_with_ones(self):
        """Test that the plot data is correct when the array is all ones."""
        arr = np.ones((5, 3))
        ax = task_func(arr)
        y_data = ax.lines[0].get_ydata()
        expected_y_data = [15.0, 0.0, 0.0, 0.0, 0.0]
        np.testing.assert_array_almost_equal(y_data, expected_y_data)
    def test_with_large_numbers(self):
        """Test that the plot data is correct when the array has large numbers."""
        arr = np.array([[i * 100 + j * 1000 for i in range(3)] for j in range(5)])
        ax = task_func(arr)
        y_data = ax.lines[0].get_ydata()
        row_sums = arr.sum(axis=1)
        fft_coefficients = fftpack.fft(row_sums)
        expected_y_data = np.abs(fft_coefficients)
        np.testing.assert_array_equal(y_data, expected_y_data)
    def tearDown(self):
        plt.close()
