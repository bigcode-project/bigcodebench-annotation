import subprocess
import time
from random import randint
import matplotlib.pyplot as plt

def f_182(commands=['ls', 'pwd', 'date', 'uname -r', 'df -h'], iterations=50):
    """
    Given a list of shell commands and a number of iterations, you will iterate iterations times, randomly choose and execute one of the shell commands. For each shell command that is run you should record its execution time and plot the histogram of execution times.
    - The x-label is of the histogram should be set to 'Time (s)' while the y-label should be set to 'Frequency'.

    Parameters:
    - commands (list of str): A list of shell commands to be executed.
    - iterations (int): Number of times a random command from the list should be executed.

    Returns:
    - list of float: A list of execution times for the commands.
    - Axes object: A histogram plot showing the distribution of execution times.

    Requirements:
    - subprocess
    - time
    - random
    - matplotlib.pyplot

    Example:
    >>> times, ax = f_182(['ls', 'pwd'], 10)
    >>> print(times)
    [0.0023, 0.0012, ...]
    """
    execution_times = []

    for _ in range(iterations):
        command = commands[randint(0, len(commands) - 1)]

        start_time = time.time()
        subprocess.call(command, shell=True)
        end_time = time.time()

        execution_times.append(end_time - start_time)

    fig, ax = plt.subplots()
    ax.hist(execution_times, bins=10)
    ax.set_title('Command Execution Times')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Frequency')
    return execution_times, ax

import unittest
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_182 function."""
    def test_case_1(self):
        # Input: default commands and 10 iterations
        times, ax = f_182(iterations=10)
        
        # Assertions
        self.assertIsInstance(times, list, "Returned execution times should be a list.")
        self.assertEqual(len(times), 10, "The length of the execution times list should match the number of iterations.")
        self.assertEqual(ax.get_title(), 'Command Execution Times', "Histogram title mismatch.")
        self.assertEqual(ax.get_xlabel(), 'Time (s)', "X-axis label mismatch.")
        self.assertEqual(ax.get_ylabel(), 'Frequency', "Y-axis label mismatch.")
        self.assertTrue(all(isinstance(t, float) for t in times), "All elements in the execution times list should be floats.")
    
    def test_case_2(self):
        # Input: two commands and 5 iterations
        times, ax = f_182(commands=['ls', 'pwd'], iterations=5)
        # Assertions
        self.assertEqual(len(times), 5, "The length of the execution times list should match the number of iterations.")
    
    def test_case_3(self):
        # Input: one command and 20 iterations
        times, ax = f_182(commands=['date'], iterations=20)
        
        # Assertions
        self.assertEqual(len(times), 20, "The length of the execution times list should match the number of iterations.")
    
    def test_case_4(self):
        # Input: three commands and 15 iterations
        times, ax = f_182(commands=['uname -r', 'df -h', 'ls'], iterations=15)
        
        # Assertions
        self.assertEqual(len(times), 15, "The length of the execution times list should match the number of iterations.")
    
    def test_case_5(self):
        # Input: default commands and 25 iterations
        times, ax = f_182(iterations=25)
        
        # Assertions
        self.assertEqual(len(times), 25, "The length of the execution times list should match the number of iterations.")

if __name__ == "__main__" :
    run_tests()