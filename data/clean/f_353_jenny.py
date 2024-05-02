import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def f_353(mu=0, sigma=1):
    """
    Draw and return a subplot of a normal distribution with the given mean and standard deviation,
    utilizing numpy's linspace to create an array of 100 linearly spaced numbers between
    `mu - 3*sigma` and `mu + 3*sigma`.

    Parameters:
    mu (float): The mean of the distribution. Default is 0.
    sigma (float): The standard deviation of the distribution. Default is 1.

    Returns:
    matplotlib.axes.Axes: The subplot representing the normal distribution.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.stats.norm

    Example:
    >>> ax = f_353(mu=5, sigma=2)
    >>> ax
    <Axes: >
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    return ax


import unittest
import numpy as np
import matplotlib.pyplot as plt


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test default parameters
        ax = f_353()
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        self.assertAlmostEqual(x[np.argmax(y)], 0, delta=0.1)
        self.assertTrue(min(x) >= -3 and max(x) <= 3)

    def test_case_2(self):
        # Test positive mu and sigma with manual calculation
        ax = f_353(mu=5, sigma=2)
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        expected_min, expected_max = 5 - 3 * 2, 5 + 3 * 2
        self.assertAlmostEqual(min(x), expected_min, delta=0.1)
        self.assertAlmostEqual(max(x), expected_max, delta=0.1)

    def test_case_3(self):
        # Test negative mu and small sigma
        ax = f_353(mu=-3, sigma=0.5)
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        self.assertAlmostEqual(x[np.argmax(y)], -3, delta=0.1)
        self.assertTrue(min(x) >= -3 - 1.5 and max(x) <= -3 + 1.5)

    def test_case_4(self):
        # Test large mu and sigma
        mu, sigma = 1e6, 1e5
        ax = f_353(mu=mu, sigma=sigma)
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        self.assertTrue(
            len(x) > 0 and len(y) > 0,
            "Plot data should not be empty even for large mu and sigma.",
        )

    def test_case_5(self):
        # Test negative mu
        ax = f_353(mu=-5, sigma=4)
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        self.assertAlmostEqual(x[np.argmax(y)], -5, delta=0.15)
        self.assertTrue(min(x) >= -5 - 12 and max(x) <= -5 + 12)

    def test_case_6(self):
        # Test the function with a sigma of 0, which might represent a degenerate distribution
        ax = f_353(mu=0, sigma=0)
        lines = ax.get_lines()
        self.assertEqual(
            len(lines),
            1,
            "Plot should contain exactly one line for a degenerate distribution.",
        )

    def test_case_7(self):
        # Test the function with extremely large values of mu and sigma to ensure it doesn't break
        ax = f_353(mu=1e6, sigma=1e5)
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        self.assertTrue(
            len(x) > 0 and len(y) > 0,
            "Plot data should not be empty even for large mu and sigma.",
        )

    def test_case_8(self):
        # Test the function with a very small positive sigma to check narrow distributions
        ax = f_353(mu=0, sigma=1e-5)
        lines = ax.get_lines()
        x, y = lines[0].get_data()
        # Checking that the plot peak is at mu and sigma affects the curve's spread.
        self.assertAlmostEqual(
            x[np.argmax(y)],
            0,
            delta=1e-5,
            msg="Peak of the distribution should be at mu.",
        )

    def tearDown(self):
        plt.close("all")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
