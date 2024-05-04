import pytz
from dateutil.parser import parse

# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"


def f_98(time_string, from_tz, to_tz):
    """
    Converts a time string from one timezone to another, considering various cases such as daylight saving time.

    Parameters:
    - time_string (str): A time string in the format 'dd/mm/yy HH:MM:SS.fff'. This string should represent a valid date and time.
    - from_tz (str): The timezone of the given time string. The timezone should be a valid IANA timezone name (e.g., 'UTC', 'America/New_York').
    - to_tz (str): The target timezone to which the time string should be converted. This should also be a valid IANA timezone name (e.g., 'Asia/Tokyo').

    Returns:
    - str: The converted time string in the format 'dd/mm/yy HH:MM:SS.fff'. The conversion takes into account any differences in daylight saving rules between the source and target timezones.

    Requirements:
    - pytz
    - dateutil

    Example:
    >>> f_98('30/03/09 16:31:32.123', 'UTC', 'America/New_York')
    '30/03/09 12:31:32.123000'

    Note: The example assumes no daylight saving time shift between the given timezones at the specified date and time.
    """
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    dt = parse(time_string, dayfirst=True)
    dt = from_zone.localize(dt)
    dt = dt.astimezone(to_zone)
    return dt.strftime(TIME_FORMAT)

import unittest
class TestCases(unittest.TestCase):
    """Test cases for f_98"""
    def test_utc_to_est(self):
        """
        Test conversion from UTC to Eastern Standard Time.
        """
        result = f_98("30/03/09 16:31:32.123", "UTC", "America/New_York")
        expected = "30/03/09 12:31:32.123000"  # Adjusted for daylight saving time if applicable
        self.assertEqual(result, expected)
    def test_est_to_utc(self):
        """
        Test conversion from Eastern Standard Time to UTC.
        """
        result = f_98("30/03/09 12:31:32.123", "America/New_York", "UTC")
        expected = "30/03/09 16:31:32.123000"  # Adjusted for daylight saving time if applicable
        self.assertEqual(result, expected)
    def test_utc_to_ist(self):
        """
        Test conversion from UTC to Indian Standard Time.
        """
        result = f_98("01/04/09 00:00:00.000", "UTC", "Asia/Kolkata")
        expected = "01/04/09 05:30:00.000000"  # IST is UTC+5:30
        self.assertEqual(result, expected)
    def test_ist_to_utc(self):
        """
        Test conversion from Indian Standard Time to UTC.
        """
        result = f_98("01/04/09 05:30:00.000", "Asia/Kolkata", "UTC")
        expected = "01/04/09 00:00:00.000000"  # IST is UTC+5:30
        self.assertEqual(result, expected)
    def test_utc_to_gmt(self):
        """
        Test conversion from UTC to GMT (should be the same).
        """
        result = f_98("15/04/09 10:30:00.000", "UTC", "GMT")
        expected = "15/04/09 10:30:00.000000"  # GMT and UTC are the same
        self.assertEqual(result, expected)
