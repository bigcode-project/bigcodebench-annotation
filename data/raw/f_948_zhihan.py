import subprocess
import os
import time
import threading

def f_948(script_path: str, timeout: int = 60) -> str:
    """
    Execute a specified R script with a given timeout. If the script execution exceeds the timeout, it is terminated.

    Parameters:
    - script_path (str): The path to the R script to be executed.
    - timeout (int): The maximum allowed time (in seconds) for the script execution. Default is 60 seconds.

    Returns:
    - str: A message indicating if the script was terminated due to timeout or executed successfully.

    Requirements:
    - subprocess
    - os
    - time
    - threading

    Examples:
    >>> f_948('/pathto/MyrScript.r')
    'Script executed successfully.'
    
    >>> f_948('/pathto/LongRunningScript.r', 30)
    'Terminating process due to timeout.'
    """
    def target():
        subprocess.call(['/usr/bin/Rscript', '--vanilla', script_path])

    thread = threading.Thread(target=target)
    thread.start()

    thread.join(timeout)

    if thread.is_alive():
        os.system(f'pkill -f "{script_path}"')
        thread.join()
        return 'Terminating process due to timeout.'
    else:
        return 'Script executed successfully.'

import unittest
from unittest.mock import patch
import time

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    @patch('subprocess.call', return_value=None)
    def test_case_1(self, mock_subprocess):
        # Test with a short-running script
        result = f_948('/path/to/short_script.r', 10)
        self.assertEqual(result, 'Script executed successfully.')

    @patch('subprocess.call', side_effect=time.sleep(15))
    def test_case_2(self, mock_subprocess):
        # Test with a long-running script and short timeout
        result = f_948('/path/to/long_script.r', 10)
        self.assertEqual(result, 'Terminating process due to timeout.')

    @patch('subprocess.call', return_value=None)
    def test_case_3(self, mock_subprocess):
        # Test default timeout behavior
        result = f_948('/path/to/short_script.r')
        self.assertEqual(result, 'Script executed successfully.')

    @patch('subprocess.call', side_effect=FileNotFoundError)
    def test_case_4(self, mock_subprocess):
        # Test with non-existent script path
        with self.assertRaises(FileNotFoundError):
            f_948('/path/to/non_existent_script.r', 10)

    @patch('subprocess.call', side_effect=time.sleep(5))
    def test_case_5(self, mock_subprocess):
        # Test with a script having a controlled delay
        result = f_948('/path/to/delayed_script.r', 3)
        self.assertEqual(result, 'Terminating process due to timeout.')



if __name__ == "__main__":
    run_tests()