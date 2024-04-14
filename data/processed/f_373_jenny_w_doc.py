import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def f_373(n_samples=1000, mu=0, sigma=1, random_seed=0):
    """
    Generates a histogram and a probability density function (PDF) plot for a specified normal distribution.

    This function draws n_samples from a normal distribution defined by mean (mu) and standard deviation (sigma),
    plots a histogram of the samples, and overlays the PDF of the normal distribution. The histogram's density
    is normalized, and the PDF is plotted with a red line with linewidth=2.

    Parameters:
    - n_samples (int): Number of samples for the histogram. Must be greater than 0. Default is 1000.
    - mu (float): Mean for the normal distribution. Default is 0.
    - sigma (float): Standard deviation for the normal distribution. Must be greater than 0. Default is 1.
    - random_seed (int): Random seed for reproducibility. Defaults to 0.

    Returns:
    - ax (matplotlib.axes._axes.Axes): Axes object with the histogram and PDF plotted.
    - samples (numpy.ndarray): Generated sample data.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.stats.norm

    Example:
    >>> ax, samples = f_373()
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(-5.0, 0, '−5'), Text(-4.0, 0, '−4'), Text(-3.0, 0, '−3'), Text(-2.0, 0, '−2'), Text(-1.0, 0, '−1'), Text(0.0, 0, '0'), Text(1.0, 0, '1'), Text(2.0, 0, '2'), Text(3.0, 0, '3'), Text(4.0, 0, '4'), Text(5.0, 0, '5')]
    """
    if n_samples <= 0 or sigma <= 0:
        raise ValueError("Invalid n_samples or sigma")
    np.random.seed(random_seed)
    plt.figure()
    samples = np.random.normal(mu, sigma, n_samples)
    _, _, _ = plt.hist(samples, 30, density=True)
    ax = plt.gca()
    ax.plot(
        np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000),
        norm.pdf(np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000), mu, sigma),
        linewidth=2,
        color="r",
    )
    return ax, samples

import unittest
import matplotlib.pyplot as plt
import numpy as np
class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.default_seed = 42
        cls.large_n_samples = 100000
        cls.small_n_samples = 100
        cls.zero_n_samples = 0
        cls.negative_n_samples = -100
        cls.default_mu = 0
        cls.default_sigma = 1
        cls.large_sigma = 5
        cls.small_sigma = 0.2
        cls.zero_sigma = 0
        cls.negative_sigma = -1
        cls.custom_mu = 5
        cls.custom_sigma = 2
    def test_case_1(self):
        # Test data generation correctness
        mu_test = 3
        sigma_test = 2
        n_samples_test = 10000
        random_seed_test = 42
        _, samples = f_373(
            n_samples=n_samples_test,
            mu=mu_test,
            sigma=sigma_test,
            random_seed=random_seed_test,
        )
        # Calculate sample mean and standard deviation
        sample_mean = np.mean(samples)
        sample_std = np.std(samples)
        # Verify sample mean and standard deviation are close to mu and sigma within a tolerance
        self.assertAlmostEqual(
            sample_mean,
            mu_test,
            places=1,
            msg="Sample mean does not match expected mean.",
        )
        self.assertAlmostEqual(
            sample_std,
            sigma_test,
            places=1,
            msg="Sample standard deviation does not match expected sigma.",
        )
    def test_case_2(self):
        # Default parameters
        ax, _ = f_373(random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)
    def test_case_3(self):
        # Custom parameters: small number of samples, custom mean and standard deviation
        ax, _ = f_373(
            n_samples=self.small_n_samples,
            mu=self.custom_mu,
            sigma=self.custom_sigma,
            random_seed=self.default_seed,
        )
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)
    def test_case_4(self):
        # Large number of samples
        ax, _ = f_373(n_samples=self.large_n_samples, random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.patches) >= 30)
    def test_case_5(self):
        # Small number of samples
        ax, _ = f_373(n_samples=self.small_n_samples, random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.patches) <= 30)
    def test_case_6(self):
        # Large standard deviation
        ax, _ = f_373(sigma=self.large_sigma, random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)
    def test_case_7(self):
        # Small standard deviation
        ax, _ = f_373(sigma=self.small_sigma, random_seed=self.default_seed)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 30)
    def test_case_8(self):
        # Invalid negative standard deviation
        with self.assertRaises(ValueError):
            f_373(sigma=self.negative_sigma)
    def test_case_9(self):
        # Invalid zero standard deviation
        with self.assertRaises(Exception):
            f_373(sigma=self.zero_sigma)
    def test_case_10(self):
        # Invalid zero samples
        with self.assertRaises(Exception):
            f_373(n_samples=self.zero_n_samples)
    def test_case_11(self):
        # Invalid negative samples
        with self.assertRaises(ValueError):
            f_373(n_samples=self.negative_n_samples)
    def test_case_12(self):
        # Reproducibility with same seed
        ax1, sample1 = f_373(random_seed=self.default_seed)
        ax2, sample2 = f_373(random_seed=self.default_seed)
        self.assertEqual(ax1.patches[0].get_height(), ax2.patches[0].get_height())
        self.assertTrue((sample1 == sample2).all())
    def tearDown(self):
        plt.close("all")
