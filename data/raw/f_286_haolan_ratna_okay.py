import subprocess
import os
import random

def f_286(directory, file_list):
    """
    Select a random file from a given list of files in a specified directory and run it as a subprocess.
    
    Args:
    directory (str): The directory path where the files are located.
    file_list (list of str): A list of file names to choose from.

    Returns:
    int: The exit code of the subprocess, or None if the process is still running or if the file list is empty.

    Requirements:
    - subprocess
    - os
    - random

    Example:
    >>> f_286("c:\Program Files\VMware\VMware Server", ["file1.bat", "file2.bat"]) #valid directory and file list
    0 
    """

    if not file_list:
        return None

    file = random.choice(file_list)
    file_path = os.path.join(directory, file)
    try:
        process = subprocess.Popen(file_path)
        process.wait()  # wait for the process to complete
        return process.returncode  # return the exit code
    except Exception as e:
        return None

import unittest
import subprocess
from unittest.mock import patch, MagicMock

class TestCases(unittest.TestCase):
    def test_valid_input(self):
        # Testing with a valid directory and file list
        directory = "valid_dir"
        file_list = ["script1.bat", "script2.bat"]
        with patch('subprocess.Popen') as mock_popen:
            mock_process = MagicMock()
            mock_process.wait.return_value = None
            mock_process.returncode = 0
            mock_popen.return_value = mock_process
            result = f_286(directory, file_list)
            self.assertEqual(result, 0)

    def test_empty_file_list(self):
        # Testing with an empty file list
        directory = "valid_dir"
        file_list = []
        result = f_286(directory, file_list)
        self.assertIsNone(result)

    def test_invalid_directory(self):
        # Testing with an invalid directory
        directory = "invalid_dir"
        file_list = ["script1.bat"]
        with patch('subprocess.Popen', side_effect=Exception("Error")):
            result = f_286(directory, file_list)
            self.assertIsNone(result)

    def test_non_zero_exit_code(self):
        # Testing a subprocess that returns a non-zero exit code
        directory = "valid_dir"
        file_list = ["script3.bat"]
        with patch('subprocess.Popen') as mock_popen:
            mock_process = MagicMock()
            mock_process.wait.return_value = None
            mock_process.returncode = 1
            mock_popen.return_value = mock_process
            result = f_286(directory, file_list)
            self.assertEqual(result, 1)

    def test_random_file_selection(self):
        # Testing that a file is randomly selected from the list
        directory = "valid_dir"
        file_list = ["script1.bat", "script2.bat", "script3.bat"]
        with patch('random.choice', side_effect=file_list):
            with patch('subprocess.Popen') as mock_popen:
                mock_process = MagicMock()
                mock_process.wait.return_value = None
                mock_process.returncode = 0
                mock_popen.return_value = mock_process
                for expected_file in file_list:
                    result = f_286(directory, file_list)
                    mock_popen.assert_called_with(os.path.join(directory, expected_file))
                    self.assertEqual(result, 0)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()