import os
import shutil

import matplotlib
import pandas as pd
from datetime import datetime
from dateutil.parser import parse
import matplotlib.pyplot as plt

# Correct CSV_PATH to reflect the current directory of this script plus 'data.csv'
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.csv')
DATE_COLUMN = 'date'  # Default column in the CSV file with the date strings


def f_507(csv_path=CSV_PATH, date_column=DATE_COLUMN):
    """
    Read a CSV file, convert a column of date strings into datetime objects,
    and draw a histogram of the year distribution of these dates.

    Parameters:
    - csv_path (str): The path to the CSV file. Default is the 'data.csv' in the script's directory.
    - date_column (str): The column in the CSV file with the date strings. Default is 'date'.

    Returns:
    - matplotlib.axes._subplots.AxesSubplot: A histogram plot object showing the distribution of years.

    Requirements:
    - pandas for data manipulation and CSV file reading.
    - datetime and dateutil.parser for date string parsing.
    - os for file path operations.
    - matplotlib.pyplot for plotting.

    Example:
    Assuming 'data.csv' with a 'date' column containing date strings:
    >>> histogram_plot = f_507()
    >>> type(histogram_plot)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"{csv_path} does not exist")

    df = pd.read_csv(csv_path)
    df[date_column] = df[date_column].apply(lambda x: parse(x))

    return df[date_column].dt.year.hist()

import unittest
import shutil
import os
import pandas as pd

class TestF507Function(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current_dir = os.path.dirname(os.path.abspath(__file__))
        cls.test_data_dir = os.path.join(cls.current_dir, 'test_data')
        if not os.path.exists(cls.test_data_dir):
            os.makedirs(cls.test_data_dir)

        # Prepare CSV files for testing
        cls.valid_data_csv = os.path.join(cls.test_data_dir, 'valid_data.csv')
        with open(cls.valid_data_csv, 'w') as f:
            f.write("date\n2020-01-01\n2021-02-02")

        cls.empty_data_csv = os.path.join(cls.test_data_dir, 'empty_data.csv')
        open(cls.empty_data_csv, 'w').close()  # Create an empty file

        # No need to create an invalid data CSV because parsing errors are tested dynamically

        cls.different_column_data_csv = os.path.join(cls.test_data_dir, 'different_column_data.csv')
        with open(cls.different_column_data_csv, 'w') as f:
            f.write("different_date_column\n2020-01-01\n2021-02-02")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_data_dir, ignore_errors=True)

    def test_valid_data(self):
        """Test with valid date data."""
        histogram_plot = f_507(self.valid_data_csv, 'date')
        self.assertIsInstance(histogram_plot, plt.Axes)

    def test_empty_file(self):
        """Test with an empty CSV file."""
        with self.assertRaises(ValueError):  # Assuming pandas raises a ValueError for an empty CSV
            f_507(self.empty_data_csv, 'date')

    def test_nonexistent_file(self):
        """Test with a nonexistent CSV file path."""
        nonexistent_csv = os.path.join(self.test_data_dir, 'nonexistent.csv')
        with self.assertRaises(FileNotFoundError):
            f_507(nonexistent_csv, 'date')

    def test_different_date_column(self):
        """Test using a different date column name."""
        histogram_plot = f_507(self.different_column_data_csv, 'different_date_column')
        self.assertIsInstance(histogram_plot, plt.Axes)

    def test_invalid_data(self):
        """Dynamically test with invalid date strings; expecting the function to handle errors gracefully."""
        invalid_data_csv = os.path.join(self.test_data_dir, 'invalid_data.csv')
        with open(invalid_data_csv, 'w') as f:
            f.write("date\nnot-a-date\n2021-13-01")
        with self.assertRaises(ValueError):
            f_507(invalid_data_csv, 'date')


if __name__ == '__main__':
    unittest.main()
