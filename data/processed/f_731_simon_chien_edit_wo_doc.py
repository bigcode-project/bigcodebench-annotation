import os
import pandas as pd
import numpy as np


def f_726(data_dir: str, csv_file: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame and replace the NaN values in
    numeric columns with the mean of the corresponding column.
    The resulting DataFrame is returned.

    If an empty csv is passed, an empty DataFrame is returned.

    Parameters:
    - data_dir (str): The path to the directory containing the CSV file.
    - csv_file (str): The name of the CSV file to be processed.

    Returns:
    pd.DataFrame: A pandas DataFrame with the processed data.

    Raises:
    FileNotFoundError: If csv_file does not exist.

    Requirements:
    - os
    - pandas
    - numpy
    
    Example:
    >>> df = f_726("/path/to/data/directory", "file.csv")
    >>> print(df)
         Fruit     Taste     Cost
    0    Apple      Good        1
    1   Orange       NaN        2
    2  Avocado       Bad        1.667
    3  Coconut     Tasty        2
    """
    file_path = os.path.join(data_dir, csv_file)
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()
    for column in df.columns:
        if np.issubdtype(df[column].dtype, np.number):  # checking for numeric columns
            df[column].fillna(df[column].mean(), inplace=True)
    return df

import unittest
import pandas as pd
import numpy as np
import os
import tempfile
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        self.folder_path = 'f_726_data_simon'
    def setUp(self):
        # Create a temporary directory for test data
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)
    def create_csv(self, filename, data):
        # Helper method to create a CSV file
        filepath = os.path.join(self.test_dir, filename)
        data.to_csv(filepath, index=False)
        return filename
    def test_empty_csv(self):
        # Test with an empty CSV file
        filename = self.create_csv('empty.csv', pd.DataFrame())
        result = f_726(self.test_dir, filename)
        self.assertTrue(result.empty)
    def test_numeric_columns_nan_replacement(self):
        data = pd.DataFrame({
            'Age': [25, np.nan, 30],
            'Salary': [50000, 60000, np.nan]
        })
        filename = self.create_csv('data.csv', data)
        expected = pd.DataFrame({
            'Age': [25.0, 27.5, 30.0],  # Ensure all ages are floats
            'Salary': [50000.0, 60000.0, 55000.0]  # Ensure all salaries are floats
        })
        result = f_726(self.test_dir, filename)
        pd.testing.assert_frame_equal(result, expected)
    def test_mixed_columns(self):
        data = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Score': [np.nan, 88, 92]
        })
        filename = self.create_csv('mixed.csv', data)
        expected = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Score': [90.0, 88.0, 92.0]  # Ensure all scores are floats
        })
        result = f_726(self.test_dir, filename)
        pd.testing.assert_frame_equal(result, expected)
    def test_all_nan_column(self):
        # Test with a column that is entirely NaN
        data = pd.DataFrame({
            'Empty': [np.nan, np.nan, np.nan]
        })
        filename = self.create_csv('all_nan.csv', data)
        result = f_726(self.test_dir, filename)
        self.assertTrue(result['Empty'].isnull().all())
    def test_no_numeric_data(self):
        # Test a CSV file with no numeric data
        data = pd.DataFrame({
            'City': ['New York', 'Los Angeles', 'Chicago']
        })
        filename = self.create_csv('cities.csv', data)
        result = f_726(self.test_dir, filename)
        pd.testing.assert_frame_equal(result, data)
    def test_file_not_found(self):
        # Test the FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            f_726(self.test_dir, "non_existent.csv")
