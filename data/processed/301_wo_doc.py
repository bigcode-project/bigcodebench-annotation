import pytz
import numpy as np
from dateutil.parser import parse
import math


SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def task_func(date_str, from_tz, to_tz):
    """
    Calculate solar activity based on the date and time, taking into account the solar cycle of 11 years.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the given date and time should be converted.

    Returns:
    float: The solar activity between 0 and 1. The value represents the solar activity 
           calculated using a cosine function based on the years since the closest solar cycle year.

    Requirements:
    - pytz
    - numpy
    - dateutil.parser
    - math

    Example:
    >>> task_func('1970-01-01 00:00:00', 'UTC', 'America/New_York')
    0.14231483827328487
    >>> task_func('1990-01-01 00:00:00', 'UTC', 'America/New_York')
    0.6548607339452851
    """

    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    given_date = parse(date_str).replace(tzinfo=from_tz)
    converted_date = given_date.astimezone(to_tz)
    solar_cycle_year = SOLAR_CYCLE_YEARS[np.argmin(np.abs(SOLAR_CYCLE_YEARS - converted_date.year))]
    years_since_solar_cycle_year = abs(converted_date.year - solar_cycle_year)
    solar_activity = math.cos(math.pi * years_since_solar_cycle_year / 11)
    return solar_activity

import unittest
import math
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: Testing with a date from the first solar cycle year
        result = task_func('1986-01-01 00:00:00', 'UTC', 'America/New_York')
        expected = 0.95949
        self.assertAlmostEqual(result, expected, places=5)
        
    def test_case_2(self):
        # Input 2: Testing with a date from a year halfway between two solar cycle years
        result = task_func('1991-01-01 00:00:00', 'UTC', 'America/New_York')
        expected = 0.415415
        self.assertAlmostEqual(result, expected, places=5)
    def test_case_3(self):
        # Input 3: Testing with a date from the third solar cycle year
        result = task_func('2008-01-01 00:00:00', 'UTC', 'America/New_York')
        expected = 0.959492
        self.assertAlmostEqual(result, expected, places=5)
    def test_case_4(self):
        # Input 4: Testing with a date from a recent year
        result = task_func('2023-01-01 00:00:00', 'UTC', 'America/New_York')
        expected = 0.654860
        self.assertAlmostEqual(result, expected, places=5)
    def test_case_5(self):
        # Input 5: Testing with a date from a year close to a solar cycle year
        result = task_func('2018-01-01 00:00:00', 'UTC', 'America/New_York')
        expected = 0.841253
        self.assertAlmostEqual(result, expected, places=5)
