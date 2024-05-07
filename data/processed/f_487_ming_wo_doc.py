from random import choice
import pytz
from dateutil.parser import parse

# Constants
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']


def f_505(date_str, from_tz):
    """
    Converts a datetime string from a given timezone to a datetime string in a randomly chosen timezone.

    Parameters:
    - date_str (str): The datetime string in "yyyy-mm-dd hh:mm:ss" format.
    - from_tz (str): The timezone of the given datetime string.

    Returns:
    - tuple: A tuple containing the converted datetime string and the randomly chosen timezone.
    
    Requirements:
    - pytz
    - dateutil.parser
    - random

    Example:
    >>> date_str, from_tz = '2023-06-15 12:00:00', 'UTC'
    >>> converted_date, to_tz = f_505(date_str, from_tz)
    >>> to_tz in TIMEZONES
    True
    """
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(choice(TIMEZONES))
    given_date = parse(date_str).replace(tzinfo=from_tz)
    converted_date = given_date.astimezone(to_tz)
    return converted_date.strftime('%Y-%m-%d %H:%M:%S'), to_tz.zone

import unittest
from datetime import datetime
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_505('2023-06-15 12:00:00', 'UTC')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
    
    def test_case_2(self):
        result = f_505('2022-01-01 00:00:00', 'America/New_York')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
        
    def test_case_3(self):
        result = f_505('2020-12-31 23:59:59', 'Asia/Shanghai')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
        
    def test_case_4(self):
        result = f_505('2019-07-04 04:04:04', 'Europe/London')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
    
    def test_case_5(self):
        result = f_505('2018-02-28 14:28:58', 'Australia/Sydney')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
