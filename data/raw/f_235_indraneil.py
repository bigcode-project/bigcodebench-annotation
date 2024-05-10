import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt


def f_235(data):
    """
    Draw a scatter plot of dots and mark the point with the maximum y-value. Return the axes object as
    well as the maximum y-value point. 
    
    Parameters:
    data (list of tuples): A list where each tuple contains two floats representing x and y coordinates.
    
    Returns:
    matplotlib.axes.Axes: Axes object with the scatter plot.
    tuple: The point with the maximum y-value.
    
    Requirements:
    - numpy
    - operator
    - matplotlib.pyplot

    Example:
    >>> ax, point = f_235([(0.1, 0.2), (0.5, 0.6), (0.3, 0.9)])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    max_y_point = max(data, key=itemgetter(1))
    points = np.array(data)
    x = points[:,0]
    y = points[:,1]

    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Points')
    ax.scatter(*max_y_point, color='red', label='Max Y Point')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    return ax, max_y_point


import unittest
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with three points where the third point has the highest y-value
        ax, _ = f_235([(0.1, 0.2), (0.5, 0.6), (0.3, 0.9)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        
    def test_case_2(self):
        # Testing with another set of points
        ax, _ = f_235([(0.2, 0.3), (0.6, 0.7), (0.4, 0.8)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        
    def test_case_3(self):
        # Testing with another set of points
        ax, max_y_point = f_235([(0.3, 0.4), (0.7, 0.8), (0.5, 0.7)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.7, 0.8))
        
    def test_case_4(self):
        # Testing with another set of points
        ax, max_y_point = f_235([(0.4, 0.5), (0.8, 0.9), (0.6, 0.6)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.8, 0.9))

    def test_case_5(self):
        # Testing with another set of points
        ax, max_y_point = f_235([(0.5, 0.6), (0.9, 0.1), (0.7, 0.5)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.5, 0.6))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
