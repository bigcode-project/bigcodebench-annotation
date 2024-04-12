from random import sample
from itertools import combinations

def f_470(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on a list of tuples, each representing row values to match and remove.
    Generates up to 'n_plots' scatter plots for random combinations of two columns from the remaining DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - tuples (list): A list of tuples, where each tuple contains values that, if matched, should result in the row being removed.
    - n_plots (int): The maximum number of scatter plots to generate from the remaining data.

    Returns:
    - pd.DataFrame: The DataFrame after specified rows have been removed.
    - list: A list of tuples, each containing a pair of column names used for the plot and the corresponding plot object.

    Requirements:
    - pandas for DataFrame manipulation.
    - numpy for numerical operations.
    - itertools for generating combinations of column names.
    - matplotlib.pyplot for creating scatter plots.

    Example:
    >>> df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
    >>> tuples = [(0.1, 0.2, 0.3, 0.4, 0.5)]
    >>> modified_df, plots = f_470(df, tuples, 3)
    """
    COLUMNS = ['A', 'B', 'C', 'D', 'E']
    df = df.set_index(list('ABCDE')).drop(tuples, errors='ignore').reset_index()
    plots = []
    possible_combinations = list(combinations(COLUMNS, 2))
    for _ in range(min(n_plots, len(possible_combinations))):
        selected_columns = sample(possible_combinations, 1)[0]
        possible_combinations.remove(selected_columns)
        ax = df.plot.scatter(x=selected_columns[0], y=selected_columns[1])
        plots.append((selected_columns, ax))
    return df, plots

import unittest
import pandas as pd
import numpy as np

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))

    def test_case_1(self):
        tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        modified_df, _ = f_470(self.df, tuples, 3)
        self.assertFalse(any(modified_df.apply(tuple, axis=1).isin(tuples)))

    def test_case_2(self):
        n_plots = 4
        _, plots = f_470(self.df, [], n_plots)
        self.assertEqual(len(plots), n_plots)

    def test_case_3(self):
        _, plots = f_470(self.df, [], 5)
        selected_columns = [plot[0] for plot in plots]
        self.assertTrue(len(selected_columns) == len(set(tuple(item) for item in selected_columns)))

    def test_case_4(self):
        modified_df, plots = f_470(self.df, [], 2)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 2)

    def test_case_5(self):
        tuples = [(101, 202, 303, 404, 505), (606, 707, 808, 909, 1000)]
        modified_df, _ = f_470(self.df, tuples, 3)
        self.assertEqual(len(modified_df), len(self.df))

if __name__ == '__main__':
    run_tests()
