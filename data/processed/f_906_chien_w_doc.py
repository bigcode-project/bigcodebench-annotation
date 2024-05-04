import pandas as pd
from matplotlib import pyplot as plt


def f_256(arr):
    """
    Calculate the sum of each row in a 2D numpy array and plot these sums as a time series.

    This function takes a 2D numpy array and computes the sum of elements in each row. It
    then creates a Pandas DataFrame with these row sums and plots them as a time series,
    using dates starting from January 1, 2020, for each row.

    Parameters:
    arr (numpy.ndarray): A 2D numpy array.

    Returns:
    matplotlib.axes._axes.Axes: A plot representing the time series of row sums.

    Requirements:
    - pandas
    - matplotlib

    Handling Scenarios:
    - For non-empty arrays: The function computes the sum of elements for each row, 
    stores these sums in a Pandas DataFrame, and then plots them. Each row in the plot represents 
    the sum for a specific day, starting from January 1, 2020.
    - For empty arrays: The function creates an empty plot with the 
    title 'Time Series of Row Sums' but without data. This is achieved by checking if the array size 
    is zero (empty array) and if so, creating a subplot without any data.
    
    Note: 
    - The function uses 'pandas' for DataFrame creation and 'matplotlib.pyplot' for plotting. 
    The dates in the plot start from January 1, 2020, and each subsequent row represents the next day.
    
    Example:
    >>> arr = np.array([[i + j for i in range(3)] for j in range(5)])
    >>> ax = f_256(arr)
    >>> ax.get_title()
    'Time Series of Row Sums'
    """
    if not arr.size:  # Check for empty array
        _, ax = plt.subplots()
        ax.set_title("Time Series of Row Sums")
        return ax
    row_sums = arr.sum(axis=1)
    df = pd.DataFrame(row_sums, columns=["Sum"])
    df.index = pd.date_range(start="1/1/2020", periods=df.shape[0])
    ax = df.plot(title="Time Series of Row Sums")
    return ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for the function f_256."""
    def test_basic_functionality(self):
        """Test the basic functionality of the function."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        ax = f_256(arr)
        # Check if the function returns Axes object
        self.assertIsInstance(ax, plt.Axes)
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Time Series of Row Sums")
        # Check if the data plotted matches the expected sum of rows
        y_data = [line.get_ydata() for line in ax.get_lines()][0]
        expected_sums = arr.sum(axis=1)
        np.testing.assert_array_equal(y_data, expected_sums)
    def test_empty_array(self):
        """Test the function with an empty array."""
        arr = np.array([])
        ax = f_256(arr)
        # Check if the function returns Axes object
        self.assertIsInstance(ax, plt.Axes)
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Time Series of Row Sums")
        # Check if the data plotted is empty
        lines = ax.get_lines()
        self.assertEqual(len(lines), 0)
    def test_single_row_array(self):
        """Test the function with a single row array."""
        arr = np.array([[1, 2, 3]])
        ax = f_256(arr)
        # Check if the function returns Axes object
        self.assertIsInstance(ax, plt.Axes)
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Time Series of Row Sums")
        # Check if the data plotted matches the expected sum of the single row
        y_data = [line.get_ydata() for line in ax.get_lines()][0]
        expected_sum = arr.sum(axis=1)
        np.testing.assert_array_equal(y_data, expected_sum)
    def test_negative_values(self):
        """Test the function with negative values."""
        arr = np.array([[-1, -2, -3], [-4, -5, -6]])
        ax = f_256(arr)
        # Check if the function returns Axes object
        self.assertIsInstance(ax, plt.Axes)
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Time Series of Row Sums")
        # Check if the data plotted matches the expected sum of rows
        y_data = [line.get_ydata() for line in ax.get_lines()][0]
        expected_sums = arr.sum(axis=1)
        np.testing.assert_array_equal(y_data, expected_sums)
    def test_zero_values(self):
        """Test the function with zero values."""
        arr = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        ax = f_256(arr)
        # Check if the function returns Axes object
        self.assertIsInstance(ax, plt.Axes)
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Time Series of Row Sums")
        # Check if the data plotted matches the expected sum of rows
        y_data = [line.get_ydata() for line in ax.get_lines()][0]
        expected_sums = arr.sum(axis=1)
        np.testing.assert_array_equal(y_data, expected_sums)
    def tearDown(self):
        plt.close()
