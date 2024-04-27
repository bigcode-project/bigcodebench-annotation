import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def f_675(file_name: str) -> pd.DataFrame:
    """Normalize data in a csv file using MinMaxScaler from sklearn.
    Only numeric columns are normalized. Columns with other dtypes are left as
    they are.
    
    Parameters:
    file_name (str): The name of the csv file.
    
    Returns:
    DataFrame: A pandas DataFrame with normalized data.

    Raises:
    ValueError: If input does not have numeric columns.

    Requirements:
    - pandas
    - sklearn.preprocessing.MinMaxScaler
    
    Example:
    >>> normalized_data = f_675("sample.csv")
    >>> print(normalized_data.head())
    Name	Age	Salary
    0	Alex Anderson	0.304651	0.122298
    1	Mr. Leslie Casey	0.28140	0.598905
    2	Anthony George	0.996744	0.216552
    3	Brian Washington	0.126279	0.459948
    4	Elias Lawrence	0.337239	0.124185
    """
    df = pd.read_csv(file_name)
    if df.select_dtypes(include='number').empty:
        raise ValueError("Input must at least have one numeric column.")

    scaler = MinMaxScaler()
    numeric_columns = df.select_dtypes(include='number').columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    return df

import unittest
import pandas as pd
import tempfile
import os
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Clean up by removing the directory
        shutil.rmtree(self.test_dir)
    def create_csv(self, filename, data):
        # Helper function to create a CSV file with the given data
        full_path = os.path.join(self.test_dir, filename)
        data.to_csv(full_path, index=False)
        return full_path
    def test_non_numeric_and_empty(self):
        # Test with non-numeric and empty data
        non_numeric_df = pd.DataFrame({
            "Name": ["Alice", "Bob"],
            "City": ["New York", "Los Angeles"]
        })
        empty_df = pd.DataFrame()
        non_numeric_path = self.create_csv("non_numeric.csv", non_numeric_df)
        empty_path = self.create_csv("empty.csv", empty_df)
        self.assertRaises(ValueError, f_675, non_numeric_path)
        self.assertRaises(ValueError, f_675, empty_path)
    def test_single_row(self):
        # Test with a single row of numeric data
        single_row_df = pd.DataFrame({
            "Name": ["Olivia Anderson"],
            "Age": [35],
            "Salary": [58000]
        })
        csv_path = self.create_csv("single_row.csv", single_row_df)
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] == 0).all() and (df['Salary'] == 0).all())
    def test_multiple_rows(self):
        # Test multiple rows with numeric data
        data_df = pd.DataFrame({
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [25, 35, 45],
            "Salary": [50000, 60000, 70000]
        })
        csv_path = self.create_csv("multiple_rows.csv", data_df)
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())
    def test_mixed_columns(self):
        # Test with a mix of numeric and non-numeric columns
        mixed_df = pd.DataFrame({
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [25, 35, 45],
            "Salary": [50000, 60000, 70000],
            "City": ["New York", "Chicago", "San Francisco"]
        })
        csv_path = self.create_csv("mixed_columns.csv", mixed_df)
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())
        self.assertTrue('City' in df.columns and df['City'].equals(mixed_df['City']))
    def test_large_dataset(self):
        # Test with a large dataset to ensure scalability
        large_df = pd.DataFrame({
            "Age": range(10000),  # Large range of ages
            "Salary": range(10000, 20000)  # Large range of salaries
        })
        csv_path = self.create_csv("large_dataset.csv", large_df)
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())
