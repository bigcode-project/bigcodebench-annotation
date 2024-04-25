import csv
import os
from datetime import datetime
from random import randint

# Constants
SENSORS = ['Temperature', 'Humidity', 'Pressure']


def f_455(hours, current_directory_path = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(__file__))[0])):
    """
    Create sensor data for the specified number of hours and save it in a CSV file.

    Parameters:
    - hours (int): The number of hours for which sensor data is to be generated.

    Returns:
    - str: The path of the generated CSV file.

    Requirements:
    - datetime
    - os
    - random
    - csv

    Example:
    >>> file_path = f_455(1)  # Generate data for 1 hour
    >>> os.path.exists(file_path)  # Check if the file was actually created
    True
    >>> isinstance(file_path, str)  # Validate that the return type is a string
    True
    >>> 'sensor_data.csv' in file_path  # Ensure the filename is correct
    True
    """
    FILE_PATH = os.path.join(current_directory_path, 'sensor_data.csv')
    directory = os.path.dirname(FILE_PATH)
    if not os.path.exists(directory):
        os.makedirs(directory)

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
import shutil
current_directory_path = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(__file__))[0])
FILE_PATH = os.path.join(current_directory_path, 'sensor_data.csv')


class TestCases(unittest.TestCase):

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

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()

