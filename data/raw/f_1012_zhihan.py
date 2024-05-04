import subprocess
import os
import json
from datetime import datetime

SCRIPT_NAME = 'backup.sh'
LOG_FILE = '/home/user/backup_log.json'

def f_1012(script_name=SCRIPT_NAME, log_file=LOG_FILE):
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
    >>> f_1012()
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
from unittest.mock import patch, mock_open, MagicMock

class TestBackupScript(unittest.TestCase):

    @patch("os.path.isfile", return_value=True)
    @patch("subprocess.call", return_value=0)
    @patch("builtins.open", new_callable=mock_open)
    def test_default_values_successful_script(self, mock_file, mock_subprocess, mock_os):
        result = f_1012()
        self.assertIn('start_time', result)
        self.assertIn('end_time', result)
        self.assertEqual(result['exit_status'], 0)

    @patch("os.path.isfile", return_value=False)
    def test_script_does_not_exist(self, mock_os):
        with self.assertRaises(FileNotFoundError):
            f_1012()

    @patch("os.path.isfile", return_value=True)
    @patch("subprocess.call", side_effect=Exception("Script failed"))
    def test_script_execution_failure(self, mock_subprocess, mock_os):
        with self.assertRaises(RuntimeError):
            f_1012()

    @patch("os.path.isfile", return_value=True)
    @patch("subprocess.call", return_value=0)
    @patch("builtins.open", new_callable=mock_open)
    def test_custom_values_successful_script(self, mock_file, mock_subprocess, mock_os):
        script_name = "custom_backup.sh"
        backup_dir = "/home/user/custom_backup"
        log_file = "/home/user/custom_backup_log.json"
        result = f_1012(script_name, backup_dir, log_file)
        self.assertIn('start_time', result)
        self.assertIn('end_time', result)
        self.assertEqual(result['exit_status'], 0)

    @patch("os.path.isfile", return_value=True)
    @patch("subprocess.call", return_value=0)
    @patch("builtins.open", new_callable=mock_open)
    def test_log_data_format(self, mock_file, mock_subprocess, mock_os):
        result = f_1012()
        self.assertTrue(result['start_time'].count(":") == 2)  # Checking format of timestamp
        self.assertTrue(result['end_time'].count(":") == 2)  # Checking format of timestamp

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBackupScript))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()