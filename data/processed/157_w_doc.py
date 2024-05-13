import pandas as pd
import seaborn as sns


def task_func(data):
    """
    Analyze a dataset by calculating the average of values across each row and visualizing the correlation matrix as a
    heatmap.

    Parameters:
    data (numpy.array): 2D array where each row represents a record and each column represents a feature

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame enhanced with an 'Average' column that represents the mean across each row.
        - Axes: The matplotlib Axes object showing the heatmap of the correlations.

    Requirements:
    - pandas
    - numpy
    - seaborn

    Raises:
    ValueError: If the input data is not a 2D array or if it contains non-numeric data.

    Example:
    >>> data = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]])
    >>> df, ax = task_func(data)
    >>> print(df['Average'].to_string(index=False))
    4.5
    4.5
    """

    if not isinstance(data, np.ndarray) or data.ndim != 2:
        raise ValueError("Input data must be a 2D numpy array.")
    df = pd.DataFrame(data)
    correlation = df.corr()
    ax = sns.heatmap(correlation, annot=True, cmap='coolwarm')
    df['Average'] = df.mean(axis=1)
    return df, ax

import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a sample data set
        self.data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
    def tearDown(self):
        # Remove any files or handle other cleanup actions
        plt.close('all')
    def test_dataframe_structure(self):
        df, _ = task_func(self.data)
        self.assertIn('Average', df.columns, "DataFrame should contain an 'Average' column")
    def test_average_calculation(self):
        df, _ = task_func(self.data)
        expected_averages = [3.125, 3.375]  # The average of rows
        pd.testing.assert_series_equal(df['Average'], pd.Series(expected_averages, name='Average'), check_dtype=True)
    def test_heatmap_plot_returned(self):
        _, ax = task_func(self.data)
        self.assertIsInstance(ax, plt.Axes,
                              "The returned object should be a plt.Axes instance indicating a plot was created")
    def test_correlation_calculation(self):
        # Test to ensure that the correlation matrix is calculated correctly
        df, _ = task_func(self.data)
        expected_correlation = pd.DataFrame(self.data).corr()
        actual_correlation = \
            sns.heatmap(pd.DataFrame(self.data).corr(), annot=True, cmap='coolwarm').get_figure().axes[0].collections[
                0].get_array()
        np.testing.assert_array_almost_equal(actual_correlation, expected_correlation.to_numpy().ravel())
    def test_input_validation(self):
        # Test to ensure that non-2D arrays are handled properly
        with self.assertRaises(ValueError):
            task_func(np.array([1, 2, 3]))  # Not a 2D array
