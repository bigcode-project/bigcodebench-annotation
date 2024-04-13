import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt


def f_117(df):
    """
    Standardize numeric columns in a DataFrame and return the heatmap of the correlation matrix. Missing values are replaced by the column's average.

    Parameters:
    - df (pandas.DataFrame): The pandas DataFrame to be standardized.

    Returns:
    - DataFrame: The pandas DataFrame after standardization.
    - AxesSubplot: A heatmap of the correlation matrix.

    Requirements:
    - pandas
    - numpy
    - sklearn.preprocessing.StandardScaler
    - seaborn
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame([[1,2,3],[4,5,6],[7.0,np.nan,9.0]], columns=["c1","c2","c3"])
    >>> standardized_df, heatmap = f_117(df)
    >>> print(standardized_df)
    # Output DataFrame here
    """
    df = df.fillna(df.mean(axis=0))
    scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])
    plt.figure(figsize=(10, 5))
    heatmap = sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    return df, heatmap


import unittest


class TestCases(unittest.TestCase):
    """Test cases for the f_117 function."""

    def test_case_1(self):
        df = pd.DataFrame(
            [[1, 2, 3], [4, 5, 6], [7, None, 9]], columns=["c1", "c2", "c3"]
        )
        # Expected output
        expected_df = df.copy()
        expected_df = expected_df.fillna(df.mean(axis=0))
        scaler = StandardScaler()
        expected_df[expected_df.columns] = scaler.fit_transform(
            expected_df[expected_df.columns]
        )
        # Function execution
        standardized_df, heatmap = f_117(df)
        pd.testing.assert_frame_equal(standardized_df, expected_df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)

        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)

    def test_case_2(self):
        df = pd.DataFrame([[3, 7, 9], [4, 1, 8], [2, 6, 5]], columns=["c1", "c2", "c3"])
        standardized_df, heatmap = f_117(df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)

        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)

    def test_case_3(self):
        df = pd.DataFrame([[4, 6, 8], [9, 5, 2], [3, 1, 7]], columns=["c1", "c2", "c3"])
        standardized_df, heatmap = f_117(df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)

        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)

    def test_case_4(self):
        df = pd.DataFrame([[9, 1, 2], [3, 4, 5], [7, 8, 6]], columns=["c1", "c2", "c3"])
        standardized_df, heatmap = f_117(df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)

        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)

    def test_case_5(self):
        df = pd.DataFrame(
            [[None, 17, 13], [None, None, 29], [42, 3, 100]], columns=["c1", "c2", "c3"]
        )
        standardized_df, heatmap = f_117(df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)

        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
