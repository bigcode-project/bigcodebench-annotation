import pandas as pd
import matplotlib.pyplot as plt


def f_545(csv_file_path: str):
    """
    This function reads data from a CSV file, normalizes a specific column named 'column1', and then plots the normalized data.

    - The title is created using Python's string formatting, aligning 'Plot Title' and 'Normalized Column 1' on either side of a 
    colon, each padded to 20 characters.
    - Similarly, the x-label is formatted with 'Index' and 'Normalized Value' on either side of a colon, 
    each padded to 20 characters.
    - The y-label is set in the same manner, with 'Frequency' and 'Normalized Value' on either side of a colon.

    Parameters:
    - csv_file_path (str): Path to the CSV file. The file must contain a column named 'column1'.

    Returns:
    - The matplotlib.axes.Axes object with the plot of the normalized data.

    Requirements:
    - pandas
    - matplotlib

    Example:
    >>> ax = f_545('data.csv')
    >>> ax.get_title()
    'Plot Title :  Normalized Column 1'
    """
    df = pd.read_csv(csv_file_path)
    mean = df["column1"].mean()
    std = df["column1"].std()
    df["column1_normalized"] = (df["column1"] - mean) / std

    # Creating a figure and axes
    _, ax = plt.subplots()
    # Plotting on the created axes
    ax.plot(df["column1_normalized"])
    title = "%*s : %*s" % (20, "Plot Title", 20, "Normalized Column 1")
    xlabel = "%*s : %*s" % (20, "Index", 20, "Normalized Value")
    ylabel = "%*s : %*s" % (20, "Frequency", 20, "Normalized Value")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Return the axes object for further manipulation
    return ax

import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for the f_545 function."""
    @patch("pandas.read_csv")
    def test_title_format(self, mock_read_csv):
        """Test that the function returns the correct title."""
        # Mocking the DataFrame
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = f_545("dummy_path")
        expected_title = "          Plot Title :  Normalized Column 1"
        self.assertEqual(ax.get_title(), expected_title)
    @patch("pandas.read_csv")
    def test_xlabel_format(self, mock_read_csv):
        """Test that the function returns the correct xlabel."""
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = f_545("dummy_path")
        expected_xlabel = "               Index :     Normalized Value"
        self.assertEqual(ax.get_xlabel(), expected_xlabel)
    @patch("pandas.read_csv")
    def test_ylabel_format(self, mock_read_csv):
        """Test that the function returns the correct ylabel."""
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = f_545("dummy_path")
        expected_ylabel = "           Frequency :     Normalized Value"
        self.assertEqual(ax.get_ylabel(), expected_ylabel)
    @patch("pandas.read_csv")
    def test_data_points_length(self, mock_read_csv):
        """Test that the function returns the correct number of data points."""
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = f_545("dummy_path")
        line = ax.get_lines()[0]
        self.assertEqual(len(line.get_data()[1]), 10)
    @patch("pandas.read_csv")
    def test_data_points_range(self, mock_read_csv):
        """Test that the function returns the correct data points."""
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = f_545("dummy_path")
        line = ax.get_lines()[0]
        data_points = line.get_data()[1]
        self.assertTrue(all(-3 <= point <= 3 for point in data_points))
    def tearDown(self):
        plt.clf()
