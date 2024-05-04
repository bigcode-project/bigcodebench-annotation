import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def f_87():
    """
    Create a numeric array of random integers, calculate the mean and standard deviation, and draw a histogram of the distribution.

    Note:
        The random integers are generated between 1 and 100. The title of the histogram is "Histogram of Random Integers". 
        The x-axis is labeled "Value" and the y-axis is labeled "Frequency". 
        The mean is plotted as a red dashed line, and the standard deviation is plotted as purple dashed lines.
        
    Returns:
    Tuple: A tuple containing the array, mean, standard deviation, and the histogram plot (Axes).

    Requirements:
    - numpy
    - matplotlib.pyplot
    
    Example:
    >>> import numpy as np
    >>> np.random.seed(0)
    >>> array, mean, std, ax = f_87()
    >>> print(mean, std)
    49.6135 28.5323416100046
    >>> plt.show()
    """
    array = np.random.randint(1, 100, size=ARRAY_SIZE)
    mean = np.mean(array)
    std = np.std(array)
    fig, ax = plt.subplots()
    ax.hist(array, bins='auto')
    ax.set_title('Histogram of Random Integers')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.axvline(mean, color='red', linestyle='dashed', linewidth=1)
    ax.axvline(mean + std, color='purple', linestyle='dashed', linewidth=1)
    ax.axvline(mean - std, color='purple', linestyle='dashed', linewidth=1)
    ax.legend(["Mean", "Standard Deviation"])
    plt.show()
    return array, mean, std, ax

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        np.random.seed(0)
        array, mean, std, ax = f_87()
        self.assertEqual(array.size, ARRAY_SIZE)
        self.assertEqual(mean, 49.6135)
        self.assertEqual(std, 28.5323416100046)
        self.assertEqual(ax.get_title(), 'Histogram of Random Integers')
    def test_case_2(self):
        array, mean, std, ax = f_87()
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
    def test_case_3(self):
        np.random.seed(1)
        array, mean, std, ax = f_87()
        self.assertEqual(mean, 50.0717)
        self.assertEqual(std, 28.559862729186918)
    def test_case_4(self):
        np.random.seed(100)
        array, mean, std, ax = f_87()
        self.assertEqual(mean, 50.2223)
        self.assertEqual(std, 28.494467580742757)
    def test_case_5(self):
        np.random.seed(500)
        array, mean, std, ax = f_87()
        self.assertEqual(mean, 49.8636)
        self.assertEqual(std, 28.516030492338864)
