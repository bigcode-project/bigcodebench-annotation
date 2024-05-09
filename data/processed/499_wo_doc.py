import csv
import os
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd

# Constants
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'


def task_func(hours, output_dir=OUTPUT_DIR):
    """
    Generates traffic data for different vehicle types over a specified number of hours,
    saves the data to a CSV file with coloumns 'Time', 'Car', 'Bus', 'Truck', and 'Bike',
    and plots the data in a line chart with 'Time' on x-axis and 'Vehicle Count' on y-axis.

    Parameters:
    - hours (int): Number of hours to generate data for.
    - output_dir (str, optional): The output file path

    Returns:
    - tuple: Path to the CSV file and the matplotlib axes object of the line plot.

    Requirements:
    - pandas
    - os
    - csv
    - matplotlib.pyplot
    - random
    - datetime

    Example:
    >>> import matplotlib
    >>> file_path, ax = task_func(2)  # Generate data for 2 hours
    >>> isinstance(file_path, str)
    True
    >>> 'traffic_data.csv' in file_path
    True
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    FILE_PATH = os.path.join(output_dir, 'traffic_data.csv')
    data = [['Time'] + VEHICLE_TYPES]
    for i in range(hours):
        row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')] + [randint(0, 50) for _ in VEHICLE_TYPES]
        data.append(row)
    with open(FILE_PATH, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    df = pd.read_csv(FILE_PATH)
    if df.empty:
        return FILE_PATH, None
    ax = df.plot(x='Time', y=VEHICLE_TYPES, kind='line', title='Traffic Data Over Time')
    plt.xlabel('Time')
    plt.ylabel('Vehicle Count')
    plt.tight_layout()
    plt.show()
    return FILE_PATH, ax

import unittest
from unittest.mock import patch
import shutil
FILE_PATH = os.path.join(OUTPUT_DIR, 'traffic_data.csv')
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up the environment for testing."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)
    @patch('matplotlib.pyplot.show')  # Mock plt.show to not render plots
    @patch('csv.writer')  # Mock csv.writer to not actually write files
    @patch('pandas.read_csv')  # Mock pd.read_csv to not read from disk
    @patch(__name__ + '.randint', return_value=25)  # Mock randint to return a fixed value
    def test_dataframe_content(self, mock_randint, mock_read_csv, mock_csv_writer, mock_plt_show):
        mock_read_csv.return_value = pd.DataFrame({
            'Time': ['2021-01-01 00:00:00.000000'],
            'Car': [25], 'Bus': [25], 'Truck': [25], 'Bike': [25]
        })
        file_path, ax = task_func(1)
        self.assertEqual(file_path, FILE_PATH)
        mock_randint.assert_called()  # Ensures randint was called, but not specifics about calls
        mock_read_csv.assert_called_with(FILE_PATH)
        mock_plt_show.assert_called()
    @patch(__name__ + '.pd.read_csv', return_value=pd.DataFrame(columns=['Time'] + VEHICLE_TYPES))
    def test_empty_dataframe_on_zero_hours(self, mock_read_csv):
        """Check for empty DataFrame on zero hours input."""
        _, ax = task_func(0)
        self.assertIsNone(ax)
    @patch('os.makedirs')
    @patch('os.path.exists', return_value=False)
    def test_directory_creation(self, mock_path_exists, mock_makedirs):
        """Ensure directory is created if it does not exist."""
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)
        task_func(1)
        mock_makedirs.assert_called_with(os.path.dirname(FILE_PATH))
    @patch(__name__ + '.plt.show')
    def test_plot_generation(self, mock_plt_show):
        """Verify that the plot is generated."""
        task_func(1)
        mock_plt_show.assert_called()
    @patch(__name__ + '.plt.show')  # Mock to skip plot rendering
    def test_task_func_runs_without_error(self, mock_show):
        """Test task_func function to ensure it runs with given hours without raising an error."""
        try:
            task_func(1)  # Attempt to run the function with a simple input
            operation_successful = True
        except Exception:
            operation_successful = False
        self.assertTrue(operation_successful, "task_func should run without errors for given input")
