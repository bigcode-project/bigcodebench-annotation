import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Updated function to handle empty input list
def f_765(d):
    """
    Scale all values with the keys "x," "y" and "z" from a list of dictionaries "d" with MinMaxScaler.

    Parameters:
    d (list): A list of dictionaries.

    Returns:
    DataFrame: A pandas DataFrame with scaled values.

    Requirements:
    - pandas
    - sklearn.preprocessing.MinMaxScaler

    Examples:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
    >>> print(f_765(data))
         x         y    z
    0  0.0  0.642857  0.0
    1  1.0  1.000000  0.5
    2  0.5  0.000000  1.0

    >>> data = [{'x': -1, 'y': 0, 'z': 5}, {'x': 3, 'y': -15, 'z': 0}, {'x': 0, 'y': 1, 'z': -7}]
    >>> print(f_765(data))
          x       y         z
    0  0.00  0.9375  1.000000
    1  1.00  0.0000  0.583333
    2  0.25  1.0000  0.000000
    """
    if not d:  # Check if the input list is empty
        return pd.DataFrame(columns=['x', 'y', 'z'])  # Return an empty DataFrame with specified columns
    df = pd.DataFrame(d)
    scaler = MinMaxScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(df[['x', 'y', 'z']]), columns=['x', 'y', 'z'])
    return scaled_df

import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        result = f_765(data)
        expected_df = pd.DataFrame({'x': [0.0, 1.0, 0.5], 'y': [0.642857, 1.0, 0.0], 'z': [0.0, 0.5, 1.0]})
        pd.testing.assert_frame_equal(result, expected_df)
    
    def test_case_2(self):
        data = [{'x': -1, 'y': 0, 'z': 5}, {'x': 3, 'y': -15, 'z': 0}, {'x': 0, 'y': 1, 'z': -7}]
        result = f_765(data)
        expected_df = pd.DataFrame({'x': [0.0, 1.0, 0.25], 'y': [0.9375, 0.0, 1.0], 'z': [1.0, 0.583333, 0.0]})
        pd.testing.assert_frame_equal(result, expected_df)
        
    def test_case_3(self):
        data = []
        result = f_765(data)
        expected_df = pd.DataFrame(columns=['x', 'y', 'z'])
        pd.testing.assert_frame_equal(result, expected_df)
    
    def test_case_4(self):
        data = [{'x': 1}, {'y': 2}, {'z': 3}]
        result = f_765(data)
        expected_df = pd.DataFrame({'x': [0.0, None, None], 'y': [None, 0.0, None], 'z': [None, None, 0.0]})
        pd.testing.assert_frame_equal(result, expected_df)
       
    def test_case_5(self):
        data = [{'x': 1, 'y': 2}, {'x': 3, 'z': 4}]
        result = f_765(data)
        expected_df = pd.DataFrame({'x': [0.0, 1.0], 'y': [0.0, None], 'z': [None, 0.0]})
        pd.testing.assert_frame_equal(result, expected_df)
