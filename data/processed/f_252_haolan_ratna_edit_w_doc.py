import pandas as pd
import random
from sklearn.preprocessing import StandardScaler

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def f_313(n_data_points=5000, min_value=0.0, max_value=10.0):
    """
    Generate a random dataset of floating point numbers, truncate each value to 3 decimal places and normalize the data using standard scaling (mean = 0, std = 1).
    
    Parameters:
    n_data_points (int): Number of data points to generate. Default is 5000.
    min_value (float): Minimum value range for data points. Default is 0.0.
    max_value (float): Maximum value range for data points. Default is 10.0.
    
    Returns:
    DataFrame: A pandas DataFrame with the normalized data.
    
    Raises:
    If max_value is less than min_value, a ValueError is raised.
    
    Note:
    - The function use "Normalized Value" for the column name in the DataFrame that being returned.

    Requirements:
    - pandas
    - random
    - sklearn.preprocessing.StandardScaler

    Example:
    >>> random.seed(0)
    >>> normalized_data = f_313(5000, 5, 5)
    >>> print(normalized_data['Normalized Value'][0])
    0.0
    """
    if max_value < min_value:
        raise ValueError()
    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data_df[['Value']])
    return pd.DataFrame(normalized_data, columns=['Normalized Value'])

import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        random.seed(0)
        df = f_313()
        self.assertIsInstance(df, pd.DataFrame, "Return type should be a DataFrame.")
        self.assertEqual(len(df), 5000, "Default number of data points should be 5000.")
        self.assertAlmostEqual(df['Normalized Value'].mean(), 0, delta=0.1, msg="Mean should be close to 0.")
        self.assertAlmostEqual(df['Normalized Value'].std(), 1, delta=0.1, msg="Standard deviation should be close to 1.")
    def test_custom_parameters(self):
        random.seed(0)
        df = f_313(1000, 1.0, 5.0)
        self.assertEqual(len(df), 1000, "Number of data points should match the specified value.")
        self.assertTrue(df['Normalized Value'].min() >= -3, "Normalized values should be within a reasonable range.")
        self.assertTrue(df['Normalized Value'].max() <= 3, "Normalized values should be within a reasonable range.")
    def test_edge_case_empty(self):
        random.seed(0)
        with self.assertRaises(ValueError):
            f_313(0)
    def test_negative_data_points(self):
        random.seed(0)
        with self.assertRaises(ValueError):
            f_313(-100)
    def test_invalid_range(self):
        random.seed(0)
        with self.assertRaises(ValueError):
            f_313(1000, 5.0, 1.0)
