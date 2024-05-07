import pandas as pd
import seaborn as sns
from scipy import stats

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def f_301(data):
    """
    Processes a given dataset to compute the average of each row, plots the distribution of these averages,
    and evaluates their normality. The function returns these averages as an additional column in a DataFrame,
    the plot of the distribution, and the p-value from the normality test if applicable.

    Parameters:
    data (numpy.array): A 2D numpy array with eight columns representing different data types or categories, with a
    shape of (n_samples, 8).

    Returns:
    tuple: Contains three elements:
        - DataFrame: A pandas DataFrame with the original data and an added 'Average' column.
        - Axes object: The Axes object from the seaborn distribution plot of the averages.
        - float or None: The p-value from the normality test on the averages, or None
        if the test could not be conducted.

    Requirements:
    - pandas
    - seaborn
    - scipy

    Raises:
    ValueError: If the input data does not have exactly eight columns.

    Note:
    The function uses seaborn's distplot for visualization and scipy's normaltest for statistical analysis.
    It requires at least 20 data points to perform the normality test.

    Example:
    >>> import numpy as np
    >>> data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
    >>> df, ax, p_value = f_301(data)
    >>> print(df)
       A  B  C  D  E  F  G  H  Average
    0  1  2  3  4  4  3  7  1    3.125
    1  6  2  3  4  3  4  4  1    3.375
    >>> print(p_value)
    None
    """
    if data.shape[1] != 8:
        raise ValueError("Data must contain exactly eight columns.")
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    df['Average'] = df.mean(axis=1)
    ax = sns.kdeplot(df['Average'], linewidth=3)
    if len(df['Average']) >= 20:
        k2, p = stats.normaltest(df['Average'])
    else:
        p = None
    return df, ax, p

import numpy as np
import pandas as pd
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Mock plt.show to prevent it from displaying plots during tests
        self.addCleanup(plt.close, 'all')
    def test_basic_functionality(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
        df, ax, p_value = f_301(data)
        expected_averages = [np.mean(row) for row in data]
        self.assertTrue(isinstance(df, pd.DataFrame), "Expected output to be a pandas DataFrame")
        self.assertIn('Average', df.columns, "DataFrame should have an 'Average' column")
        self.assertTrue(np.array_equal(df['Average'], expected_averages), "Averages are not calculated correctly")
        self.assertTrue(isinstance(ax, plt.Axes), "Expected a matplotlib Axes object for plotting")
    def test_empty_input(self):
        data = np.array([[]])
        with self.assertRaises(ValueError):
            f_301(data)
    def test_insufficient_columns(self):
        data = np.random.rand(10, 7)  # Only 7 columns, one less than required
        with self.assertRaises(ValueError):
            f_301(data)
    def test_non_numeric_input(self):
        data = np.array([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']])
        with self.assertRaises(TypeError):
            f_301(data)
    def test_plot_output(self):
        data = np.random.rand(20, 8)
        df, ax, _ = f_301(data)
        self.assertEqual(len(ax.lines), 1, "There should be one line on the plot")
    def test_normality_test(self):
        # Create a dataset large enough to properly trigger the normality test
        data = np.random.rand(20, 8)  # Increase to 20 rows
        df, ax, p_value = f_301(data)
        self.assertIsNotNone(p_value, "p-value should not be None for sufficient data size")
