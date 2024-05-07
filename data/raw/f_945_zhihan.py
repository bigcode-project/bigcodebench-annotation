import subprocess
import os
import glob
import time
# import rpy2.robjects as robjects


def f_945(test_dir):
    """
    Run all R scripts in a specific directory and return their execution times.

    Parameters:
    - script_path (str): Path to the directory for R script(s) to be executed.
    
    Returns:
    dict: A dictionary with the script names as keys and their execution times as values.

    Requirements:
    - subprocess
    - os
    - glob
    - time

    Example:
    >>> f_945("/mnt/data/mix_files/")
    {"script1.r": 100, "script2.r": 5}
    """
    execution_times = {}
    r_scripts = glob.glob(os.path.join(test_dir, '*.r'))

    for r_script in r_scripts:
        start_time = time.time()
        subprocess.call(['/usr/bin/Rscript', '--vanilla', r_script])
        # robjects.r.source(r_script, encoding="utf-8")
        end_time = time.time()
        execution_times[os.path.basename(r_script)] = end_time - start_time

    return execution_times
    

import unittest
import os
import glob
import time
import shutil

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_f_945/'
        os.makedirs(self.test_dir, exist_ok=True)
        self.sample_directory = 'testdir_f_945/sample_directory'
        os.makedirs(self.sample_directory, exist_ok=True)
        f = open(self.sample_directory+"/script1.r","w")
        f.write("a <- 42/nA <- a * 2/nprint(a)")
        f.close()
        f = open(self.sample_directory+"/script2.r","w")
        f.write("a <- 42/nA <- a * 2/nprint(a)/nprint(A)")
        f.close()
        f = open(self.sample_directory+"/script3.r","w")
        f.write("a <- 42/nA <- a * 2/nprint(A)")
        f.close()
        self.empty_directory = "testdir_f_945/empty_directory"
        os.makedirs(self.empty_directory, exist_ok=True)
        self.mixed_directory = "testdir_f_945/mixed_directory"
        os.makedirs(self.mixed_directory, exist_ok=True)
        f = open(self.mixed_directory+"/1.txt","w")
        f.write("invalid")
        f.close()
        f = open(self.mixed_directory+"/script4.r","w")
        f.write("print('Hello from script4')")
        f.close()
        self.invalid_directory = "testdir_f_945/invalid_directory"
        os.makedirs(self.invalid_directory, exist_ok=True)
        f = open(self.invalid_directory+"/1.r","w")
        f.write("invalid")
        f.close()
        

    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)

    def test_case_1(self):
        # Testing with the created R scripts directory
        result = f_945(self.sample_directory)
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
        empty_dir = self.empty_directory
        os.makedirs(empty_dir, exist_ok=True)
        result = f_945(empty_dir)
        self.assertEqual(result, {})

    def test_case_4(self):
        # Testing with a directory containing other types of files (should return an empty dictionary)
        other_files_dir = self.invalid_directory
        result = f_945(other_files_dir)
        self.assertEqual(result, {})

    def test_case_5(self):
        # Testing with a directory containing a mix of R scripts and other files
        mix_files_dir = self.mixed_directory
        result = f_945(mix_files_dir)
        self.assertEqual(len(result), 1)  # Only 1 R script
        self.assertTrue("script4.r" in result)
        for time_taken in result.values():
            self.assertTrue(time_taken >= 0)  # Execution time should be non-negative
if __name__ == "__main__":
    run_tests()