from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def f_955(timestamp, tz):
    """
    Converts the Unix timestamp to a formatted string "% Y-% m-% d% H:% M:% S" in a specific time zone.
    
    Parameters:
    timestamp (int): The Unix timestamp.
    tz (str): The timezone.
    
    Returns:
    str: The timestamp in the format '%Y-%m-%d %H:%M:%S' in the given timezone.
    
    Requirements:
    - datetime
    - pytz
    
    Example:
    >>> f_955(1347517370, 'America/New_York')
    "2012-09-13 04:22:50"
    """
    dt = datetime.fromtimestamp(timestamp, pytz.timezone(tz))
    
    return dt.strftime(DATE_FORMAT)

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_955(1347517370, 'America/New_York')
        self.assertEqual(result, "2012-09-13 04:22:50")

    def test_case_2(self):
        result = f_955(0, 'UTC')
        self.assertEqual(result, "1970-01-01 00:00:00")

    def test_case_3(self):
        result = f_955(1609459200, 'Asia/Tokyo')
        self.assertEqual(result, "2021-01-01 09:00:00")

    def test_case_4(self):
        result = f_955(0, 'Asia/Kolkata')
        self.assertEqual(result, "1970-01-01 05:30:00")

    def test_case_5(self):
        result = f_955(1672531199, 'Australia/Sydney')
        self.assertEqual(result, "2023-01-01 11:59:59")
if __name__ == "__main__":
    run_tests()