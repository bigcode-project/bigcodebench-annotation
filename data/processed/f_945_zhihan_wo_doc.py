import subprocess
import os
import glob
import time


def f_965(test_dir):
    """
    Run all Python codes in a specific directory and return their execution times.

    Parameters:
    - script_path (str): Path to the directory for Python code(s) to be executed.
    
    Returns:
    dict: A dictionary with the script names as keys and their execution times as values.

    Requirements:
    - subprocess
    - os
    - glob
    - time

    Example:
    >>> f_965("/mnt/data/mix_files/")
    {'script1.py': 0.04103803634643555, "script2.py": 5}
    """
    execution_times = {}
    py_scripts = glob.glob(os.path.join(test_dir, '*.py'))
    for py_script in py_scripts:
        start_time = time.time()
        subprocess.call(['python', py_script])
        end_time = time.time()
        execution_times[os.path.basename(py_script)] = end_time - start_time
    return execution_times

import unittest
import os
import glob
import time
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_f_965/'
        os.makedirs(self.test_dir, exist_ok=True)
        self.sample_directory = 'testdir_f_965/sample_directory'
        os.makedirs(self.sample_directory, exist_ok=True)
        f = open(self.sample_directory+"/script1.py","w")
        f.write("a <- 42/nA <- a * 2/nprint(a)")
        f.close()
        f = open(self.sample_directory+"/script2.py","w")
        f.write("a <- 42/nA <- a * 2/nprint(a)/nprint(A)")
        f.close()
        f = open(self.sample_directory+"/script3.py","w")
        f.write("a <- 42/nA <- a * 2/nprint(A)")
        f.close()
        self.empty_directory = "testdir_f_965/empty_directory"
        os.makedirs(self.empty_directory, exist_ok=True)
        self.mixed_directory = "testdir_f_965/mixed_directory"
        os.makedirs(self.mixed_directory, exist_ok=True)
        f = open(self.mixed_directory+"/1.txt","w")
        f.write("invalid")
        f.close()
        f = open(self.mixed_directory+"/script4.py","w")
        f.write("print('Hello from script4')")
        f.close()
        self.invalid_directory = "testdir_f_965/invalid_directory"
        os.makedirs(self.invalid_directory, exist_ok=True)
        f = open(self.invalid_directory+"/1.txt","w")
        f.write("invalid")
        f.close()
        
    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)
    def test_case_1(self):
        # Testing with the created R scripts directory
        result = f_965(self.sample_directory)
        self.assertEqual(len(result), 3)  # There are 3 R scripts
        self.assertTrue("script1.py" in result)
        self.assertTrue("script2.py" in result)
        self.assertTrue("script3.py" in result)
        for time_taken in result.values():
            self.assertTrue(time_taken >= 0)  # Execution time should be non-negative
    def test_case_2(self):
        # Testing with a non-existent directory (should return an empty dictionary)
        result = f_965("/non/existent/path/")
        self.assertEqual(result, {})
    def test_case_3(self):
        # Testing with a directory that has no Python scripts (should return an empty dictionary)
        empty_dir = self.empty_directory
        os.makedirs(empty_dir, exist_ok=True)
        result = f_965(empty_dir)
        self.assertEqual(result, {})
    def test_case_4(self):
        # Testing with a directory containing other types of files (should return an empty dictionary)
        other_files_dir = self.invalid_directory
        result = f_965(other_files_dir)
        self.assertEqual(result, {})
    def test_case_5(self):
        # Testing with a directory containing a mix of Python scripts and other files
        mix_files_dir = self.mixed_directory
        result = f_965(mix_files_dir)
        self.assertEqual(len(result), 1)  # Only 1 Python script
        self.assertTrue("script4.py" in result)
        for time_taken in result.values():
            self.assertTrue(time_taken >= 0)  # Execution time should be non-negative
