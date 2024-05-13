import os
from datetime import datetime

# Constants
LOG_DIR = './logs'

def task_func(metrics, filename, log_dir=LOG_DIR):
    """
    This function writes a dictionary of metrics to a specified log file, appending a timestamp to each entry.
    
    Parameters:
    - metrics (dict): A dictionary containing metric names as keys and their corresponding values.
    - filename (str): The name of the file to which the metrics will be logged.
    - log_dir (str, optional): The directory where the log file is stored. Default is './logs'.
    
    Returns:
    - bool: True if the metrics were successfully written to the file, False otherwise.
    
    Requirements:
    - os
    - datetime
    
    Examples:
    >>> metrics = {'accuracy': 0.98, 'loss': 0.05}
    >>> task_func(metrics, 'metrics.log')
    An error occurred: [Errno 2] No such file or directory: './logs/metrics.log'
    False
    
    >>> metrics = {'precision': 0.75, 'recall': 0.80}
    >>> task_func(metrics, 'evaluation.log')
    An error occurred: [Errno 2] No such file or directory: './logs/evaluation.log'
    False
    """
    if not isinstance(metrics, dict):
        raise ValueError("Metrics must be a dictionary")
    if not isinstance(filename, str):
        raise ValueError("Filename must be a string")
    try:
        with open(os.path.join(log_dir, filename), 'a') as f:
            f.write(f'{datetime.now()}\n')
            for key, value in metrics.items():
                f.write(f'{key}: {value}\n')
            f.write('\n')
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

import unittest
from unittest.mock import patch, mock_open, MagicMock
class TestCases(unittest.TestCase):
    def setUp(self):
        self.metrics = {'accuracy': 0.98, 'loss': 0.05}
        self.filename = 'metrics.log'
        self.log_dir = './temp_logs'
    def test_non_string_filename(self):
        with self.assertRaises(ValueError):
            task_func(self.metrics, 12345, log_dir=self.log_dir)
    def test_non_dictionary_metrics(self):
        with self.assertRaises(ValueError):
            task_func('accuracy: 0.95', self.filename, log_dir=self.log_dir)
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    def test_normal_metrics_logging(self, mock_exists, mock_file, mock_makedirs):
        result = task_func(self.metrics, self.filename, log_dir=self.log_dir)
        self.assertTrue(result)
        mock_file.assert_called_once_with(os.path.join(self.log_dir, self.filename), 'a')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    def test_normal_metrics_logging(self, mock_exists, mock_file, mock_makedirs):
        result = task_func(self.metrics, self.filename, log_dir=self.log_dir)
        self.assertTrue(result)
        mock_file.assert_called_once_with(os.path.join(self.log_dir, self.filename), 'a')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_non_existent_log_directory(self, mock_exists, mock_file, mock_makedirs):
        result = task_func(self.metrics, self.filename, log_dir='./nonexistent_dir')
        self.assertTrue(result)
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=MagicMock)
    @patch('os.path.exists', return_value=True)
    def test_empty_metrics(self, mock_exists, mock_open, mock_makedirs):
        # Setup the mock file handle that open returns
        mock_file_handle = mock_open.return_value.__enter__.return_value
        
        # Call the function
        metrics = {}
        filename = 'empty_metrics.log'
        log_dir = './temp_logs'
        result = task_func(metrics, filename, log_dir=log_dir)
        # Assert that the function returned True for successful logging
        self.assertTrue(result)
        # Check that 'write' was called exactly twice: once for the timestamp, once for the newline
        self.assertEqual(mock_file_handle.write.call_count, 2)
        # Check that the calls were for writing the timestamp and an empty line
        args_list = mock_file_handle.write.call_args_list
        self.assertTrue(args_list[0][0][0].endswith('\n'))  # Check if first write is a timestamp ending with newline
        self.assertEqual(args_list[1][0][0], '\n')  # Check if second write is just a newline
    def test_non_string_filename(self):
        with self.assertRaises(ValueError):
            task_func(self.metrics, 12345, log_dir=self.log_dir)
    def test_non_dictionary_metrics(self):
        with self.assertRaises(ValueError):
            task_func('accuracy: 0.95', self.filename, log_dir=self.log_dir)
