import pandas as pd
from datetime import datetime
import random


def f_824(start_date, end_date, num_series, seed=None):
    """
    Generates a DataFrame with multiple random integer time series (each ranging
    from 0 to 100) from a start date to an end date, then returns the generated time series
    on a line plot.

    Parameters:
    - start_date (str): The start date in "yyyy-mm-dd" format.
    - end_date (str): The end date in "yyyy-mm-dd" format.
    - num_series (int): The number of random time series to generate.
    - seed (int, optional): Seed for the random number generator. Defaults to None (not set).

    Returns:
    - pandas.DataFrame: A pandas DataFrame containing the generated time series, indexed by date.
    - plt.Axes: A matplotlib line plot of the time series.

    Raises:
    - ValueError: If start_date is later than end_date; or if num_series is less than 1.

    Requirements:
    - pandas
    - datetime
    - random

    Notes:
    - The line plot's title is set to "Random Time Series", the x-axis label to "Date",
      and the y-axis label to "Value".
    - Each time series is plotted as a separate line with automatic coloring and legend
      entry labeled as "series_x" where x is the series number.

    Example:
    >>> df, ax = f_824('2020-01-01', '2020-12-31', 3, 42)
    >>> df.head(2)
                series_1  series_2  series_3
    2020-01-01        81        67        19
    2020-01-02        14        20        29
    """
    if seed is not None:
        random.seed(seed)

    start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
    if start_date_dt > end_date_dt:
        raise ValueError("start_date must be earlier than or equal to end_date.")
    if num_series < 1:
        raise ValueError("num_series must be at least 1.")

    date_range = pd.date_range(start_date_dt, end_date_dt)

    data = {}
    for i in range(num_series):
        series_name = f"series_{i+1}"
        data[series_name] = [random.randint(0, 100) for _ in range(len(date_range))]

    df = pd.DataFrame(data, index=date_range)

    ax = df.plot()
    ax.set_title("Random Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")

    return df, ax


import unittest
import pandas as pd
import matplotlib
import warnings


class TestCases(unittest.TestCase):
    def test_valid_input(self):
        """Tests correct DataFrame structure and plot type with valid inputs."""
        df, ax = f_824("2022-01-01", "2022-01-10", 2, seed=42)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[1], 2)
        self.assertEqual(len(df.index), 10)
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes)
        self.assertTrue((df <= 100).all().all() and (df >= 0).all().all())

    def test_seed_reproducibility(self):
        """Tests if providing a seed results in reproducible outputs."""
        df1, _ = f_824("2022-01-01", "2022-01-05", 1, seed=42)
        df2, _ = f_824("2022-01-01", "2022-01-05", 1, seed=42)
        pd.testing.assert_frame_equal(df1, df2)
        self.assertTrue((df1 <= 100).all().all() and (df1 >= 0).all().all())

    def test_negative_num_series(self):
        """Tests if function raises an error when num_series is less than 1."""
        with self.assertRaises(ValueError):
            f_824("2022-01-01", "2022-01-10", 0)

    def test_start_date_after_end_date(self):
        """Tests if function raises an error when start date is after end date."""
        with self.assertRaises(ValueError):
            f_824("2022-01-10", "2022-01-01", 1)

    def test_single_day_series(self):
        """Tests DataFrame structure and plot type when start and end dates are the same."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)
            df, ax = f_824("2022-07-01", "2022-07-01", 1, seed=42)
        self.assertEqual(len(df.index), 1)
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes)
        self.assertTrue((df <= 100).all().all() and (df >= 0).all().all())

    def test_multiple_series_names(self):
        """Tests if the generated DataFrame contains correct series names."""
        df, _ = f_824("2022-01-01", "2022-01-05", 3, seed=42)
        expected_columns = ["series_1", "series_2", "series_3"]
        self.assertListEqual(list(df.columns), expected_columns)
        self.assertTrue((df <= 100).all().all() and (df >= 0).all().all())

    def test_plot_attributes(self):
        """Tests the attributes of the plot, including title, x-label, and y-label."""
        _, ax = f_824("2022-01-01", "2022-01-05", 2, seed=42)
        self.assertEqual(ax.get_title(), "Random Time Series")
        self.assertEqual(ax.get_xlabel(), "Date")
        self.assertEqual(ax.get_ylabel(), "Value")
        self.assertTrue(len(ax.lines) == 2)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
