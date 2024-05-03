import pandas as pd
import os
output_dir = './output'


def f_554(df, filename):
    """
    Save a Pandas DataFrame to a JSON file in a specified directory.
    
    Parameters:
    df (DataFrame): A Pandas DataFrame to be saved.
    filename (str): The filename of the JSON file where the DataFrame will be saved.
    
    Returns:
    str: The full file path where the DataFrame is saved.
    
    Requirements:
    - os
    - pandas

    Note:
    - The function manipulates a Pandas DataFrame and saves it as a JSON file.

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    >>> 'data.json' in f_554(df, 'data.json')
    True
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, filename)
    df_clean = df.where(pd.notnull(df), None)
    with open(file_path, 'w') as f:
        df_clean.to_json(f, orient='records')
    return file_path

import unittest
import json
import shutil
class TestCases(unittest.TestCase):
    @classmethod
    def setUp(self):
        """Set up testing environment; ensure data directory exists."""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    def tearDown(self):
        """Clean up; remove the data directory and its contents after tests."""
        shutil.rmtree(output_dir, ignore_errors=True)
    def test_basic_dataframe(self):
        """Test saving a simple DataFrame."""
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        filepath = f_554(df, 'basic.json')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{"A": 1, "B": 3}, {"A": 2, "B": 4}])
    def test_nan_values(self):
        """Test DataFrame with NaN values."""
        df = pd.DataFrame({'A': [1, None], 'B': [None, 4]})
        filepath = f_554(df, 'nan_values.json')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{"A": 1, "B": None}, {"A": None, "B": 4}])
    def test_integer_conversion(self):
        """Test converting float to int where applicable."""
        df = pd.DataFrame({'A': [1.0, 2.5], 'B': [3.0, 4.5]})
        filepath = f_554(df, 'int_conversion.json')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{"A": 1, "B": 3.0}, {"A": 2.5, "B": 4.5}])
    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        df = pd.DataFrame()
        filepath = f_554(df, 'empty.json')
        self.assertTrue(os.path.isfile(filepath))
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [])
    def test_all_nan_dataframe(self):
        """Test DataFrame with all NaN values."""
        df = pd.DataFrame({'A': [None, None], 'B': [None, None]})
        filepath = f_554(df, 'all_nan.json')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{"A": None, "B": None}, {"A": None, "B": None}])
