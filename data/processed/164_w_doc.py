import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def task_func(num_labels=5, data_range=(0, 1)):
    """
    Generate random numeric data across a specified range for a given number of categories and visualize it with
     a stacked bar chart.

    Parameters:
    num_labels (int): Specifies the number of distinct categories or labels to generate data for. Defaults to 5.
    data_range (tuple): Defines the lower and upper bounds for the random data values. Defaults to (0, 1).

    Returns:
    matplotlib.figure.Figure: A Figure object containing the stacked bar chart of the generated data.

    Requirements:
    - pandas
    - matplotlib
    - numpy

    Example:
    >>> fig = task_func()
    >>> fig.show()  # This will display the figure with default parameters

    >>> fig = task_func(num_labels=3, data_range=(1, 10))
    >>> fig.show()  # This will display the figure with three labels and data range from 1 to 10
    """

    np.random.seed(0)
    columns = [f'Label{i + 1}' for i in range(num_labels)]
    data = pd.DataFrame(np.random.uniform(data_range[0], data_range[1], size=(num_labels, num_labels)), columns=columns)
    fig, ax = plt.subplots()
    data.plot(kind='bar', stacked=True, ax=ax)
    return fig

import unittest
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)  # Fixing the seed for the sake of determinism in tests
    @patch('matplotlib.pyplot.subplots')
    @patch('pandas.DataFrame.plot')
    def test_default_parameters(self, mock_plot, mock_subplots):
        """Test using default parameters."""
        # Mock figure and axes creation
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        # Call the function
        fig = task_func()
        # Assertions to ensure plot was called correctly
        mock_plot.assert_called_once()
        mock_plot.assert_called_with(kind='bar', stacked=True, ax=mock_ax)
        self.assertIsInstance(fig, MagicMock)
    @patch('matplotlib.pyplot.subplots')
    @patch('pandas.DataFrame.plot')
    def test_custom_parameters(self, mock_plot, mock_subplots):
        """Test with custom parameters."""
        # Mock figure and axes creation
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        # Call the function with custom parameters
        num_labels = 4
        data_range = (1, 10)
        fig = task_func(num_labels=num_labels, data_range=data_range)
        # Assertions to ensure plot was called correctly
        mock_plot.assert_called_once()
        mock_plot.assert_called_with(kind='bar', stacked=True, ax=mock_ax)
        self.assertIsInstance(fig, MagicMock)
    @patch('matplotlib.pyplot.subplots')
    @patch('pandas.DataFrame.plot')
    def test_custom_data_range(self, mock_plot, mock_subplots):
        """Test with a custom data range."""
        data_range = (10, 20)
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        # Call the function with a custom data range
        fig = task_func(data_range=data_range)
        # Assertions to ensure plot was called correctly
        mock_plot.assert_called_once()
        mock_plot.assert_called_with(kind='bar', stacked=True, ax=mock_ax)
        self.assertIsInstance(fig, MagicMock)
    @patch('matplotlib.pyplot.subplots')
    @patch('pandas.DataFrame.plot')
    def test_combined_parameters(self, mock_plot, mock_subplots):
        """Test with combined custom parameters."""
        num_labels = 7
        data_range = (5, 15)
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        # Call the function with custom number of labels and data range
        fig = task_func(num_labels=num_labels, data_range=data_range)
        # Assertions to ensure plot was called correctly
        mock_plot.assert_called_once()
        mock_plot.assert_called_with(kind='bar', stacked=True, ax=mock_ax)
        self.assertIsInstance(fig, MagicMock)
    def test_generate_data_structure(self):
        """Test the structure and range of generated data"""
        num_labels = 4
        data_range = (10, 20)
        columns = [f'Label{i + 1}' for i in range(num_labels)]
        df = pd.DataFrame(np.random.uniform(data_range[0], data_range[1], size=(num_labels, num_labels)),
                          columns=columns)
        # Check correct number of labels (columns)
        self.assertEqual(len(df.columns), num_labels)
        # Check correct number of entries (rows)
        self.assertEqual(len(df), num_labels)
        # Check all values are within specified range
        for value in df.values.flatten():
            self.assertTrue(data_range[0] <= value <= data_range[1])
