import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


def f_880(s1, s2):
    """
    Performs a comparative analysis of two pandas Series by visualizing their distributions using a histogram
    and assessing statistical differences through a two-sample t-test.

    Note:
    - The labels on the histogram bars correspond to the Series names if available.

    Parameters:
    - s1 (pd.Series): The first pandas Series for comparison.
    - s2 (pd.Series): The second pandas Series for comparison.
    
    Returns:
    - matplotlib.axes.Axes: An Axes object representing the overlaid histograms of both Series.
    - float: The t-statistic from the t-test, indicating the degree of difference between the two Series' means.
    - float: The two-tailed p-value from the t-test, suggesting the probability of
      observing the data if the null hypothesis (no difference in means) is true.

    Requirements:
    - pandas
    - matplotlib
    - scipy

    Example:
    >>> s1 = pd.Series(np.random.normal(0, 1, 1000))
    >>> s2 = pd.Series(np.random.normal(1, 1, 1000))
    >>> ax, t_stat, p_value = f_880(s1, s2)
    >>> plt.show() # Display the plot in a non-interactive environment
    """

    ax = s1.plot(
        kind="hist", bins=30, alpha=0.5, label=s1.name or "Series 1", legend=True
    )
    s2.plot(
        kind="hist", bins=30, alpha=0.5, label=s2.name or "Series 2", ax=ax, legend=True
    )
    t_stat, p_value = ttest_ind(
        s1, s2, equal_var=False
    )  # Assuming unequal variances by default
    return ax, t_stat, p_value


import pandas as pd
import numpy as np
import unittest
import matplotlib.pyplot as plt


class TestCases(unittest.TestCase):
    """Test cases for f_880."""

    def test_significantly_different_means(self):
        """Scenario: Two distributions with significantly different means.
        Expected: The t-test should detect a significant difference (p-value < 0.05).
        """
        np.random.seed(42)
        s1 = pd.Series(np.random.normal(0, 1, 1000))
        np.random.seed(42)
        s2 = pd.Series(np.random.normal(5, 1, 1000))
        _, t_stat, p_value = f_880(s1, s2)
        self.assertLess(p_value, 0.05)
        self.assertAlmostEqual(t_stat, -114.1764492547248)

    def test_same_distribution(self):
        """Scenario: Two distributions sampled from the same distribution (i.e., same mean and variance).
        Expected: The t-test should not detect a significant difference (p-value >= 0.05).
        """
        np.random.seed(123)
        s1 = pd.Series(np.random.normal(0, 1, 1000))
        np.random.seed(123)
        s2 = pd.Series(np.random.normal(0, 1, 1000))
        _, t_stat, p_value = f_880(s1, s2)
        self.assertGreaterEqual(p_value, 0.05)
        self.assertAlmostEqual(t_stat, 0.0)

    def test_same_mean_different_variance(self):
        """Scenario: Two distributions with the same mean but different variances.
        Expected: The t-test might or might not detect a significant difference.
        """
        np.random.seed(0)
        s1 = pd.Series(np.random.normal(0, 1, 1000))
        np.random.seed(0)
        s2 = pd.Series(np.random.normal(0, 3, 1000))
        _, t_stat, p_value = f_880(s1, s2)
        self.assertTrue(0 <= p_value <= 1)
        self.assertAlmostEqual(t_stat, 0.9165664411422174)

    def test_histogram_labels(self):
        """Scenario: Testing if the histogram labels match the series names.
        Expected: The labels on the histogram should match the series names.
        """
        np.random.seed(0)
        s1 = pd.Series(np.random.normal(0, 1, 1000), name="Dist1")
        np.random.seed(0)
        s2 = pd.Series(np.random.normal(1, 1, 1000), name="Dist2")
        ax, _, _ = f_880(s1, s2)
        legend_texts = [text.get_text() for text in ax.legend().get_texts()]
        self.assertIn("Dist1", legend_texts)
        self.assertIn("Dist2", legend_texts)

    def test_distributions_with_outliers(self):
        """Scenario: One distribution with outliers and another without.
        Expected: The t-test should detect a significant difference if outliers are far from the mean.
        """
        np.random.seed(42)
        s1 = pd.Series(
            np.concatenate([np.random.normal(0, 1, 990), np.array([50] * 10)])
        )
        np.random.seed(42)
        s2 = pd.Series(np.random.normal(0, 1, 1000))
        _, t_stat, p_value = f_880(s1, s2)
        self.assertLess(p_value, 0.05)
        self.assertAlmostEqual(t_stat, 3.0719987200209986)

    def tearDown(self):
        plt.clf()


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
