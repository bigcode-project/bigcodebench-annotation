import os
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

def f_750(directory: str, pattern: str) -> list:
    """
    Searches a directory for CSV files matching a given regular expression pattern,
    reads sales data from these files, and plots the sales data with month on the x-axis and sales on the y-axis.
    
    Note:
    - Each CSV file contains two columns: 'Month' and 'Sales'.

    Parameters:
    - directory (str): The directory path where the CSV files are located.
    - pattern (str): The regular expression pattern to match the filenames.

    Returns:
    - A list of matplotlib.axes._subplots.AxesSubplot objects, each representing a plot of sales data from a matched CSV file.

    Examples:
    >>> axes = f_750('/path/to/data/', r'^sales_data_\d{4}.csv')
    >>> len(axes)
    2
    >>> axes[0].get_title()
    'sales_data_2021.csv'
    """

    plots = []
    for file in os.listdir(directory):
        if re.match(pattern, file):
            df = pd.read_csv(os.path.join(directory, file))
            ax = df.plot(x='Month', y='Sales', title=file)
            plots.append(ax)
    plt.show()
    return plots

import unittest
import shutil
class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Prepare test data
        cls.directory = "f_750_data_wenhao/"
        cls.pattern = r"^sales_data_\d{4}.csv"
        os.makedirs(cls.directory, exist_ok=True)
        data_2021 = pd.DataFrame({
            'Month': ['January', 'February', 'March'],
            'Sales': [100, 150, 200]
        })
        data_2022 = pd.DataFrame({
            'Month': ['January', 'February', 'March'],
            'Sales': [120, 130, 210]
        })
        data_2021.to_csv(cls.directory + "sales_data_2021.csv", index=False)
        data_2022.to_csv(cls.directory + "sales_data_2022.csv", index=False)

    @classmethod
    def tearDownClass(cls):
        # Clean up test data
        shutil.rmtree(cls.directory)

    def test_plots_generated(self):
        plots = f_750(self.directory, self.pattern)
        self.assertEqual(len(plots), 2, "Should generate two plots for two CSV files")

    def test_plot_titles(self):
        plots = f_750(self.directory, self.pattern)
        expected_titles = ['sales_data_2022.csv', 'sales_data_2021.csv']
        plot_titles = [plot.get_title() for plot in plots]
        self.assertEqual(plot_titles, expected_titles, "Plot titles should match the CSV filenames")

    def test_no_files_matched(self):
        plots = f_750(self.directory, r"^no_match_\d{4}.csv")
        self.assertEqual(len(plots), 0, "Should return an empty list if no files match the pattern")

    def test_invalid_directory(self):
        with self.assertRaises(FileNotFoundError):
            f_750("/invalid/directory/", self.pattern)

    def test_plot_data_integrity(self):
        plots = f_750(self.directory, self.pattern)
        # Read the CSV files again to get expected data
        expected_data = []
        for file in os.listdir(self.directory):
            if re.match(self.pattern, file):
                df = pd.read_csv(os.path.join(self.directory, file))
                expected_data.append(df['Sales'].to_list())

        for plot, expected_sales in zip(plots, expected_data):
            lines = plot.get_lines()
            for line in lines:
                y_data = line.get_ydata()
                # Use np.isclose for floating point comparison, if necessary
                self.assertTrue(any(np.array_equal(y_data, expected) for expected in expected_data), "Plotted data should match the CSV file content")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
