import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt


def f_250(original):
    """
    Create a numeric array from the "original" list, calculate Fast Fourier Transform (FFT) and record the 
    original and FFT data. Additionally, plot the histogram of the magnitude of the FFT data and return the
    axes object of the plot. For an empty list, return an empty array for the FFT data and None for the 
    axes object.

    Parameters:
    original (list): The original list with (str, int) tuples to be unzipped into a numpy array.

    Returns:
    np.array: A numpy array for the original data.
    np.array: FFT data.
    plt.Axes: The axes object of the plot.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.fft

    Example:
    >>> original = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    >>> arr, fft_data, ax  = f_250(original)
    >>> print(arr)
    [1 2 3 4]
    >>> print(fft_data)
    [10.-0.j -2.+2.j -2.-0.j -2.-2.j]
    """
    arr = np.array([b for (_, b) in original])

    if arr.size == 0:
        fft_data = np.array([])
        return arr, fft_data, None

    fft_data = fft(arr)
    _, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    return arr, fft_data, ax

import unittest
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        original = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
        arr, fft_data, _ = f_250(original)
        self.assertTrue(np.array_equal(arr, np.array([1, 2, 3, 4])))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (4,))

    def test_case_2(self):
        original = [('a', i) for i in range(1, 101)]
        arr, fft_data, ax = f_250(original)
        self.assertTrue(np.array_equal(arr, np.array(range(1, 101))))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (100,))
        # Test that the plot is created
        self.assertIsInstance(ax, plt.Axes)
        # Test the axis limits
        self.assertEqual(ax.get_xlim(), (-200.0, 5300.0))


    def test_case_3(self):
        original = [('a', 5) for i in range(10)]
        arr, fft_data, _ = f_250(original)
        self.assertTrue(np.array_equal(arr, np.array([5]*10)))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (10,))

    def test_case_4(self):
        original = [('a', i) for i in range(10)]
        arr, fft_data, ax = f_250(original)
        self.assertTrue(np.array_equal(arr, np.array(range(10))))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (10,))
        # Test the plot data array
        self.assertEqual(len(ax.get_children()), 20)
        # Test the plot limits
        self.assertEqual(ax.get_xlim(), (3.0, 47.0))

    def test_case_5(self):
        original = []
        arr, fft_data, ax = f_250(original)
        self.assertTrue(np.array_equal(arr, np.array([])))
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (0,))
        self.assertIsNone(ax)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
