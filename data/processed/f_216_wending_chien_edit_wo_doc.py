import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def f_110(num_groups=5, data_size=5, labels=None):
    """
    Generate random data and visualize it with a stacked bar chart, saving the chart to a file.
    This function facilitates the exploration and sharing of data distribution across multiple categories.

    Parameters:
    num_groups (int): Number of groups for which data is to be generated, defaulting to 5.
    data_size (int): Number of data points for each group, defaulting to 5.
    labels (list of str, optional): Labels for the groups. If None, default labels 'Group1', 'Group2', ...,
    'GroupN' are generated.

    Returns:
    tuple: A tuple containing:
        - matplotlib.figure.Figure: The Figure object containing the stacked bar chart.
        - pandas.DataFrame: The DataFrame with randomly generated data.
        - str: The filename where the plot is saved ('test_plot.png').

    Requirements:
    - pandas
    - matplotlib
    - numpy

    Example:
    >>> np.random.seed(0)
    >>> fig, data, plot_filename = f_110(3, 3, ['A', 'B', 'C'])
    >>> print(data)
              A         B         C
    0  0.548814  0.715189  0.602763
    1  0.544883  0.423655  0.645894
    2  0.437587  0.891773  0.963663
    >>> print(plot_filename)
    test_plot.png
    """
    if labels is None:
        labels = [f'Group{i + 1}' for i in range(num_groups)]
    data = pd.DataFrame(np.random.rand(data_size, num_groups), columns=labels)
    fig, ax = plt.subplots()
    data.plot(kind='bar', stacked=True, ax=ax)
    plot_filename = 'test_plot.png'
    fig.savefig(plot_filename)
    return fig, data, plot_filename

import unittest
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')
class TestCases(unittest.TestCase):
    def tearDown(self):
        """Ensure no files are left after tests."""
        try:
            os.remove('test_plot.png')
        except FileNotFoundError:
            pass
    def test_default_parameters(self):
        """Test the function with default parameters."""
        fig, data, plot_filename = f_110()
        self.assertIsInstance(fig, plt.Figure, "The function should return a matplotlib.figure.Figure object.")
        self.assertEqual(data.shape, (5, 5), "The default DataFrame should have 5 rows and 5 columns.")
        expected_columns = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
        self.assertListEqual(list(data.columns), expected_columns, "Default column labels are incorrect.")
        self.assertTrue(os.path.exists(plot_filename), "Plot file should be created.")
    def test_custom_parameters(self):
        """Test the function with custom number of groups, data size, and labels."""
        num_groups, data_size, labels = 3, 4, ['A', 'B', 'C']
        fig, data, plot_filename = f_110(num_groups=num_groups, data_size=data_size, labels=labels)
        self.assertIsInstance(fig, plt.Figure, "The function should return a matplotlib.figure.Figure object.")
        self.assertEqual(data.shape, (4, 3), "DataFrame dimensions should match the custom parameters.")
        self.assertListEqual(list(data.columns), labels, "Column labels should match the custom labels provided.")
    def test_data_values(self):
        """Test that the data in the DataFrame is within the expected range (0.0, 1.0)."""
        fig, data, plot_filename = f_110()
        self.assertTrue((data >= 0.0).all().all() and (data <= 1.0).all().all(),
                        "All data should be within the range [0.0, 1.0].")
    def test_no_labels_provided(self):
        """Test that default labels are used when no labels are provided."""
        fig, data, plot_filename = f_110(num_groups=3)
        expected_columns = ['Group1', 'Group2', 'Group3']
        self.assertListEqual(list(data.columns), expected_columns,
                             "Default column labels are incorrect when no labels are provided.")
    def test_plot_file_cleanup(self):
        """Test that the plot file is cleaned up after a test."""
        fig, data, plot_filename = f_110()
        self.assertTrue(os.path.exists(plot_filename), "Plot file should exist immediately after creation.")
        os.remove(plot_filename)
        self.assertFalse(os.path.exists(plot_filename), "Plot file should be deleted in tearDown.")
