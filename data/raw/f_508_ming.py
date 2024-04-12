import pytz
from datetime import datetime
from dateutil.parser import parse

def f_508(date_str, from_tz, to_tz):
    """
    Convert a date string from one time zone to another and return the time difference in seconds to the current time in the destination time zone.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the date string should be converted.

    Returns:
    int: The time difference in seconds.

    Requirements:
    - datetime
    - pytz
    - dateutil.parser
    Example:
    >>> f_508('2022-10-22 11:59:59', 'UTC', 'America/Chicago')
    <some_integer_output>
    """
    # Get timezone objects for the source and destination timezones
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)

    # Parse the given date string and localize it to the source timezone
    given_date_naive = parse(date_str)
    given_date = from_tz_obj.localize(given_date_naive)

    # Convert the given date to the destination timezone
    given_date_in_to_tz = given_date.astimezone(to_tz_obj)

    # Get the current time in the destination timezone
    current_date_in_to_tz = datetime.now(pytz.utc).astimezone(to_tz_obj)

    # Calculate the time difference in seconds
    time_difference = current_date_in_to_tz - given_date_in_to_tz

    return int(time_difference.total_seconds())

import unittest
from datetime import datetime, timedelta

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test conversion from UTC to America/Chicago with a date in the past
        result = f_508('2022-01-01 11:59:59', 'UTC', 'America/Chicago')
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

    def test_case_2(self):
        # Test conversion from America/New_York to Asia/Kolkata with a date in the past
        result = f_508('2022-01-01 11:59:59', 'America/New_York', 'Asia/Kolkata')
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

    def test_known_time_zone_offset_difference(self):
        """Test the function with time zones having a known, static offset."""
        # Assuming we're using 'Etc/GMT+2' which is 2 hours behind UTC (in sign notation, it's ahead, but physically it's behind UTC).
        # The actual offset in seconds should be -7200 seconds (2 hours * 60 minutes * 60 seconds).
        # This test will not directly test against "current" time but demonstrates handling of static offsets.
        known_date_utc = '2023-01-01 12:00:00'
        utc_zone = 'UTC'
        target_zone = 'Etc/GMT+2'
        # f_508 should correctly handle the conversion; however, we can't directly test the "current" time difference.
        # Instead, we verify the function executes without errors for this scenario.
        # This is a limitation without controlling "now" in the test environment.
        try:
            result = f_508(known_date_utc, utc_zone, target_zone)
            self.assertTrue(isinstance(result, int), "Result should be an integer representing seconds.")
        except Exception as e:
            self.fail(f"f_508 raised an exception with known static offset time zones: {e}")

    def test_case_4(self):
        # Test conversion with a future date from UTC to America/Chicago
        future_date = (datetime.utcnow() + timedelta(days=10)).strftime('%Y-%m-%d %H:%M:%S')
        result = f_508(future_date, 'UTC', 'America/Chicago')
        self.assertIsInstance(result, int)
        self.assertLess(result, 0)

    def test_case_5(self):
        # Test conversion from Asia/Kolkata to America/Los_Angeles with a date in the past
        result = f_508('2022-01-01 11:59:59', 'Asia/Kolkata', 'America/Los_Angeles')
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()