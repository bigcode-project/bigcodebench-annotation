import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler



# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'

def f_239(df, dict_mapping, plot_histogram=False):
    """
    Pre-processes a DataFrame by replacing values according to a dictionary mapping, standardizing specified features, 
    and optionally drawing a histogram of the target variable.

    Parameters:
    - df (DataFrame): The input DataFrame to be preprocessed. It should contain columns named as in FEATURES and TARGET.
    - dict_mapping (dict): A dictionary for replacing values in df. The keys should correspond to existing values in df.
    - plot_histogram (bool, optional): If True, a histogram of the target variable is displayed. Default is False.

    Returns:
    - DataFrame: The preprocessed DataFrame with standardized features and values replaced as per dict_mapping.
    - Axes: The histogram of the target variable if plot_histogram is True, otherwise None.

    Requirements:
    - matplotlib.pyplot
    - sklearn.preprocessing.StandardScaler

    Examples:
    >>> df = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'feature3': [7, 8, 9],'feature4': [10, 11, 12], 'feature5': [13, 14, 15], 'target': [0, 1, 1]})
    >>> dict_mapping = {1: 11, 0: 22}
    >>> isinstance(f_239(df, dict_mapping, plot_histogram=True)[1], plt.Axes)
    True
    """

    # Check if all required columns are present in the DataFrame
    required_columns = FEATURES + [TARGET]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in DataFrame: {missing_columns}")

    # Replace values using dictionary mapping
    df = df.replace(dict_mapping)
    
    # Standardize the features
    scaler = StandardScaler()
    df[FEATURES] = scaler.fit_transform(df[FEATURES])
    
    # Plot histogram of the target variable if requested
    if plot_histogram:
        ax = df[TARGET].plot.hist(bins=50)
        return df, ax
    else:
        return df, None

import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_value_replacement(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9],
            'feature4': [10, 11, 12],
            'feature5': [13, 14, 15],
            'target': [0, 1, 1]
        })
        dict_mapping = {1: 11, 0: 22}
        result_df, _ = f_239(df, dict_mapping)
        self.assertTrue(11 in result_df.values)
        self.assertTrue(22 in result_df.values)
    def test_feature_standardization(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9],
            'feature4': [10, 11, 12],
            'feature5': [13, 14, 15],
            'target': [0, 1, 1]
        })
        result_df, _ = f_239(df, {})
        for feature in ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']:
            self.assertAlmostEqual(result_df[feature].mean(), 0, places=1)
            self.assertAlmostEqual(int(result_df[feature].std()), 1, places=1)
    def test_no_histogram_plotting(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9],
            'feature4': [10, 11, 12],
            'feature5': [13, 14, 15],
            'target': [0, 1, 1]
        })
        result, _ = f_239(df, {}, plot_histogram=False)
        self.assertIsInstance(result, pd.DataFrame)
    def test_missing_features_handling(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'target': [0, 1, 1]
        })
        with self.assertRaises(ValueError):
            f_239(df, {})
    def test_histogram_plotting(self):
        df = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9],
            'feature4': [10, 11, 12],
            'feature5': [13, 14, 15],
            'target': [0, 1, 1]
        })
        result_df, ax = f_239(df, {}, plot_histogram=True)
        self.assertTrue(hasattr(ax, 'hist'))
        self.assertIsInstance(ax, plt.Axes)
