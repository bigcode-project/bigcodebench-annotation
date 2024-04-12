import shutil
from datetime import datetime
import os
from random import randint
import csv

# Constants
current_directory_path = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(__file__))[0])
FILE_PATH = os.path.join(current_directory_path, 'sensor_data.csv')
SENSORS = ['Temperature', 'Humidity', 'Pressure']


def ensure_directory_exists(file_path):
    """
    Checks if the directory for the provided file path exists, and creates it if not.

    Parameters:
    - file_path (str): The file path for which the directory needs to be checked/created.
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def f_455(hours):
    """
    Create sensor data for the specified number of hours and save it in a CSV file.

    Parameters:
    - hours (int): The number of hours for which sensor data is to be generated.

    Returns:
    - str: The path of the generated CSV file.

    Requirements:
    - datetime: To generate the current timestamp for each sensor data row.
    - os: For handling file and directory paths.
    - random: To generate random sensor data values.
    - csv: For writing the sensor data to a CSV file.

    Example:
    >>> file_path = f_455(24)
    >>> print(file_path)
    The function will return the path to the created CSV file containing the sensor data.

    Note:
    This function also demonstrates the use of the 'os' module to check for the existence of
    the directory where the CSV file will be saved, creating it if necessary, to ensure that
    the file writing operation does not fail due to a missing directory.
    """
    ensure_directory_exists(FILE_PATH)  # Ensure the directory exists

    data = [['Time'] + SENSORS]
    for i in range(hours):
        row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')] + [randint(0, 100) for _ in SENSORS]
        data.append(row)

    with open(FILE_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    return FILE_PATH


import unittest
import os

class TestF455(unittest.TestCase):

    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(current_directory_path):
            shutil.rmtree(current_directory_path)

    def test_csv_file_creation(self):
        """Test if the CSV file is successfully created."""
        f_455(1)
        self.assertTrue(os.path.exists(FILE_PATH))

    def test_csv_file_rows(self):
        """Test if the CSV file contains the correct number of rows for 24 hours."""
        f_455(24)
        with open(FILE_PATH, 'r') as f:
            self.assertEqual(len(f.readlines()), 25)  # Including header

    def test_csv_file_header(self):
        """Test if the CSV file header matches the expected sensors."""
        f_455(0)
        with open(FILE_PATH, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['Time', 'Temperature', 'Humidity', 'Pressure'])

    def test_file_path_return(self):
        """Test if the correct file path is returned."""
        file_path = f_455(1)
        self.assertEqual(file_path, FILE_PATH)

    def test_no_hours_data(self):
        """Test sensor data generation with 0 hours."""
        f_455(0)
        with open(FILE_PATH, 'r') as f:
            self.assertEqual(len(f.readlines()), 1)  # Only header row expected


if __name__ == '__main__':
    unittest.main()

