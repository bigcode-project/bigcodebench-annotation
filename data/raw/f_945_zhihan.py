import subprocess
import os
import glob
import time

# Constants
R_SCRIPTS_DIR = '/pathto/rscripts/'

def f_945():
    """
    Run all R scripts in a specific directory and return their execution times.

    Returns:
    dict: A dictionary with the script names as keys and their execution times as values.

    Requirements:
    - subprocess
    - os
    - glob
    - time

    Example:
    >>> f_945()
    """
    execution_times = {}
    r_scripts = glob.glob(os.path.join(R_SCRIPTS_DIR, '*.r'))

    for r_script in r_scripts:
        start_time = time.time()
        subprocess.call(['/usr/bin/Rscript', '--vanilla', r_script])
        end_time = time.time()
        execution_times[os.path.basename(r_script)] = end_time - start_time

    return execution_times
    

import unittest
import os
import glob
import time

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with the created R scripts directory
        result = f_945(r_scripts_test_dir)
        self.assertEqual(len(result), 3)  # There are 3 R scripts
        self.assertTrue("script1.r" in result)
        self.assertTrue("script2.r" in result)
        self.assertTrue("script3.r" in result)
        for time_taken in result.values():
            self.assertTrue(time_taken >= 0)  # Execution time should be non-negative

    def test_case_2(self):
        # Testing with a non-existent directory (should return an empty dictionary)
        result = f_945("/non/existent/path/")
        self.assertEqual(result, {})

    def test_case_3(self):
        # Testing with a directory that has no R scripts (should return an empty dictionary)
        empty_dir = "/mnt/data/empty_dir/"
        os.makedirs(empty_dir, exist_ok=True)
        result = f_945(empty_dir)
        self.assertEqual(result, {})

    def test_case_4(self):
        # Testing with a directory containing other types of files (should return an empty dictionary)
        other_files_dir = "/mnt/data/other_files/"
        os.makedirs(other_files_dir, exist_ok=True)
        with open(os.path.join(other_files_dir, "not_an_r_script.txt"), 'w') as file:
            file.write("This is not an R script.")
        result = f_945(other_files_dir)
        self.assertEqual(result, {})

    def test_case_5(self):
        # Testing with a directory containing a mix of R scripts and other files
        mix_files_dir = "/mnt/data/mix_files/"
        os.makedirs(mix_files_dir, exist_ok=True)
        with open(os.path.join(mix_files_dir, "script4.r"), 'w') as file:
            file.write("print('Hello from script4')")
        with open(os.path.join(mix_files_dir, "not_an_r_script.txt"), 'w') as file:
            file.write("This is not an R script.")
        result = f_945(mix_files_dir)
        self.assertEqual(len(result), 1)  # Only 1 R script
        self.assertTrue("script4.r" in result)
        for time_taken in result.values():
            self.assertTrue(time_taken >= 0)  # Execution time should be non-negative
if __name__ == "__main__":
    run_tests()