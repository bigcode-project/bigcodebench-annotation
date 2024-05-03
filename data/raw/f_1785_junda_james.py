import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def f_1785(data=np.random.normal(loc=10, scale=5, size=100), seed=0):
    """
    Fit a normal distribution to the data and plot the PDF over the data histogram. Returns the fit parameters along with the plot.
    
    Parameters:
    - data (array, optional): NumPy array of data to fit. Default is a random normal distribution with loc=10, scale=5, size=100.
    - seed (int, optional): Seed for NumPy's random number generator. Defaults to 0.

    Returns:
    - ax (matplotlib.axes.Axes): A matplotlib Axes object with the histogram and PDF plot. The plot includes a histogram of the data in blue, a fitted PDF in red, title 'Histogram with Fitted PDF', x-axis label 'Data Value', and y-axis label 'Probability'.
    - mu (float): Estimated mean of the distribution.
    - sigma (float): Estimated standard deviation of the distribution.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy

    Example:
    >>> np.random.seed(0)  # Setting seed for reproducibility
    >>> data = np.random.normal(loc=10, scale=5, size=100)
    >>> ax, mu, sigma = f_1785(data)
    """
    np.random.seed(seed)
    if data is None:
        data = np.random.normal(loc=10, scale=5, size=100)

    # Fit a normal distribution to the data
    mu, sigma = stats.norm.fit(data)

    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, density=True, alpha=0.7, color='blue')

    # Plot PDF
    x = np.linspace(min(data), max(data), 100)
    pdf = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, pdf, 'r-', linewidth=2)

    # Customize plot
    ax.set_title('Histogram with Fitted PDF')
    ax.set_xlabel('Data Value')
    ax.set_ylabel('Probability')

    plt.show()

    return ax, mu, sigma

import unittest
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Assuming f_1785 is defined as previously described

class TestCases(unittest.TestCase):
    def setUp(self):
        # Seed set for reproducibility in tests
        np.random.seed(0)
        self.data = np.random.normal(loc=10, scale=5, size=100)

    def test_return_type_and_values(self):
        """Test the types of return values and fit parameters."""
        ax, mu, sigma = f_1785(self.data, seed=0)
        self.assertIsInstance(ax, plt.Axes, "ax should be a matplotlib Axes instance")
        self.assertIsInstance(mu, float, "mu should be a float")
        self.assertIsInstance(sigma, float, "sigma should be a float")
        # Check if mu and sigma are within expected bounds, given the data generation parameters
        self.assertAlmostEqual(mu, 10, delta=1, msg="Estimated mu should be close to 10")
        self.assertAlmostEqual(sigma, 5, delta=1, msg="Estimated sigma should be close to 5")

    def test_plot_labels(self):
        """Ensure plot labels and title match specified strings."""
        ax, mu, sigma = f_1785(self.data, seed=0)
        self.assertEqual(ax.get_title(), 'Histogram with Fitted PDF', "Plot title does not match")
        self.assertEqual(ax.get_xlabel(), 'Data Value', "X-axis label does not match")
        self.assertEqual(ax.get_ylabel(), 'Probability', "Y-axis label does not match")

    def test_custom_data(self):
        """Test the function with custom, non-default data."""
        custom_data = np.random.exponential(scale=2, size=100)
        ax, mu, sigma = f_1785(custom_data, seed=1)
        self.assertIsInstance(ax, plt.Axes, "ax should be a matplotlib Axes instance when custom data is used")

    def test_empty_data(self):
        """Test the function's response to empty data."""
        with self.assertRaises(ValueError):
            f_1785(np.array([]), seed=2)

    def test_random_seed_effect(self):
        """Verify that setting the seed affects the results consistently."""
        _, mu1, sigma1 = f_1785(seed=42)
        _, mu2, sigma2 = f_1785(seed=42)
        self.assertEqual(mu1, mu2, "Mu should be the same for the same seed")
        self.assertEqual(sigma1, sigma2, "Sigma should be the same for the same seed")

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
