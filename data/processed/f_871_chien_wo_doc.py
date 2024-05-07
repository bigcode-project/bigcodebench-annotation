import subprocess
import time
import json
import platform

LOGFILE_PATH = "logfile.log"


def f_222(interval, duration):
    """
    Monitors and logs CPU usage at specified intervals over a given duration.

    Parameters:
    interval (int): The frequency, in seconds, at which CPU usage data is captured. Must be greater than zero.
    duration (int): The total duration, in seconds, for which CPU usage is monitored. Must be greater than zero.

    Returns:
    str: Path to the log file where CPU usage data is saved. Returns None if an IOError occurs during file operations.

    Raises:
    ValueError: If either 'interval' or 'duration' is less than or equal to zero.

    Requirements:
    - subprocess
    - time
    - json
    - platform

    Note: 
    Actual run time of the function may slightly exceed the specified 'duration' due to processing time and system response delay.
    The function records the CPU usage percentage at regular intervals for a specified duration.
    The data is captured every 'interval' seconds until the 'duration' is reached or exceeded.
    Each record includes a timestamp and the CPU usage percentage at that moment.
    The data is saved in JSON format in a log file named 'logfile.log'.
    The function supports different commands for CPU usage monitoring on Windows and Unix/Linux platforms.
    
    Example:
    >>> f_222(5, 60)
    'logfile.log'
    """
    if interval <= 0 or duration <= 0:
        raise ValueError("Interval and duration must be greater than zero.")
    start_time = time.time()
    try:
        with open(LOGFILE_PATH, "w", encoding="utf-8") as logfile:
            while time.time() - start_time <= duration:
                operation_start_time = time.time()
                if platform.system() == "Windows":
                    command = [
                        "typeperf",
                        "\\Processor(_Total)\\% Processor Time",
                        "-sc",
                        "1",
                    ]
                else:
                    command = ["top", "-b", "-n1"]
                output = subprocess.check_output(command)
                cpu_usage_line = (
                    output.decode("utf-8").split("\n")[2]
                    if platform.system() == "Windows"
                    else output.decode("utf-8").split("\n")[2]
                )
                cpu_usage = (
                    cpu_usage_line.split(",")[-1].strip().replace('"', "")
                    if platform.system() == "Windows"
                    else cpu_usage_line.split(":")[1].split(",")[0].strip()
                )
                log_data = {"timestamp": time.time(), "cpu_usage": cpu_usage}
                json.dump(log_data, logfile)
                logfile.write("\n")
                sleep_time = max(0, interval - (time.time() - operation_start_time))
                time.sleep(sleep_time)
    except IOError as e:
        print(f"Error writing to file {LOGFILE_PATH}: {e}")
        return None
    return LOGFILE_PATH

import unittest
import os
import json
from unittest.mock import patch
class TestCases(unittest.TestCase):
    """Test cases for f_222."""
    def setUp(self):
        """
        Setup before each test case.
        """
        self.logfile_path = "logfile.log"
    def tearDown(self):
        """
        Cleanup after each test case.
        """
        if os.path.exists(self.logfile_path):
            os.remove(self.logfile_path)
    @patch("time.time")
    def test_normal_operation(self, mock_time):
        """
        Test the normal operation of the function.
        It should create a log file with the expected content.
        """
        # Create an iterator that starts at 0 and increments by 5 every time it's called
        time_iter = iter(range(0, 100, 5))
        mock_time.side_effect = lambda: next(time_iter)
        result = f_222(5, 25)
        self.assertEqual(result, self.logfile_path)
        self.assertTrue(os.path.exists(self.logfile_path))
    def test_invalid_interval(self):
        """
        Test the function with an invalid interval value (less than or equal to zero).
        It should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            f_222(-1, 10)
    def test_invalid_duration(self):
        """
        Test the function with an invalid duration value (less than or equal to zero).
        It should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            f_222(5, -10)
    @patch("subprocess.check_output")
    @patch("time.time")
    @patch("platform.system")
    def test_subprocess_output_handling_windows(
        self, mock_platform, mock_time, mock_subprocess
    ):
        """
        Test handling of subprocess output on Windows.
        It should correctly parse the CPU usage from the subprocess output.
        """
        mock_platform.return_value = "Windows"
        mock_time.side_effect = iter(range(0, 100, 5))
        mock_output = b'"\\Processor(_Total)\\% Processor Time","5.0"\n\n"2023-04-01 12:34:56.789","5.0"\n'
        mock_subprocess.return_value = mock_output
        result = f_222(5, 10)
        self.assertEqual(result, self.logfile_path)
    @patch("subprocess.check_output")
    @patch("time.time")
    @patch("platform.system")
    def test_subprocess_output_handling_linux(
        self, mock_platform, mock_time, mock_subprocess
    ):
        """
        Test handling of subprocess output on Linux.
        It should correctly parse the CPU usage from the subprocess output.
        """
        mock_platform.return_value = "Linux"
        mock_time.side_effect = iter(range(0, 100, 5))
        mock_output = b"Linux 4.15.0-54-generic (ubuntu) \nTasks: 195 total...\n%Cpu(s):  5.0 us,  2.0 sy,  0.0 ni, 92.0 id,  0.0 wa,  0.0 hi,  1.0 si,  0.0 st\n"
        mock_subprocess.return_value = mock_output
        result = f_222(5, 10)
        self.assertEqual(result, self.logfile_path)
    @patch("builtins.open", side_effect=IOError("Mocked error"))
    def test_io_error_handling(self, mock_open):
        """
        Test the function's behavior when an IOError occurs during file operations.
        It should handle the error and return None.
        """
        result = f_222(5, 10)
        self.assertIsNone(result)
