import matplotlib
# Check and set the backend
print("Current backend:", matplotlib.get_backend())  # Optional: Check the current backend
matplotlib.use('Agg')  # Set to 'Agg' to avoid GUI-related issues

import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi

def f_450(size=SIZE, frequency=1):
    '''
    Create a list of random sinusoidal values and plot them in a graph.
    
    Parameters:
    - size (int): The number of points for the sinusoidal wave. Default is 1000.
    - frequency (float): The frequency of the sinusoidal wave. Default is 1.
    
    Returns:
    - Axes object: The plot of the sinusoidal wave.
    
    Requirements:
    - random
    - math
    - matplotlib.pyplot
    - numpy
    
    Example:
    >>> ax = f_450(size=1000, frequency=1)
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    >>> len(ax.lines[0].get_ydata()) == 1000  # Verify the number of data points in the sinusoidal wave
    True
    >>> isinstance(ax.lines[0].get_ydata()[0], float)  # Check if y-values are floating-point numbers
    True
    '''
    x_values = np.arange(0, size)
    y_values = [math.sin((2 * PI / RANGE) * (x + int(RANGE * random.random()) * frequency)) for x in range(size)]
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    
    return ax
    

import unittest
import random

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = f_450()
        x_data, y_data = ax.lines[0].get_data()
        self.assertEqual(len(x_data), SIZE)
        self.assertTrue(min(y_data) >= -1 and max(y_data) <= 1)
    
    def test_case_2(self):
        ax = f_450(size=500)
        x_data, y_data = ax.lines[0].get_data()
        self.assertEqual(len(x_data), 500)
        self.assertTrue(min(y_data) >= -1 and max(y_data) <= 1)
    
    def test_case_3(self):
        ax = f_450(frequency=2)
        x_data, y_data = ax.lines[0].get_data()
        self.assertEqual(len(x_data), SIZE)
        self.assertTrue(min(y_data) >= -1 and max(y_data) <= 1)
        
    def test_case_4(self):
        ax = f_450(size=1500, frequency=0.5)
        x_data, y_data = ax.lines[0].get_data()
        self.assertEqual(len(x_data), 1500)
        self.assertTrue(min(y_data) >= -1 and max(y_data) <= 1)
    
    def test_case_5(self):
        size_random = random.randint(500, 1500)
        frequency_random = random.uniform(0.1, 3)
        ax = f_450(size=size_random, frequency=frequency_random)
        x_data, y_data = ax.lines[0].get_data()
        self.assertEqual(len(x_data), size_random)
        self.assertTrue(min(y_data) >= -1 and max(y_data) <= 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()