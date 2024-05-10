import numpy as np
import matplotlib.pyplot as plt
import itertools


def f_252(data_list):
    """
    Unzips the provided list of tuples and plots the numerical values for each position.
    
    Parameters:
    - data_list (list of tuples): A list containing tuples. Each tuple should contain a character and two numerical values.
    
    Returns:
    - Axes: The plot with the unzipped numerical values.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - itertools

    Raises:
    - ValueError: If the data_list is empty.
    
    Example:
    >>> plot = f_252([('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)])
    >>> type(plot)
    <class 'matplotlib.axes._axes.Axes'>
    """
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    if len(unzipped_data) == 0:
        raise ValueError('Empty data_list')
    
    fig, ax = plt.subplots()
    for i, column in enumerate(unzipped_data[1:], start=1):
        ax.plot(column, label='Position {}'.format(i))
    ax.legend()
    return ax


import unittest
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        plot = f_252(data_list)
        self.assertIsInstance(plot, type(plt.gca()))

    def test_case_2(self):
        data_list = [('a', 6, 7), ('b', 7, 8), ('c', 8, 9)]
        plot = f_252(data_list)
        self.assertIsInstance(plot, type(plt.gca()))
        # Test the plot data
        self.assertEqual(len(plot.lines), 2)

    def test_case_3(self):
        data_list = []
        with self.assertRaises(ValueError):  # Expecting a ValueError due to empty data_list
            f_252(data_list)

    def test_case_4(self):
        data_list = [('a', 10, 11), ('b', 11, 12), ('c', 12, 13), ('d', 13, 14)]
        plot = f_252(data_list)
        self.assertIsInstance(plot, type(plt.gca()))
        # Test the plot data array
        self.assertEqual(len(plot.lines), 2)
        # Test the plot limits
        self.assertAlmostEqual(plot.get_xlim()[0], -0.15, places=1)
        self.assertAlmostEqual(plot.get_xlim()[1], 3.15, places=1)

    def test_case_5(self):
        data_list = [('a', np.nan, np.nan), ('b', np.nan, np.nan)]
        plot = f_252(data_list)
        self.assertIsInstance(plot, type(plt.gca()))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
