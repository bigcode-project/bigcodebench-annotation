from scipy import stats
import matplotlib.pyplot as plt


def f_303(data_dict, data_keys):
    """
    Calculate the correlation between two data series and return a scatter plot along with the correlation coefficient.
    
    Parameters:
    data_dict (dict): The dictionary containing data. Keys should match those provided in data_keys.
    data_keys (list): The list of keys (length of 2) used to access data in data_dict for correlation.
    
    Returns:
    tuple: 
        - float: The correlation coefficient.
        - Axes: The scatter plot of the two data series.
    
    Requirements:
    - scipy
    - matplotlib.pyplot
    
    Example:
    >>> data_dict = {'X': [1, 2, 3, 4, 5], 'Y': [2, 3, 5, 7, 8]}
    >>> data_keys = ['X', 'Y']
    >>> correlation, plot = f_303(data_dict, data_keys)
    >>> round(correlation, 4)
    0.9923
    >>> isinstance(plot, plt.Axes)
    True
    """
    x = data_dict[data_keys[0]]
    y = data_dict[data_keys[1]]
    correlation, _ = stats.pearsonr(x, y)
    
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    
    return correlation, ax


import unittest
import numpy as np
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        data_dict = {'X': [1, 2, 3, 4, 5], 'Y': [2, 3, 5, 7, 8]}
        data_keys = ['X', 'Y']
        correlation, plot = f_303(data_dict, data_keys)
        self.assertAlmostEqual(correlation, 0.9923, places=4)
        self.assertTrue(isinstance(plot, plt.Axes))
        
    def test_case_2(self):
        data_dict = {'A': [5, 4, 3, 2, 1], 'B': [1, 2, 3, 4, 5]}
        data_keys = ['A', 'B']
        correlation, plot = f_303(data_dict, data_keys)
        self.assertAlmostEqual(correlation, -1.0, places=4)
        self.assertTrue(isinstance(plot, plt.Axes))
        
    def test_case_3(self):
        data_dict = {'X': [1, 1, 1, 1, 1], 'Y': [1, 1, 1, 1, 1]}
        data_keys = ['X', 'Y']
        correlation, plot = f_303(data_dict, data_keys)
        self.assertTrue(np.isnan(correlation))
        self.assertTrue(isinstance(plot, plt.Axes))
        
    def test_case_4(self):
        data_dict = {'X': [1, 2, 3, 4, 5], 'Y': [1, 4, 9, 16, 25]}
        data_keys = ['X', 'Y']
        correlation, plot = f_303(data_dict, data_keys)
        self.assertAlmostEqual(correlation, 0.9811, places=4)
        self.assertTrue(isinstance(plot, plt.Axes))
        
    def test_case_5(self):
        data_dict = {'X': [1, 3, 5, 7, 9], 'Y': [2, 6, 10, 14, 18]}
        data_keys = ['X', 'Y']
        correlation, plot = f_303(data_dict, data_keys)
        self.assertAlmostEqual(correlation, 1.0, places=4)
        self.assertTrue(isinstance(plot, plt.Axes))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
