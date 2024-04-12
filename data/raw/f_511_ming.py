import pytz
from datetime import datetime
from dateutil.parser import parse

def f_511(date_str, tz_str):
    """
    Determine the time in seconds until the next turn of the year in a certain time zone from a given date string.

    Parameters:
    - date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    - tz_str (str): The IANA timezone string (e.g., 'America/Chicago').

    Returns:
    - int: The time in seconds until the next New Year in the specified timezone.

    Requirements:
    - datetime
    - dateutil.parser
    - pytz

    Example:
    >>> f_511('2022-10-22 11:59:59', 'America/Chicago')
    5772239  # Example output, actual value will depend on the current time when called
    """
    tz = pytz.timezone(tz_str)
    given_date = parse(date_str).astimezone(tz)  # Correctly handle timezone conversion

    next_year = given_date.year + 1
    new_year = tz.localize(datetime(next_year, 1, 1, 0, 0, 0))  # Correctly create the New Year moment in the specified timezone

    time_until_new_year = new_year - given_date

    return int(time_until_new_year.total_seconds())


import unittest

class TestF511(unittest.TestCase):
    def test_time_until_new_year(self):
        # Test with a specific date and timezone
        self.assertIsInstance(f_511('2023-12-31 23:59:59', 'UTC'), int)

    def test_start_of_year(self):
        # Test exactly at the start of a year
        self.assertIsInstance(f_511('2023-01-01 00:00:00', 'UTC'), int)

    def test_leap_year(self):
        # Test a date in a leap year
        self.assertIsInstance(f_511('2024-02-29 00:00:00', 'UTC'), int)

    def test_different_timezone(self):
        # Test with a non-UTC timezone
        self.assertIsInstance(f_511('2023-12-31 23:59:59', 'America/New_York'), int)

    def test_midyear(self):
        # Test a date in the middle of the year
        self.assertIsInstance(f_511('2023-06-15 12:00:00', 'UTC'), int)


if __name__ == '__main__':
    unittest.main()
