import subprocess
import logging

def task_func(filepath):
    """
    Attempts to compile a existing C++ file specified by 'filepath'. The output of the compilation process
    is logged, indicating whether the compilation was successful or not. This function is useful
    for automating the compilation of C++ code and tracking compilation results.
    The log should indicate whether the compilation was successful or if an error occurred.

    Parameters:
    filepath (str): The path of the C++ file to be compiled.

    Returns:
    None: This function does not return anything but logs the outcome of the compilation process.

    Raises:
    - subprocess.CalledProcessError: If the compilation process fails.
    - FileNotFoundError: If the compiler is not found or the specified file does not exist.

    Requirements:
    - subprocess
    - logging

    Examples:
    >>> import os
    >>> with open('example.cpp', 'w') as f: \
            _ = f.write("int main(){return 0;}")
    >>> task_func('example.cpp')
    >>> os.path.exists('example')
    True
    """
    logging.basicConfig(level=logging.INFO)
    try:
        subprocess.check_call(['g++', filepath, '-o', filepath.split('.')[0]])
        logging.info('Successfully compiled %s', filepath)
    except subprocess.CalledProcessError as e:
        logging.error('Failed to compile %s: %s', filepath, e)
    except FileNotFoundError as e:
        logging.error('Compiler not found or file does not exist: %s', e)

import os
import unittest
import logging
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup an empty test file
        self.empty_file = './empty_file.cpp'
        with open(self.empty_file, 'w') as f:
            f.write("")
    @patch('subprocess.check_call')
    def test_successful_compilation(self, mock_check_call):
        task_func('example.cpp')
        mock_check_call.assert_called_with(['g++', 'example.cpp', '-o', 'example'])
    @patch('subprocess.check_call', side_effect=subprocess.CalledProcessError(1, ['g++']))
    def test_compilation_failure(self, mock_check_call):
        task_func('example.cpp')
        mock_check_call.assert_called_with(['g++', 'example.cpp', '-o', 'example'])
    
    @patch('logging.error')
    @patch('subprocess.check_call', side_effect=FileNotFoundError)
    def test_compiler_not_found(self, mock_check_call, mock_logging_error):
        task_func('example.cpp')
        mock_logging_error.assert_called()
    @patch('logging.error')
    def test_empty_file(self, mock_logging_error):
        task_func(self.empty_file)
        mock_logging_error.assert_called()
    @patch('logging.error')
    @patch('subprocess.check_call', side_effect=FileNotFoundError())
    def test_logging_output(self, mock_check_call, mock_logging):
        task_func('example.cpp')
        mock_logging.assert_called()
    def tearDown(self):
        # Clean up created files
        os.remove(self.empty_file)
