import os
import csv
import random
from datetime import datetime

def f_622():
    """
    Create a CSV file "f_622_data_xiaoheng/Output.txt" with sensor data for temperature and humidity.
    The data is generated randomly and written in append mode.

    Parameters:
    - None

    Returns:
    - Returns the path to the CSV file "f_622_data_xiaoheng/Output.txt".

    Requirements:
    - os
    - csv
    - random
    - datetime

    Constants:
    - FILE_NAME: Name of the CSV file.
    - FIELDS: Headers for the CSV file.

    Example:
    >>> f_622()
    'f_622_data_xiaoheng/Output.txt'
    """
    FILE_NAME = 'f_622_data_xiaoheng/Output.txt'
    FIELDS = ['Timestamp', 'Temperature', 'Humidity']

    temperature = random.uniform(20, 30)  # temperature between 20 and 30
    humidity = random.uniform(50, 60)  # humidity between 50 and 60
    timestamp = datetime.now()

    # Check if file exists and write headers if not
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(FIELDS)

    # Append data
    with open(FILE_NAME, 'a') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([timestamp, temperature, humidity])

    return FILE_NAME

import unittest
import os
import csv

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def test_return_value(self):
        # Test if the function returns the correct file path
        self.assertEqual(f_622(), "f_622_data_xiaoheng/Output.txt")

    def test_file_existence(self):
        # Test if the file exists after function execution
        self.assertTrue(os.path.isfile("f_622_data_xiaoheng/Output.txt"))

    def test_file_content(self):
        # Validate the content of the file
        with open("f_622_data_xiaoheng/Output.txt", 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['Timestamp', 'Temperature', 'Humidity'])
            
            for row in reader:
                # Check if there are 3 columns in every row
                self.assertEqual(len(row), 3)
                # Check if temperature and humidity values are within the expected range
                self.assertTrue(20 <= float(row[1]) <= 30)
                self.assertTrue(50 <= float(row[2]) <= 60)

    def test_data_appending(self):
        # Test repeated executions to ensure data is appended correctly
        initial_line_count = sum(1 for line in open("f_622_data_xiaoheng/Output.txt"))
        f_622()
        final_line_count = sum(1 for line in open("f_622_data_xiaoheng/Output.txt"))
        self.assertEqual(final_line_count, initial_line_count + 1)

    def test_headers_only_once(self):
        # Ensure headers are not duplicated
        with open("f_622_data_xiaoheng/Output.txt", 'r') as f:
            reader = csv.reader(f)
            header_count = sum(1 for row in reader if row == ['Timestamp', 'Temperature', 'Humidity'])
            self.assertEqual(header_count, 1)

if __name__ == "__main__":
    run_tests()