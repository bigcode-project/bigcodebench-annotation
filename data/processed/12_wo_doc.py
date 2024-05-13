import subprocess
import os
import json
from datetime import datetime


def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    """
    Runs the provided backup shell script and logs the start time, end time, and exit status 
    in a specified JSON log file.
    
    Parameters:
    - script_name (str): The name of the shell script to run. Default is 'backup.sh'.
    - log_file (str): The path to the JSON log file where the execution details will be recorded. Default is '/home/user/backup_log.json'.
    
    Returns:
    dict: A dictionary containing:
        - 'start_time': The start time of the script execution in the format '%Y-%m-%d %H:%M:%S'.
        - 'end_time': The end time of the script execution in the format '%Y-%m-%d %H:%M:%S'.
        - 'exit_status': The exit status of the script execution (0 for success, other values indicate an error).
    
    Raises:
    - FileNotFoundError: If the script file does not exist.
    - RuntimeError: If there is an error executing the script.
        
    Requirements:
    - subprocess
    - os
    - datetime
    - json
    
    Example:
    >>> task_func()
    {'start_time': '2023-09-19 14:30:00', 'end_time': '2023-09-19 14:35:00', 'exit_status': 0}
    """

    log_data = {}
    if not os.path.isfile(script_name):
        raise FileNotFoundError(f"Script {script_name} does not exist.")
    start_time = datetime.now()
    log_data['start_time'] = start_time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        exit_status = subprocess.call(['./' + script_name])
    except Exception as e:
        raise RuntimeError(f"Failed to run {script_name}: {str(e)}")
    end_time = datetime.now()
    log_data['end_time'] = end_time.strftime('%Y-%m-%d %H:%M:%S')
    log_data['exit_status'] = exit_status
    with open(log_file, 'w') as f:
        json.dump(log_data, f)
    return log_data

import unittest
from unittest.mock import patch, mock_open
class TestCases(unittest.TestCase):
    
    @patch("os.path.isfile", return_value=True)
    @patch("subprocess.call", return_value=0)
    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_default_values_successful_script(self, mock_file, mock_subprocess, mock_os):
        """Test the function with default parameters and successful execution"""
        result = task_func()
        self.assertIn('start_time', result)
        self.assertIn('end_time', result)
        self.assertEqual(result['exit_status'], 0)
    @patch("os.path.isfile", return_value=False)
    def test_script_does_not_exist(self, mock_os):
        """Test the function raising FileNotFoundError when the script file does not exist"""
        with self.assertRaises(FileNotFoundError):
            task_func()
    @patch("os.path.isfile", return_value=True)
    @patch("subprocess.call", side_effect=Exception("Script failed"))
    def test_script_execution_failure(self, mock_subprocess, mock_os):
        """Test the function raising RuntimeError on script execution failure"""
        with self.assertRaises(RuntimeError):
            task_func()
    @patch("os.path.isfile", return_value=True)
    @patch("subprocess.call", return_value=0)
    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_custom_values_successful_script(self, mock_file, mock_subprocess, mock_os):
        """Test the function with custom script name and log file with successful execution"""
        script_name = "custom_backup.sh"
        log_file = "/home/user/custom_backup_log.json"
        result = task_func(script_name, log_file)
        self.assertIn('start_time', result)
        self.assertIn('end_time', result)
        self.assertEqual(result['exit_status'], 0)
    @patch("os.path.isfile", return_value=True)
    @patch("subprocess.call", return_value=0)
    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_log_data_format(self, mock_file, mock_subprocess, mock_os):
        """Test that the timestamps are in the correct format"""
        result = task_func()
        self.assertTrue(result['start_time'].count(":") == 2)
        self.assertTrue(result['end_time'].count(":") == 2)
    @patch("os.path.isfile", return_value=True)
    @patch("subprocess.call", return_value=1)
    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_non_zero_exit_status(self, mock_file, mock_subprocess, mock_os):
        """Test the function with a non-zero exit status"""
        result = task_func()
        self.assertEqual(result['exit_status'], 1)
