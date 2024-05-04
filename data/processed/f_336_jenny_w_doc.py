import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns


def f_444(df1, df2):
    """Perform the feature selection with SelectKBest (k=2) and return a heatmap of the feature correlations.

    Parameters:
    - df1 (pd.DataFrame): The dataframe containing features.
    - df2 (pd.DataFrame): The dataframe containing the target variable. Must have an 'id' column corresponding to df1.

    Returns:
    - tuple: A tuple containing:
        - list: A list of the selected features.
        - Axes: A heatmap showing the correlation between the selected features.

    Requirements:
    - pandas
    - sklearn.feature_selection.SelectKBest
    - sklearn.feature_selection.f_classif
    - seaborn

    Example:
    >>> df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6], 'feature2': [2.3, 4.5, 6.7], 'feature3': [3.4, 5.6, 7.8]})
    >>> df2 = pd.DataFrame({'id': [1, 2, 3], 'target': [4.5, 6.7, 8.9]})
    >>> selected_features, heatmap = f_444(df1, df2)
    >>> heatmap
    <Axes: >
    >>> selected_features
    ['feature2', 'feature3']
    """
    df = pd.merge(df1, df2, on="id")
    features = df1.columns.drop("id")
    X = df[features]
    y = df["target"]
    selector = SelectKBest(f_classif, k=2)
    X_new = selector.fit_transform(X, y)
    selected_features = [x for x, y in zip(features, selector.get_support()) if y]
    heatmap = sns.heatmap(
        pd.DataFrame(X_new, columns=selected_features).corr(), annot=True
    )
    return selected_features, heatmap

import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def tearDown(self):
        plt.close("all")
    def test_case_1(self):
        # Dataset with clear distinction between features
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3, 4, 5],
                "feature1": [5.5, 6.7, 7.8, 8.9, 9.0],
                "feature2": [1.1, 2.2, 3.3, 4.4, 5.5],
                "feature3": [0.5, 1.5, 2.5, 3.5, 4.5],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "target": [1, 0, 1, 0, 1]})
        # Calling the function and asserting results
        selected_features, ax = f_444(df1, df2)
        self.assertListEqual(selected_features, ["feature1", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_2(self):
        # Dataset with features having moderate correlation
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [1.2, 3.4, 5.6],
                "feature2": [2.3, 4.5, 6.7],
                "feature3": [3.4, 5.6, 7.8],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [4.5, 6.7, 8.9]})
        # Calling the function and asserting results
        selected_features, ax = f_444(df1, df2)
        self.assertListEqual(selected_features, ["feature2", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_3(self):
        # Dataset with balanced target values
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3, 4],
                "feature1": [2.5, 3.5, 4.5, 5.5],
                "feature2": [6.6, 7.7, 8.8, 9.9],
                "feature3": [10.1, 11.1, 12.1, 13.1],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3, 4], "target": [0, 1, 0, 1]})
        # Calling the function and asserting results
        selected_features, ax = f_444(df1, df2)
        self.assertListEqual(selected_features, ["feature2", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_4(self):
        # Smaller dataset
        df1 = pd.DataFrame(
            {
                "id": [1, 2],
                "feature1": [3.3, 4.4],
                "feature2": [5.5, 6.6],
                "feature3": [7.7, 8.8],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2], "target": [1, 0]})
        # Calling the function and asserting results
        selected_features, ax = f_444(df1, df2)
        self.assertListEqual(selected_features, ["feature2", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_5(self):
        # Dataset with different feature correlations
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [10, 20, 30],
                "feature2": [40, 50, 60],
                "feature3": [70, 80, 90],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1, 0, 1]})
        # Calling the function and asserting results
        selected_features, ax = f_444(df1, df2)
        self.assertListEqual(selected_features, ["feature2", "feature3"])
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
    def test_case_6(self):
        # Test handling errors - no "id"
        df1 = pd.DataFrame(
            {
                "feature1": [10, 20, 30],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1, 0, 1]})
        with self.assertRaises(KeyError):
            f_444(df1, df2)
    def test_case_7(self):
        # Test handling errors - wrong types
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": ["a", "b", 3],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [1, 0, 1]})
        with self.assertRaises(ValueError):
            f_444(df1, df2)
