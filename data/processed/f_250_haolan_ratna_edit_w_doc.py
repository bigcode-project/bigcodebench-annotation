import pandas as pd
import random


# Constants
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def f_668(n_data_points=N_DATA_POINTS):
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
    >>> random.seed(0)
    >>> data = f_668(20)
    >>> print(data.shape)
    (20, 1)
    >>> MIN_VALUE <= data.iloc[0]['Value'] <= MAX_VALUE
    True
    '''
    if n_data_points == 0:
        return pd.DataFrame(columns=['Value'])
    
    data = [round(random.uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    return data_df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_return_type(self):
        random.seed(0)
        result = f_668()
        self.assertIsInstance(result, pd.DataFrame)
    def test_data_points_count(self):
        random.seed(0)
        result = f_668()
        self.assertEqual(len(result), 10000)
    def test_value_range(self):
        random.seed(0)
        result = f_668()
        within_range = result['Value'].apply(lambda x: 0.0 <= x <= 10.0)
        self.assertTrue(within_range.all())
    def test_value_truncation(self):
        random.seed(0)
        result = f_668()
        correctly_truncated = result['Value'].apply(lambda x: len(str(x).split('.')[1]) <= 3 if '.' in str(x) else True)
        self.assertTrue(correctly_truncated.all())
    def test_empty_data_frame(self):
        random.seed(0)
        result = f_668(n_data_points=0)
        self.assertTrue(result.empty)
