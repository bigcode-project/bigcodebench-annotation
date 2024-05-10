import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def f_1729(mean, std_dev, num_samples):
    """
    Generates a histogram of samples drawn from a normal distribution and overlays
    the probability density function (PDF) of the normal distribution. The plot is titled
    with the fit results, showing the mean and standard deviation used in the generation.
    The function returns both the plot and the samples generated.

    Parameters:
        mean (float): The mean of the normal distribution.
        std_dev (float): The standard deviation of the normal distribution.
        num_samples (int): The number of samples to draw from the distribution.

    Requirements:
    - numpy
    - scipy.stats.norm
    - matplotlib.pyplot

    Notes:
    - The plot title is "Fit results: mean = %.2f, std = %.2f". This title format on the plot displays the mean and standard deviation
        of the normal distribution used to generate the histogram. The values are presented in a format where %.2f
        is replaced by the floating-point numbers corresponding to `mean` and `std_dev` respectively, rounded to two decimal places.
    - The number of bins is set to 30

    Returns:
        tuple: A tuple containing:
            - matplotlib.figure.Figure: The figure object for the plot.
            - numpy.ndarray: An array of samples drawn from the normal distribution.

    Examples:
    >>> import matplotlib
    >>> samples, fig = f_1729(0, 1, 1000)
    >>> len(samples)
    1000
    >>> type(samples)
    <class 'numpy.ndarray'>
    >>> isinstance(fig, matplotlib.figure.Figure)
    True

    Note: The actual values in the array depend on the random seed and will vary each time the function is called.
    """
    samples = np.random.normal(mean, std_dev, num_samples)
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)
    ax.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mean = %.2f,  std = %.2f" % (mean, std_dev)
    ax.set_title(title)

    return samples, fig

import unittest
import numpy as np

class TestCases(unittest.TestCase):
    def setUp(self):
        """ Set up for each test, fixing the random seed for reproducibility. """
        np.random.seed(0)

    def test_samples_length(self):
        """ Test if the number of generated samples is correct. """
        samples, _ = f_1729(0, 1, 1000)
        self.assertEqual(len(samples), 1000)

    def test_samples_type(self):
        """ Test the type of the samples. """
        samples, _ = f_1729(0, 1, 1000)
        self.assertIsInstance(samples, np.ndarray)

    def test_mean_approximation(self):
        """ Test if the mean of the samples is approximately equal to the specified mean. """
        samples, _ = f_1729(0, 1, 1000)
        self.assertAlmostEqual(np.mean(samples), 0, places=1)

    def test_std_dev_approximation(self):
        """ Test if the standard deviation of the samples is approximately equal to the specified standard deviation. """
        samples, _ = f_1729(0, 1, 1000)
        self.assertAlmostEqual(np.std(samples), 1, places=1)

    def test_plot_title(self):
        """ Test if the plot title correctly reflects the mean and standard deviation. """
        _, fig = f_1729(0, 1, 1000)
        self.assertIn("mean = 0.00,  std = 1.00", fig.axes[0].get_title())

    def test_histogram_bins(self):
        """ Test if the histogram displays the correct number of bins. """
        _, fig = f_1729(0, 1, 1000)
        self.assertEqual(len(fig.axes[0].patches), 30)  # Check for 30 bins, as defined in the function

    def test_pdf_overlay(self):
        """ Test if the probability density function (PDF) is correctly overlayed on the histogram. """
        _, fig = f_1729(0, 1, 1000)
        lines = fig.axes[0].get_lines()
        self.assertGreater(len(lines), 0)  # Ensure that at l

    def test_pdf_overlay_accuracy(self):
        """ Test if the PDF overlay accurately represents the normal distribution. """
        mean, std_dev, num_samples = 0, 1, 1000
        _, fig = f_1729(mean, std_dev, num_samples)
        ax = fig.axes[0]
        line = ax.get_lines()[0]  # Assuming the first line is the PDF
        x, y = line.get_data()
        expected_y = norm.pdf(x, mean, std_dev)
        np.testing.assert_array_almost_equal(y, expected_y, decimal=2)


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
