import subprocess
import shlex
from datetime import datetime

def task_func(script_path: str) -> dict:
    '''
    Run an R script and return the start time, end time, decoded stdout, and decoded stderr as a dictionary.
    
    Requirements:
    - subprocess
    - shlex
    - datetime
    
    Parameters:
    - script_path (str): Path to the R script to be executed.
    
    Returns:
    - dict: A dictionary containing the start time, end time, stdout, and stderr of the script run.
    
    Example:
    >>> task_func("/path/to/script.r")
    {
        'Start Time': '2023-09-26 14:30:00',
        'End Time': '2023-09-26 14:32:00',
        'Stdout': 'Script output here...',
        'Stderr': 'Any errors here...'
    }
    '''
    start_time = datetime.now()
    process = subprocess.Popen(shlex.split(f"/usr/bin/Rscript --vanilla {script_path}"),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = datetime.now()
    log_details = {
        'Start Time': str(start_time),
        'End Time': str(end_time),
        'Stdout': stdout.decode('utf-8'),
        'Stderr': stderr.decode('utf-8')
    }
    return log_details

import unittest
from unittest.mock import patch, Mock
class TestCases(unittest.TestCase):
    @patch('subprocess.Popen')
    def test_case_1(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"Script output here...", b"Any errors here...")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/script.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "Script output here...")
        self.assertEqual(result['Stderr'], "Any errors here...")
    
    @patch('subprocess.Popen')
    def test_case_2(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"Another output...", b"")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/different_script.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "Another output...")
        self.assertEqual(result['Stderr'], "")
    
    @patch('subprocess.Popen')
    def test_case_3(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"", b"An error occurred...")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/erroneous_script.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "")
        self.assertEqual(result['Stderr'], "An error occurred...")
    @patch('subprocess.Popen')
    def test_case_4(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"Script output for case 4...", b"")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/script_4.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "Script output for case 4...")
        self.assertEqual(result['Stderr'], "")
    
    @patch('subprocess.Popen')
    def test_case_5(self, mock_subprocess):
        mock_process = Mock()
        mock_process.communicate.return_value = (b"", b"Error for case 5...")
        mock_subprocess.return_value = mock_process
        
        result = task_func("/path/to/erroneous_script_5.r")
        
        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], "")
        self.assertEqual(result['Stderr'], "Error for case 5...")
