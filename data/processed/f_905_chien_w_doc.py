import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def f_816(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    """
    Plots a histogram of normalized data from an input 2D numpy array alongside the probability density function (PDF)
    of a standard normal distribution.

    Note:
    - Takes in a 2D numpy array as input.
    - Calculates the sum of elements in each row of the array.
    - Normalizes these row sums to have a mean of 0 and a standard deviation of 1.
      - Normalization is achieved by first calculating the mean and standard deviation of the row sums.
      - Each row sum is then transformed by subtracting the mean and dividing by the standard deviation.
      - If the standard deviation is 0 (indicating all row sums are equal), normalization results in an array of zeros with the same shape.
    - Plots a histogram of the normalized data.
      - Uses 30 bins for the histogram.
      - The histogram is density-based, meaning it represents the probability density rather than raw frequencies.
      - The bars of the histogram are semi-transparent (60% opacity) and green in color.
    - Overlays the PDF of a standard normal distribution on the histogram for comparison.
      - The PDF curve is plotted in red with a line width of 2.
      - The range of the PDF curve is set to cover 99% of a standard normal distribution.
    - Sets the title of the plot to "Histogram of Normalized Data with Standard Normal PDF".

    Parameters:
    - arr: A 2D numpy array. The array should contain numerical data.

    Returns:
    - A tuple containing:
      - A matplotlib Axes object with the histogram of the normalized data and the overlaid standard normal PDF.
      - The normalized data as a 1D numpy array.

    Requirements:
    - numpy
    - scipy
    - matplotlib

    Example:
    >>> ax, normalized_data = f_816(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> print(normalized_data)
    [-1.22474487  0.          1.22474487]
    """
    row_sums = arr.sum(axis=1)
    mean = np.mean(row_sums)
    std_dev = np.std(row_sums)
    normalized_data = (
        (row_sums - mean) / std_dev if std_dev != 0 else np.zeros_like(row_sums)
    )
    _, ax = plt.subplots()
    ax.hist(normalized_data, bins=30, density=True, alpha=0.6, color="g")
    x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
    ax.plot(x, norm.pdf(x), "r-", lw=2)
    ax.set_title("Histogram of Normalized Data with Standard Normal PDF")
    return ax, normalized_data

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    """Tests for `f_816`."""
    def test_histogram_and_pdf(self):
        """Test that the histogram and PDF are plotted."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        ax, _ = f_816(arr)
        self.assertEqual(
            ax.get_title(),
            "Histogram of Normalized Data with Standard Normal PDF",
        )
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(len(ax.patches), 30)
    def test_normalized_data(self):
        """Test that the normalized data is correct."""
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        _, normalized_data = f_816(arr)
        expected_data = [-1.22474487, 0.0, 1.22474487]
        for i in range(len(expected_data)):
            self.assertTrue(np.isclose(normalized_data[i], expected_data[i]))
    def test_empty_array(self):
        """Test empty array."""
        arr = np.array([[], [], []])
        _, normalized_data = f_816(arr)
        for value in normalized_data:
            self.assertTrue(np.isclose(value, 0))
    def test_single_value_array(self):
        """Test single value array."""
        arr = np.array([[5], [5], [5]])
        _, normalized_data = f_816(arr)
        for value in normalized_data:
            self.assertTrue(np.isclose(value, 0))
    def test_large_values(self):
        """Test large values."""
        arr = np.array([[1e6, 2e6, 3e6], [4e6, 5e6, 6e6], [7e6, 8e6, 9e6]])
        _, normalized_data = f_816(arr)
        expected_data = [-1.22474487, 0.0, 1.22474487]
        for i in range(len(expected_data)):
            self.assertTrue(np.isclose(normalized_data[i], expected_data[i]))
