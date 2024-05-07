import math
from random import randint
import matplotlib.pyplot as plt


def f_60():
    """
    Create and draw a sine wave with random frequency, amplitude and phase shift. The return ax object
    has 'Random Sine Wave' title, 'Time' on the x axis and 'Amplitude' on the y axis.

    Parameters:
    None

    Returns:
    ax (matplotlib.axes._axes.Axes): The axis object of the generated sine wave plot.

    Requirements:
    - math
    - random
    - matplotlib.pyplot

    Example:
    >>> ax = f_60()
    """
    x = [i/100 for i in range(1000)]
    frequency = randint(1, 5)
    amplitude = randint(1, 5)
    phase_shift = randint(0, 360)
    y = [amplitude * math.sin(2 * math.pi * frequency * (xi + phase_shift)) for xi in x]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.grid(True)
    return ax  # Return the axis object for testing

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = f_60()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')
        
    def test_case_2(self):
        ax = f_60()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')
        
    def test_case_3(self):
        ax = f_60()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')
        
    def test_case_4(self):
        ax = f_60()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')
        
    def test_case_5(self):
        ax = f_60()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')
