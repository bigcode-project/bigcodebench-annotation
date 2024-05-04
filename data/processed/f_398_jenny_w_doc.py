import pandas as pd
import numpy as np


def f_648(column, data):
    """
    Analyzes a list of stock data and calculates the sum, mean, minimum, and maximum
    values for a specified column.

    Parameters:
    - column (str): The name of the column to analyze. Valid options are 'Date', 'Open', 'High',
                    'Low', 'Close', and 'Volume'.
    - data (list of lists): A list where each element is a list representing stock data for a single day.
                            Each inner list should contain values in the following order:
                            'Date', 'Open', 'High', 'Low', 'Close', 'Volume'.
    Returns:
    - dict: A dictionary containing the calculated 'sum', 'mean', 'min' (minimum), and 'max' (maximum)
            for the specified column. If the input data is empty, 'sum' will be 0, and 'mean', 'min', and
            'max' will be NaN.

    Requirements:
    - pandas
    - numpy

    Raises:
    - ValueError: If the specified column name is not valid.
    
    Example:
    >>> data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000]]
    >>> results = f_648('Open', data)
    >>> results
    {'sum': 100, 'mean': 100.0, 'min': 100, 'max': 100}
    >>> type(results)
    <class 'dict'>
    """
    valid_columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
    if column not in valid_columns:
        raise ValueError(f"Invalid column name.")
    if not isinstance(data, list) or (
        len(data) > 0
        and not all(
            isinstance(row, list) and len(row) == len(valid_columns) for row in data
        )
    ):
        raise ValueError(
            "Data must be a list of lists, with each inner list matching the length of the column names."
        )
    df = pd.DataFrame(data, columns=valid_columns)
    column_data = df[column]
    result = {
        "sum": np.sum(column_data) if not column_data.empty else 0,
        "mean": np.mean(column_data) if not column_data.empty else float("nan"),
        "min": np.min(column_data) if not column_data.empty else float("nan"),
        "max": np.max(column_data) if not column_data.empty else float("nan"),
    }
    return result

import unittest
import numpy as np
from datetime import datetime
class TestCases(unittest.TestCase):
    def assertDictAlmostEqual(self, d1, d2, msg=None):
        # Helper function for testing
        for k, v in d1.items():
            if isinstance(v, float) and np.isnan(v):
                self.assertTrue(np.isnan(d2[k]), msg or f"{k} not almost equal")
            else:
                self.assertAlmostEqual(v, d2[k], msg=msg or f"{k} not equal")
    def test_case_1(self):
        # Test with valid data for a specific column
        data = [
            [datetime(2022, 1, 1), 100, 105, 95, 102, 10000],
            [datetime(2022, 1, 2), 102, 108, 100, 105, 15000],
            [datetime(2022, 1, 3), 105, 110, 103, 108, 20000],
        ]
        result = f_648("Open", data)
        expected_result = {
            "sum": 307,
            "mean": 102.33333333333333,
            "min": 100,
            "max": 105,
        }
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_2(self):
        # Test with empty data list
        data = []
        result = f_648("Open", data)
        expected_result = {
            "sum": 0,
            "mean": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
        }
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_3(self):
        # Test with an invalid column name
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000]]
        with self.assertRaises(ValueError):
            f_648("InvalidColumn", data)
    def test_case_4(self):
        # Test with NaN values in the target column
        data = [
            [datetime(2022, 1, 1), np.nan, 105, 95, 102, 10000],
            [datetime(2022, 1, 2), 102, np.nan, 100, 105, 15000],
            [datetime(2022, 1, 3), 105, np.nan, 103, 108, 20000],
        ]
        result = f_648("Open", data)
        expected_result = {"sum": 207, "mean": 103.5, "min": 102, "max": 105}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_5(self):
        # Test with all values in the target column being the same
        data = [[datetime(2022, 1, 1), 100, 100, 100, 100, 10000]] * 3
        result = f_648("Open", data)
        expected_result = {"sum": 300, "mean": 100, "min": 100, "max": 100}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_6(self):
        # Test for handling mixed data types within a single column
        data = [
            [datetime(2022, 1, 1), 100, 105, 95, 102, 10000],
            [datetime(2022, 1, 2), "102", 108, 100, 105, 15000],
        ]
        with self.assertRaises(TypeError):
            f_648("Open", data)
    def test_case_7(self):
        # Test with extremely large values in the target column
        data = [[datetime(2022, 1, 1), 1e18, 1.05e18, 0.95e18, 1.02e18, 10000]]
        result = f_648("Open", data)
        expected_result = {"sum": 1e18, "mean": 1e18, "min": 1e18, "max": 1e18}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_8(self):
        # Test with a single row of data
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000]]
        result = f_648("Open", data)
        expected_result = {"sum": 100, "mean": 100, "min": 100, "max": 100}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_9(self):
        # Test with a very large dataset to check performance/scalability
        large_data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000]] * 10000
        result = f_648("Open", large_data)
        expected_result = {"sum": 1000000, "mean": 100, "min": 100, "max": 100}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_10(self):
        # Test for column case sensitivity
        data = [
            [datetime(2022, 1, 1), 100, 105, 95, 102, 10000],
        ]
        with self.assertRaises(ValueError):
            f_648("open", data)
    def test_case_11(self):
        # Test with incorrect data
        data = "Incorrect data type"
        with self.assertRaises(ValueError):
            f_648("Open", data)
    def test_case_12(self):
        # Test for data list containing lists of varying lengths
        data = [
            [datetime(2022, 1, 1), 100, 105, 95, 102, 10000],
            [datetime(2022, 1, 2), 102, 108, 100],
        ]
        with self.assertRaises(ValueError):
            f_648("Open", data)
    def test_case_13(self):
        # Test for data list containing elements other than lists (mixed types)
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000], "Not a list"]
        with self.assertRaises(ValueError):
            f_648("Open", data)
    def test_case_14(self):
        # Test for a correctly structured and typed data list but with an empty inner list
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000], []]
        with self.assertRaises(ValueError):
            f_648("Open", data)
