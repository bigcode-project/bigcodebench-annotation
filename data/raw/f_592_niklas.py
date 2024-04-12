import pandas as pd
import numpy as np
from scipy import stats

def f_592(df, column, alpha):
    """
    Test the normality of a particular numeric column from a DataFrame with Shapiro-Wilk test.

    Parameters:
    - df (DataFrame): The input DataFrame.
    - column (str): The column name.
    - alpha (float): The significance level.

    Returns:
    - bool: True if the column passes the normality test, False otherwise.

    Requirements:
    - pandas
    - numpy
    - scipy

    Example:
    >>> df = pd.DataFrame({'Value': np.random.normal(0, 1, 1000)})
    >>> print(f_592(df, 'Value', 0.05))
    True
    """
    if column not in df.columns:
        raise ValueError('Column does not exist in DataFrame')

    _, p = stats.shapiro(df[column])
    if p > alpha:
        return True
    else:
        return False

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'Value': np.random.normal(0, 1, 1000)})
        self.assertTrue(f_592(df, 'Value', 0.05))

    def test_case_2(self):
        df = pd.DataFrame({'Value': np.random.uniform(0, 1, 1000)})
        self.assertFalse(f_592(df, 'Value', 0.05))

    def test_case_3(self):
        df = pd.DataFrame({'Value': np.random.exponential(1, 1000)})
        self.assertFalse(f_592(df, 'Value', 0.05))

    def test_case_4(self):
        df = pd.DataFrame({'Value': np.random.lognormal(0, 1, 1000)})
        self.assertFalse(f_592(df, 'Value', 0.05))

    def test_case_5(self):
        df = pd.DataFrame({'Value': np.random.chisquare(1, 1000)})
        self.assertFalse(f_592(df, 'Value', 0.05))

run_tests()
if __name__ == "__main__":
    run_tests()