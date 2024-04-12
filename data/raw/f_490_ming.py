import pandas as pd
import os
import unittest
import shutil
import os


# Set the directory for data relative to the current file's location
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, 'data')

def ensure_dir_exists(path):
    """
    Ensure the specified directory exists; if not, create it.

    Parameters:
    - path (str): The path of the directory to check and possibly create.

    Returns:
    None: Creates the directory if it does not exist, otherwise does nothing.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def f_490(dataset, filename):
    """
    Writes multiple Pandas DataFrames to a single CSV file, separating each DataFrame by a line of hyphens ("------").

    Parameters:
    - dataset (list of pd.DataFrame): A list containing the DataFrames to be written to the file.
    - filename (str): The name of the file (excluding the path) where the DataFrames will be written.

    Returns:
    None: The function writes the DataFrames to a CSV file but does not return any value.

    Requirements:
    - pandas: For handling DataFrames and writing to CSV files.
    - os: For checking and creating directories.

    Example:
    >>> df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    >>> df2 = pd.DataFrame({"D": [5, 6], "E": [7, 8]})
    >>> f_490([df1, df2], 'sample.csv')
    This will write df1 and df2 to 'sample.csv' in the './data' directory, separating them with a line of hyphens.
    """
    ensure_dir_exists(DATA_DIR)  # Ensure the data directory exists
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w', newline='') as f:
        for i, df in enumerate(dataset):
            if i > 0:
                # Write the separator with a newline at the end only
                f.write('------\n')
            # Avoid writing the index and ensure no extra newline is added at the end of the DataFrame
            df.to_csv(f, index=False, header=True, mode='a')
            if i < len(dataset) - 1:
                # Add a newline after the DataFrame content, except after the last DataFrame
                f.write('\n')



import unittest
import os
import shutil


class TestF490(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Ensure the data directory exists before any tests are run."""
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

    @classmethod
    def tearDownClass(cls):
        """Clean up by removing the data directory and its contents after all tests."""
        shutil.rmtree(DATA_DIR, ignore_errors=True)

    def test_single_dataframe(self):
        """Test with a single DataFrame."""
        df = pd.DataFrame({"Column1": [1, 2], "Column2": [3, 4]})
        f_490([df], 'single_dataframe.csv')
        self.assertTrue(os.path.exists(os.path.join(DATA_DIR, 'single_dataframe.csv')))

    def test_multiple_dataframes(self):
        """Test with multiple DataFrames."""
        df1 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
        df2 = pd.DataFrame({"C": [9, 10], "D": [11, 12]})
        f_490([df1, df2], 'multiple_dataframes.csv')
        self.assertTrue(os.path.exists(os.path.join(DATA_DIR, 'multiple_dataframes.csv')))

    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        df = pd.DataFrame()
        f_490([df], 'empty_dataframe.csv')
        self.assertTrue(os.path.exists(os.path.join(DATA_DIR, 'empty_dataframe.csv')))

    def test_varying_row_counts(self):
        """Test with DataFrames having varying numbers of rows."""
        df1 = pd.DataFrame({"E": [13], "F": [14]})
        df2 = pd.DataFrame({"G": [15, 16, 17], "H": [18, 19, 20]})
        f_490([df1, df2], 'varying_row_counts.csv')
        self.assertTrue(os.path.exists(os.path.join(DATA_DIR, 'varying_row_counts.csv')))

    def test_no_dataframes(self):
        """Test with no DataFrames provided."""
        f_490([], 'no_dataframes.csv')
        self.assertTrue(os.path.exists(os.path.join(DATA_DIR, 'no_dataframes.csv')))


if __name__ == "__main__":
    unittest.main()

