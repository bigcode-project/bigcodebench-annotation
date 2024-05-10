import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def f_397(column, data):
    """
    Analyze and visualize statistical properties of a specified weather data column.

    This function calculates the sum, mean, minimum, and maximum values of a specified column in the given data.
    It also generates a histogram plot of the data in the column. The dataset is expected to be a list of weather
    observations, where each observation includes date, temperature, humidity, wind speed, and precipitation values.
    If the provided data list is empty, resulting in an empty DataFrame, the function handles it by setting:
    - The 'mean' value to np.nan.
    - The 'min' value to np.inf.
    - The 'max' value to -np.inf.

    Parameters:
    column (str): The column to analyze. Valid columns include 'Temperature', 'Humidity', 'Wind Speed', and 'Precipitation'.
    data (list of lists): The weather data where each inner list contains the following format:
                          [Date (datetime object), Temperature (int), Humidity (int), Wind Speed (int), Precipitation (float)]

    Returns:
    - result (dict): A dictionary containing:
        - 'sum': Sum of the values in the specified column.
        - 'mean': Mean of the values in the specified column.
        - 'min': Minimum value in the specified column.
        - 'max': Maximum value in the specified column.
        - 'plot': A matplotlib BarContainer object of the histogram plot for the specified column.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot

    Example:
    >>> data = [[datetime(2022, 1, 1), -5, 80, 10, 0], [datetime(2022, 1, 3), -2, 83, 15, 0]]
    >>> result = f_397('Temperature', data)
    >>> result['sum']
    -7
    >>> type(result['plot'])
    <class 'matplotlib.container.BarContainer'>
    """
    COLUMNS = ["Date", "Temperature", "Humidity", "Wind Speed", "Precipitation"]
    df = pd.DataFrame(data, columns=COLUMNS)
    column_data = df[column]

    result = {
        "sum": np.sum(column_data),
        "mean": np.nan if df.empty else np.mean(column_data),
        "min": np.inf if df.empty else np.min(column_data),
        "max": -np.inf if df.empty else np.max(column_data),
    }

    _, _, ax = plt.hist(column_data)
    plt.title(f"Histogram of {column}")

    result["plot"] = ax

    return result


import unittest
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


class TestCases(unittest.TestCase):
    def setUp(self):
        self.data = [
            [datetime(2022, 1, 1), -5, 80, 10, 0],
            [datetime(2022, 1, 2), -3, 85, 12, 0.5],
            [datetime(2022, 1, 3), -2, 83, 15, 0],
            [datetime(2022, 1, 4), -1, 82, 13, 0.2],
            [datetime(2022, 1, 5), 0, 80, 11, 0.1],
        ]

    def test_case_1(self):
        # Testing the 'Temperature' column
        result = f_397("Temperature", self.data)
        self.assertEqual(result["sum"], -11)
        self.assertEqual(result["mean"], -2.2)
        self.assertEqual(result["min"], -5)
        self.assertEqual(result["max"], 0)
        self.assertIsInstance(result["plot"], matplotlib.container.BarContainer)

    def test_case_2(self):
        # Testing the 'Humidity' column
        result = f_397("Humidity", self.data)
        self.assertEqual(result["sum"], 410)
        self.assertEqual(result["mean"], 82)
        self.assertEqual(result["min"], 80)
        self.assertEqual(result["max"], 85)
        self.assertIsInstance(result["plot"], matplotlib.container.BarContainer)

    def test_case_3(self):
        # Testing the 'Wind Speed' column
        result = f_397("Wind Speed", self.data)
        self.assertEqual(result["sum"], 61)
        self.assertEqual(result["mean"], 12.2)
        self.assertEqual(result["min"], 10)
        self.assertEqual(result["max"], 15)
        self.assertIsInstance(result["plot"], matplotlib.container.BarContainer)

    def test_case_4(self):
        # Testing the 'Precipitation' column
        result = f_397("Precipitation", self.data)
        self.assertAlmostEqual(result["sum"], 0.8, places=6)
        self.assertAlmostEqual(result["mean"], 0.16, places=6)
        self.assertAlmostEqual(result["min"], 0, places=6)
        self.assertAlmostEqual(result["max"], 0.5, places=6)
        self.assertIsInstance(result["plot"], matplotlib.container.BarContainer)

    def test_case_5(self):
        # Testing with empty data
        result = f_397("Temperature", [])
        self.assertTrue(np.isnan(result["mean"]))
        self.assertEqual(result["sum"], 0)
        self.assertTrue(
            np.isinf(result["min"]) and result["min"] > 0
        )  # Checking for positive infinity for min
        self.assertTrue(
            np.isinf(result["max"]) and result["max"] < 0
        )  # Checking for negative infinity for max
        self.assertIsInstance(result["plot"], matplotlib.container.BarContainer)

    def tearDown(self):
        plt.close("all")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
