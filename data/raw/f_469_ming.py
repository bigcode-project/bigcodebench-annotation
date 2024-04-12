import pandas as pd
import numpy as np
import seaborn as sns
from random import sample

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def f_469(df, tuples, n_plots):
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
    - pandas
    - numpy
    - seaborn
    - random

    Example:
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plots = f_469(df, tuples, 3)
    """
    # Removing rows based on the tuples
    df = df.set_index(list('ABCDE')).drop(tuples, errors='ignore').reset_index()
    
    plots = []
    for _ in range(n_plots):
        # Randomly select two columns for pairplot
        selected_columns = sample(COLUMNS, 2)
        plot = sns.pairplot(df, vars=selected_columns)
        plots.append(plot)
    
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
        modified_df, plots = f_469(self.df, tuples, 3)
        self.assertTrue(all(row not in modified_df.values for row in tuples))
        self.assertEqual(len(plots), 3)

    def test_case_2(self):
        tuples = [(200, 200, 200, 200, 200), (300, 300, 300, 300, 300)]
        modified_df, plots = f_469(self.df, tuples, 2)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 2)

    def test_case_3(self):
        tuples = []
        modified_df, plots = f_469(self.df, tuples, 1)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 1)

    def test_case_4(self):
        tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        modified_df, plots = f_469(self.df, tuples, 0)
        self.assertTrue(all(row not in modified_df.values for row in tuples))
        self.assertEqual(len(plots), 0)

    def test_case_5(self):
        tuples = [(10, 20, 30, 40, 50), (200, 200, 200, 200, 200)]
        modified_df, plots = f_469(self.df, tuples, 4)
        self.assertTrue((10, 20, 30, 40, 50) not in modified_df.values)
        self.assertEqual(len(plots), 4)
if __name__ == "__main__":
    run_tests()