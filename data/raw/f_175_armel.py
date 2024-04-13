import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants

def f_175(data):
    """
    Calculate the mean and standard deviation of the X and Y values in the dictionary and draw a line plot of Y vs X.

    Parameters:
    - data (dict): A dictionary with 2 keys 'X' and 'Y'. The corresponding values are lists of float values.

    Returns:
    - dict: A dictionary with 4 keys :
        - 'X_mean' and 'X_std' which respectively represent the mean and the standard deviation of the X values.
        - 'Y_mean' and 'Y_std' which respectively represent the mean and the standard deviation of the Y values. 

    Requirements:
    - numpy
    - pandas
    - matplotlib

    Example:
    >>> data = {
        'X': [1, 2, 3, 4, 5],
        'Y': [2, 4, 6, 8, 10]
    }
    >>> stats, ax = f_175(data)
    >>> stats
    {'X_mean': 3.0, 'X_std': 1.4142135623730951, 'Y_mean': 6.0, 'Y_std': 2.8284271247461903}
    >>> ax  # Returns the Axes object of the plot
    """
    df = pd.DataFrame(data)
    statistics = {
        'X_mean': np.mean(df['X']),
        'X_std': np.std(df['X']),
        'Y_mean': np.mean(df['Y']),
        'Y_std': np.std(df['Y']),
    }
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(df['X'], df['Y'])
    return statistics, ax

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_175 function."""
    def test_case_1(self):
        data = {
            'X': [1, 2, 3, 4, 5],
            'Y': [2, 4, 6, 8, 10]
        }
        stats, ax = f_175(data)
        expected_stats = {
            'X_mean': 3.0, 
            'X_std': np.std([1, 2, 3, 4, 5], ddof=0),
            'Y_mean': 6.0,
            'Y_std': np.std([2, 4, 6, 8, 10], ddof=0)
        }
        self.assertEqual(stats, expected_stats)
        self.assertEqual(ax.get_lines()[0].get_xdata().tolist(), data['X'])
        self.assertEqual(ax.get_lines()[0].get_ydata().tolist(), data['Y'])

    def test_case_2(self):
        data = {
            'X': [2, 4, 6, 8, 10],
            'Y': [1, 3, 5, 7, 9]
        }
        stats, ax = f_175(data)
        expected_stats = {
            'X_mean': 6.0,
            'X_std': np.std([2, 4, 6, 8, 10], ddof=0),
            'Y_mean': 5.0,
            'Y_std': np.std([1, 3, 5, 7, 9], ddof=0)
        }
        self.assertEqual(stats, expected_stats)
        self.assertEqual(ax.get_lines()[0].get_xdata().tolist(), data['X'])
        self.assertEqual(ax.get_lines()[0].get_ydata().tolist(), data['Y'])

    def test_case_3(self):
        data = {
            'X': [10, 20, 30, 40, 50],
            'Y': [5, 10, 15, 20, 25]
        }
        stats, ax = f_175(data)
        expected_stats = {
            'X_mean': 30.0,
            'X_std': np.std([10, 20, 30, 40, 50], ddof=0),
            'Y_mean': 15.0,
            'Y_std': np.std([5, 10, 15, 20, 25], ddof=0)
        }
        self.assertEqual(stats, expected_stats)
        self.assertEqual(ax.get_lines()[0].get_xdata().tolist(), data['X'])
        self.assertEqual(ax.get_lines()[0].get_ydata().tolist(), data['Y'])

    def test_case_4(self):
        data = {
            'X': [0, 0, 0, 0, 0],
            'Y': [1, 1, 1, 1, 1]
        }
        stats, ax = f_175(data)
        expected_stats = {
            'X_mean': 0.0,
            'X_std': 0.0,
            'Y_mean': 1.0,
            'Y_std': 0.0
        }
        self.assertEqual(stats, expected_stats)
        self.assertEqual(ax.get_lines()[0].get_xdata().tolist(), data['X'])
        self.assertEqual(ax.get_lines()[0].get_ydata().tolist(), data['Y'])

    def test_case_5(self):
        data = {
            'X': [-1, -2, -3, -4, -5],
            'Y': [-2, -4, -6, -8, -10]
        }
        stats, ax = f_175(data)
        expected_stats = {
            'X_mean': -3.0,
            'X_std': np.std([-1, -2, -3, -4, -5], ddof=0),
            'Y_mean': -6.0,
            'Y_std': np.std([-2, -4, -6, -8, -10], ddof=0)
        }
        self.assertEqual(stats, expected_stats)
        self.assertEqual(ax.get_lines()[0].get_xdata().tolist(), data['X'])
        self.assertEqual(ax.get_lines()[0].get_ydata().tolist(), data['Y'])

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__" :
    run_tests()