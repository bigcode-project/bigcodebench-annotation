from datetime import datetime, timedelta
import pytz
import calendar


def f_394(days_in_past=7):
    """
    Get the weekday of the date 'days_in_past' days ago from today.

    This function computes the date that is 'days_in_past' number of days ago from the current
    system time's date in UTC. It then determines the weekday of this target date using calendar
    and returns its name as a string.

    Parameters:
    days_in_past (int): The number of days to go back from the current date to find the weekday.
                        Defaults to 7 (one week ago). Must be a non-negative integer.

    Returns:
    weekday (str)     : The name of the weekday (e.g., 'Monday', 'Tuesday') for the computed date.

    Requirements:
    - datetime.datetime
    - datetime.timedelta
    - pytz
    - calendar

    Example:
    >>> f_394()
    'Monday'
    >>> f_394(3)
    'Friday'
    """
    if days_in_past < 0:
        raise ValueError("Days in the past cannot be negative")

    date = datetime.now(pytz.UTC) - timedelta(days=days_in_past)
    weekday = calendar.day_name[date.weekday()]

    return weekday

import unittest
from datetime import datetime, timedelta
import pytz
import calendar
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: Default input
        result = f_394()
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for 7 days ago
        expected_date = datetime.now(pytz.UTC) - timedelta(days=7)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_2(self):
        # Input 2: Test with 3 days in the past
        result = f_394(3)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for 3 days ago
        expected_date = datetime.now(pytz.UTC) - timedelta(days=3)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_3(self):
        # Input 3: Test with 0 days in the past (today)
        result = f_394(0)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for today
        expected_date = datetime.now(pytz.UTC)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_4(self):
        # Input 4: Test with 30 days in the past (approximately a month ago)
        result = f_394(30)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for 30 days ago
        expected_date = datetime.now(pytz.UTC) - timedelta(days=30)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_5(self):
        # Input 5: Test handling invalid days_in_the_past
        for invalid in [-1, "1"]:
            with self.assertRaises(Exception):
                f_394(invalid)
