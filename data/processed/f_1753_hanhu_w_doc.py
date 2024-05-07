import numpy as np
import matplotlib.pyplot as plt

def f_259(mu, sigma, sample_size):
    """
    Generates a numpy array of random samples drawn from a normal distribution
    and plots the histogram of these samples. This function specifies the mean (mu), 
    standard deviation (sigma), and sample size (sample_size), making it useful 
    for simulating data, conducting statistical experiments, or initializing 
    algorithms that require normally distributed data with visualization.

    Parameters:
        mu (float): The mean of the normal distribution.
        sigma (float): The standard deviation of the normal distribution.
        sample_size (int): The number of samples to draw from the distribution.

    Returns:
        ndarray: A numpy array of shape (sample_size,) containing samples drawn from the
                 specified normal distribution.

    Notes:
        Plots a histogram of the generated samples to show the distribution. The histogram
        features:
        - X-axis labeled "Sample values", representing the value of the samples.
        - Y-axis labeled "Frequency", showing how often each value occurs.
        - Title "Histogram of Generated Samples", describing the content of the graph.
        - Number of bins set to 30, to discretize the sample data into 30 intervals.
        - Alpha value of 0.75 for bin transparency, making the histogram semi-transparent.
        - Color 'blue', giving the histogram a blue color.

    Requirements:
    - numpy
    - matplotlib.pyplot

    Examples:
    >>> data = f_259(0, 1, 1000)
    >>> len(data)
    1000
    >>> isinstance(data, np.ndarray)
    True
    """
    samples = np.random.normal(mu, sigma, sample_size)
    plt.hist(samples, bins=30, alpha=0.75, color='blue')
    plt.title('Histogram of Generated Samples')
    plt.xlabel('Sample values')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    return samples

import unittest
from unittest.mock import patch
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """ Test that the function returns a numpy array. """
        result = f_259(0, 1, 1000)
        self.assertIsInstance(result, np.ndarray)
    def test_sample_size(self):
        """ Test that the returned array has the correct size. """
        result = f_259(0, 1, 1000)
        self.assertEqual(len(result), 1000)
    def test_normal_distribution_properties(self):
        """ Test if the generated samples have the correct mean and standard deviation. """
        mu, sigma = 0, 1
        result = f_259(mu, sigma, 1000000)
        self.assertAlmostEqual(np.mean(result), mu, places=1)
        self.assertAlmostEqual(np.std(result), sigma, places=1)
    @patch('matplotlib.pyplot.show')
    def test_plot_labels_and_title(self, mock_show):
        """ Test if the plot has correct labels and title. """
        with patch('matplotlib.pyplot.hist') as mock_hist:
            f_259(0, 1, 1000)
            args, kwargs = mock_hist.call_args
            self.assertIn('bins', kwargs)
            self.assertEqual(kwargs['bins'], 30)
            self.assertEqual(kwargs['alpha'], 0.75)
            self.assertEqual(kwargs['color'], 'blue')
            self.assertEqual(plt.gca().get_xlabel(), 'Sample values')
            self.assertEqual(plt.gca().get_ylabel(), 'Frequency')
            self.assertEqual(plt.gca().get_title(), 'Histogram of Generated Samples')
    def test_mock_random_normal(self):
        """ Test the function with a mock of np.random.normal. """
        with patch('numpy.random.normal', return_value=np.full(1000, 0.5)) as mock_random_normal:
            mu, sigma = 0, 1
            result = f_259(mu, sigma, 1000)
            mock_random_normal.assert_called_once_with(mu, sigma, 1000)
            self.assertTrue(all(x == 0.5 for x in result))
    def test_output_consistency(self):
        """ Test if repeated calls with the same parameters produce different results. """
        mu, sigma = 0, 1
        result1 = f_259(mu, sigma, 1000)
        result2 = f_259(mu, sigma, 1000)
        self.assertFalse(np.array_equal(result1, result2))
