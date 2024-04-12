from datetime import datetime
import pytz
from dateutil import parser

def f_442(date_str, from_tz, to_tz):
    """
    Converts a date time from one timezone to another.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the date should be converted.

    Returns:
    str: The converted datetime string in "yyyy-mm-dd hh:mm:ss" format.

    Requirements:
    - datetime
    - pytz
    - dateutil.parser

    Example:
    >>> f_442('2022-03-01 12:00:00', 'UTC', 'America/New_York')
    '2022-03-01 07:00:00'
    """
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    date = parser.parse(date_str).replace(tzinfo=from_tz)
    date = date.astimezone(to_tz)

    return date.strftime('%Y-%m-%d %H:%M:%S')


import unittest

class TestF442(unittest.TestCase):
    def test_utc_to_new_york(self):
        """Test conversion from UTC to America/New_York timezone."""
        result = f_442('2022-03-01 12:00:00', 'UTC', 'America/New_York')
        self.assertEqual(result, '2022-03-01 07:00:00')

    def test_utc_to_los_angeles_summer_time(self):
        """Test conversion from UTC to America/Los_Angeles with daylight saving."""
        result = f_442('2022-06-01 12:00:00', 'UTC', 'America/Los_Angeles')
        self.assertEqual(result, '2022-06-01 05:00:00')

    def test_invalid_date_format(self):
        """Test handling of invalid date format."""
        with self.assertRaises(ValueError):
            f_442('invalid-date', 'UTC', 'America/New_York')

    def test_same_timezone_conversion(self):
        """Test conversion where from_tz and to_tz are the same."""
        result = f_442('2022-03-01 12:00:00', 'UTC', 'UTC')
        self.assertEqual(result, '2022-03-01 12:00:00')

    def test_utc_to_london_summer_time(self):
        """Test conversion from UTC to Europe/London during summer (BST)."""
        result = f_442('2022-06-01 12:00:00', 'UTC', 'Europe/London')
        self.assertEqual(result, '2022-06-01 13:00:00')


if __name__ == '__main__':
    unittest.main()
