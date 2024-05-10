import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


ANGLES = np.arange(0, 2*np.pi, 0.01)

def f_251(n_waves, seed=0):
    """
    Generate a series of n sine waves with increasing frequency with a fidelity of 0.01 radians as 
    provided by the ANGLES array. The amplitude of each wave is 1. The function returns a list of
    numpy arrays with the y values of the sine waves. Additionally, calculate the Fast Fourier Transform
    (FFT) of the mixed signal and plot the histogram of the magnitude of the FFT data. If n_waves is less
    than 1, return an empty list for the sine waves, an empty array for the FFT data, and None for the axes
    object.
    
    Parameters:
    n_waves (int): The number of sine waves in the series.
    seed (int, Optional): The seed for the random number generator. Defaults to 0.
    
    Returns:
    list: A list of numpy arrays with the y values of the sine waves.
    np.array: FFT data.
    plt.Axes: The axes object of the plot.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.fft

    Example:
    >>> sine_waves, fft_data, ax = f_251(5)
    >>> len(sine_waves)
    5
    >>> fft_data.shape
    (629,)
    """
    np.random.seed(seed)
    sine_wave_series = []

    if n_waves < 1:
        return sine_wave_series, np.array([]), None

    for frequency in range(1, n_waves+1):
        wave = np.sin(frequency * ANGLES)
        sine_wave_series.append(wave)

    fft_data = fft(np.sum(sine_wave_series, axis=0))
    _, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    return sine_wave_series, fft_data, ax

import unittest
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing basic functionality with 3 waves
        sine_waves, fft_data, ax = f_251(3)
        self.assertEqual(len(sine_waves), 3)  # Should return 3 waves
        self.assertTrue(isinstance(sine_waves[0], np.ndarray))  # Each wave should be a numpy array
        # Testing if the FFT data is a numpy array
        self.assertIsInstance(fft_data, np.ndarray)
        # Testing if the axes object is returned
        self.assertIsInstance(ax, plt.Axes)

    def test_case_2(self):
        # Testing with 5 waves
        sine_waves, fft_data, ax = f_251(5)
        self.assertEqual(len(sine_waves), 5)
        self.assertTrue(isinstance(sine_waves[4], np.ndarray))
        # Test the axis limits of the histogram
        self.assertAlmostEqual(ax.get_xlim()[1], 331.2, places=1)
        # Test the axis bins
        self.assertEqual(len(ax.patches), 10)

    def test_case_3(self):
        # Testing with 1 wave
        sine_waves, fft_data, ax = f_251(1, seed=5)
        self.assertEqual(len(sine_waves), 1)
        self.assertTrue(isinstance(sine_waves[0], np.ndarray))
        # Test the FFT data
        self.assertIsInstance(fft_data, np.ndarray)
        self.assertEqual(fft_data.shape, (629,))
        # test the maximum value of the FFT data
        self.assertAlmostEqual(np.max(np.abs(fft_data)), 314.3, places=1)

    def test_case_4(self):
        # Testing edge case with 0 waves
        sine_waves, fft_data, ax = f_251(0)
        self.assertEqual(len(sine_waves), 0)
        self.assertEqual(fft_data.shape, (0,))
        self.assertIsNone(ax)

    def test_case_5(self):
        # Testing with negative number, should return empty list
        sine_waves, fft_data, ax = f_251(-5)
        self.assertEqual(len(sine_waves), 0)
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
