import subprocess
import psutil
import time

def f_1017(process_name: str) -> str:
    '''
    Check if a particular process is running based on its name. If it is not running, start it using the process name as a command. 
    If it is running, terminate the process and restart it by executing the process name as a command.

    Parameters:
    - process_name (str): The name of the process to check and manage. This should be executable as a command.

    Returns:
    - str: A message indicating the action taken:
        - "Process not found. Starting <process_name>."
        - "Process found. Restarting <process_name>."

    Requirements:
    - subprocess: Used to start processes.
    - psutil: Used to iterate over and manage running processes.
    - time: Used to pause execution between termination and restarting of a process.

    Example:
    >>> f_1017('notepad')
    "Process not found. Starting notepad."
    OR
    >>> f_1017('notepad')
    "Process found. Restarting notepad."
    '''
    # Check if the process is running
    is_running = any([proc for proc in psutil.process_iter() if proc.name() == process_name])
    
    # If the process is running, terminate it
    if is_running:
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                proc.terminate()
                time.sleep(5)
        subprocess.Popen(process_name)
        return f"Process found. Restarting {process_name}."
    else:
        subprocess.Popen(process_name)
        return f"Process not found. Starting {process_name}."
    

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_1017('notepad')
        self.assertIn(result, [f"Process found. Restarting notepad.", f"Process not found. Starting notepad."])

    def test_case_2(self):
        result = f_1017('random_non_existent_process')
        self.assertEqual(result, "Process not found. Starting random_non_existent_process.")
        
    def test_case_3(self):
        result = f_1017('another_random_process')
        self.assertEqual(result, "Process not found. Starting another_random_process.")

    def test_case_4(self):
        result = f_1017('sample_process')
        self.assertEqual(result, "Process not found. Starting sample_process.")

    def test_case_5(self):
        result = f_1017('test_process')
        self.assertEqual(result, "Process not found. Starting test_process.")
if __name__ == "__main__":
    run_tests()