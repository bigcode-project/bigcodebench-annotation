import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


def task_func(signal, precision=2, seed=777):
    """
    Calculate the one-dimensional discrete N-point Fourier Transform (DFT) for a real or complex sequence (signal) 
    using the Fast Fourier Transform (FFT) algorithm. Plot the original signal and the transformed signal, rounding 
    the transformed signal values to the specified accuracy.

    Parameters:
    - signal (array): An array representing the signal.
    - precision (int, optional): The number of decimal places to which to round the transformed signal values. 
                                 Defaults to 2.
    - seed (int, optional): The seed for the random number generator. Defaults to 777.

    Returns:
    - ndarray: A numpy array of transformed signal values (rounded to the specified precision).
    - tuple: A tuple containing the Axes objects for the original signal and transformed signal plots.

    Requirements:
    - numpy
    - matplotlib
    - scipy

    Example:
    >>> signal = np.array([0., 1., 0., -1.])
    >>> transformed_signal, (ax1, ax2) = task_func(signal)
    >>> print(transformed_signal)
    [0.-0.j 0.-2.j 0.-0.j 0.+2.j]
    """
    np.random.seed(seed)
    transformed_signal = fft(signal)
    transformed_signal_rounded = np.round(transformed_signal, precision).tolist()
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(signal)
    ax[0].set_title('Original Signal')
    ax[1].plot(transformed_signal_rounded)
    ax[1].set_title('Transformed Signal')
    plt.tight_layout()  # Adjust layout to avoid overlap
    return np.array(transformed_signal_rounded), ax

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a constant signal
        signal = np.array([1.0, 1.0, 1.0, 1.0])
        transformed_signal, (ax1, ax2) = task_func(signal)
        
        # Assert transformed signal
        self.assertTrue(all(transformed_signal == np.array([4.0, 0.0, 0.0, 0.0])))
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')
    
    def test_case_2(self):
        # Test with a sine wave signal
        signal = np.sin(np.linspace(0, 2 * np.pi, 100))
        transformed_signal, (ax1, ax2) = task_func(signal, precision=3)
        
        # Assert transformed signal values (checking just the first few)
        self.assertTrue(np.isclose(transformed_signal[0], 0.0, atol=1e-3))
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')
    
    def test_case_3(self):
        # Test with a random signal
        signal = np.random.rand(50)
        transformed_signal, (ax1, ax2) = task_func(signal, precision=4)
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')
    
    def test_case_4(self):
        # Test with a short signal
        signal = np.array([0., 1., 0., -1.])
        transformed_signal, (ax1, ax2) = task_func(signal, precision=1)
        
        # Assert transformed signal
        self.assertTrue(all(transformed_signal == np.array([-0.-0.j, 0.-2.j, 0.-0.j, 0.+2.j])))
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')
    
    def test_case_5(self):
        # Test with a complex signal
        signal = np.array([1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j])
        transformed_signal, (ax1, ax2) = task_func(signal, precision=2)
        
        # Assert plot titles
        self.assertEqual(ax1.get_title(), 'Original Signal')
        self.assertEqual(ax2.get_title(), 'Transformed Signal')
