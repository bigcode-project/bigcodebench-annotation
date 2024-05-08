import pandas as pd
from random import uniform


def f_176(n_data_points=1000, min_value=0.0, max_value=10.0, column_name='Value'):
    """
    Generate a random dataset of floating-point numbers, truncate each value to 3 decimal places, then return the generated DataFrame with
    the specified column name.

    Parameters:
    n_data_points (int, optional): The number of data points to generate. Default is 1000.
    min_value (float, optional): The minimum value for the generated data. Default is 0.0.
    max_value (float, optional): The maximum value for the generated data. Default is 10.0.
    column_name (str, optional): The column name in generated DataFrame. Default is 'Value'.


    Returns:
    DataFrame: A pandas DataFrame with the generated data.
    
    Requirements:
    - pandas
    - random.uniform

    Example:
    >>> random.seed(0)
    >>> data = f_176()
    >>> data.shape[0]
    1000
    """
    data = [round(uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=[column_name])
    return data_df

import unittest
import random
class TestCases(unittest.TestCase):
    def test_dataframe_type(self):
        """Test if the returned object is a pandas DataFrame."""
        random.seed(0)
        result = f_176()
        self.assertIsInstance(result, pd.DataFrame, "Returned object is not a pandas DataFrame")
    def test_dataframe_size(self):
        """Test if the DataFrame contains the correct number of data points."""
        random.seed(0)
        result = f_176()
        self.assertEqual(len(result), 1000, "DataFrame does not contain 1000 data points")
    def test_value_range(self):
        """Test if values are within the specified range."""
        random.seed(0)
        result = f_176(100)
        for value in result['Value']:
            self.assertGreaterEqual(value, 0.0, "Value is less than 0.0")
            self.assertLessEqual(value, 10.0, "Value is greater than 10.0")
    def test_decimal_precision(self):
        """Test if values have up to 3 decimal places."""
        random.seed(0)
        result = f_176(10, 5.0, 8.0)
        for value in result['Value']:
            self.assertLessEqual(len(str(value).split('.')[1]), 3, "Value does not have up to 3 decimal places")
    def test_dataframe_columns(self):
        """Test if the DataFrame has the correct column name."""
        random.seed(0)
        column_name = 'User'
        result = f_176(10, 5.0, 8.0, column_name)
        self.assertIn(column_name, result.columns, "DataFrame does not have a column named "+column_name)
