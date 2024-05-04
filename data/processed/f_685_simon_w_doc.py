import time
import numpy as np


def f_175(samples=10, delay=0.1):
    """
    Make a delay for a given amount of time for a specified number of samples,
    measure the actual delay and calculate the statistical properties of the
    delay times.

    Parameters:
    - samples (int): Number of samples for which the delay is measured.
                     Default is 10.
    - delay (float): Amount of time (in seconds) for each delay.
                     Default is 0.1 second.

    Returns:
    tuple: The mean and standard deviation of the delay times.

    Requirements:
    - time
    - numpy

    Example:
    >>> mean, std = f_175(samples=5, delay=0.05)
    >>> print(f'Mean: %.3f, Std: %.1f' % (mean, std))
    Mean: 0.050, Std: 0.0
    >>> mean, std = f_175(100, 0.001)
    >>> print(f'Mean: %.3f, Std: %.4f' % (mean, std))
    Mean: 0.001, Std: 0.0000
    """
    delay_times = []
    for _ in range(samples):
        t1 = time.time()
        time.sleep(delay)
        t2 = time.time()
        delay_times.append(t2 - t1)
    delay_times = np.array(delay_times)
    mean = np.mean(delay_times)
    std = np.std(delay_times)
    return mean, std

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        start = time.time()
        mean, std = f_175(samples=100, delay=0.001)
        end = time.time()
        self.assertAlmostEqual(100 * 0.001, end-start, delta=3)
        self.assertAlmostEqual(mean, 0.001, places=0)
        self.assertTrue(0 <= std <= 0.01)
        
    def test_case_2(self):
        start = time.time()
        mean, std = f_175(samples=3, delay=0.1)
        end = time.time()
        self.assertAlmostEqual(3 * 0.1, end-start, places=1)
        self.assertAlmostEqual(mean, 0.1, delta=0.2)
        self.assertTrue(0 <= std <= 0.01)
    def test_case_3(self):
        start = time.time()
        mean, std = f_175(samples=2, delay=0.2)
        end = time.time()
        self.assertAlmostEqual(2 * 0.2, end-start, places=1)
        self.assertTrue(0.19 <= mean <= 0.21)
        self.assertTrue(0 <= std <= 0.02)
    def test_case_4(self):
        start = time.time()
        mean, std = f_175(samples=100, delay=0.05)
        end = time.time()
        self.assertTrue(3 <= end-start <= 7)
        self.assertTrue(0.03 <= mean <= 0.07)
        self.assertTrue(0 <= std <= 0.05)
    def test_case_5(self):
        start = time.time()
        mean, std = f_175(samples=1, delay=1)
        end = time.time()
        self.assertAlmostEqual(1, end-start, places=0)
        self.assertTrue(0.9 <= mean <= 1.1)
        self.assertTrue(0 <= std <= 0.1)
