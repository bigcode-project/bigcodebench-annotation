import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def f_3591(mean, std_dev, n):
    """
    Generates a set of samples from a normal distribution with a specified mean and standard deviation.
    It also visualizes the generated samples by plotting their histogram and the probability density function.

    Parameters:
    mean (float): The mean (mu) of the normal distribution.
    std_dev (float): The standard deviation (sigma) of the distribution.
    n (int): The number of samples to generate.

    Returns:
    numpy.ndarray: An array of generated samples from the normal distribution.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Examples:
    Generate 1000 samples from a normal distribution with mean 0 and standard deviation 1.
    >>> len(f_3591(0, 1, 1000))
    1000

    Generate 500 samples from a normal distribution with mean 5 and standard deviation 2.
    >>> len(f_3591(5, 2, 500))
    500
    """
    samples = np.random.normal(mean, std_dev, n)

    plt.figure(figsize=(10, 6))
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std_dev)
    plt.plot(x, p, 'k', linewidth=2)

    title = f'Normal Distribution: Mean = {mean}, Std Dev = {std_dev}'
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.show()

    return samples

import unittest
class TestCases(unittest.TestCase):
    def test_sample_length(self):
        # Test if the function returns the correct number of samples
        samples = f_3591(0, 1, 1000)
        self.assertEqual(len(samples), 1000)
    def test_sample_mean(self):
        # Test if the mean of the samples is approximately equal to the specified mean
        samples = f_3591(0, 1, 100000)
        self.assertAlmostEqual(np.mean(samples), 0, places=1)
    def test_sample_std_dev(self):
        # Test if the standard deviation of the samples is approximately equal to the specified standard deviation
        samples = f_3591(0, 1, 100000)
        self.assertAlmostEqual(np.std(samples), 1, places=1)
    def test_negative_std_dev(self):
        # Test if a ValueError is raised for negative standard deviations
        with self.assertRaises(ValueError):
            f_3591(0, -1, 1000)
    def test_zero_samples(self):
        # Test if the function can handle a request for zero samples
        samples = f_3591(0, 1, 0)
        self.assertEqual(len(samples), 0)
    def test_return_type(self):
        # Test if the function returns a numpy array
        samples = f_3591(0, 1, 100)
        self.assertIsInstance(samples, np.ndarray)
    def test_non_integer_samples(self):
        # Test if the function raises a TypeError for non-integer n
        with self.assertRaises(TypeError):
            f_3591(0, 1, '100')
    def test_non_numeric_mean_or_std(self):
        # Test if the function raises a TypeError for non-numeric mean or std_dev
        with self.assertRaises(TypeError):
            f_3591('0', 1, 100)
        with self.assertRaises(TypeError):
            f_3591(0, '1', 100)
    def test_very_small_n(self):
        # Test if the function behaves correctly for very small n
        samples = f_3591(0, 1, 1)
        self.assertEqual(len(samples), 1)
