import os
import pandas as pd


def f_402(filename: str) -> pd.DataFrame:
    """
    Read a CSV file into a Pandas DataFrame and then delete the entire contents of the original file.

    Parameters:
    - filename (str): The name of the CSV file to read and erase.

    Returns:
    - DataFrame: The contents of the CSV file as a pandas DataFrame.

    Raises:
    - FileNotFoundError: If the CSV file does not exist.

    Requirements:
    - os
    - pandas

    Example:
    >>> import os
    >>> from unittest.mock import patch
    >>> with patch('os.path.exists', return_value=False):
    ...     f_402('nonexistent.csv')
    Traceback (most recent call last):
        ...
    FileNotFoundError: No such file: 'nonexistent.csv'
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"No such file: '{filename}'")
    if os.stat(filename).st_size == 0:
        return pd.DataFrame()
    df = pd.read_csv(filename)
    with open(filename, 'w') as file:
        file.truncate()
    return df

import unittest
import shutil
OUTPUT_DIR = r'./output'
class TestCases(unittest.TestCase):
    def setUp(self):
        self.output_dir = OUTPUT_DIR
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.test_file = os.path.join(self.output_dir, 'test.csv')
        with open(self.test_file, 'w') as f:
            f.write("col1,col2\n1,2\n3,4")
        # Debugging: Verify file content immediately after writing
        with open(self.test_file, 'r') as f:
            content = f.read()
        print(f"Debug: Content written to {self.test_file}: {content}")
    def tearDown(self):
        # Clean up by removing the test file and the test_data directory
        shutil.rmtree(self.output_dir, ignore_errors=True)
    def test_file_not_found(self):
        """Test the function with a filename that does not exist."""
        with self.assertRaises(FileNotFoundError):
            f_402('nonexistent.csv')
    def test_file_removal(self):
        """Ensure the function does not remove the file, only erases contents."""
        f_402(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))
    def test_empty_csv(self):
        """Test reading an empty CSV file."""
        open(self.test_file, 'w').close()  # Ensure the file is empty
        df = f_402(self.test_file)
        self.assertTrue(df.empty, "DataFrame should be empty for an empty CSV file.")
        self.assertEqual(os.path.getsize(self.test_file), 0, "The file should still be erased.")
    def test_file_is_erased_after_reading(self):
        """Ensure the CSV file is erased after its content is read into a DataFrame."""
        _ = f_402(self.test_file)
        # Check that the file exists but its content is erased
        self.assertTrue(os.path.exists(self.test_file), "The file should still exist.")
        self.assertEqual(os.path.getsize(self.test_file), 0, "The file's content should be erased.")
    def test_handling_non_existent_file(self):
        """Test the function's response to being given a non-existent file path."""
        non_existent_file = os.path.join(self.output_dir, 'non_existent.csv')
        with self.assertRaises(FileNotFoundError, msg="Expected FileNotFoundError for non-existent file."):
            _ = f_402(non_existent_file)
