import seaborn as sns
from scipy.stats import chi2_contingency


def f_233(df1, df2, column1="feature1", column2="feature2"):
    """
    Merge two dataframes based on the 'id' column, perform a chi-square independence test on the merged dataframe,
    and draw a heatmap of the contingency table created from the features in column1, column2.

    Parameters:
    - df1 (DataFrame): Left dataframe to merge. Must contain columns 'id' and one matching column1.
    - df2 (DataFrame): Right dataframe to merge from. Must contain columns 'id' and one matching column2.
    - column1   (str): Name of column containing features in df1. Defaults to 'feature1'.
    - column2   (str): Name of column containing features in df2. Defaults to 'feature2'.

    Returns:
    tuple: A tuple containing:
        - p (float): The p-value of the Chi-Squared test.
        - heatmap (matplotlib.pyplot.Axes): Seaborn heatmap of the contingency table.

    Requirements:
    - seaborn
    - scipy.stats.chi2_contingency

    Example:
    >>> import pandas as pd
    >>> df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': ['A', 'B', 'A']})
    >>> df2 = pd.DataFrame({'id': [1, 2, 3], 'feature2': ['X', 'Y', 'X']})
    >>> p_value, heatmap = f_233(df1, df2)
    >>> p_value
    0.6650055421020291
    >>> heatmap
    <Axes: xlabel='feature2', ylabel='feature1'>
    """
    df = pd.merge(df1, df2, on="id")
    contingency_table = pd.crosstab(df[column1], df[column2])
    heatmap = sns.heatmap(contingency_table)
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return p, heatmap

import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing basic functionality with simple data
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": ["A", "B", "A"]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": ["X", "Y", "X"]})
        p_value, heatmap = f_233(df1, df2)
        # P-value should be between 0 and 1 inclusive
        self.assertTrue(0.0 <= p_value <= 1.0)
        self.assertEqual(len(heatmap.get_yticklabels()), 2)  # A and B
        self.assertEqual(len(heatmap.get_xticklabels()), 2)  # X and Y
    def test_case_2(self):
        # Testing with distinct feature values across both dataframes
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": ["C", "D", "C"]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": ["W", "W", "Z"]})
        p_value, heatmap = f_233(df1, df2)
        self.assertTrue(0.0 <= p_value <= 1.0)
        self.assertEqual(len(heatmap.get_yticklabels()), 2)  # C and D
        self.assertEqual(len(heatmap.get_xticklabels()), 2)  # W and Z
    def test_case_3(self):
        # Test custom feature column names
        df1 = pd.DataFrame({"id": [1, 2, 3], "foo": ["A", "B", "A"]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "bar": ["X", "Y", "X"]})
        p_value, heatmap = f_233(df1, df2, column1="foo", column2="bar")
        self.assertTrue(0.0 <= p_value <= 1.0)
        self.assertEqual(len(heatmap.get_yticklabels()), 2)
        self.assertEqual(len(heatmap.get_xticklabels()), 2)
    def test_case_4(self):
        # Testing a scenario where the p-value is expected to be close to 0
        # This is because there's a strong association between feature1 and feature2
        df1 = pd.DataFrame(
            {"id": list(range(1, 21)), "feature1": ["A"] * 10 + ["B"] * 10}
        )
        df2 = pd.DataFrame(
            {"id": list(range(1, 21)), "feature2": ["X"] * 10 + ["Y"] * 10}
        )
        p_value, _ = f_233(df1, df2)
        self.assertTrue(0.0 <= p_value < 0.01)  # Expected p-value to be close to 0
    def test_case_5(self):
        # Test error handling - should fail when there is no 'id' column
        df1 = pd.DataFrame({"foo": [1, 2], "bar": [3, 4]})
        df2 = pd.DataFrame({"foo": [1, 2], "bar": [3, 4]})
        with self.assertRaises(KeyError):
            f_233(df1, df2)
    def tearDown(self):
        plt.close("all")
