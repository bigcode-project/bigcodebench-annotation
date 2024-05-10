from datetime import datetime
import numpy as np
from dateutil.parser import parse

LEAP_SECONDS = np.array(
    [
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1985,
        1988,
        1990,
        1993,
        1994,
        1997,
        1999,
        2006,
        2009,
        2012,
        2015,
        2016,
        2020,
    ]
)


def f_889(date_str):
    """
    Calculate the total number of seconds elapsed from a given date until the current time,
    including any leap seconds that occurred in this period.

    Parameters:
    date_str (str): The date and time from which to calculate, in "yyyy-mm-dd hh:mm:ss" format.

    Returns:
    int: The total number of elapsed seconds, including leap seconds, since the given date.

    Requirements:
    - datetime.datetime
    - numpy
    - dateutil.parser.parse
    
    Note:
    This function uses the datetime, numpy, and dateutil.parser modules.
    The LEAP_SECONDS array should contain years when leap seconds were added.

    Example:
    >>> total_seconds = f_889('1970-01-01 00:00:00')
    >>> print(total_seconds)
    1702597276
    """
    given_date = parse(date_str)
    current_date = datetime.now()

    total_seconds = (current_date - given_date).total_seconds()

    # Count leap seconds that occurred between the two dates
    leap_seconds = np.sum(LEAP_SECONDS >= given_date.year)

    total_seconds += leap_seconds

    return int(total_seconds)


import unittest
from datetime import datetime, timedelta
import numpy as np


class TestCases(unittest.TestCase):
    """Test cases for the function f_889."""

    def test_recent_date(self):
        """
        Test the function with a recent date.
        """
        test_date = "2022-01-01 00:00:00"
        expected_result = (datetime.now() - datetime(2022, 1, 1)).total_seconds()
        expected_result += np.sum(LEAP_SECONDS >= 2022)
        self.assertEqual(f_889(test_date), int(expected_result))

    def test_date_before_leap_seconds(self):
        """
        Test the function with a date before the introduction of leap seconds.
        """
        test_date = "1960-01-01 00:00:00"
        expected_result = (datetime.now() - datetime(1960, 1, 1)).total_seconds()
        expected_result += np.sum(LEAP_SECONDS >= 1960)
        self.assertEqual(f_889(test_date), int(expected_result))

    def test_date_with_leap_second(self):
        """
        Test the function with a date in a year when a leap second was added.
        """
        test_date = "2016-01-01 00:00:00"
        expected_result = (datetime.now() - datetime(2016, 1, 1)).total_seconds()
        expected_result += np.sum(LEAP_SECONDS >= 2016)
        self.assertAlmostEqual(f_889(test_date), int(expected_result), delta=1)


    def test_future_date(self):
        """
        Test the function with a future date.
        """
        future_date = datetime.now() + timedelta(days=30)
        future_date_str = future_date.strftime("%Y-%m-%d %H:%M:%S")
        result = f_889(future_date_str)
        expected_result = -30 * 24 * 3600  # Negative seconds for future dates

        # Allowing a margin of error of 1 second
        self.assertTrue(abs(result - expected_result) <= 1)

    def test_current_date(self):
        """
        Test the function with the current date and time.
        """
        current_date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(f_889(current_date_str), 0)


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
