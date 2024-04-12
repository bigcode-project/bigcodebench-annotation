import re
import datetime
import time

def f_671(logfile, duration=60):
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
    >>> f_671('/path/to/access.log', 5)
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

class TestF33(unittest.TestCase):

    def test_zero_errors(self):
        self.assertEqual(f_671('/path/to/f_671_data_xiaoheng/mock_log_0.log'), 0)

    def test_some_errors(self):
        result = f_671('/path/to/f_671_data_xiaoheng/mock_log_1.log')
        self.assertTrue(result > 0 and result < 100)

    def test_all_errors(self):
        result = f_671('/path/to/f_671_data_xiaoheng/mock_log_2.log')
        self.assertTrue(result == 100)

    def test_empty_file(self):
        self.assertEqual(f_671('/path/to/f_671_data_xiaoheng/empty.log'), 0)

    def test_file_not_present(self):
        with self.assertRaises(FileNotFoundError):
            f_671('/path/to/non_existent.log')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestF33))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()