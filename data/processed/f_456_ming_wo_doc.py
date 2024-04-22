import shutil
import matplotlib
# Check and set the backend
print("Current backend:", matplotlib.get_backend())  # Optional: Check the current backend
matplotlib.use('Agg')  # Set to 'Agg' to avoid GUI-related issues
import sys
import pandas as pd
from datetime import datetime
from random import randint
import csv
import matplotlib.pyplot as plt
import os

# Constants

current_directory_path = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(__file__))[0])
FILE_PATH = os.path.join(current_directory_path, 'traffic_data.csv')
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
# sys.path.append(current_directory_path)


def ensure_directory(current_directory_path):
    if not os.path.exists(current_directory_path):
        os.makedirs(current_directory_path)


def f_456(hours):
    """
    Generates traffic data for different vehicle types over a specified number of hours,
    saves the data to a CSV file, and plots the data in a line chart.

    Parameters:
    - hours (int): Number of hours to generate data for.

    Returns:
    - tuple: Path to the CSV file and the matplotlib axes object of the line plot.

    Requirements:
    - pandas
    - os
    - csv
    - matplotlib.pyplot

    Example:
    >>> file_path, ax = f_456(2)  # Generate data for 2 hours
    >>> isinstance(file_path, str)
    True
    >>> 'traffic_data.csv' in file_path
    True
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """
    ensure_directory(current_directory_path)

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
from unittest.mock import patch, MagicMock, ANY, call
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up the environment for testing."""
        if not os.path.exists(current_directory_path):
            os.makedirs(current_directory_path)
    @classmethod
    def tearDownClass(cls):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(current_directory_path):
            shutil.rmtree(current_directory_path)
    @patch('matplotlib.pyplot.show')  # Mock plt.show to not render plots
    @patch('csv.writer')  # Mock csv.writer to not actually write files
    @patch('pandas.read_csv')  # Mock pd.read_csv to not read from disk
    @patch(__name__ + '.randint', return_value=25)  # Mock randint to return a fixed value
    def test_dataframe_content(self, mock_randint, mock_read_csv, mock_csv_writer, mock_plt_show):
        mock_read_csv.return_value = pd.DataFrame({
            'Time': ['2021-01-01 00:00:00.000000'],
            'Car': [25], 'Bus': [25], 'Truck': [25], 'Bike': [25]
        })
        file_path, ax = f_456(1)
        self.assertEqual(file_path, FILE_PATH)
        mock_randint.assert_called()  # Ensures randint was called, but not specifics about calls
        mock_read_csv.assert_called_with(FILE_PATH)
        mock_plt_show.assert_called()
    @patch(__name__ + '.pd.read_csv', return_value=pd.DataFrame(columns=['Time'] + VEHICLE_TYPES))
    def test_empty_dataframe_on_zero_hours(self, mock_read_csv):
        """Check for empty DataFrame on zero hours input."""
        _, ax = f_456(0)
        self.assertIsNone(ax)
    @patch('os.makedirs')
    @patch('os.path.exists', return_value=False)
    def test_directory_creation(self, mock_path_exists, mock_makedirs):
        """Ensure directory is created if it does not exist."""
        if os.path.exists(current_directory_path):
            shutil.rmtree(current_directory_path)
        f_456(1)
        mock_makedirs.assert_called_with(os.path.dirname(FILE_PATH))
    @patch(__name__ + '.plt.show')
    def test_plot_generation(self, mock_plt_show):
        """Verify that the plot is generated."""
        f_456(1)
        mock_plt_show.assert_called()
    @patch(__name__ + '.plt.show')  # Mock to skip plot rendering
    def test_f_456_runs_without_error(self, mock_show):
        """Test f_456 function to ensure it runs with given hours without raising an error."""
        try:
            f_456(1)  # Attempt to run the function with a simple input
            operation_successful = True
        except Exception:
            operation_successful = False
        self.assertTrue(operation_successful, "f_456 should run without errors for given input")
