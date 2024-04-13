import pandas as pd
import os

def f_730(data_dir: str, csv_files: list) -> pd.DataFrame:
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
    >>> df = f_730('/path/to/data/directory', ['file1.csv', 'file2.csv', 'file3.csv'])
    >>> print(df.head())
            Name  Age  Gender
    0    Simon   5     Male
    1    Bobby   32    Male
    0    Elena   13  Female
    1      Tom   23    Male
    0   Franko   12    Male

    >>> df = f_730('/path/to/data/directory', ['file1.csv', 'other_file.csv])
    >>> print(df.head())
            Name  Age  Gender  Animal Size
    0    Simon   5     Male      None  None
    1    Bobby   32    Male      None  None
    0    Elena   13  Female      None  None
    2     None  None   None      Tiger  12
    """
    merged_df = pd.DataFrame()

    for file in csv_files:
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)
        merged_df = pd.concat([merged_df, df])

    return merged_df

import unittest


import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = 'f_730_data_simon'
        self.csv_files = ['test_file1.csv', 'test_file2.csv', 'test_file3.csv']

    def test_case_1(self):
        # Test with all three CSV files
        df = f_730(self.test_data_dir, self.csv_files)
        
        merged_df = pd.DataFrame()

        for file in self.csv_files:
            file_path = os.path.join(self.test_data_dir, file)
            frame = pd.read_csv(file_path)
            merged_df = pd.concat([merged_df, frame])
        pd.testing.assert_frame_equal(df, merged_df)

    def test_case_2(self):
        # Test with only the first CSV file
        df = f_730(self.test_data_dir, [self.csv_files[0]])
        merged_df = pd.DataFrame()

        for file in [self.csv_files[0]]:
            file_path = os.path.join(self.test_data_dir, file)
            frame = pd.read_csv(file_path)
            merged_df = pd.concat([merged_df, frame])

        pd.testing.assert_frame_equal(df, merged_df)


    def test_case_3(self):
        # Test with the first and third CSV files
        df = f_730(self.test_data_dir, [self.csv_files[0], self.csv_files[2]])

        merged_df = pd.DataFrame()
        for file in [self.csv_files[0], self.csv_files[2]]:
            file_path = os.path.join(self.test_data_dir, file)
            frame = pd.read_csv(file_path)
            merged_df = pd.concat([merged_df, frame])

        pd.testing.assert_frame_equal(df, merged_df)

    def test_case_different_columns(self):
        diff = 'test_file4.csv'
        df = f_730(self.test_data_dir, [self.csv_files[0], diff])

        merged_df = pd.DataFrame()
        for file in [self.csv_files[0], diff]:
            file_path = os.path.join(self.test_data_dir, file)
            frame = pd.read_csv(file_path)
            merged_df = pd.concat([merged_df, frame])
       
        pd.testing.assert_frame_equal(df, merged_df)

    def test_case_4(self):
        # Test with an empty list of CSV files
        df = f_730(self.test_data_dir, [])
        self.assertEqual(len(df), 0)  # No rows should be present

    def test_case_5(self):
        # Test with non-existing CSV file
        with self.assertRaises(FileNotFoundError):
            f_730(self.test_data_dir, ["non_existing.csv"])


if __name__ == "__main__":
    run_tests()