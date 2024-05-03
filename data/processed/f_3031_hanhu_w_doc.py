import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window

def f_160(amplitude, frequency, time):
    """
    Generates and plots a complex wave with a specified amplitude and frequency over given time points,
    applying a Hann window to reduce edge effects. The wave is represented as a complex number where the real part 
    is the cosine component, and the imaginary part is the sine component. It returns both the wave and the plot object.

    Parameters:
        amplitude (float): The amplitude of the complex wave.
        frequency (float): The frequency of the complex wave.
        time (numpy.ndarray): The time points to generate the wave.

    Returns:
        numpy.ndarray: The generated complex wave as a numpy array of complex numbers.
        matplotlib.figure.Figure: The figure object of the plot.
        matplotlib.axes.Axes: The axes object of the plot.

    Requirements:
    - numpy
    - math
    - matplotlib.pyplot
    - scipy.signal.get_window

    Notes:
    - The plot title is "Complex Wave with Hann Window".
    - The x-label of the plot is "Time".
    - The y-label of the plot is "Amplitude".
    - The plot displays both the real and imaginary parts of the complex wave.

    Examples:
    >>> wave, fig, ax = f_160(1, 1, np.linspace(0, 1, 10, endpoint=False))
    >>> len(wave) == 10
    True
    >>> isinstance(wave[0], complex)
    True
    """
    wave = amplitude * np.exp(1j * 2 * math.pi * frequency * time)
    window = get_window('hann', time.size)  # Apply a Hann window
    wave *= window  # Apply the window to the wave

    # Plot the wave
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(time, np.real(wave), label="Real Part")
    ax.plot(time, np.imag(wave), label="Imaginary Part")
    ax.set_title("Complex Wave with Hann Window")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.legend()

    return wave, fig, ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.signal import get_window
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up common constants for the tests."""
        self.amplitude = 1
        self.frequency = 5
        self.time = np.linspace(0, 1, 500, endpoint=False)
    def test_return_types(self):
        """Test that the function returns a numpy array, a matplotlib figure, and axes objects."""
        wave, fig, ax = f_160(self.amplitude, self.frequency, self.time)
        self.assertIsInstance(wave, np.ndarray)
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, plt.Axes)
    def test_array_length(self):
        """Test the length of the returned array matches the length of the time array."""
        wave, _, _ = f_160(self.amplitude, self.frequency, self.time)
        self.assertEqual(len(wave), len(self.time))
    def test_wave_properties(self):
        """Test that the wave properties conform to expected cosine and sine functions with Hann window applied."""
        wave, _, _ = f_160(self.amplitude, self.frequency, self.time)
        window = get_window('hann', self.time.size)  # Apply a Hann window
        expected_wave = self.amplitude * np.exp(1j * 2 * math.pi * self.frequency * self.time) * window
        np.testing.assert_array_almost_equal(wave, expected_wave)
    def test_zero_amplitude(self):
        """Test that the wave is zero throughout when amplitude is zero."""
        wave, _, _ = f_160(0, self.frequency, self.time)
        self.assertTrue(np.all(wave == 0))
    def test_different_frequencies(self):
        """Test the function with different frequencies to ensure the wave changes accordingly."""
        wave_1, _, _ = f_160(self.amplitude, 1, self.time)
        wave_2, _, _ = f_160(self.amplitude, 2, self.time)
        self.assertFalse(np.array_equal(wave_1, wave_2))
    def test_negative_frequency(self):
        """Test that the function correctly handles negative frequencies with Hann window applied."""
        wave, _, _ = f_160(self.amplitude, -1, self.time)
        window = get_window('hann', self.time.size)  # Apply a Hann window
        expected_wave = self.amplitude * np.exp(-1j * 2 * math.pi * self.time) * window
        np.testing.assert_array_almost_equal(wave, expected_wave)
    def test_plot_title(self):
        """Test that the plot title is correctly set."""
        _, fig, _ = f_160(self.amplitude, self.frequency, self.time)
        self.assertEqual(fig.axes[0].get_title(), "Complex Wave with Hann Window")
    def test_plot_x_label(self):
        """Test that the x-axis label is correctly set to 'Time'."""
        _, _, ax = f_160(self.amplitude, self.frequency, self.time)
        self.assertEqual(ax.get_xlabel(), "Time")
    def test_plot_y_label(self):
        """Test that the y-axis label is correctly set to 'Amplitude'."""
        _, _, ax = f_160(self.amplitude, self.frequency, self.time)
        self.assertEqual(ax.get_ylabel(), "Amplitude")
    def test_plot_lines(self):
        """Test that the plot includes both real and imaginary parts of the complex wave."""
        _, _, ax = f_160(self.amplitude, self.frequency, self.time)
        lines = ax.get_lines()
        # Assu the first line is the real part and the second line is the imaginary part
        self.assertEqual(len(lines), 2, "Plot does not contain two lines for real and imaginary parts")
