import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    """
    Create a numeric array of random integers, calculate the mean and standard deviation, and draw a histogram of the distribution.

    Returns:
    Tuple: A tuple containing the array, mean, standard deviation, and the histogram plot (Axes).

    Note:
        The random integers are generated between 1 and 100. The title of the histogram is "Histogram of Random Values". 
        The x-axis is labeled "Val" and the y-axis is labeled "Freq". 
        The mean is plotted as a red dashed line, and the standard deviation is plotted as purple dashed lines.
        
    Requirements:
    - numpy
    - matplotlib.pyplot
    
    Example:
    >>> import numpy as np
    >>> np.random.seed(0)
    >>> array, mean, std, ax = task_func()
    >>> print(mean, std)
    250.7154 142.85617453522966
    >>> plt.show()
    """
    array = np.random.randint(1, 500, size=ARRAY_SIZE)
    mean = np.mean(array)
    std = np.std(array)
    fig, ax = plt.subplots()
    ax.hist(array, bins='auto')
    ax.set_title('Histogram of Random Values')
    ax.set_xlabel('Val')
    ax.set_ylabel('Freq')
    return array, mean, std, ax

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        np.random.seed(0)
        array, mean, std, ax = task_func()
        self.assertEqual(array.size, ARRAY_SIZE)
        self.assertEqual(mean, 250.7154)
        self.assertEqual(std, 142.85617453522966)
        self.assertEqual(ax.get_title(), 'Histogram of Random Values')
    def test_case_2(self):
        array, mean, std, ax = task_func()
        self.assertEqual(ax.get_xlabel(), 'Val')
        self.assertEqual(ax.get_ylabel(), 'Freq')
    def test_case_3(self):
        np.random.seed(42)
        array, mean, std, ax = task_func()
        self.assertEqual(array[0], 103)
        self.assertEqual(array[-1], 474)
        self.assertEqual(mean, 250.171)
        self.assertEqual(std, 144.01374920124815)
        
    def test_case_4(self):
        np.random.seed(142)
        array, mean, std, ax = task_func()
        self.assertEqual(array[0], 278)
        self.assertEqual(array[-1], 113)
        self.assertEqual(mean, 251.1245)
        self.assertEqual(std, 144.49066405740547)
    def test_case_5(self):
        np.random.seed(250)
        array, mean, std, ax = task_func()
        self.assertEqual(array[0], 367)
        self.assertEqual(array[-1], 190)
        self.assertEqual(mean, 249.037)
        self.assertEqual(std, 144.32681882103546)
