import numpy as np
import pandas as pd


def f_531(data_str, separator=",", bins=20):
    """
    Convert a string of numerical values separated by a specified separator into a pandas
    numerical series with int64, and then draw a histogram of the data.

    The function raises a ValueError if data is empty or it fails to convert the data.
    It plots the histogram with the following attributes:
    - grid: True
    - rwidth: 0.9
    - color: '#607c8e'

    Parameters:
    - data_str (str): The string of numbers separated by the specified separator.
    - separator (str, optional): The separator used in the data string. Default is ','.
    - bins (int, optional): Number of histogram bins. Default is 20.

    Returns:
    - tuple: A tuple containing:
        1. Series: A pandas Series of the data coonverted into integers.
        2. Axes: The Axes object of the plotted histogram.

    Requirements:
    - numpy
    - pandas

    Example:
    >>> series, ax = f_531('1,2,3,4,5,5,5,4,3,2,1')
    >>> print(type(series), series.tolist())
    <class 'pandas.core.series.Series'> [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
    >>> print(type(ax))
    <class 'matplotlib.axes._axes.Axes'>
    """

    data = np.fromstring(data_str, sep=separator)
    if data.size == 0:
        raise ValueError("Failed to find valid data")

    data = pd.Series(data, dtype='int64')
    ax = data.plot.hist(grid=True, bins=bins, rwidth=0.9, color="#607c8e")
    return data, ax

import unittest
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.default_str = "1,2,3,4,5,5,5,4,3,2,1"
        self.default_expected = pd.Series([1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1])
    def assertHistogramAttributes(self, series, ax):
        # Check that the y-axis gridlines are set to True
        self.assertTrue(ax.yaxis.grid)
        # Ensure the histogram bars have the correct color
        self.assertEqual(matplotlib.colors.to_hex(ax.patches[0].get_fc()), "#607c8e")
        # Validate the heights of the histogram bars
        for patch in ax.patches:
            if (
                round(patch.get_x()) in series.values
                or round(patch.get_x() + patch.get_width()) in series.values
            ):
                self.assertTrue(patch.get_height() >= 0)
    def test_case_1(self):
        # Test default case
        series, ax = f_531(self.default_str)
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, self.default_expected)
    def test_case_2(self):
        # Test function works on different bin sizes
        for bins in [5, 10, 15, 30, 100]:
            with self.subTest(bins=bins):
                series, ax = f_531(self.default_str, bins=bins)
                self.assertIsInstance(series, pd.Series)
                self.assertHistogramAttributes(series, ax)
                pd.testing.assert_series_equal(series, self.default_expected)
    def test_case_3(self):
        # Test custom separators
        data_str = "1|2|3|4|5"
        series, ax = f_531(data_str, separator="|")
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, pd.Series([1, 2, 3, 4, 5]))
    def test_case_4(self):
        # Test negative and zero
        data_str = "-5,-4,-3,-2,-1,0"
        series, ax = f_531(data_str)
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, pd.Series([-5, -4, -3, -2, -1, 0]))
    def test_case_5(self):
        # Test single item
        data_str = "1"
        series, ax = f_531(data_str)
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, pd.Series([1]))
    def test_case_6(self):
        # Test with float
        series, ax = f_531("1.0,2.0,3.0,4.0,5.0,5.0,5.0,4.0,3.0,2.0,1.0")
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, self.default_expected)
    def test_case_7(self):
        # Test with empty string
        data_str = ""
        with self.assertRaises(ValueError):
            f_531(data_str)
    def test_case_8(self):
        # Test with invalid data (contains string)
        data_str = "a,b,c, 1"
        with self.assertRaises(ValueError):
            f_531(data_str)
    def tearDown(self):
        plt.close("all")
