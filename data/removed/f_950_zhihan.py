import subprocess
import os
import re
import sys

# Constants
R_SCRIPT_PATH = '/usr/bin/Rscript --vanilla /pathto/MyrScript.r'

def f_950():
    """
    Run an R script (specified by the constant R_SCRIPT_PATH) and check the log. 
    If there is an error message, return the error message, otherwise return "No error".
    
    Returns:
    str: The error message in the log in the format "Error: <message>" or "No error".
    
    Requirements:
    - subprocess
    - os
    - re
    - sys
    - The R script must be located at the path specified by R_SCRIPT_PATH.
    
    Example:
    >>> f_950()
    "Error: <specific error message>"
    or
    >>> f_950()
    "No error"
    """
    log_file = '/tmp/log.txt'
    command = R_SCRIPT_PATH + ' > ' + log_file
    subprocess.call(command, shell=True)

    with open(log_file, 'r') as f:
        log_content = f.read()

    error_message = re.search('Error: (.*)', log_content)
    if error_message:
        return "Error: " + error_message.group(1)
    else:
        return "No error"

import unittest

# Mock data for log files
mock_logs = [
    "Execution started...
Error: Sample error message 1
Execution completed.",
    "Execution started...
Error: Sample error message 2
Execution completed.",
    "Execution started...
Execution completed.",
    "Execution started...
Error: Sample error message 3
Execution completed.",
    "Execution started...
Execution completed."
]

def mock_r_script(log_content, log_file_path):
    with open(log_file_path, 'w') as file:
        file.write(log_content)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        mock_r_script(mock_logs[0], '/tmp/log.txt')
        result = f_950()
        self.assertEqual(result, "Error: Sample error message 1")

    def test_case_2(self):
        mock_r_script(mock_logs[1], '/tmp/log.txt')
        result = f_950()
        self.assertEqual(result, "Error: Sample error message 2")

    def test_case_3(self):
        mock_r_script(mock_logs[2], '/tmp/log.txt')
        result = f_950()
        self.assertEqual(result, "No error")

    def test_case_4(self):
        mock_r_script(mock_logs[3], '/tmp/log.txt')
        result = f_950()
        self.assertEqual(result, "Error: Sample error message 3")

    def test_case_5(self):
        mock_r_script(mock_logs[4], '/tmp/log.txt')
        result = f_950()
        self.assertEqual(result, "No error")

if __name__ == "__main__":
    run_tests()