import numpy as np
from itertools import chain
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def f_482(L):
    '''
    Convert a list of lists 'L' into a single list of integers, standardize the integers, and plot the standardized values.
    
    Requirements:
    - numpy: For reshaping the list into an array.
    - itertools: For chaining sublists into a single list.
    - sklearn.preprocessing: For standardizing the list of integers.
    - matplotlib.pyplot: For plotting the standardized values.

    Parameters:
    L (list of lists): A list of lists where each sublist contains integers.
    
    Returns:
    matplotlib.axes._subplots.AxesSubplot: A plot displaying the standardized values.

    Examples:
    >>> ax = f_482([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    '''
    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)

    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data)

    fig, ax = plt.subplots()
    ax.plot(standardized_data)
    plt.close(fig)
    return ax
    

import unittest
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = f_482([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 9)

    def test_case_2(self):
        ax = f_482([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 9)

    def test_case_3(self):
        ax = f_482([[1, -2, 3], [-4, 5, -6], [7, -8, 9]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 9)

    def test_case_4(self):
        ax = f_482([[1, 2, 3, 4, 5]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 5)

    def test_case_5(self):
        ax = f_482([[1, 2], [3, 4, 5, 6], [7]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 7)


if __name__ == "__main__":
    run_tests()