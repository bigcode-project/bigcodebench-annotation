import pandas as pd
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import os

TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
current_directory_path = os.getcwd()
# print(current_directory_path)
FILE_PATH = os.path.join(current_directory_path, 'custom_data.csv')


def f_454(hours, file_path=FILE_PATH):
    """
    Generate temperature data for the specified number of hours, save it in a CSV file, 
    and plot the data using matplotlib.
    
    Parameters:
    hours (int): The number of hours for which temperature data is to be generated.
    file_path (str, optional): Path where the CSV file will be saved. Defaults to 'temp_data.csv'.
    
    Returns:
    tuple: 
        - str: The path of the generated CSV file.
        - AxesSubplot: The plot object for further manipulation or saving.
    
    Requirements:
    - pandas
    - datetime
    - random
    - matplotlib.pyplot
    
    Data Structure:
    The function uses a dictionary to manage the generated temperature data with keys: 'Time', 'Temperature', and 'Category'.
    
    Example:
    >>> f_454(24)
    ('temp_data.csv', <AxesSubplot:>)

    """
    data = {'Time': [], 'Temperature': [], 'Category': []}
    for i in range(hours):
        temp = randint(-10, 40)  # random temperature between -10 and 40
        data['Time'].append(datetime.now().strftime('%H:%M:%S.%f'))
        data['Temperature'].append(temp)
        if temp < 0:
            data['Category'].append(TEMP_CATEGORIES[0])
        elif temp > 25:
            data['Category'].append(TEMP_CATEGORIES[2])
        else:
            data['Category'].append(TEMP_CATEGORIES[1])

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    
    ax = df.plot(x = 'Time', y = 'Temperature', kind = 'line', title="Temperature Data Over Time")
    plt.show()

    return file_path, ax

import unittest
import pandas as pd
import os


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)

    def test_case_1(self):
        # Testing with 1 hour
        file_path, ax = f_454(1)
        self.assertEqual(file_path, FILE_PATH)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 1)

    def test_case_2(self):
        # Testing with 24 hours
        file_path, ax = f_454(24)
        self.assertEqual(file_path, FILE_PATH)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 24)

    def test_case_3(self):
        # Testing with 120 hours
        file_path, ax = f_454(120)
        self.assertEqual(file_path, FILE_PATH)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 120)

    def test_case_4(self):
        # Testing with a custom file path
        file_path, ax = f_454(24, FILE_PATH)
        self.assertEqual(file_path, FILE_PATH)
        self.assertTrue(os.path.exists(FILE_PATH))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 24)

    def test_case_5(self):
        # Testing the categories in the generated CSV file
        file_path, ax = f_454(24, FILE_PATH)
        df = pd.read_csv(file_path)
        categories = df['Category'].unique().tolist()
        for cat in categories:
            self.assertIn(cat, ['Cold', 'Normal', 'Hot'])


if __name__ == "__main__":
    run_tests()