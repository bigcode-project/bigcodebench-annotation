import pandas as pd
import numpy as np


def f_106(data, key, min_value, max_value):
    '''
    Add a new column with random values to the "data" DataFrame.

    Parameters:
    data (DataFrame): The input data as a pandas DataFrame.
    key (str): The name of the new column to be added.
    min_value (int): The minimum value for randomly generated integers in the new column.
    max_value (int): The maximum value for randomly generated integers in the new column.

    Returns:
    DataFrame: Updated DataFrame with the new column added.

    Raises:
    - The function will raise an error if the input data is not pandas DataFrame
    
    Requirements:
    - numpy
    - pandas
    
    Example:
    >>> np.random.seed(0)
    >>> data = pd.DataFrame({'key1': ['value1', 'value2', 'value3'], 'key2': [1, 2, 3]})
    >>> updated_data = f_106(data, 'new_key', 0, 10)
    >>> print(updated_data)
         key1  key2  new_key
    0  value1     1        5
    1  value2     2        0
    2  value3     3        3
    '''
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input 'data' must be a pandas DataFrame.")
    
    random_generated = np.random.randint(min_value, max_value + 1, size=len(data))
    data[key] = random_generated
    return data

import unittest
import numpy as np
import pandas as pd
# Blackbox test cases
class TestCases(unittest.TestCase):
    def test_empty_data(self):
        np.random.seed(0)
        data = pd.DataFrame()
        key = 'new_column'
        min_value = 0
        max_value = 10
        updated_data = f_106(data, key, min_value, max_value)
        self.assertIsInstance(updated_data, pd.DataFrame)
        self.assertTrue(key in updated_data.columns)
        self.assertEqual(len(updated_data), 0)
    
    def test_non_empty_data(self):
        np.random.seed(0)
        data = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        key = 'random_values'
        min_value = 0
        max_value = 10
        updated_data = f_106(data, key, min_value, max_value)
        self.assertIsInstance(updated_data, pd.DataFrame)
        self.assertTrue(key in updated_data.columns)
        self.assertEqual(len(updated_data), 3)  # Assu the length of the input data is 3
        self.assertTrue(all(min_value <= val <= max_value for val in updated_data[key]))
        
    def test_negative_values(self):
        np.random.seed(0)
        data = pd.DataFrame({'X': ['x1', 'x2'], 'Y': ['y1', 'y2']})
        key = 'random'
        min_value = -10
        max_value = -5
        updated_data = f_106(data, key, min_value, max_value)
        self.assertIsInstance(updated_data, pd.DataFrame)
        self.assertTrue(key in updated_data.columns)
        self.assertEqual(len(updated_data), 2)
        self.assertTrue(all(min_value <= val <= max_value for val in updated_data[key]))
        
    def test_single_row_data(self):
        np.random.seed(0)
        data = pd.DataFrame({'A': [5], 'B': ['abc']})
        key = 'new_col'
        min_value = 0
        max_value = 10
        updated_data = f_106(data, key, min_value, max_value)
        self.assertIsInstance(updated_data, pd.DataFrame)
        self.assertTrue(key in updated_data.columns)
        self.assertEqual(len(updated_data), 1)
        self.assertTrue(all(min_value <= val <= max_value for val in updated_data[key]))
        
    def test_large_data(self):
        np.random.seed(0)
        data = pd.DataFrame({'X': ['x' + str(i) for i in range(1000)], 'Y': ['y' + str(i) for i in range(1000)]})
        key = 'random_numbers'
        min_value = 1
        max_value = 100
        updated_data = f_106(data, key, min_value, max_value)
        self.assertIsInstance(updated_data, pd.DataFrame)
        self.assertTrue(key in updated_data.columns)
        self.assertEqual(len(updated_data), 1000)
        self.assertTrue(all(min_value <= val <= max_value for val in updated_data[key]))
    def test_non_dataframe_input(self):
        np.random.seed(0)
        with self.assertRaises(ValueError):
            data = {'key1': ['value1', 'value2', 'value3'], 'key2': [1, 2, 3]}
            f_106(data, 'new_key', 0, 10)
