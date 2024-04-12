import numpy as np
import pandas as pd
from random import randint
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def f_497(rows):
    """
    Create a Pandas DataFrame with random integer values between 0 and 9 for a given number of rows.
    Count the non-zero values in each column and visualize this information using a bar plot.
    
    Parameters:
    rows (int): The number of rows in the DataFrame.

    Returns:
    tuple: A tuple containing the following elements:
        - DataFrame: The generated DataFrame with random integer values.
        - Axes: The matplotlib Axes object containing the bar plot.

    Requirements:
    - numpy
    - pandas
    - random
    - matplotlib.pyplot

    Example:
    >>> df, ax = f_497(10)
    >>> print(df)
    >>> print(ax.title.get_text())  # Should return 'Non-Zero Value Counts'
    """
    plt.close('all')  # Clear previous plots
    
    # Create an empty DataFrame and Axes object for negative or zero rows
    if rows <= 0:
        empty_ax = plt.gca()
        empty_ax.set_title('Non-Zero Value Counts')
        return pd.DataFrame(columns=COLUMNS), empty_ax
    
    # Generate random data and create DataFrame
    data = np.random.randint(10, size=(rows, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Count non-zero values in each column
    counts = df.astype(bool).sum(axis=0)
    
    # Create bar plot for non-zero counts
    ax = counts.plot(kind='bar')
    ax.set_title('Non-Zero Value Counts')
    
    return df, ax

import unittest

# Test function
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test when rows is 0
        df, ax = f_497(0)
        self.assertTrue(df.empty)
        self.assertEqual(len(ax.patches), 0)
        self.assertEqual(ax.title.get_text(), 'Non-Zero Value Counts')

    def test_case_2(self):
        # Test when rows is 1
        df, ax = f_497(1)
        self.assertEqual(len(df), 1)
        self.assertEqual(len(ax.patches), 5)
        self.assertEqual(ax.title.get_text(), 'Non-Zero Value Counts')

    def test_case_3(self):
        # Test when rows is 10
        df, ax = f_497(10)
        self.assertEqual(len(df), 10)
        self.assertEqual(len(ax.patches), 5)
        self.assertEqual(ax.title.get_text(), 'Non-Zero Value Counts')

    def test_case_4(self):
        # Test when rows is negative
        df, ax = f_497(-5)
        self.assertTrue(df.empty)
        self.assertEqual(len(ax.patches), 0)
        self.assertEqual(ax.title.get_text(), 'Non-Zero Value Counts')

    def test_case_5(self):
        # Test when rows is large (e.g., 1000)
        df, ax = f_497(1000)
        self.assertEqual(len(df), 1000)
        self.assertEqual(len(ax.patches), 5)
        self.assertEqual(ax.title.get_text(), 'Non-Zero Value Counts')


if __name__ == "__main__":
    run_tests()