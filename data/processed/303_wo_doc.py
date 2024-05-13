import pytz
import numpy as np
from dateutil.parser import parse
import math


MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def task_func(date_str, from_tz, to_tz):
    """
    Calculate the moon phase by the date and time taking into account the lunar phase cycle of 7 years. The 
    function uses a constant array `MOON_PHASES_YEARS` to determine the reference years for the moon phases.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the given date and time should be converted.

    Returns:
    float: The moon phase between 0 and 1. A value of 0 indicates a new moon and a value of 1 indicates a full moon.

    Requirements:
    - pytz
    - numpy
    - dateutil.parser
    - math

    Example:
    >>> task_func('1970-01-01 00:00:00', 'UTC', 'America/New_York')
    0.9749279121818237
    """

    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    given_date = parse(date_str).replace(tzinfo=from_tz)
    converted_date = given_date.astimezone(to_tz)
    moon_phase_year = MOON_PHASES_YEARS[np.argmin(np.abs(MOON_PHASES_YEARS - converted_date.year))]
    years_since_moon_phase_year = abs(converted_date.year - moon_phase_year)
    moon_phase = math.sin(math.pi * years_since_moon_phase_year / 7)
    return moon_phase

import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Given a date in the past, in UTC timezone, convert to America/New_York timezone
        result = task_func('1970-01-01 00:00:00', 'UTC', 'America/New_York')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1
    
    def test_case_2(self):
        # Given a date in the future, in Asia/Kolkata timezone, convert to Europe/London timezone
        result = task_func('2050-12-31 23:59:59', 'Asia/Kolkata', 'Europe/London')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1
    def test_case_3(self):
        # Given a date close to a reference year in MOON_PHASES_YEARS, in UTC timezone, convert to America/New_York timezone
        result = task_func('2016-06-15 12:00:00', 'UTC', 'America/New_York')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1
    
    def test_case_4(self):
        # Given a date far from any reference year in MOON_PHASES_YEARS, in America/Los_Angeles timezone, convert to Asia/Tokyo timezone
        result = task_func('2110-03-10 08:30:00', 'America/Los_Angeles', 'Asia/Tokyo')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1
    
    def test_case_5(self):
        # Given a date with a different date format, in UTC timezone, convert to America/New_York timezone
        result = task_func('01 Jan 1990 01:01:01', 'UTC', 'America/New_York')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1
