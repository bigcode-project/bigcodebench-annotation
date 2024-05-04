import subprocess
import os
import time
from datetime import datetime


def f_725(script_dir, scripts, delay):
    """
    Execute a list of bash scripts with a specified delay between each script.

    Parameters:
    script_dir (str): Path to the directory containing the scripts.
    scripts (list): List of script filenames to be executed. Must not be empty.
                    If a script is not found, the function raises a FileNotFoundError.
    delay (int): The delay in seconds between each script execution. Must at least 0.

    Returns:
    list: A list of timestamps indicating the start time of each script execution.

    Raises:
    - ValueError: If the delay is negative or no scripts are provided.
    
    Requirements:
    - subprocess
    - os
    - time
    - datetime.datetime

    Example:
    >>> f_725('/path/to/scripts/', ['script1.sh', 'script2.sh'], 5)
    ['2023-09-09 10:10:10', '2023-09-09 10:10:15']
    """
    if delay < 0:
        raise ValueError("delay cannot be negative.")
    if not scripts:
        raise ValueError("No scripts provided.")
    start_times = []
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        start_times.append(start_time)
        result = subprocess.call(script_path, shell=True)
        if result != 0:
            raise FileNotFoundError(f"Script not found: {script_path}")
        time.sleep(delay)
    return start_times

import unittest
import tempfile
import os
from datetime import datetime
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store scripts
        self.temp_dir = tempfile.TemporaryDirectory()
        self.script_dir = self.temp_dir.name
    def tearDown(self):
        # Clean up the temporary directory
        self.temp_dir.cleanup()
    def create_temp_script(self, script_content):
        # Helper function to create a temporary script file with the given content
        fd, path = tempfile.mkstemp(dir=self.script_dir, suffix=".sh")
        with os.fdopen(fd, "w") as f:
            f.write("#!/bin/bash\n")
            f.write(script_content)
        os.chmod(path, 0o755)
        return os.path.basename(path)
    def test_case_1(self):
        # Testing with a single script and delay of 1 second
        script_name = self.create_temp_script("echo 'Test'")
        scripts = [script_name]
        delay = 1
        start_times = f_725(self.script_dir, scripts, delay)
        self.assertEqual(len(start_times), 1)
        self.assertTrue(
            isinstance(datetime.strptime(start_times[0], "%Y-%m-%d %H:%M:%S"), datetime)
        )
    def test_case_2(self):
        # Testing with multiple scripts and a longer delay
        script_names = [
            self.create_temp_script("echo 'Test'"),
            self.create_temp_script("echo 'Test 2'"),
        ]
        delay = 2
        start_times = f_725(self.script_dir, script_names, delay)
        self.assertEqual(len(start_times), 2)
        time_diff = datetime.strptime(
            start_times[1], "%Y-%m-%d %H:%M:%S"
        ) - datetime.strptime(start_times[0], "%Y-%m-%d %H:%M:%S")
        self.assertEqual(time_diff.seconds, delay)
    def test_case_3(self):
        # Testing with an invalid script path
        with self.assertRaises(FileNotFoundError):
            f_725(self.script_dir, ["this-doesn't-exist"], 1)
    def test_case_4(self):
        # Testing with no scripts (empty list)
        with self.assertRaises(Exception):
            f_725(self.script_dir, [], 1)
    def test_case_5(self):
        # Testing with zero delay
        script_names = [
            self.create_temp_script("echo 'Test'"),
            self.create_temp_script("echo 'Test 2'"),
        ]
        delay = 0
        start_times = f_725(self.script_dir, script_names, delay)
        self.assertEqual(len(start_times), 2)
    def test_case_6(self):
        # Test handling invalid delay
        script_names = [
            self.create_temp_script("echo 'Test'"),
            self.create_temp_script("echo 'Test 2'"),
        ]
        with self.assertRaises(Exception):
            f_725(self.script_dir, script_names, -1)
