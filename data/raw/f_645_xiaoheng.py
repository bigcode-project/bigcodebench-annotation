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

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_returned_script_name(self):
        # Test that the function returns a valid script name from the predefined list
        script_name = f_645()
        self.assertIn(script_name, SCRIPTS)
    
    def test_returned_script_name_multiple_times(self):
        # Test multiple times to ensure random selection from the list
        for _ in range(100):
            script_name = f_645()
            self.assertIn(script_name, SCRIPTS)

    def test_script_execution(self):
        # Test that the selected script is actually executed
        script_name = f_645()
        expected_output = "Running {}\n".format(script_name)
        with subprocess.Popen(os.path.join(self.temp_dir, script_name), stdout=subprocess.PIPE, shell=True) as proc:
            output = proc.stdout.read().decode('utf-8')
            self.assertEqual(output, expected_output)

    def test_random_seed(self):
        # Test that setting a random seed produces consistent results
        random.seed(42)
        script_name1 = f_645()
        random.seed(42)
        script_name2 = f_645()
        self.assertEqual(script_name1, script_name2)

    def test_empty_script_list(self):
        # Test the behavior when the script list is empty
        global SCRIPTS
        original_scripts = SCRIPTS
        SCRIPTS = []
        with self.assertRaises(IndexError):
            f_645()
        SCRIPTS = original_scripts

if __name__ == "__main__":
    run_tests()