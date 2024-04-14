import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt


def f_869(kwargs):
    """
    Performs a two-sample t-test on numerical data from two groups to determine if there is a significant
    difference in their means. The function handles NaN values, computes descriptive statistics for each group,
    and generates a boxplot and histograms for data visualization.

    Parameters:
    - kwargs (dict): A dictionary with two keys, 'group1' and 'group2'. Each key maps to a list of numbers.
                     Lists can contain NaN values, which will be excluded from analysis.

    Returns:
    - dict: A dictionary containing:
        - 'significant': Boolean. True if the means of the two groups are significantly different (p < 0.05).
        - 'group1_stats': Dictionary with mean and standard deviation of 'group1' (excluding NaNs).
        - 'group2_stats': Dictionary with mean and standard deviation of 'group2' (excluding NaNs).
        - 'ax_boxplot': A matplotlib Axes object with a boxplot comparing 'group1' and 'group2'.
        - 'ax_histogram': A matplotlib Axes object with histograms of 'group1' and 'group2'.

    Raises:
    - ValueError: If either group is empty, contains only NaN values, has less than two non-NaN values,
                  or if the variance in one or both groups is below a threshold (1e-8).

    Requirements:
    - numpy
    - scipy
    - matplotlib

    Note:
    - The function sets the significance level (alpha) at 0.05.
    - It removes NaN values before performing any calculations or plotting.
    - A t-test is performed with the 'nan_policy' set to 'omit' to ignore NaNs.
    - The function checks for sufficient non-NaN data points and adequate variance in each group before conducting the t-test.
    - The boxplot and histograms provide a visual comparison of the data distributions.
    
    Example:
    >>> data = {'group1': [1, 2, 3, 4], 'group2': [5, 6, 7, 8]}
    >>> results = f_869(data)
    >>> results['significant']
    True
    """
    alpha = 0.05  # Define the significance level

    group1 = np.array(kwargs.get("group1", []))
    group2 = np.array(kwargs.get("group2", []))

    # Check for empty or all-NaN groups
    if (
        len(group1) == 0
        or len(group2) == 0
        or np.all(np.isnan(group1))
        or np.all(np.isnan(group2))
    ):
        raise ValueError("One or both groups are empty or contain only NaN values.")

    # Removing NaN values and ensuring sufficient data
    valid_group1 = group1[~np.isnan(group1)]
    valid_group2 = group2[~np.isnan(group2)]

    # Check for sufficient size and variance
    if len(valid_group1) < 2 or len(valid_group2) < 2:
        raise ValueError("Each group must have at least two non-NaN values.")

    if np.var(valid_group1) < 1e-8 or np.var(valid_group2) < 1e-8:
        raise ValueError("Variance in one or both groups is too low.")

    # Perform t-test
    _, p_val = ttest_ind(valid_group1, valid_group2, nan_policy="omit")

    significant = p_val < alpha

    # Calculate descriptive statistics
    group1_stats = {"mean": np.mean(valid_group1), "std": np.std(valid_group1)}
    group2_stats = {"mean": np.mean(valid_group2), "std": np.std(valid_group2)}

    # Plotting
    _, (ax_boxplot, ax_histogram) = plt.subplots(2, 1, figsize=(8, 12))

    # Boxplot
    ax_boxplot.boxplot([valid_group1, valid_group2], labels=["group1", "group2"])

    # Histogram
    ax_histogram.hist(valid_group1, alpha=0.5, label="group1")
    ax_histogram.hist(valid_group2, alpha=0.5, label="group2")
    ax_histogram.legend()

    return {
        "significant": significant,
        "group1_stats": group1_stats,
        "group2_stats": group2_stats,
        "ax_boxplot": ax_boxplot,
        "ax_histogram": ax_histogram,
    }

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for the function."""
    def test_different_means(self):
        """Test with groups having significantly different means."""
        data = {"group1": [1, 2, 3], "group2": [4, 5, 6]}
        result = f_869(data)
        self.assertTrue(result["significant"])
    def test_similar_means(self):
        """Test with groups having similar means."""
        data = {"group1": [1, 2, 3], "group2": [1, 2, 3]}
        result = f_869(data)
        self.assertFalse(result["significant"])
    def test_with_nan_values(self):
        """Test with groups containing NaN values but with at least two non-NaN values in each group."""
        data = {"group1": [np.nan, 2, 3], "group2": [1, np.nan, 3]}
        result = f_869(data)
        self.assertIsNotNone(result)
    def test_empty_group(self):
        """Test with one of the groups being empty."""
        data = {"group1": [], "group2": [1, 2, 3]}
        with self.assertRaises(ValueError):
            f_869(data)
    def test_all_nan_values(self):
        """Test with groups containing only NaN values."""
        data = {"group1": [np.nan, np.nan], "group2": [np.nan, np.nan]}
        with self.assertRaises(ValueError):
            f_869(data)
    def test_insufficient_group_size(self):
        """Test with one of the groups having less than two non-NaN values."""
        data = {"group1": [1, np.nan], "group2": [2, 3, 4]}
        with self.assertRaises(ValueError):
            f_869(data)
    def test_low_variance(self):
        """Test with one of the groups having extremely low variance."""
        data = {"group1": [1.00000001, 1.00000002], "group2": [2, 3, 4]}
        with self.assertRaises(ValueError):
            f_869(data)
