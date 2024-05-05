from scipy.stats import zscore
import matplotlib.pyplot as plt


def f_116(df):
    """
    Calculate Z-scores for numeric columns in a DataFrame and draw a histogram for each column.
    - Missing values are replaced by the column's average.
    - The histograms are plotted with 10 bins.

    Parameters:
    - df (pandas.DataFrame): The input pandas DataFrame with numeric columns.

    Returns:
    - tuple:
        1. pandas.DataFrame: A DataFrame with computed z-scores.
        2. list: A list of Axes objects representing the histograms of the numeric columns.

    Requirements:
    - pandas.
    - numpy.
    - scipy.stats.zscore.
    - matplotlib.pyplot.

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> df_input = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["col1", "col2", "col3"])
    >>> zscore_output, plots = f_116(df_input)
    """
    # Fill missing values with column's average
    df = df.fillna(df.mean(axis=0))
    # Compute Z-scores
    df = df.apply(zscore)
    # Plot histograms for each numeric column
    axes = df.hist(grid=False, bins=10, layout=(1, df.shape[1]))
    plt.tight_layout()
    return df, axes


import unittest
import pandas as pd
import numpy as np


class TestCases(unittest.TestCase):
    """Test cases for the f_116 function."""

    def test_case_1(self):
        df = pd.DataFrame(
            {
                "col1": [1, 7, 3],
                "col2": [4, 5, 7],
                "col3": [None, None, None],
            }
        )
        zscores, plots = f_116(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 3)

    def test_case_2(self):
        df = pd.DataFrame(
            {
                "col1": [None, None, 3],
                "col2": [None, 5, 7],
                "col3": [8, 6, 4],
            }
        )
        zscores, plots = f_116(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 3)

    def test_case_3(self):
        df = pd.DataFrame(
            {
                "col1": [None, 17, 11, None],
                "col2": [0, 4, 15, 27],
                "col3": [7, 9, 3, 8],
            }
        )
        # Expected solutions
        expected_df = df.copy()
        expected_df = expected_df.fillna(expected_df.mean(axis=0))
        expected_df = expected_df.apply(zscore)
        # Function execution
        zscores, plots = f_116(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 3)
        pd.testing.assert_frame_equal(zscores, expected_df)

    def test_case_4(self):
        df = pd.DataFrame(
            {
                "col1": [1, 7, 3, None],
                "col2": [4, 5, 7, 2],
            }
        )
        zscores, plots = f_116(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 2)

    def test_case_5(self):
        df = pd.DataFrame(
            {
                "col1": [1, 2, 3, 4, 5],
                "col2": [None, None, None, None, None],
            }
        )
        zscores, plots = f_116(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 2)

    def test_case_6(self):
        df = pd.DataFrame(
            {
                "A": [np.nan, np.nan, np.nan],
                "B": [np.nan, np.nan, np.nan],
                "C": [np.nan, np.nan, np.nan],
            }
        )
        zscores, plots = f_116(df)
        self.assertTrue(zscores.isnull().all().all())
        self.assertEqual(len(plots[0]), 3)

    def test_case_7(self):
        df = pd.DataFrame(
            {
                "A": [1, 2.5, 3, 4.5, 5],
                "B": [5, 4.5, np.nan, 2, 1.5],
                "C": [2.5, 3, 4, 5.5, 6],
            }
        )
        zscores, plots = f_116(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 3)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
