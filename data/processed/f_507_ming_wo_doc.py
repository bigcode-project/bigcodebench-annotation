import os
import pandas as pd
from dateutil.parser import parse
OUTPUT_DIR = './output'

def f_305(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    """
    Read a CSV file, convert a column of date strings into datetime objects,
    and draw a histogram of the year distribution of these dates.

    Parameters:
    - csv_path (str): The path to the CSV file. Default is the 'data.csv' in the script's directory.
    - date_column (str): The column in the CSV file with the date strings. Default is 'date'.

    Returns:
    - matplotlib.axes._axes.Axes: A histogram plot object showing the distribution of years.

    Requirements:
    - pandas
    - dateutil.parser
    - os

    Example:
    >>> import os
    >>> from unittest.mock import patch
    >>> with patch('os.path.exists', return_value=False):
    ...     f_305('nonexistent.csv')
    Traceback (most recent call last):
        ...
    FileNotFoundError: nonexistent.csv does not exist
    """
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"{csv_path} does not exist")
    df = pd.read_csv(csv_path)
    df[date_column] = df[date_column].apply(lambda x: parse(x))
    return df[date_column].dt.year.hist()

import unittest
import shutil
import os
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.output_dir = OUTPUT_DIR
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        # Prepare CSV files for testing
        self.valid_data_csv = os.path.join(self.output_dir, 'valid_data.csv')
        with open(self.valid_data_csv, 'w') as f:
            f.write("date\n2020-01-01\n2021-02-02")
        self.empty_data_csv = os.path.join(self.output_dir, 'empty_data.csv')
        open(self.empty_data_csv, 'w').close()  # Create an empty file
        # No need to create an invalid data CSV because parsing errors are tested dynamically
        self.different_column_data_csv = os.path.join(self.output_dir, 'different_column_data.csv')
        with open(self.different_column_data_csv, 'w') as f:
            f.write("different_date_column\n2020-01-01\n2021-02-02")
    def tearDown(self):
        shutil.rmtree(self.output_dir, ignore_errors=True)
    def test_valid_data(self):
        """Test with valid date data."""
        histogram_plot = f_305(self.valid_data_csv, 'date')
        self.assertIsInstance(histogram_plot, plt.Axes)
    def test_empty_file(self):
        """Test with an empty CSV file."""
        with self.assertRaises(ValueError):  # Assuming pandas raises a ValueError for an empty CSV
            f_305(self.empty_data_csv, 'date')
    def test_nonexistent_file(self):
        """Test with a nonexistent CSV file path."""
        nonexistent_csv = os.path.join(self.output_dir, 'nonexistent.csv')
        with self.assertRaises(FileNotFoundError):
            f_305(nonexistent_csv, 'date')
    def test_different_date_column(self):
        """Test using a different date column name."""
        histogram_plot = f_305(self.different_column_data_csv, 'different_date_column')
        self.assertIsInstance(histogram_plot, plt.Axes)
    def test_invalid_data(self):
        """Dynamically test with invalid date strings; expecting the function to handle errors gracefully."""
        invalid_data_csv = os.path.join(self.output_dir, 'invalid_data.csv')
        with open(invalid_data_csv, 'w') as f:
            f.write("date\nnot-a-date\n2021-13-01")
        with self.assertRaises(ValueError):
            f_305(invalid_data_csv, 'date')
