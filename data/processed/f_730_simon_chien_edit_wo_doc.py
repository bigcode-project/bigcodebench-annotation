import pandas as pd
import os


def f_752(data_dir: str, csv_files: list) -> pd.DataFrame:
    """
    Merge / Concatenate multiple CSV files from a specified directory into a single Pandas DataFrame.

    If an empty list of files is passed, an empty DataFrame is returned.
    
    Parameters:
    data_dir (str): The directory path where the CSV files are located.
    csv_files (list): A list of CSV file names to be merged.
    
    Returns:
    pd.DataFrame: A pandas DataFrame with the merged data.
    
    Requirements:
    - pandas
    - os
    
    Example:
    >>> df = f_752('/path/to/data/directory', ['file1.csv', 'file2.csv', 'file3.csv'])
    >>> print(df.head())
            Name  Age  Gender
    0    Simon   5     Male
    1    Bobby   32    Male
    0    Elena   13  Female
    1      Tom   23    Male
    0   Franko   12    Male
    """
    merged_df = pd.DataFrame()
    for file in csv_files:
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)
        merged_df = pd.concat([merged_df, df], ignore_index=True)
    return merged_df

import unittest
import pandas as pd
import os
import shutil
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to hold CSV files
        self.test_dir = tempfile.mkdtemp()
        self.files = {
            'file1.csv': pd.DataFrame({
                'Name': ['Alice', 'Bob'],
                'Age': [25, 30]
            }),
            'file2.csv': pd.DataFrame({
                'Name': ['Charlie'],
                'Age': [35]
            }),
            'file3.csv': pd.DataFrame({
                'Name': ['David', 'Eve'],
                'Age': [45, 55],
                'Gender': ['Male', 'Female']
            }),
            'file4.csv': pd.DataFrame({
                'Name': ['Faythe'],
                'Animal': ['Cat']
            })
        }
        # Write files to disk
        for filename, df in self.files.items():
            df.to_csv(os.path.join(self.test_dir, filename), index=False)
    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)
    def test_with_multiple_files(self):
        # Test merging multiple files
        result = f_752(self.test_dir, ['file1.csv', 'file2.csv'])
        expected_df = pd.concat([self.files['file1.csv'], self.files['file2.csv']],
                                ignore_index=True)
        pd.testing.assert_frame_equal(result, expected_df)
    def test_with_different_columns(self):
        # Test files with different columns
        result = f_752(self.test_dir, ['file1.csv', 'file3.csv', 'file4.csv'])
        expected_df = pd.concat([self.files['file1.csv'], self.files['file3.csv'], self.files['file4.csv']],
                                ignore_index=True)
        pd.testing.assert_frame_equal(result, expected_df)
    def test_with_empty_list(self):
        # Test with an empty list of files
        result = f_752(self.test_dir, [])
        self.assertTrue(result.empty)
    def test_with_nonexistent_file(self):
        # Test referencing a non-existent file
        with self.assertRaises(FileNotFoundError):
            f_752(self.test_dir, ['nonexistent.csv'])
    def test_single_file(self):
        # Test with a single file
        result = f_752(self.test_dir, ['file2.csv'])
        expected_df = self.files['file2.csv']
        pd.testing.assert_frame_equal(result, expected_df)
