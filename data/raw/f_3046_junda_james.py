import pandas as pd
import os

def f_3046(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    """
    Copies data from an Excel spreadsheet into a new Excel file, then reads the new Excel file and returns its contents.

    Parameters:
    - original_file_location (str): Path to the original Excel file. Defaults to 'test.xlsx'.
    - new_file_location (str): Path to save the new Excel file. Defaults to 'new_test.xlsx'.
    - sheet_name (str): Name of the sheet to load data from. Defaults to 'Sheet1'.

    Returns:
    - DataFrame: A pandas DataFrame representing the content of the new Excel file.

    Raises:
    - FileNotFoundError: If the original Excel file does not exist at the specified path.
    - ValueError: If the specified sheet does not exist in the workbook.

    Requirements:
    - pandas
    - os

    Example:
    >>> file_path, file_new_path, sheet_name = 'test.xlsx', 'new_test.xlsx', 'Sheet1'
    >>> create_dummy_excel(file_path, sheet_name)
    >>> df = f_3046(file_path, file_new_path, sheet_name)
    >>> os.remove(file_path)
    >>> os.remove(file_new_path)
    """
    if not os.path.exists(original_file_location):
        raise FileNotFoundError(f"No file found at {original_file_location}")

    # Read data from the original Excel file
    try:
        original_df = pd.read_excel(original_file_location, sheet_name=sheet_name)
    except ValueError as e:
        raise ValueError(f"Error reading sheet: {e}")

    # Write data to a new Excel file
    original_df.to_excel(new_file_location, index=False)

    # Read and return data from the new Excel file
    new_df = pd.read_excel(new_file_location)
    return new_df

import unittest
import os
import pandas as pd

def create_dummy_excel(file_path='test.xlsx', sheet_name='Sheet1'):
    """
    Creates a dummy Excel file for testing with a specified sheet name and sample data.
    """
    df = pd.DataFrame({'A': [10, 30], 'B': [20, 40]})
    df.to_excel(file_path, index=False, sheet_name=sheet_name)

class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_dummy_excel()

    @classmethod
    def tearDownClass(cls):
        os.remove('test.xlsx')
        if os.path.exists('new_test.xlsx'):
            os.remove('new_test.xlsx')

    def test_normal_functionality(self):
        df = f_3046('test.xlsx', 'new_test.xlsx', 'Sheet1')
        
        expect = pd.DataFrame({'A': [10, 30], 'B': [20, 40]})
        self.assertIsInstance(df, pd.DataFrame)
        pd.testing.assert_frame_equal(expect, df)

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            f_3046('non_existent.xlsx', 'new_test.xlsx', 'Sheet1')

    def test_invalid_sheet_name(self):
        with self.assertRaises(ValueError):
            f_3046('test.xlsx', 'new_test.xlsx', 'NonExistentSheet')

    def test_data_integrity(self):
        df = f_3046('test.xlsx', 'new_test.xlsx', 'Sheet1')
        expected_df = pd.DataFrame({'A': [10, 30], 'B': [20, 40]})
        pd.testing.assert_frame_equal(df, expected_df)

    def test_column_names_preserved(self):
        df = f_3046('test.xlsx', 'new_test.xlsx', 'Sheet1')
        self.assertListEqual(list(df.columns), ['A', 'B'])

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()