import pandas as pd
from random import uniform


# Constants
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def f_250(n_data_points=N_DATA_POINTS):
    '''
    Generate a random set of floating-point numbers, truncate each value to 3 decimal places, and return them in a DataFrame.
    The number of data points to generate can be specified. If zero, returns an empty DataFrame.

    Parameters:
    n_data_points (int): Number of data points to generate. Default is 10000.

    Returns:
    DataFrame: A pandas DataFrame containing one column 'Value' with the generated data. Empty if n_data_points is 0.

    Note:
    - This function use 'Value' for the column name in returned DataFrame 

    Requirements:
    - pandas
    - random

    Example:
    >>> data = f_250()
    >>> print(data.head())
    Value
    0  1.234
    1  2.345
    2  3.456
    3  4.567
    4  5.678
    '''
    if n_data_points == 0:
        return pd.DataFrame(columns=['Value'])
    
    data = [round(uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    return data_df

import unittest
class TestCases(unittest.TestCase):
    def test_return_type(self):
        result = f_250()
        self.assertIsInstance(result, pd.DataFrame)
    def test_data_points_count(self):
        result = f_250()
        self.assertEqual(len(result), 10000)
    def test_value_range(self):
        result = f_250()
        within_range = result['Value'].apply(lambda x: 0.0 <= x <= 10.0)
        self.assertTrue(within_range.all())
    def test_value_truncation(self):
        result = f_250()
        correctly_truncated = result['Value'].apply(lambda x: len(str(x).split('.')[1]) <= 3 if '.' in str(x) else True)
        self.assertTrue(correctly_truncated.all())
    def test_empty_data_frame(self):
        result = f_250(n_data_points=0)
        self.assertTrue(result.empty)
