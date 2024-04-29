import subprocess
import tempfile
import shutil
import os

def f_947(script_path: str) -> str:
    """
    Execute a given R script in a temporary directory and clean up after execution.
    
    Functionality:
    This function creates a temporary directory, copies the specified R script to this directory, 
    executes the R script, and then cleans up the temporary directory.
    
    Input:
    - script_path (str): The path to the R script that needs to be executed.
    
    Output:
    - Returns a string indicating the success or failure of the script execution.
    
    Requirements:
    - subprocess
    - tempfile
    - shutil
    - os
    
    Example:
    >>> f_947('/path/to/example_script.r')
    'Script executed successfully!'
    
    Note: Make sure the provided R script path is valid and accessible.
    """
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            shutil.copy(script_path, temp_dir)
            temp_script_path = os.path.join(temp_dir, os.path.basename(script_path))
            result = subprocess.call(['/usr/bin/Rscript', '--vanilla', temp_script_path])
            
            if result == 0:
                return "Script executed successfully!"
            else:
                return "Script execution failed!"
    except Exception as e:
        return f"Error: {e}"

import unittest

# Assuming the refined function has been imported as f_947

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Testing with a non-existent script path
        result = f_947('/path/to/non_existent_script.r')
        self.assertEqual(result, "Error: [Errno 2] No such file or directory: '/path/to/non_existent_script.r'")
    
    def test_case_2(self):
        # Testing with a valid script path but the script contains errors
        # Assuming we have a script named "error_script.r" which contains intentional errors
        result = f_947('/path/to/error_script.r')
        self.assertEqual(result, "Script execution failed!")
        
    def test_case_3(self):
        # Testing with a valid script path and the script executes successfully
        # Assuming we have a script named "success_script.r" which runs without errors
        result = f_947('/path/to/success_script.r')
        self.assertEqual(result, "Script executed successfully!")
    
    def test_case_4(self):
        # Testing with a script that takes a long time to execute
        # Assuming we have a script named "long_running_script.r" that intentionally runs for a long time
        result = f_947('/path/to/long_running_script.r')
        # The exact output will depend on how the script is written, but for this test, 
        # we assume it eventually completes successfully.
        self.assertEqual(result, "Script executed successfully!")
    
    def test_case_5(self):
        # Testing with a script that requires certain packages or libraries
        # Assuming we have a script named "package_script.r" that requires specific R packages
        result = f_947('/path/to/package_script.r')
        # The exact output will depend on the presence or absence of the required packages.
        # For this test, we'll assume that the required packages are present and the script runs successfully.
        self.assertEqual(result, "Script executed successfully!")
if __name__ == "__main__":
    run_tests()