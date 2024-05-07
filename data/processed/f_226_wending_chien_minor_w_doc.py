import numpy as np
import matplotlib.pyplot as plt

# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']


def f_197(data_size):
    """
    Generates random numeric data and creates a histogram of the data.
    The color of the histogram bars is randomly selected from a predefined list.

    Parameters:
    data_size (int): The number of data points to generate.

    Returns:
    tuple:
        - ndarray: The array of randomly generated data.
        - str: The color used for the histogram bars.

    Requirements:
    - numpy
    - matplotlib

    Example:
    >>> data, color = f_197(5)
    >>> print(data.shape)
    (5,)
    >>> print(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    True
    """
    np.random.seed(0)
    data = np.random.randn(data_size)
    color = np.random.choice(BAR_COLOR)
    plt.hist(data, bins=np.arange(-3, 4, 0.5), color=color, edgecolor='black')
    return data, color

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data, color = f_197(100)
        self.assertEqual(len(data), 100)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    def test_case_2(self):
        data, color = f_197(50)
        self.assertEqual(len(data), 50)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    def test_case_3(self):
        data, color = f_197(150)
        self.assertEqual(len(data), 150)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    def test_case_4(self):
        data, color = f_197(200)
        self.assertEqual(len(data), 200)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    def test_case_5(self):
        data, color = f_197(250)
        self.assertEqual(len(data), 250)
        self.assertTrue(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
