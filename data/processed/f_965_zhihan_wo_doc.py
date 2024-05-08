import csv
import random

# Constants
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}

def f_976(file_name="data.csv"):
    """
    Generate a CSV file with weather data for each hour of the current day.

    Parameters:
    file_name (str): The path to the CSV file to be created.
    
    Returns:
    str: The path to the created file.

    Note:
    - The row names for the csv are 'Temperature', 'Humidity', and 'Pressure' 
    - Temperature ranged rom -50 to 50
    - Humidity ranged rom 0 to 100
    - Pressure ranged rom 980 to 1040

    Requirements:
    - os
    - datetime
    - csv
    - random

    Example:
    >>> f_976("data.csv")
    'path/to/data.csv'
    """
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time'] + DATA)
        for hour in range(24):
            row = [f'{hour}:00']
            for data_type in DATA:
                min_val, max_val = RANGE[data_type]
                row.append(random.uniform(min_val, max_val))
            writer.writerow(row)
    return file_name

import unittest
import os
import csv
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup for the test cases, creating a mock file name
        self.mock_file_name = "test_f_976_data.csv"
        
    def tearDown(self):
        # Cleanup after each test, removing the generated file if it exists
        if os.path.exists(self.mock_file_name):
            os.remove(self.mock_file_name)
    def test_case_1(self):
        # Testing default file name
        random.seed(0)
        returned_file = f_976(self.mock_file_name)
        self.assertTrue(os.path.exists(returned_file))
        
    def test_case_2(self):
        # Testing custom file name
        random.seed(0)
        returned_file = f_976(self.mock_file_name)
        self.assertTrue(os.path.exists(returned_file))
        
    def test_case_3(self):
        # Testing content structure of the CSV file
        random.seed(0)
        f_976(self.mock_file_name)
        with open(self.mock_file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(header, ['Time', 'Temperature', 'Humidity', 'Pressure'])
            
    def test_case_4(self):
        # Testing content data ranges of the CSV file
        random.seed(0)
        f_976(self.mock_file_name)
        with open(self.mock_file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                temp, humidity, pressure = float(row[1]), float(row[2]), float(row[3])
                self.assertTrue(-50 <= temp <= 50)
                self.assertTrue(0 <= humidity <= 100)
                self.assertTrue(980 <= pressure <= 1040)
                
    def test_case_5(self):
        # Testing number of rows (24 hours + header)
        random.seed(0)
        f_976(self.mock_file_name)
        with open(self.mock_file_name, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 25)
