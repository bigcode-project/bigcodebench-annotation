import matplotlib.pyplot as plt
from itertools import zip_longest


# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

def f_254(data, labels):
    """    
    Plot a list of data with different colors. If there are more data series than the predefined colors, 
    the function cycles through the colors. In case of even more series than colors + labels, 'black' is used.
    
    Parameters:
    data (list): A list of lists, each representing a series of data.
    labels (list): A list of labels for the data series.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plot.
    
    Requirements:
    - matplotlib.pyplot
    - itertools.zip_longest
    - Predefined colors are ['red', 'green', 'blue', 'yellow', 'purple'].
    
    Example:
    >>> data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
    >>> labels = ['Series 1', 'Series 2', 'Series 3']
    >>> ax = f_254(data, labels)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    fig, ax = plt.subplots()
    for series, label, color in zip_longest(data, labels, COLORS, fillvalue='black'):
        ax.plot(series, label=label, color=color)
        
    ax.legend()
    return ax


import unittest
import doctest


class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
        labels = ['Series 1', 'Series 2', 'Series 3']
        ax = f_254(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_color(), 'red')
        self.assertEqual(lines[1].get_color(), 'green')
        self.assertEqual(lines[2].get_color(), 'blue')

    def test_case_2(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        labels = ['A', 'B', 'C', 'D']
        ax = f_254(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[3].get_color(), 'yellow')

    def test_case_3(self):
        data = [[1, 2], [3, 4]]
        labels = ['X', 'Y']
        ax = f_254(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_color(), 'red')
        self.assertEqual(lines[1].get_color(), 'green')

    def test_case_4(self):
        data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
        labels = ['Series 1', 'Series 2', 'Series 3', 'Series 4', 'Series 5', 'Series 6']
        ax = f_254(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[5].get_color(), 'black')
        
    def test_case_5(self):
        data = [[1, 2, 3], [4, 5, 6]]
        labels = []
        ax = f_254(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_color(), 'red')
        self.assertEqual(lines[1].get_color(), 'green')


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
