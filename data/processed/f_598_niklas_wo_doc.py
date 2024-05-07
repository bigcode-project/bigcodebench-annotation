import json
import numpy as np

def f_504(df):
    """
    Given a DataFrame with random values and an 'IntCol' column, transform the 'IntCol' column by a logarithm (base 10) and write it to a `IntCol.json` file as a list. Also return the DataFrame.

    Parameters:
    - df (DataFrame): A pandas DataFrame with a 'IntCol' column.

    Returns:
    - df (DataFrame): A pandas DataFrame to describe the transformed data.

    Requirements:
    - json
    - pandas
    - numpy
    - os

    Example:
    >>> df = pd.DataFrame({'IntCol': [10, 100, 1000, 10000, 100000]})
    >>> df_transformed = f_504(df)
    >>> print(df_transformed)
       IntCol
    0     1.0
    1     2.0
    2     3.0
    3     4.0
    4     5.0

    """
    df['IntCol'] = np.log10(df['IntCol'])
    int_col_list = df['IntCol'].tolist()
    with open('IntCol.json', 'w') as json_file:
        json.dump(int_col_list, json_file)
    return df

import unittest
import os
import pandas as pd
class TestCases(unittest.TestCase):
    def tearDown(self):
        if os.path.exists('IntCol.json'):
            os.remove('IntCol.json')
    
    def test_case_1(self):
        df = pd.DataFrame({'IntCol': [10, 100, 1000, 10000, 100000]})
        df_transformed = f_504(df)
        self.assertTrue(np.allclose(df_transformed['IntCol'], [1, 2, 3, 4, 5]))
        # Check if JSON file exists
        self.assertTrue(os.path.exists('IntCol.json'))
        # Check the contents of the JSON file
        with open('IntCol.json', 'r') as json_file:
            int_col_data = json.load(json_file)
        self.assertTrue(np.allclose(int_col_data, [1, 2, 3, 4, 5]))
    def test_case_2(self):
        df = pd.DataFrame({'IntCol': [10000000, 100000000, 1000000000, 10000000000, 100000000000]})
        df_transformed = f_504(df)
        self.assertTrue(np.allclose(df_transformed['IntCol'], [7, 8, 9, 10, 11]))
        # Check if JSON file exists
        self.assertTrue(os.path.exists('IntCol.json'))
        # Check the contents of the JSON file
        with open('IntCol.json', 'r') as json_file:
            int_col_data = json.load(json_file)
        self.assertTrue(np.allclose(int_col_data, [7, 8, 9, 10, 11]))
    def test_case_3(self):
        df = pd.DataFrame({'IntCol': [0, 0, 0, 0, 0]})
        df_transformed = f_504(df)
        self.assertTrue(np.allclose(df_transformed['IntCol'], [-np.inf, -np.inf, -np.inf, -np.inf, -np.inf]))
        # Check if JSON file exists
        self.assertTrue(os.path.exists('IntCol.json'))
        # Check the contents of the JSON file
        with open('IntCol.json', 'r') as json_file:
            int_col_data = json.load(json_file)
        self.assertTrue(np.allclose(int_col_data, [-np.inf, -np.inf, -np.inf, -np.inf, -np.inf]))
    def test_case_4(self):
        df = pd.DataFrame({'IntCol': [10000000]})
        df_transformed = f_504(df)
        self.assertTrue(np.allclose(df_transformed['IntCol'], [7]))
        # Check if JSON file exists
        self.assertTrue(os.path.exists('IntCol.json'))
        # Check the contents of the JSON file
        with open('IntCol.json', 'r') as json_file:
            int_col_data = json.load(json_file)
        self.assertTrue(np.allclose(int_col_data, [7]))
    def test_case_5(self):
        df = pd.DataFrame({'IntCol': [1, 10, 100, 1000, 10000, 100000]})
        df_transformed = f_504(df)
        self.assertTrue(np.allclose(df_transformed['IntCol'], [0, 1, 2, 3, 4, 5]))
        # Check if JSON file exists
        self.assertTrue(os.path.exists('IntCol.json'))
        # Check the contents of the JSON file
        with open('IntCol.json', 'r') as json_file:
            int_col_data = json.load(json_file)
        self.assertTrue(np.allclose(int_col_data, [0, 1, 2, 3, 4, 5]))
