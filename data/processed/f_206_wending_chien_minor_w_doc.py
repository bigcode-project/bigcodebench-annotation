import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def f_497(data):
    """
    Computes the average of each row in a provided 2D array and appends these averages as a new column.
    Additionally, it plots the averages against their respective row indices.

    Parameters:
    data (numpy.array): A 2D numpy array with exactly eight columns, corresponding to 'A' through 'H'.

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame which includes the original data and an additional 'Average' column.
        - Axes: A matplotlib Axes object with the plot of row averages.

    Requirements:
    - pandas
    - matplotlib

    Example:
    >>> import numpy as np
    >>> data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
    >>> df, ax = f_497(data)
    >>> print(df.to_string(index=False))
     A  B  C  D  E  F  G  H  Average
     1  2  3  4  4  3  7  1    3.125
     6  2  3  4  3  4  4  1    3.375
    """
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    df['Average'] = df.mean(axis=1)

    # Creating a new figure and axis for plotting
    fig, ax = plt.subplots()
    df['Average'].plot(ax=ax)
    ax.set_ylabel('Average')  # Setting the Y-axis label to 'Average'

    return df, ax

import unittest
import numpy as np
import matplotlib
matplotlib.use('Agg')
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
        df, ax = f_497(data)
        # Testing the DataFrame
        self.assertEqual(df.shape, (2, 9))
        self.assertIn('Average', df.columns)
        self.assertAlmostEqual(df['Average'][0], 3.125, places=3)
        self.assertAlmostEqual(df['Average'][1], 3.375, places=3)
        # Testing the plot
        self.assertEqual(ax.get_title(), '')
        self.assertEqual(ax.get_xlabel(), '')
        self.assertEqual(ax.get_ylabel(), 'Average')
        self.assertEqual(len(ax.lines), 1)
    def test_case_2(self):
        data = np.array([[1, 1, 1, 1, 1, 1, 1, 1]])
        df, ax = f_497(data)
        # Testing the DataFrame
        self.assertEqual(df.shape, (1, 9))
        self.assertIn('Average', df.columns)
        self.assertEqual(df['Average'][0], 1.0)
        # Testing the plot
        self.assertEqual(len(ax.lines), 1)
    def test_case_3(self):
        data = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]])
        df, ax = f_497(data)
        # Testing the DataFrame
        self.assertEqual(df.shape, (2, 9))
        self.assertIn('Average', df.columns)
        self.assertEqual(df['Average'][0], 4.5)
        self.assertEqual(df['Average'][1], 4.5)
        # Testing the plot
        self.assertEqual(len(ax.lines), 1)
    def test_case_4(self):
        data = np.array([[0, 0, 0, 0, 0, 0, 0, 0], [10, 10, 10, 10, 10, 10, 10, 10]])
        df, ax = f_497(data)
        # Testing the DataFrame
        self.assertEqual(df.shape, (2, 9))
        self.assertIn('Average', df.columns)
        self.assertEqual(df['Average'][0], 0.0)
        self.assertEqual(df['Average'][1], 10.0)
        # Testing the plot
        self.assertEqual(len(ax.lines), 1)
    def test_case_5(self):
        data = np.array([[5, 5, 5, 5, 5, 5, 5, 5]])
        df, ax = f_497(data)
        # Testing the DataFrame
        self.assertEqual(df.shape, (1, 9))
        self.assertIn('Average', df.columns)
        self.assertEqual(df['Average'][0], 5.0)
        # Testing the plot
        self.assertEqual(len(ax.lines), 1)
