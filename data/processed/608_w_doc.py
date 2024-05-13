import seaborn as sns
from random import sample


# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    """
    Remove rows from a dataframe based on values of multiple columns, and then create n random pairs of two columns 
    against each other to generate pairplots.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    tuples (list of tuple): A list of tuples, where each tuple represents a row to be removed based on its values.
    n_plots (int): The number of pairplots to be generated using randomly selected column pairs.

    Returns:
    tuple: A tuple containing:
        - DataFrame: The modified DataFrame after removing specified rows.
        - list of Axes: A list containing the generated pairplots.

    Requirements:
    - seaborn
    - random

    Example:
    >>> import numpy as np, pandas as pd
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plots = task_func(df, tuples, 3)
    """

    if not df.empty:
        df = df[~df.apply(tuple, axis=1).isin(tuples)]
    plots = []
    if n_plots > 0 and not df.empty:
        available_columns = df.columns.tolist()
        for _ in range(min(n_plots, len(available_columns) // 2)):  # Ensure we have enough columns
            selected_columns = sample(available_columns, 2)
            plot = sns.pairplot(df, vars=selected_columns)
            plots.append(plot)
    return df, plots

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # Common setup for generating DataFrame for testing
        self.df = pd.DataFrame({
            'A': list(range(0, 100, 10)) + [10, 60],
            'B': list(range(10, 110, 10)) + [20, 70],
            'C': list(range(20, 120, 10)) + [30, 80],
            'D': list(range(30, 130, 10)) + [40, 90],
            'E': list(range(40, 140, 10)) + [50, 100]
        })
    def test_case_1(self):
        tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        modified_df, plots = task_func(self.df, tuples, 3)
        self.assertTrue(all(tuple(row) not in tuples for row in modified_df.to_numpy()))
        # Check the number of plots does not exceed min(n_plots, len(df.columns) // 2)
        expected_plot_count = min(3, len(self.df.columns) // 2)
        self.assertEqual(len(plots), expected_plot_count)
    def test_case_2(self):
        tuples = [(200, 200, 200, 200, 200), (300, 300, 300, 300, 300)]
        modified_df, plots = task_func(self.df, tuples, 2)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 2)
    def test_case_3(self):
        tuples = []
        modified_df, plots = task_func(self.df, tuples, 1)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 1)
    def test_case_4(self):
        tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        modified_df, plots = task_func(self.df, tuples, 0)
        self.assertTrue(all(row not in modified_df.values for row in tuples))
        self.assertEqual(len(plots), 0)
    def test_case_5(self):
        tuples = [(10, 20, 30, 40, 50), (200, 200, 200, 200, 200)]
        modified_df, plots = task_func(self.df, tuples, 4)
        # Ensure the specific tuple is not in the DataFrame
        self.assertTrue((10, 20, 30, 40, 50) not in modified_df.values)
        # Check the number of plots does not exceed min(n_plots, len(df.columns) // 2)
        expected_plot_count = min(4, len(self.df.columns) // 2)
        self.assertEqual(len(plots), expected_plot_count)
