import csv
import os
from random import randint
import matplotlib.pyplot as plt

def f_190(data_directory, filename=None):
    """
    Plots data from a specified or randomly selected CSV file from the given directory 
    and returns the plot's Axes object.
    
    Parameters:
    - data_directory (str): The path to the directory containing the CSV files.
    - filename (str, optional): The name of a specific CSV file to plot. If not provided, a random CSV file will be selected from the directory.
    
    Libraries Used:
    - csv: To read data from the CSV files.
    - os: To list and join file paths.
    - random: To randomly select a CSV file if no filename is provided.
    - matplotlib.pyplot: To plot the data.
    
    Returns:
    - matplotlib.axes._subplots.AxesSubplot: Axes object of the plotted data.
    
    Example:
    >>> ax = f_190("/path/to/csv/files", "file1.csv")
    """
    # Get all CSV files from the provided directory
    csv_files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]
    # Use provided filename or randomly select a CSV file
    file = filename or csv_files[randint(0, len(csv_files)-1)]
    file_path = os.path.join(data_directory, file)

    # Read data from the CSV file and convert to numeric values
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = [(float(x), float(y)) for x, y in reader]

    # Plot the data and return the Axes object
    fig, ax = plt.subplots()
    ax.plot(*zip(*data))
    ax.set_xlabel(headers[0])
    ax.set_ylabel(headers[1])
    return ax

import unittest
import random

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


import unittest
import random
import pandas as pd
import os

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    """Test cases for the f_190 function.""" 
    def setUp(self):
        self.test_dir = "data/f_190"
        os.makedirs(self.test_dir, exist_ok=True)
        df = pd.DataFrame(
            {
                "x" : [1.0, 2.0, 3.0, 4.0],
                "y" : [5.0, 10.0, 15.0, 20.0]
            }
        )
        df.to_csv(os.path.join(self.test_dir, "csv_1.csv"), index=False)

        df = pd.DataFrame(
            {
                "x" : [1.0, 2.0, 3.0, 4.0],
                "y" : [2.0, 4.0, 6.0, 8.0]
            }
        )
        df.to_csv(os.path.join(self.test_dir, "csv_2.csv"), index=False)
        with open(os.path.join(self.test_dir, "csv_3.csv"), "w") as f :
            f.write("if __name__ == '__main__' :\n\tprint('hello world!')")
        with open(os.path.join(self.test_dir, "hello_world.py"), "r") as f :
            f.write("")

    def test_case_1(self):
        # Testing with a specific CSV file
        ax = f_190(self.test_dir, "csv_1.csv")
        # Asserting that the x and y data matches the CSV content
        self.assertEqual(ax.lines[0].get_xdata().tolist(), [1.0, 2.0, 3.0, 4.0])
        self.assertEqual(ax.lines[0].get_ydata().tolist(), [5.0, 10.0, 15.0, 20.0])
        
    def test_case_2(self):
        # Testing with another specific CSV file
        ax = f_190(self.test_dir, "csv_2.csv")
        # Asserting that the x and y data matches the CSV content
        self.assertEqual(ax.lines[0].get_xdata().tolist(), [1.0, 2.0, 3.0, 4.0])
        self.assertEqual(ax.lines[0].get_ydata().tolist(), [2.0, 4.0, 6.0, 8.0])
        
    def test_case_3(self):
        # Testing without specifying a CSV file (random selection)
        random.seed(122)
        ax = f_190(self.test_dir)
        # Asserting that a plot
        self.assertTrue(isinstance(ax, plt.Axes))
        
    def test_case_4(self):
        # Testing with a non-existing CSV file should raise a FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            f_190(self.test_dir, "non_existent.csv")
            
    def test_case_5(self):
        # Testing with a non-CSV file (using function.py for this test)
        # This should raise a ValueError as we're expecting two values from each row of the CSV
        with self.assertRaises(ValueError):
            f_190(self.test_dir, "hello_world.py")

if __name__ == "__main__":
    run_tests()