import os
import pandas as pd


def f_506(filename: str) -> pd.DataFrame:
    """
    Read a CSV file into a Pandas DataFrame and then delete the entire contents of the original file.

    Parameters:
    - filename (str): The name of the CSV file to read and erase.

    Returns:
    - DataFrame: The contents of the CSV file as a pandas DataFrame.

    Requirements:
    - os
    - pandas

    Example:
    >>> df = f_506('data.csv')
    DataFrame with the contents of 'data.csv', which is now erased.
    """
    if os.stat(filename).st_size == 0:
        # File is empty, return an empty DataFrame with no columns.
        return pd.DataFrame()

    df = pd.read_csv(filename)

    # Erase the original file's content
    open(filename, 'w').close()

    return df

import unittest
import tempfile
import shutil

class TestF506(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current_dir = os.path.dirname(os.path.abspath(__file__))
        cls.test_data_dir = os.path.join(cls.current_dir, 'test_data')
        if not os.path.exists(cls.test_data_dir):
            os.makedirs(cls.test_data_dir)

        cls.test_file = os.path.join(cls.test_data_dir, 'test.csv')
        with open(cls.test_file, 'w') as f:
            f.write("col1,col2\n1,2\n3,4")

        # Debugging: Verify file content immediately after writing
        with open(cls.test_file, 'r') as f:
            content = f.read()
        print(f"Debug: Content written to {cls.test_file}: {content}")

    @classmethod
    def tearDownClass(cls):
        # Clean up by removing the test file and the test_data directory
        shutil.rmtree(cls.test_data_dir, ignore_errors=True)

    def test_file_not_found(self):
        """Test the function with a filename that does not exist."""
        with self.assertRaises(FileNotFoundError):
            f_506('nonexistent.csv')

    def test_file_removal(self):
        """Ensure the function does not remove the file, only erases contents."""
        f_506(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_empty_csv(self):
        """Test reading an empty CSV file."""
        open(self.test_file, 'w').close()  # Ensure the file is empty
        df = f_506(self.test_file)
        self.assertTrue(df.empty, "DataFrame should be empty for an empty CSV file.")
        self.assertEqual(os.path.getsize(self.test_file), 0, "The file should still be erased.")

    def test_file_is_erased_after_reading(self):
        """Ensure the CSV file is erased after its content is read into a DataFrame."""
        _ = f_506(self.test_file)
        # Check that the file exists but its content is erased
        self.assertTrue(os.path.exists(self.test_file), "The file should still exist.")
        self.assertEqual(os.path.getsize(self.test_file), 0, "The file's content should be erased.")

    def test_handling_non_existent_file(self):
        """Test the function's response to being given a non-existent file path."""
        non_existent_file = os.path.join(self.test_data_dir, 'non_existent.csv')
        with self.assertRaises(FileNotFoundError, msg="Expected FileNotFoundError for non-existent file."):
            _ = f_506(non_existent_file)


if __name__ == '__main__':
    unittest.main()
