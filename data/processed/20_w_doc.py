from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def task_func(df, age: int, height: int):
    """
    Filters the input DataFrame based on specified 'Age' and 'Height' conditions and applies KMeans clustering.
    - If the filtered dataframe has less than 3  columns, add to it a column 'Cluster' with 0 for each row.
    - Otherwise, do a KMeans clustering (by Age and Height) with 3 clusters and add a column 'Cluster' to the dataframe which corresponds to the cluster
    index of the cluster to which each row belongs to.
    - Plot a scatter plot of the 'Age' and 'height' and colored by the cluster indices.
    - the xlabel should be 'Age', the ylabel 'Height' and the title 'KMeans Clustering based on Age and Height'.

    Parameters:
    df (DataFrame): The text to analyze.
    age (int): Filter out the rows of the dataframe which 'Age' value is less than or equal to this value.
    height (int): Filter out the rows of the dataframe which 'Height' value is greater than or equal to this value.

    Returns:
    DataFrame: The filtered dataframe with the new column.
    matplotlib.axes.Axes: The Axes object of the plotted data. If no KMeans was done, returns None.

    Requirements:
    - sklearn
    - matplotlib

    Example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'Age': [30, 45, 60, 75],
    ...     'Height': [160, 170, 165, 190],
    ...     'Weight': [55, 65, 75, 85]
    ... })
    >>> selected_df, ax = task_func(df, 50, 180)
    >>> print(selected_df)
       Age  Height  Weight  Cluster
    2   60     165      75        0
    """
    selected_df = df[(df["Age"] > age) & (df["Height"] < height)].copy()
    if len(selected_df) >= 3:
        kmeans = KMeans(n_clusters=3)
        selected_df["Cluster"] = kmeans.fit_predict(selected_df[["Age", "Height"]])
        plt.figure(figsize=(10, 5))
        plt.scatter(selected_df["Age"], selected_df["Height"], c=selected_df["Cluster"])
        plt.xlabel("Age")
        plt.ylabel("Height")
        plt.title("KMeans Clustering based on Age and Height")
        ax = plt.gca()
        return selected_df, ax
    else:
        selected_df["Cluster"] = 0
        return selected_df, None

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        data = {
            "Age": [25, 30, 35, 40, 45],
            "Height": [160, 155, 170, 165, 150],
            "Weight": [60, 65, 70, 75, 80],
        }
        df = pd.DataFrame(data)
        result, ax = task_func(df, 28, 165)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue("Cluster" in result.columns)
        self.assertListEqual(result["Cluster"].tolist(), [0, 0])
        self.assertTrue(max(result.loc[:, "Cluster"]) < 3)
        self.assertEqual(len(result), 2)
        self.assertIsNone(ax)
    def test_case_2(self):
        data = {
            "Age": [20, 25, 30, 35, 40],
            "Height": [150, 155, 160, 165, 170],
            "Weight": [55, 60, 65, 70, 75],
        }
        df = pd.DataFrame(data)
        result, ax = task_func(df, 30, 160)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue("Cluster" in result.columns or len(result) < 3)
        self.assertEqual(len(result), 0)
        self.assertIsNone(ax)
    def test_case_3(self):
        data = {
            "Age": [29, 30, 35, 40, 75],
            "Height": [140, 155, 170, 165, 210],
            "Weight": [60, 65, 70, 75, 70],
        }
        df = pd.DataFrame(data)
        result, ax = task_func(df, 28, 220)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue("Cluster" in result.columns or len(result) < 3)
        self.assertEqual(len(result), 5)
        self.assertEqual(ax.get_xlabel(), "Age")
        self.assertEqual(ax.get_ylabel(), "Height")
        self.assertEqual(ax.get_title(), "KMeans Clustering based on Age and Height")
    def test_case_4(self):
        data = {
            "Age": [25, 30, 35, 40, 45],
            "Height": [160, 155, 170, 165, 150],
            "Weight": [60, 65, 70, 75, 80],
        }
        df = pd.DataFrame(data)
        result, ax = task_func(df, 28, 180)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue("Cluster" in result.columns)
        self.assertTrue(max(result.loc[:, "Cluster"]) < 3)
        self.assertEqual(len(result), 4)
    def test_case_5(self):
        data = {
            "Age": [25, 30, 35, 40, 45],
            "Height": [160, 155, 170, 165, 150],
            "Weight": [60, 65, 70, 75, 80],
        }
        df = pd.DataFrame(data)
        result, ax = task_func(df, 24, 165)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue("Cluster" in result.columns)
        self.assertTrue(max(result.loc[:, "Cluster"]) < 3)
        self.assertEqual(len(result), 3)
