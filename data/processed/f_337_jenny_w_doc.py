from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def f_109(df1, df2, column1="feature1", column2="feature2"):
    """Merge datasets, perform KMeans clustering, then return cluster labels and scatterplot.

    Each dataset is assumed to contain at least one id column and one feature column. The column to process
    is specified for df1 and df2 via column1 and column2, respectively. KMeans clustering is applied
    with k=2 and n_init=10. Resulting scatterplot shows column1 on the x-axis, column2 on the y-axis,
    and predicted cluster as color.

    Parameters:
    - df1 (pd.DataFrame): Dataframe with columns 'id' and feature columns including column1.
    - df2 (pd.DataFrame): Dataframe with columns 'id' and feature columns including column2.
    - column1 (str): Name of column containing features to model in df1. Defaults to "feature1".
    - column2 (str): Name of column containing features to model in df2. Defaults to "feature2".

    Returns:
    - labels (numpy.ndarray): Cluster labels for each data point (dtype=int32).
    - ax (matplotlib.axes._axes.Axes): The plotted figure's Axes object.

    Requirements:
    - sklearn.cluster.KMeans
    - matplotlib.pyplot

    Example:
    >>> df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6]})
    >>> df2 = pd.DataFrame({'id': [1, 2, 3], 'feature2': [2.3, 4.5, 6.7]})
    >>> labels, ax = f_109(df1, df2)
    >>> type(labels)
    <class 'numpy.ndarray'>
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    df = pd.merge(df1, df2, on="id")
    X = df[[column1, column2]]
    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(X)
    labels = kmeans.labels_
    _, ax = plt.subplots()
    ax.scatter(X[column1], X[column2], c=kmeans.labels_)
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    return labels, ax

import unittest
import pandas as pd
import numpy as np
import matplotlib
class TestCases(unittest.TestCase):
    def setUp(self):
        # Sample dataframes for testing
        self.df1_base = pd.DataFrame(
            {"id": [1, 2, 3, 4, 5], "feature1": [1.2, 3.4, 5.6, 7.8, 9.0]}
        )
        self.df2_base = pd.DataFrame(
            {"id": [1, 2, 3, 4, 5], "feature2": [2.3, 4.5, 6.7, 8.9, 10.1]}
        )
    def tearDown(self):
        plt.close("all")
    def test_case_1(self):
        # Test scatterplot
        _, ax = f_109(self.df1_base, self.df2_base)
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes)
        self.assertEqual(ax.get_xlabel(), "feature1")
        self.assertEqual(ax.get_ylabel(), "feature2")
    def test_case_2(self):
        # Expect 2 clusters
        labels, _ = f_109(self.df1_base, self.df2_base)
        self.assertEqual(len(labels), 5)
        self.assertEqual(len(np.unique(labels)), 2)
    def test_case_3(self):
        # Mixed valid data types
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [1.1, 2.2, 3.3]})
        labels, _ = f_109(df1, df2)
        self.assertEqual(len(labels), 3)
    def test_case_4(self):
        # Partial matches
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1.2, 3.4, 5.6]})
        df2 = pd.DataFrame({"id": [1, 2, 6], "feature2": [1.2, 3.1, 6.7]})
        labels, _ = f_109(df1, df2)
        self.assertEqual(len(labels), 2)
        self.assertEqual(len(np.unique(labels)), 2)
    def test_case_5(self):
        # Should fail when there's no matching id
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1.2, 3.4, 5.6]})
        df2 = pd.DataFrame({"id": [4, 5, 6], "feature2": [2.3, 4.5, 6.7]})
        with self.assertRaises(ValueError):
            f_109(df1, df2)
    def test_case_6(self):
        # Should fail on non-numeric columns
        df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": ["a", "b", "c"]})
        df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [1.1, 2.2, 3.3]})
        with self.assertRaises(Exception):
            f_109(df1, df2)
    def test_case_7(self):
        # Should fail on missing value
        df1 = pd.DataFrame(
            {"id": [1, 2, 3, 4, 5], "feature1": [1.2, np.nan, 5.6, 7.8, 9.0]}
        )
        df2 = pd.DataFrame(
            {"id": [1, 2, 3, 4, 5], "feature2": [2.3, 4.5, np.nan, 8.9, 10.1]}
        )
        with self.assertRaises(ValueError):
            f_109(df1, df2)
