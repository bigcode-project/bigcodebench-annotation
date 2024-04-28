import json
from datetime import datetime

def f_522(json_data):
    """
    Determine if the given datetime is a weekend.

    Parameters:
    - json_data (str): JSON string containing the datetime in UTC format.

    Returns:
    bool: True if the date is a weekend (Saturday or Sunday), False otherwise.

    Note:
    - The datetime to be extracted is located in the 'utc_datetime' key in the JSON data.

    Requirements:
    - json
    - datetime

    Example:
    >>> json_data = '{"utc_datetime": "2024-04-19T12:00:00"}'
    >>> f_522(json_data)
    False
    """
    try:
        # Convert JSON string to Python dictionary
        data = json.loads(json_data)

        # Extract datetime string from dictionary
        datetime_str = data['utc_datetime']

        # Convert datetime string to datetime object
        utc_datetime = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')

        # Check if the day of the week is Saturday (5) or Sunday (6)
        return utc_datetime.weekday() >= 5
    except Exception as e:
        raise e

import unittest
from datetime import datetime
import json
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Create a datetime object for a weekday (Monday)
        utc_datetime = datetime(2024, 4, 15, 12, 0, 0)  # Monday, April 15, 2024
        json_data = json.dumps({'utc_datetime': utc_datetime.isoformat()})
        result = f_522(json_data)
        self.assertFalse(result)  # Monday is not a weekend)
    def test_saturday(self):
        # Create a datetime object for a Saturday
        utc_datetime = datetime(2024, 4, 13, 12, 0, 0)  # Saturday, April 13, 2024
        json_data = json.dumps({'utc_datetime': utc_datetime.isoformat()})
        result = f_522(json_data)
        self.assertTrue(result)  # Saturday is a weekend day
    def test_sunday(self):
        # Create a datetime object for a Sunday
        utc_datetime = datetime(2024, 4, 14, 12, 0, 0)  # Sunday, April 14, 2024
        json_data = json.dumps({'utc_datetime': utc_datetime.isoformat()})
        result = f_522(json_data)
        self.assertTrue(result)  # Sunday is a weekend day
    def test_empty_json(self):
        # Test with empty JSON input
        json_data = json.dumps({})
        with self.assertRaises(KeyError):
            f_522(json_data)
    def test_no_utc_datetime(self):
        # Test with JSON input missing 'utc_datetime' key
        json_data = json.dumps({'date': '2024-04-14T12:00:00'})
        with self.assertRaises(KeyError):
            f_522(json_data)
