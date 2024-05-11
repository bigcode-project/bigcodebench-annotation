import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler


def task_func(df1, df2):
    """
    Merge two dataframes on the 'id' column and then scale the numeric features.

    This function merges two dataframes via outer join on the 'id' column, and scales the merged dataframe's
    numeric features from df1 to have a mean of 0 and standard deviation of 1. It also returns a pair plot of
    the scaled features from df1.

    Parameters:
    - df1 (pd.DataFrame): Left dataframe to merge into.
    - df2 (pd.DataFrame): Right dataframe to merge from.

    Returns:
    - merged_df (pd.DataFrame): The partially scaled and merged dataframe.
    - pair_plot (seaborn.axisgrid.PairGrid): Pair plot of the scaled dataframe.

    Requirements:
    - pandas
    - sklearn
    - seaborn

    Example:
    >>> df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6], 'feature2': [2.3, 4.5, 6.7]})
    >>> df2 = pd.DataFrame({'id': [1, 2, 3], 'feature4': [4.5, 6.7, 8.9], 'feature5': [5.6, 7.8, 9.0]})
    >>> scaled_df, plot = task_func(df1, df2)
    >>> scaled_df
       id  feature1  feature2  feature4  feature5
    0   1 -1.224745 -1.224745       4.5       5.6
    1   2  0.000000  0.000000       6.7       7.8
    2   3  1.224745  1.224745       8.9       9.0
    >>> type(scaled_df)
    <class 'pandas.core.frame.DataFrame'>
    >>> type(plot)
    <class 'seaborn.axisgrid.PairGrid'>
    """
    merged_df = pd.merge(df1, df2, on="id", how="outer")
    numeric_features_df1 = df1.select_dtypes(
        include=["float64", "int64"]
    ).columns.tolist()
    if "id" in numeric_features_df1:
        numeric_features_df1.remove("id")
    if not merged_df.empty and numeric_features_df1:
        scaler = StandardScaler()
        merged_df[numeric_features_df1] = scaler.fit_transform(
            merged_df[numeric_features_df1]
        )
    pair_plot = None
    if numeric_features_df1:
        pair_plot = sns.pairplot(merged_df[numeric_features_df1])
    return merged_df, pair_plot

import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Standard data merging on 'id' and checking scaled values
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [1.2, 3.4, 5.6],
                "feature2": [2.3, 4.5, 6.7],
                "feature3": [3.4, 5.6, 7.8],
            }
        )
        df2 = pd.DataFrame(
            {"id": [1, 2, 3], "feature4": [4.5, 6.7, 8.9], "feature5": [5.6, 7.8, 9.0]}
        )
        scaled_df, _ = task_func(df1, df2)
        self.assertEqual(
            list(scaled_df.columns),
            ["id", "feature1", "feature2", "feature3", "feature4", "feature5"],
        )
        self.assertAlmostEqual(scaled_df["feature1"].mean(), 0, places=5)
    def test_case_2(self):
        # Random data merging and checking scaled values
        df1 = pd.DataFrame(
            {
                "id": [1, 3, 5],
                "feature1": [10, 20, 30],
                "feature2": [5, 15, 25],
                "feature3": [6, 16, 26],
            }
        )
        df2 = pd.DataFrame(
            {"id": [1, 5, 3], "feature4": [7, 17, 27], "feature5": [8, 18, 28]}
        )
        scaled_df, _ = task_func(df1, df2)
        self.assertAlmostEqual(scaled_df["feature2"].std(), 1.224745, places=5)
    def test_case_3(self):
        # Negative values and merging on 'id' and checking scaled values
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [-1, -2, -3],
                "feature2": [-5, -6, -7],
                "feature3": [-8, -9, -10],
            }
        )
        df2 = pd.DataFrame(
            {"id": [1, 2, 3], "feature4": [-11, -12, -13], "feature5": [-14, -15, -16]}
        )
        scaled_df, _ = task_func(df1, df2)
        self.assertAlmostEqual(scaled_df["feature3"].max(), 1.224745, places=5)
    def test_case_4(self):
        # Zero values and checking if scaled values remain zero
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3, 4],
                "feature1": [0, 0, 0, 0],
                "feature2": [0, 0, 0, 0],
                "feature3": [0, 0, 0, 0],
            }
        )
        df2 = pd.DataFrame(
            {"id": [1, 2, 3, 4], "feature4": [0, 0, 0, 0], "feature5": [0, 0, 0, 0]}
        )
        scaled_df, _ = task_func(df1, df2)
        self.assertAlmostEqual(scaled_df["feature1"].min(), 0, places=5)
    def test_case_5(self):
        # Large values and checking scaled min values
        df1 = pd.DataFrame(
            {
                "id": [1, 2],
                "feature1": [1000, 2000],
                "feature2": [500, 1500],
                "feature3": [100, 200],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2], "feature4": [10, 20], "feature5": [1, 2]})
        scaled_df, _ = task_func(df1, df2)
        self.assertAlmostEqual(scaled_df["feature2"].min(), -1, places=5)
    def test_case_6(self):
        # Testing the plot's attributes
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [1, 2, 3],
                "feature2": [4, 5, 6],
                "feature3": [7, 8, 9],
            }
        )
        df2 = pd.DataFrame(
            {"id": [1, 2, 3], "feature4": [10, 11, 12], "feature5": [13, 14, 15]}
        )
        _, pair_plot = task_func(df1, df2)
        # Checking if the pair plot has the expected attributes
        self.assertEqual(
            len(pair_plot.axes), 3
        )  # Because we have 3 valid features in df1
        self.assertIn("feature1", pair_plot.data.columns)
        self.assertIn("feature2", pair_plot.data.columns)
        self.assertIn("feature3", pair_plot.data.columns)
    def test_case_7(self):
        # Testing with empty dataframes
        df1 = pd.DataFrame(columns=["id", "feature1", "feature2", "feature3"])
        df2 = pd.DataFrame(columns=["id", "feature4", "feature5"])
        scaled_df, _ = task_func(df1, df2)
        self.assertTrue(scaled_df.empty)
    def test_case_8(self):
        # Testing with NaN values in the dataframes
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [1, 2, None],
                "feature2": [4, None, 6],
                "feature3": [7, 8, 9],
            }
        )
        df2 = pd.DataFrame(
            {"id": [1, 2, 3], "feature4": [10, 11, 12], "feature5": [13, 14, 15]}
        )
        scaled_df, _ = task_func(df1, df2)
        self.assertTrue(scaled_df.isnull().any().any())  # Checking if NaN values exist
    def tearDown(self):
        plt.close("all")
