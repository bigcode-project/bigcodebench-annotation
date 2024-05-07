import pandas as pd
import matplotlib.pyplot as plt
from random import sample

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']


def f_62(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    '''
    Remove rows from a dataframe based on column values and generate random scatter plots.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to be modified.
    - tuples (list): A list of tuples, each representing a row's values for removal.
    - n_plots (int): Number of scatter plots to generate from random pairs of columns.

    Returns:
    - pd.DataFrame: The DataFrame after removal of specified rows.
    - list: A list containing matplotlib Axes objects of the generated plots.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - random

    Example:
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=COLUMNS)
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plots = f_62(df, tuples, 3)
    '''
    df = df[~df.apply(tuple, axis=1).isin(tuples)]
    plots = []
    for _ in range(n_plots):
        selected_columns = sample(COLUMNS, 2)
        ax = df.plot(x=selected_columns[0], y=selected_columns[1], kind='scatter')
        plots.append(ax)
    plt.show()
    return df, plots

import unittest
from unittest.mock import patch
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=COLUMNS)
        self.tuples = [(self.df.iloc[0].values), (self.df.iloc[1].values)]
    def test_no_plots_generated(self):
        """Test case with zero plots requested."""
        _, plots = f_62(self.df, [], 0)  # Request 0 plots.
        self.assertEqual(len(plots), 0, "No plots should be generated when n_plots is 0.")
    def test_plot_generation(self):
        _, plots = f_62(self.df, [], 3)
        self.assertEqual(len(plots), 3, "Should generate exactly 3 plots.")
    @patch('matplotlib.pyplot.show')
    def test_empty_dataframe(self, mock_show):
        empty_df = pd.DataFrame(columns=COLUMNS)
        modified_df, plots = f_62(empty_df, [], 2)
        self.assertTrue(modified_df.empty, "DataFrame should be empty.")
        self.assertEqual(len(plots), 2, "Should attempt to generate 2 plots even for an empty DataFrame.")
    def test_no_row_removal(self):
        modified_df, _ = f_62(self.df, [(999, 999, 999, 999, 999)], 0)
        self.assertEqual(len(modified_df), len(self.df), "No rows should be removed.")
    def test_random_plot_columns(self):
        _, plots = f_62(self.df, [], 1)
        # Assuming f_62 generates at least one plot and adds it to the list,
        # access the first plot for testing.
        first_plot = plots[0]
        plot_columns = [first_plot.get_xlabel(), first_plot.get_ylabel()]
        self.assertIn(plot_columns[0], COLUMNS, "X-axis should be from COLUMNS.")
        self.assertIn(plot_columns[1], COLUMNS, "Y-axis should be from COLUMNS.")
