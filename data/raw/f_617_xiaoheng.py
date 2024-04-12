import sys
import os
import subprocess

# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def f_617(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    """
    Switch to a specific version of Python and add a specific path to sys.path.
    
    Note: This function changes the global Python version and should be used carefully.
    
    Parameters:
    - python_version (str): The Python version to switch to. Default is '3.8'.
    - path_to_append (str): The path to append to sys.path. Default is '/path/to/whatever'.

    Returns:
    - python_version (str): The Python version that was switched to.

    Requirements:
    - sys
    - os
    - subprocess

    Example:
    >>> f_617('3.7', '/path/to/new_directory')
    '3.7'
    """
    subprocess.run(['pyenv', 'global', python_version], check=True)
    sys.path.append(path_to_append)

    return python_version

import unittest
from unittest.mock import patch

class TestCases(unittest.TestCase):

    @patch('subprocess.run')
    @patch('sys.path.append')
    def test_switch_to_default_python_version(self, mock_append, mock_run):
        result = f_617()
        mock_run.assert_called_with(['pyenv', 'global', '3.8'], check=True)
        mock_append.assert_called_with('/path/to/whatever')
        self.assertEqual(result, '3.8')

    @patch('subprocess.run')
    @patch('sys.path.append')
    def test_switch_to_python_3_7(self, mock_append, mock_run):
        result = f_617('3.7', '/another/path')
        mock_run.assert_called_with(['pyenv', 'global', '3.7'], check=True)
        mock_append.assert_called_with('/another/path')
        self.assertEqual(result, '3.7')

    @patch('subprocess.run')
    @patch('sys.path.append')
    def test_switch_to_python_3_9(self, mock_append, mock_run):
        result = f_617('3.9')
        mock_run.assert_called_with(['pyenv', 'global', '3.9'], check=True)
        mock_append.assert_called_with('/path/to/whatever')
        self.assertEqual(result, '3.9')

    @patch('subprocess.run')
    @patch('sys.path.append')
    def test_switch_to_python_2_7(self, mock_append, mock_run):
        result = f_617('2.7')
        mock_run.assert_called_with(['pyenv', 'global', '2.7'], check=True)
        mock_append.assert_called_with('/path/to/whatever')
        self.assertEqual(result, '2.7')

    @patch('subprocess.run')
    @patch('sys.path.append')
    def test_switch_to_python_3_6(self, mock_append, mock_run):
        result = f_617('3.6', '/different/path')
        mock_run.assert_called_with(['pyenv', 'global', '3.6'], check=True)
        mock_append.assert_called_with('/different/path')
        self.assertEqual(result, '3.6')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()