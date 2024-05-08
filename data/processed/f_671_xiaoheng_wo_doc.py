import re
import datetime
import time

def f_660(logfile, duration=60):
    """
    Monitor the access log file of an HTTP server and count the number of 500 errors in a given duration.
    
    Parameters:
    - logfile (str): The path to the access log file.
    - duration (int, optional): Duration in seconds for monitoring the log file. Defaults to 60 seconds.
    
    Returns:
    - error_count (int): The number of 500 errors.
    
    Requirements:
    - re
    - datetime
    - time
    
    Example:
    >>> f_660('/path/to/access.log', 5)
    3

    Note: 
    - This function will return the number of 500 errors within the specified monitoring duration.
    """
    start_time = datetime.datetime.now()
    error_count = 0
    last_line_read = 0
    while True:
        with open(logfile, 'r') as f:
            lines = f.readlines()[last_line_read:]
            last_line_read += len(lines)
        for line in lines:
            if re.search(r' 500 ', line):
                error_count += 1
        if (datetime.datetime.now() - start_time).seconds >= duration:
            break
        time.sleep(1)
    return error_count

import unittest
from unittest.mock import mock_open, patch
import re
import datetime
# Assuming your original f_660 function here
class TestCases(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='error 500 occurred\nok\nerror 500 occurred')
    def test_some_errors(self, mock_file):
        # Test where there are some 500 errors in the log
        result = f_660('mock_log.log')
        self.assertEqual(result, 2)
    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_empty_file(self, mock_file):
        # Test with an empty log file
        result = f_660('empty.log')
        self.assertEqual(result, 0)
    @patch('builtins.open', new_callable=mock_open, read_data='error 500 occurred\n' * 100)
    def test_all_errors(self, mock_file):
        # Test where all lines are 500 errors
        result = f_660('all_errors.log')
        self.assertEqual(result, 100)
    @patch('os.path.exists')
    def test_file_not_present(self, mock_exists):
        # Simulate file not existing
        mock_exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            f_660('non_existent.log')
    @patch('builtins.open', new_callable=mock_open, read_data='error 500 occurred')
    def test_single_error(self, mock_file):
        # Test with a single error
        result = f_660('single_error.log')
        self.assertEqual(result, 1)
