import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def f_203(data_dict, data_keys):
    """
    Normalize data specified by keys in a dictionary using MinMax scaling and plot the results. This function is
    useful for preprocessing data for machine learning models where data scaling can impact performance.

    Parameters:
    data_dict (dict): A dictionary where keys map to lists of numeric values.
    data_keys (list): Keys within the dictionary whose corresponding values are to be normalized.

    Returns:
    tuple: A tuple containing a DataFrame of normalized values and a matplotlib Axes object representing a plot of the
    normalized data.

    Requirements:
    pandas, numpy, matplotlib.pyplot, sklearn.preprocessing

    Raises:
    ValueError: If no keys in `data_keys` are found in `data_dict`.

    Example:
    >>> data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    >>> data_keys = ['A', 'B']
    >>> normalized_df, ax = f_203(data_dict, data_keys)
    >>> print(normalized_df.to_string(index=False))
      A   B
    0.0 0.0
    0.5 0.5
    1.0 1.0
    """
    # Extract and transform the data for the specified keys
    data_for_keys = {key: data_dict[key] for key in data_keys if key in data_dict}
    df = pd.DataFrame(data_for_keys)

    # Check if DataFrame is empty (i.e., no keys matched)
    if df.empty:
        raise ValueError("No matching keys found in data dictionary, or keys list is empty.")

    # Apply MinMax normalization
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(df)
    normalized_df = pd.DataFrame(normalized_data, columns=data_keys)

    # Plot the normalized data
    ax = normalized_df.plot(kind='line')
    ax.set_title('Normalized Data')
    ax.set_ylabel('Normalized Value')
    ax.set_xlabel('Index')

    return normalized_df, ax

import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        # Sample data dictionary
        self.data_dict = {
            'A': [10, 20, 30, 40],
            'B': [20, 30, 40, 50],
            'C': [30, 40, 50, 60]
        }
    def test_normalization_single_key(self):
        # Test normalization with a single key
        data_keys = ['A']
        normalized_df, ax = f_203(self.data_dict, data_keys)
        self.assertTrue((normalized_df >= 0).all().all() and (normalized_df <= 1).all().all(),
                        "Normalized data should be in the range [0, 1]")
    def test_normalization_multiple_keys(self):
        # Test normalization with multiple keys
        data_keys = ['A', 'B']
        normalized_df, ax = f_203(self.data_dict, data_keys)
        self.assertEqual(len(normalized_df.columns), 2, "Normalized DataFrame should have 2 columns")
        self.assertTrue({'A', 'B'}.issubset(normalized_df.columns), "DataFrame should contain specified keys")
    def test_normalization_all_keys(self):
        # Test normalization with all keys in the dictionary
        data_keys = list(self.data_dict.keys())
        normalized_df, ax = f_203(self.data_dict, data_keys)
        self.assertEqual(len(normalized_df.columns), 3, "Normalized DataFrame should have 3 columns")
        self.assertTrue({'A', 'B', 'C'}.issubset(normalized_df.columns), "DataFrame should contain all keys")
    def test_empty_keys(self):
        # Test with no keys specified
        data_keys = []
        with self.assertRaises(ValueError):
            f_203(self.data_dict, data_keys)
    def test_key_not_in_dict(self):
        # Test with a key that's not in the dictionary
        data_keys = ['D']  # Assuming 'D' is not in `data_dict`
        with self.assertRaises(ValueError):
            f_203(self.data_dict, data_keys)
