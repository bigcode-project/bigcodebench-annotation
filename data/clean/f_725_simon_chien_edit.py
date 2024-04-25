import pandas as pd
from statsmodels.tsa.stattools import adfuller


def f_725(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    """
    Determines if a specific subset of data is stationary.
    
    Functionality:
        1. Filters rows where column_b > 50 and column_c == 900.
        2. Checks if the resulting subset of data in column_a is stationary using the Augmented Dickey-Fuller test.
        3. Returns True if the data is stationary, False otherwise.

    Data is considered to be stationary if the p_value returned by the 
    Augmented Dickey-Fuller test is smaller than 0.05.

    If column_a is empty after filtering or if its values are constant, True
    is returned.
    
    Parameters:
        df (pd.DataFrame): A DataFrame containing the data.
        column_a (str): The name of the column to test for stationarity.
        column_b (str): The name of the column used for filtering based on its value being greater than 50.
        column_c (str): The name of the column used for filtering based on its value being equal to 900.
    
    Output:
        bool: True if the data in column_a (after filtering based on column_b and column_c) is stationary, False otherwise.
    
    Requirements:
        pandas
        statsmodels: for using the adfuller test

    Example:
    >>> df = pd.DataFrame({
    ...      'A': [1, 2, 3, 4, 5, 6],
    ...      'B': [60, 70, 80, 90, 100, 110],
    ...      'C': [900, 900, 900, 900, 900, 900]
    ... })
    >>> f_725(df, 'A', 'B', 'C')
    False

    >>> df = pd.DataFrame({
    ...     'TempA': [],
    ...     'TempB': [],
    ...     'TempC': []
    ... })
    >>> f_725(df, 'TempA', 'TempB', 'TempC')
    True
    """
    # Filter rows based on column_b and column_c
    filtered_df = df[(df[column_b] > 50) & (df[column_c] == 900)]

    if filtered_df[column_a].nunique() <= 1:
        return True

    # If dataframe is empty after filtering, return False
    if filtered_df.empty:
        return True

    # Perform Augmented Dickey-Fuller test
    adf_result = adfuller(filtered_df[column_a])
    p_value = adf_result[1]
    return p_value <= 0.05


import unittest
import os
import pandas as pd


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def setUp(self):
        # Create DataFrame in setUp for test isolation
        self.data = pd.DataFrame({
            'A': list(range(100)),
            'B': [x * 2 for x in range(100)],
            'C': [900 if x % 2 == 0 else 800 for x in range(100)]
        })

    def test_constant_value(self):
        # All values in column A are constant after filtering
        self.data['A'] = 5
        result = f_725(self.data, 'A', 'B', 'C')
        self.assertTrue(result, "Should be True as data is constant.")

    def test_empty_after_filter(self):
        # After filtering, no rows remain
        result = f_725(self.data[self.data['B'] > 1000], 'A', 'B', 'C')
        self.assertTrue(result, "Should be True as no data remains after filter.")

    def test_non_stationary_data(self):
        # Test a clearly non-stationary dataset
        result = f_725(self.data, 'A', 'B', 'C')
        self.assertFalse(result, "Should be False as data is non-stationary.")

    def test_stationary_data(self):
        # Test a stationary dataset
        self.data['A'] = 5
        result = f_725(self.data, 'A', 'B', 'C')
        self.assertTrue(result, "Should be True as data is stationary.")

    def test_edge_case_small_dataset(self):
        # Test a very small dataset
        small_data = pd.DataFrame({
            'A': [1, 1],
            'B': [60, 70],
            'C': [900, 900]
        })
        result = f_725(small_data, 'A', 'B', 'C')
        self.assertTrue(result, "Should be True due to small dataset size or no variation.")


if __name__ == '__main__':
    run_tests()
