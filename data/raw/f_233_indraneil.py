import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt


def f_233(data):
    """
    Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1.
    
    Parameters:
    data (list of tuple): A list of tuples where each tuple contains two integers.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plot for further manipulation and testing.
    
    Requirements:
    - numpy
    - operator
    - matplotlib.pyplot
    
    Example:
    >>> ax = f_233([(10, 20), (30, 40), (25, 50)])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    max_tuple = max(data, key=itemgetter(1))
    tuples = np.array(data)
    x = tuples[:,0]
    y = tuples[:,1]
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data')
    ax.scatter(*max_tuple, color='red', label='Max Tuple')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Max Tuple Highlighted')
    ax.legend()
    return ax


import unittest
import doctest


class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = [(10, 20), (30, 50), (60, 25), (80, 65)]
        ax = f_233(data)
        
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Max Tuple Highlighted")
        
        # Check the x and y axis labels
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "y")
        
        # Check the data points
        x_data, y_data = ax.collections[0].get_offsets().T
        self.assertTrue(np.array_equal(x_data, [10, 30, 60, 80]))
        self.assertTrue(np.array_equal(y_data, [20, 50, 25, 65]))
        
        # Check the highlighted point (Max Tuple)
        x_max, y_max = ax.collections[1].get_offsets().T
        self.assertEqual(x_max, 80)
        self.assertEqual(y_max, 65)
        
    def test_case_2(self):
        data = [(5, 10), (15, 35), (40, 55), (70, 30)]
        ax = f_233(data)
        
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Max Tuple Highlighted")
        
        # Check the x and y axis labels
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "y")
        
        # Check the data points
        x_data, y_data = ax.collections[0].get_offsets().T
        self.assertTrue(np.array_equal(x_data, [5, 15, 40, 70]))
        self.assertTrue(np.array_equal(y_data, [10, 35, 55, 30]))
        
        # Check the highlighted point (Max Tuple)
        x_max, y_max = ax.collections[1].get_offsets().T
        self.assertEqual(x_max, 40)
        self.assertEqual(y_max, 55)
        
    def test_case_3(self):
        data = [(3, 7), (9, 11), (13, 17), (19, 23)]
        ax = f_233(data)
        
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Max Tuple Highlighted")
        
        # Check the x and y axis labels
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "y")
        
        # Check the data points
        x_data, y_data = ax.collections[0].get_offsets().T
        self.assertTrue(np.array_equal(x_data, [3, 9, 13, 19]))
        self.assertTrue(np.array_equal(y_data, [7, 11, 17, 23]))
        
        # Check the highlighted point (Max Tuple)
        x_max, y_max = ax.collections[1].get_offsets().T
        self.assertEqual(x_max, 19)
        self.assertEqual(y_max, 23)
    
    def test_case_4(self):
        data = [(2, 3), (4, 5), (6, 7), (8, 9)]
        ax = f_233(data)
        
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Max Tuple Highlighted")
        
        # Check the x and y axis labels
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "y")
        
        # Check the data points
        x_data, y_data = ax.collections[0].get_offsets().T
        self.assertTrue(np.array_equal(x_data, [2, 4, 6, 8]))
        self.assertTrue(np.array_equal(y_data, [3, 5, 7, 9]))
        
        # Check the highlighted point (Max Tuple)
        x_max, y_max = ax.collections[1].get_offsets().T
        self.assertEqual(x_max, 8)
        self.assertEqual(y_max, 9)
        
    def test_case_5(self):
        data = [(20, 30), (40, 50), (60, 10), (80, 90)]
        ax = f_233(data)
        
        # Check the title of the plot
        self.assertEqual(ax.get_title(), "Max Tuple Highlighted")
        
        # Check the x and y axis labels
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "y")
        
        # Check the data points
        x_data, y_data = ax.collections[0].get_offsets().T
        self.assertTrue(np.array_equal(x_data, [20, 40, 60, 80]))
        self.assertTrue(np.array_equal(y_data, [30, 50, 10, 90]))
        
        # Check the highlighted point (Max Tuple)
        x_max, y_max = ax.collections[1].get_offsets().T
        self.assertEqual(x_max, 80)
        self.assertEqual(y_max, 90)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
