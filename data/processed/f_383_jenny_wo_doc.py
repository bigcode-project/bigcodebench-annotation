from datetime import datetime, timedelta
import pytz
import numpy as np
import matplotlib.pyplot as plt


def f_348(start_time, end_time):
    """
    Plots the hourly difference between UTC and specified global time zones across a date range.

    This function visualizes the time difference in hours between UTC and predefined time zones for each day
    within the specified date range. Predefined time zones include UTC, America/Los_Angeles, Europe/Paris,
    Asia/Kolkata, and Australia/Sydney. The differences are plotted on a graph, using a distinct color for
    each time zone's time difference curve, selecting from ["b", "g", "r", "c", "m", "y", "k"].

    Parameters:
    - start_time (str): The start date in the format "yyyy-mm-dd".
    - end_time (str): The end date in the format "yyyy-mm-dd".

    Returns:
    - matplotlib.axes.Axes: The Axes object with the plotted time differences in hours between UTC and 
                            other time zones.

    Requirements:
    - datetime.datetime
    - datetime.timedelta
    - pytz
    - numpy
    - matplotlib.pyplot

    Example:
    >>> ax = f_348('2021-01-01', '2021-01-10')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(18628.0, 0, '2021-01-01'), Text(18629.0, 0, '2021-01-02'), Text(18630.0, 0, '2021-01-03'), Text(18631.0, 0, '2021-01-04'), Text(18632.0, 0, '2021-01-05'), Text(18633.0, 0, '2021-01-06'), Text(18634.0, 0, '2021-01-07'), Text(18635.0, 0, '2021-01-08'), Text(18636.0, 0, '2021-01-09')]
    """
    TIMEZONES = [
        "UTC",
        "America/Los_Angeles",
        "Europe/Paris",
        "Asia/Kolkata",
        "Australia/Sydney",
    ]
    COLORS = ["b", "g", "r", "c", "m", "y", "k"]
    start_date = datetime.strptime(start_time, "%Y-%m-%d")
    end_date = datetime.strptime(end_time, "%Y-%m-%d")
    current_tz = pytz.timezone("UTC")
    dates = np.arange(start_date, end_date, timedelta(days=1)).astype(datetime)
    differences = []
    for tz in TIMEZONES:
        other_tz = pytz.timezone(tz)
        difference = [
            (other_tz.localize(dt) - current_tz.localize(dt)).total_seconds() / 3600
            for dt in dates
        ]
        differences.append(difference)
    fig, ax = plt.subplots()
    for i, difference in enumerate(differences):
        ax.plot(dates, difference, color=COLORS[i % len(COLORS)], label=TIMEZONES[i])
    ax.set_xlabel("Date")
    ax.set_ylabel("Time difference (hours)")
    ax.legend()
    return ax

import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic functionality
        ax = f_348("2021-01-01", "2021-01-10")
        self._common_assertions(ax)
    def test_case_2(self):
        # Test single day range
        ax = f_348("2021-01-01", "2021-01-01")
        self._common_assertions(ax)
    def test_case_3(self):
        # Test leap year
        ax = f_348("2020-02-28", "2020-03-01")
        self._common_assertions(ax)
    def test_case_4(self):
        # Test DST transition
        ax = f_348("2021-03-27", "2021-03-29")
        self._common_assertions(ax)
    def test_case_5(self):
        # Test plotting consistency
        ax = f_348("2021-01-01", "2021-01-10")
        colors = [line.get_color() for line in ax.get_lines()]
        self.assertEqual(len(set(colors)), len(colors))  # Check if colors are unique
    def test_case_6(self):
        # Testing input validation via invalid date format
        with self.assertRaises(ValueError):
            f_348("01-01-2021", "10-01-2021")
    def _common_assertions(self, ax):
        """Common assertions for all test cases"""
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_xlabel(), "Date")
        self.assertEqual(ax.get_ylabel().lower(), "time difference (hours)".lower())
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        expected_timezones = [
            "UTC",
            "America/Los_Angeles",
            "Europe/Paris",
            "Asia/Kolkata",
            "Australia/Sydney",
        ]
        self.assertListEqual(legend_labels, expected_timezones)
    def tearDown(self):
        plt.close("all")
