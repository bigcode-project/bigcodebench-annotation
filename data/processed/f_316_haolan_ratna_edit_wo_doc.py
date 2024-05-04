import collections
import pandas as pd

def f_641(my_tuple, path_csv_files):
    """
    Count the occurrences of each value in the specified columns in multiple CSV files.

    Parameters:
    my_tuple (tuple): The tuple of column names.
    path_csv_files (list of string): The list of csv files to read.

    Returns:
    dict: A dictionary where keys are column names and values are dictionaries 
        with unique values in the column as keys and their counts as values.

    Requirements:
    - collections
    - pandas

    Example:
    >>> from unittest.mock import MagicMock
    >>> import pandas as pd
    >>> df1 = pd.DataFrame({'Country': ['USA', 'Canada', 'USA'], 'Gender': ['Male', 'Female', 'Male']})
    >>> df2 = pd.DataFrame({'Country': ['UK', 'USA', 'Germany'], 'Gender': ['Male', 'Male', 'Female']})
    >>> pd.read_csv = MagicMock(side_effect=[df1, df2])
    >>> result = f_641(('Country', 'Gender'), ['file1.csv', 'file2.csv'])
    >>> print(result['Country'])
    Counter({'USA': 3, 'Canada': 1, 'UK': 1, 'Germany': 1})
    """
    counter = {column: collections.Counter() for column in my_tuple}
    for csv_file in path_csv_files:
        df = pd.read_csv(csv_file)
        for column in my_tuple:
            if column in df:
                counter[column].update(df[column])
    return counter

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
class TestCases(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_read_csv_files(self, mock_read_csv):
        # Mocking pandas.read_csv to return a DataFrame
        mock_read_csv.side_effect = lambda x: pd.DataFrame({'Country': ['USA', 'Canada', 'USA'], 'Gender': ['Male', 'Female', 'Male']})
        # Call the function with mocked data
        result = f_641(('Country', 'Gender'), ['file1.csv'])
        # Assertions to verify the function behavior
        self.assertEqual(result['Country'], {'USA': 2, 'Canada': 1})
        self.assertEqual(result['Gender'], {'Male': 2, 'Female': 1})
   
    @patch('pandas.read_csv')
    def test_empty_csv_files(self, mock_read_csv):
        # Mocking pandas.read_csv to return an empty DataFrame
        mock_read_csv.side_effect = lambda x: pd.DataFrame(columns=['Country', 'Gender'])
        # Call the function with mocked data
        result = f_641(('Country', 'Gender'), ['file1.csv'])
        # Assertions to verify the function behavior
        self.assertEqual(result['Country'], {})
        self.assertEqual(result['Gender'], {})
    @patch('pandas.read_csv')
    def test_missing_column(self, mock_read_csv):
        # Mocking pandas.read_csv to return a DataFrame with missing 'Gender' column
        mock_read_csv.side_effect = lambda x: pd.DataFrame({'Country': ['USA', 'Canada', 'USA']})
        # Call the function with mocked data
        result = f_641(('Country', 'Gender'), ['file1.csv', 'file2.csv'])
        # Assertions to verify the function behavior
        self.assertEqual(result['Country'], {'USA': 4, 'Canada': 2})
        self.assertEqual(result['Gender'], {})
    @patch('pandas.read_csv')
    def test_no_csv_files(self, mock_read_csv):
        # Call the function with mocked data
        result = f_641(('Country', 'Gender'), [])
        # Assertions to verify the function behavior
        self.assertEqual(result['Country'], {})
        self.assertEqual(result['Gender'], {})
    @patch('pandas.read_csv')
    def test_invalid_csv_files(self, mock_read_csv):
        # Mocking pandas.read_csv to raise an exception when reading the CSV files
        mock_read_csv.side_effect = Exception
        # Call the function with mocked data
        with self.assertRaises(Exception):
            result = f_641(('Country', 'Gender'), ['file3.csv'])
