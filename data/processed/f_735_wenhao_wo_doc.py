import re
from datetime import time

def f_735(logs: list):
    """
    Analyze the given list of logs for the occurrence of errors and calculate the average time of occurrence of errors.
    
    Parameters:
    - logs (list): A list of log strings.
    
    Returns:
    - list: A list of times when errors occurred.
    - time: The average time of occurrence of these errors.
    
    Requirements:
    - re
    - datetime
    
    Example:
    >>> f_735(['2021-06-15 09:45:00 ERROR: Failed to connect to database',\
            '2021-06-15 10:15:00 WARNING: Low disk space',\
            '2021-06-15 10:35:00 INFO: Backup completed successfully'])
    ([datetime.time(9, 45)], datetime.time(9, 45))
    """
    
    error_times = []
    total_time = 0

    for log in logs:
        if "ERROR" in log:
            time_match = re.search(r'(\d{2}):(\d{2}):\d{2}', log)
            if time_match:
                hour, minute = map(int, time_match.groups())
                error_times.append(time(hour, minute))
                total_time += hour * 60 + minute

    if error_times:
        avg_hour = (total_time // len(error_times)) // 60
        avg_minute = (total_time // len(error_times)) % 60
        avg_time = time(avg_hour, avg_minute)
    else:
        avg_time = time(0, 0)

    return error_times, avg_time

import unittest
from datetime import time
class TestCases(unittest.TestCase):
    def test_case_1(self):
        logs = ['2021-06-15 09:45:00 ERROR: Failed to connect to database',
                '2021-06-15 10:15:00 WARNING: Low disk space',
                '2021-06-15 10:35:00 INFO: Backup completed successfully']
        result = f_735(logs)
        self.assertEqual(result, ([time(9, 45)], time(9, 45)))
    def test_case_2(self):
        logs = ['2021-06-15 08:45:00 ERROR: Failed to authenticate',
                '2021-06-15 09:15:00 ERROR: Failed to connect to database',
                '2021-06-15 10:35:00 INFO: Backup completed successfully']
        result = f_735(logs)
        self.assertEqual(result, ([time(8, 45), time(9, 15)], time(9, 0)))
    def test_case_3(self):
        logs = ['2021-06-15 07:45:00 INFO: Backup started',
                '2021-06-15 08:15:00 WARNING: Low memory',
                '2021-06-15 09:35:00 INFO: Backup completed successfully']
        result = f_735(logs)
        self.assertEqual(result, ([], time(0, 0)))
    def test_case_4(self):
        logs = []
        result = f_735(logs)
        self.assertEqual(result, ([], time(0, 0)))
    def test_case_5(self):
        logs = ['2021-06-15 09:45:00 ERROR: Failed to connect to database',
                '2021-06-15 10:15:00 WARNING: Low disk space',
                '2021-06-15 11:45:00 ERROR: Failed to authenticate']
        result = f_735(logs)
        self.assertEqual(result, ([time(9, 45), time(11, 45)], time(10, 45)))
    def test_case_invalid_format(self):
        logs = ['Invalid log format',
                'Another invalid log format',
                'Yet another invalid log format']
        result = f_735(logs)
        self.assertEqual(result, ([], time(0, 0)))
