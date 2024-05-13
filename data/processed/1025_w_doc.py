import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Constants
PLOT_TITLE = "Scaled Values"


def task_func(data_dict):
    """
    Scales the values in a given dictionary using MinMaxScaler and plots the scaled data.

    Parameters:
    - data_dict (dict): A dictionary where keys represent column names and values are lists of numerical data.
                        The values may contain missing data (None), which are handled by dropping them before scaling.

    Returns:
    - pandas.DataFrame containing the scaled data.
    - matplotlib Axes object that displays the plot of the scaled data.

    Requirements:
    - pandas
    - scikit-learn
    - matplotlib

    Example:
    >>> data = {'a': [1, 2, None, 4], 'b': [5, None, 7, 8]}
    >>> scaled_df, plot_ax = task_func(data)
    >>> scaled_df
         a    b
    0  0.0  0.0
    1  1.0  1.0
    >>> plot_ax.get_title()
    'Scaled Values'
    """

    df = pd.DataFrame(data_dict).dropna()
    if df.empty:
        ax = plt.gca()
        ax.set_title(PLOT_TITLE)
        return df, ax
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(scaled_data, columns=df.columns)
    ax = df_scaled.plot()
    ax.set_title(PLOT_TITLE)
    return df_scaled, ax

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Unit tests for the function."""
    def test_empty_data(self):
        """
        Test with an empty dictionary. Should return an empty DataFrame and a plot object.
        """
        result_df, result_ax = task_func({})
        self.assertTrue(result_df.empty)
        self.assertIsNotNone(result_ax)
    def test_all_none_data(self):
        """
        Test with a dictionary where all values are None. Should return an empty DataFrame and a plot object.
        """
        data = {"a": [None, None], "b": [None, None]}
        result_df, result_ax = task_func(data)
        self.assertTrue(result_df.empty)
        self.assertIsNotNone(result_ax)
    def test_normal_data(self):
        """
        Test with a normal data dictionary. Should return a non-empty DataFrame and a plot object.
        """
        data = {"a": [1, 2, 3], "b": [4, 5, 6]}
        result_df, result_ax = task_func(data)
        self.assertEqual(result_ax.get_title(), "Scaled Values")
        self.assertFalse(result_df.empty)
        self.assertEqual(result_df.shape, (3, 2))
        self.assertIsNotNone(result_ax)
    def test_with_missing_values(self):
        """
        Test data with some missing values. Missing values should be dropped, and scaled data should be returned.
        """
        data = {"a": [1, None, 3], "b": [4, 5, None]}
        result_df, result_ax = task_func(data)
        self.assertEqual(result_df.shape, (1, 2))  # Only one row without missing values
        self.assertIsNotNone(result_ax)
    def test_with_negative_values(self):
        """
        Test data with negative values. Should handle negative values correctly and return scaled data.
        """
        data = {"a": [-1, -2, -3], "b": [1, 2, 3]}
        result_df, result_ax = task_func(data)
        self.assertFalse(result_df.empty)
        self.assertEqual(result_df.shape, (3, 2))
        self.assertIsNotNone(result_ax)
