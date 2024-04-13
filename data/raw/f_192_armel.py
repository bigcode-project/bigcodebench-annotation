import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Constants
INITIAL_GUESS = [1.0, 0.0, 0.0]

def f_192(data, attribute):
    '''
    Adjust a sine function to a set of data points and record the original data and the adapted curve. That is, given a set of points {(x_i, y_i)}_{i=1}^{N} find a, b and c such that for all i, a*sin(b*x_i + c) approximates y_i.
    You will try to get to the optimal parameters a, b and c by starting from a initial guess stored in the constant INITIAL_GUESS
    
    Parameters:
    data (numpy.ndarray): The data points. Each row of the array is expected to represent a point in 2D space, with the first element being the x-coordinate and the second element being the y-coordinate.
    attribute (str): The attribute to label on the y-axis of the plot.

    Returns:
    tuple: A tuple containing:
        - list: The coefficients of the fitted sinusoidal function.
        - Axes: The Axes object of the plot.

    Requirements:
    - numpy
    - scipy.optimize
    - matplotlib

    Example:
    >>> data = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
    >>> coeffs, ax = f_192(data, "y")
    >>> coeffs
    [1.0, 0.0, 0.0]
    '''
    def sin_func(x, a, b, c):
        return a * np.sin(b * x + c)

    popt, pcov = curve_fit(sin_func, data[:,0], data[:,1], p0=INITIAL_GUESS)

    fig, ax = plt.subplots()
    ax.plot(data[:,0], data[:,1], 'b-', label='data')
    ax.plot(data[:,0], sin_func(data[:,0], *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    ax.set_xlabel('x')
    ax.set_ylabel(attribute)
    ax.legend()
    plt.show()

    return list(popt), ax

import numpy as np
import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_192 function."""
    def test_case_1(self):
        data = np.array([
            [0, 0],
            [np.pi / 2, 1],
            [np.pi, 0],
            [3 * np.pi / 2, -1],
            [2 * np.pi, 0]
        ])
        coeffs, ax = f_192(data, "y")
        self.assertTrue(len(coeffs) == 3)
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "y")
        self.assertTrue(len(ax.legend().get_texts()) == 2)

    def test_case_2(self):
        data = np.array([
            [0, 1],
            [np.pi / 2, 0],
            [np.pi, -1],
            [3 * np.pi / 2, 0],
            [2 * np.pi, 1]
        ])
        coeffs, ax = f_192(data, "amplitude")
        self.assertTrue(len(coeffs) == 3)
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "amplitude")
        self.assertTrue(len(ax.legend().get_texts()) == 2)
        
    def test_case_3(self):
        data = np.array([
            [0, 0.5],
            [np.pi / 2, 1.5],
            [np.pi, 0.5],
            [3 * np.pi / 2, -0.5],
            [2 * np.pi, 0.5]
        ])
        coeffs, ax = f_192(data, "magnitude")
        self.assertTrue(len(coeffs) == 3)
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "magnitude")
        self.assertTrue(len(ax.legend().get_texts()) == 2)

    def test_case_4(self):
        data = np.array([
            [1,1], 
            [2,2], 
            [3,3], 
            [4,4], 
            [5,5]
        ])
        with self.assertRaises(RuntimeError):
            f_192(data, "y")

    def test_case_5(self):
        data = np.array([
            [1,5], 
            [2,4], 
            [3,3], 
            [4,2], 
            [5,1]
        ])
        with self.assertRaises(RuntimeError):
            f_192(data, "y")
    def test_case_6(self):
        data = np.array(
            [
                [-np.pi, 0],
                [-np.pi/2, -1],
                [-np.pi/4, -1/np.sqrt(2)],
                [0, 0], 
                [np.pi/4, 1/np.sqrt(2)], 
                [np.pi/2, 1],
                [np.pi, 0]
            ]
        )
        coeffs, ax = f_192(data, "sinus")
        self.assertTrue(len(coeffs) == 3)
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "sinus")
        self.assertTrue(len(ax.legend().get_texts()) == 2)
        self.assertTrue(np.allclose(coeffs, np.array([1.0, 1.0, 0.0])))
        
if __name__ == "__main__" :
    run_tests()