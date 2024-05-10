import subprocess
import os
import signal
import time


def f_299(process_name: str) -> int:
    """
    Stops all running processes with a specific name.

    Parameters:
    process_name (str): The name of the processes to be stopped.

    Returns:
    int: The number of processes stopped. If no processes are found, returns 0.

    Requirements:
    - subprocess
    - os
    - signal
    - time

    Note:
    - The function sends a termination signal to the processes and waits for 1 second. 
      There is no guarantee that all processes will have terminated within this time.

    Example:
    >>> pids = f_299('test_name') # Dummy example, should return 0
    >>> pids
    0
    """
    # Find all processes with the given name, and get their PIDs
    try:
        pids = subprocess.check_output(['pgrep', '-f', process_name]).decode().split('\n')[:-1] 
    except subprocess.CalledProcessError:
        pids = []

    # Send SIGTERM signal to each process
    for pid in pids:
        os.kill(int(pid), signal.SIGTERM)

    # Wait for processes to stop
    time.sleep(1)

    return len(pids)


import unittest
from unittest.mock import patch
import doctest


class TestCases(unittest.TestCase):

    @patch('subprocess.check_output')
    @patch('os.kill')
    def test_case_1(self, mock_os_kill, mock_subprocess_check_output):
        # Mock the subprocess output to simulate 3 processes with the name 'python'
        mock_subprocess_check_output.return_value = b'1234\n5678\n91011\n'
        
        result = f_299('python')
        self.assertEqual(result, 3)

    @patch('subprocess.check_output')
    @patch('os.kill')
    def test_case_2(self, mock_os_kill, mock_subprocess_check_output):
        # Mock the subprocess output to simulate no processes with the name 'java'
        mock_subprocess_check_output.return_value = b''
        
        result = f_299('java')
        self.assertEqual(result, 0)

    @patch('subprocess.check_output')
    @patch('os.kill')
    def test_case_3(self, mock_os_kill, mock_subprocess_check_output):
        # Mock the subprocess output to simulate 2 processes with the name 'node'
        mock_subprocess_check_output.return_value = b'1234\n5678\n'
        
        result = f_299('node')
        self.assertEqual(result, 2)

    @patch('subprocess.check_output')
    @patch('os.kill')
    def test_case_4(self, mock_os_kill, mock_subprocess_check_output):
        # Mock the subprocess output to simulate 1 process with the name 'ruby'
        mock_subprocess_check_output.return_value = b'1234\n'
        
        result = f_299('ruby')
        self.assertEqual(result, 1)

    @patch('subprocess.check_output')
    @patch('os.kill')
    def test_case_5(self, mock_os_kill, mock_subprocess_check_output):
        # Mock the subprocess output to simulate 4 processes with the name 'go'
        mock_subprocess_check_output.return_value = b'1234\n5678\n91011\n1213\n'
        
        result = f_299('go')
        self.assertEqual(result, 4)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
