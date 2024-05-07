import subprocess
import tempfile
import shutil
import os

def f_947(script_path: str, temp_dir: str) -> str:
    """
    Execute a given Python code in a temporary directory.
    
    Input:
    - script_path (str): The path to the Python code that needs to be executed.
    - temp_dir (str): The path for the code to copy the Python code
    
    Output:
    - str: String indicating the success or failure of the script execution.
    
    Requirements:
    - subprocess
    - tempfile
    - shutil
    - os
    
    Example:
    >>> f_947('/path/to/example_script.py')
    'Script executed successfully!'
    
    Note: 
    - If the Python code can be run successfully return "Script executed successfully!", otherwise "Script execution failed!"
    """
    try:
        shutil.copy(script_path, temp_dir)
        temp_script_path = os.path.join(temp_dir, os.path.basename(script_path))
        result = subprocess.call(["python", temp_script_path])
        print(result)
        if result == 0:
            return "Script executed successfully!"
        else:
            return "Script execution failed!"
    except Exception as e:
        return "Script execution failed!"

import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_f_947'
        os.makedirs(self.test_dir, exist_ok=True)
        f = open(self.test_dir+"/script4.py","w")
        f.write("print('Hello from script4')")
        f.close()
        f = open(self.test_dir+"/script1.py","w")
        f.write("import time\ntime.sleep(20)\nprint('waiting')")
        f.close()
        f = open(self.test_dir+"/script2.py","w")
        f.close()
        f = open(self.test_dir+"/script3.py","w")
        f.write("invalid python code")
        f.close()
        
        self.temp_dir = 'testdir_f_947/temp_dir'
        os.makedirs(self.temp_dir, exist_ok=True)
        

    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)
    
    def test_case_1(self):
        # Testing with a non-existent script path
        result = f_947('/path/to/non_existent_script.py', self.temp_dir)
        self.assertEqual(result, "Script execution failed!")
        self.assertEqual(os.path.exists(self.temp_dir+"/non_existent_script.py"), False)
    
    def test_case_2(self):
        # Testing with a valid script path but the script contains errors
        # Assuming we have a script named "error_script.r" which contains intentional errors
        result = f_947(self.test_dir+"/script3.py", self.temp_dir)
        self.assertEqual(result, "Script execution failed!")
        self.assertEqual(os.path.exists(self.temp_dir+"/script3.py"), True)
        
    def test_case_3(self):
        # Testing with a valid script path and the script executes successfully
        # Assuming we have a script named "sscript4.r" which runs without errors
        result = f_947(self.test_dir+"/script4.py", self.temp_dir)
        self.assertEqual(result, "Script executed successfully!")
        self.assertEqual(os.path.exists(self.temp_dir+"/script4.py"), True)
    
    def test_case_4(self):
        # Testing with a script that takes a long time to execute
        # Assuming we have a script named "script1.r" that intentionally runs for a long time
        result = f_947(self.test_dir+"/script1.py", self.temp_dir)
        self.assertEqual(result, "Script executed successfully!")
        self.assertEqual(os.path.exists(self.temp_dir+"/script1.py"), True)
    
    def test_case_5(self):
         # Testing with a script that empty
        result = f_947(self.test_dir+"/script2.py", self.temp_dir)
        self.assertEqual(result, "Script executed successfully!")
        self.assertEqual(os.path.exists(self.temp_dir+"/script2.py"), True)

if __name__ == "__main__":
    run_tests()