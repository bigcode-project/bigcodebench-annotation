import subprocess
import random

# Constants
SCRIPTS = ['script1.sh', 'script2.sh', 'script3.sh']

def f_645():
    """
    Run a random bash script from a list of scripts.

    Parameters:
    - None

    Returns:
    - script (str): The name of the script that was executed.

    Requirements:
    - subprocess
    - random

    Example:
    >>> random.seed(42)
    >>> script = f_645()
    >>> print(f"Executed script: {script}")
    Executed script: script3.sh
    """
    script = random.choice(SCRIPTS)
    subprocess.call(script, shell=True)

    return script

import unittest
from unittest.mock import patch, MagicMock
import subprocess
import os

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory attribute
        self.temp_dir = '/path/to/scripts'  # You can set this to a real or mock directory as per your setup
        self.scripts_full_path = [os.path.join(self.temp_dir, script) for script in SCRIPTS]

        # Patch subprocess.call to prevent actual script execution
        self.patcher = patch('subprocess.call', return_value=0)
        self.mock_subprocess_call = self.patcher.start()

    def tearDown(self):
        # Stop the patcher after each test
        self.patcher.stop()

    def test_script_execution(self):
        # Test that the selected script is actually executed
        script_name = f_645()
        self.mock_subprocess_call.assert_called_with(script_name, shell=True)

        # Optional: check if the script is called with the correct path
        called_script_path = self.mock_subprocess_call.call_args[0][0]
        self.assertIn(called_script_path, self.scripts_full_path)

if __name__ == "__main__":
    run_tests()