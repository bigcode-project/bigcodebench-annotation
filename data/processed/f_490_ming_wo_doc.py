import os
import time
OUTPUT_DIR = './output'


def f_213(dataset, filename, output_dir=OUTPUT_DIR):
    """
    Writes multiple Pandas DataFrames to a single CSV file, separating each DataFrame by a line of hyphens ("------").

    Parameters:
    - dataset (list of pd.DataFrame): A list containing the DataFrames to be written to the file.
    - filename (str): The name of the file (excluding the path) where the DataFrames will be written.
    - output_dir (str, optional): the ouput directory.

    Returns:
    None: The function writes the DataFrames to a CSV file but does not return any value.

    Requirements:
    - os
    - time

    Example:
    >>> import pandas as pd
    >>> df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    >>> df2 = pd.DataFrame({"D": [5, 6], "E": [7, 8]})
    >>> f_213([df1, df2], 'sample.csv')
    """
    start_time = time.time()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', newline='') as f:
        for i, df in enumerate(dataset):
            if i > 0:
                f.write('------\n')
            df.to_csv(f, index=False, header=True, mode='a')
            if i < len(dataset) - 1:
                f.write('\n')
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."

import unittest
import shutil
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        """Ensure the data directory exists before any tests are run."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    def tearDown(self):
        """Clean up by removing the data directory and its contents after all tests."""
        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    def test_single_dataframe(self):
        """Test with a single DataFrame."""
        df = pd.DataFrame({"Column1": [1, 2], "Column2": [3, 4]})
        f_213([df], 'single_dataframe.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'single_dataframe.csv')))
    def test_multiple_dataframes(self):
        """Test with multiple DataFrames."""
        df1 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
        df2 = pd.DataFrame({"C": [9, 10], "D": [11, 12]})
        f_213([df1, df2], 'multiple_dataframes.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'multiple_dataframes.csv')))
    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        df = pd.DataFrame()
        f_213([df], 'empty_dataframe.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'empty_dataframe.csv')))
    def test_varying_row_counts(self):
        """Test with DataFrames having varying numbers of rows."""
        df1 = pd.DataFrame({"E": [13], "F": [14]})
        df2 = pd.DataFrame({"G": [15, 16, 17], "H": [18, 19, 20]})
        f_213([df1, df2], 'varying_row_counts.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'varying_row_counts.csv')))
    def test_no_dataframes(self):
        """Test with no DataFrames provided."""
        f_213([], 'no_dataframes.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'no_dataframes.csv')))
