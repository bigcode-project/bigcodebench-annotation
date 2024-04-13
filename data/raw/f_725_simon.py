import pandas as pd
from statsmodels.tsa.stattools import adfuller


def f_725(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    '''
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
    '''
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

    def setUp(self) -> None:
        self.csv_path = os.path.join('f_725_data_simon', 'complex_data.csv')

    def test_case_1(self):
        df = pd.read_csv(self.csv_path)
        df = df.rename(columns={'A': 'X', 'B': 'Y', 'C': 'Z'})
        df_sliced = df.iloc[:500]
        result = f_725(df_sliced, 'X', 'Y', 'Z')
        self.assertTrue(result)

    def test_case_2(self):
        df = pd.read_csv(self.csv_path)
        df = df.rename(columns={'A': 'Alpha', 'B': 'Beta', 'C': 'Gamma'})
        df_sliced = df.iloc[500:]
        result = f_725(df_sliced, 'Alpha', 'Beta', 'Gamma')
        self.assertTrue(result)

    def test_case_3(self):
        df = pd.read_csv(self.csv_path)
        df = df.rename(columns={'A': 'Col1', 'B': 'Col2', 'C': 'Col3'})
        df['Col1'] = 50
        result = f_725(df, 'Col1', 'Col2', 'Col3')
        self.assertTrue(result)

    def test_case_4(self):
        df = pd.read_csv(self.csv_path)
        df = df.rename(columns={'A': 'Data1', 'B': 'Data2', 'C': 'Data3'})
        df['Data2'] = 40
        df['Data3'] = 910
        result = f_725(df, 'Data1', 'Data2', 'Data3')
        self.assertTrue(result)

    def test_case_5(self):
        df = pd.DataFrame({
            'TempA': [],
            'TempB': [],
            'TempC': []
        })
        result = f_725(df, 'TempA', 'TempB', 'TempC')
        self.assertTrue(result)

    def test_case_6(self):
        df = pd.read_csv(self.csv_path)
        df = df.rename(columns={'A': 'Data1', 'B': 'Data2', 'C': 'Data3'})
        df['Data2'] = 80
        df['Data3'] = 900
        df['Data1'] = [5*x**5 for x in range(len(df['Data1']))]
        result = f_725(df, 'Data1', 'Data2', 'Data3')
        self.assertFalse(result)


if __name__ == '__main__':
    run_tests()
