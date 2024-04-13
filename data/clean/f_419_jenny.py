from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def f_419(df, n_clusters=3, random_state=None, n_init=10):
    """
    Identify duplicate points in a DataFrame, perform KMeans clustering on the unique points,
    and record the clusters.

    Parameters:
    df (pd.DataFrame): A DataFrame containing at least two columns 'x' and 'y' representing points.
    n_clusters (int, optional): Number of clusters for KMeans clustering. Default is 3.
    random_state (int, optional): The seed used by the random number generator for reproducibility. Default is None.
    n_init (int, optional): Number of time the k-means algorithm will be run with different centroid seeds.
                            The final results will be the best output of n_init consecutive runs in terms of
                            within-cluster sum of squares. Default is 10.

    Returns:
    tuple: A tuple containing:
        - Counter: A Counter object with the count of duplicate points.
        - pd.DataFrame: A DataFrame with an additional column 'cluster' representing cluster assignments for unique points.
        - Axes: A scatter plot of the clustered data.

    Requirements:
    - collections.Counter
    - sklearn.cluster.KMeans
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame({\
            'x': [1, 2, 2, 2, 3, 4],\
            'y': [1, 1, 1, 1, 3, 3]\
        })
    >>> duplicates, df_clustered, ax = f_419(df, random_state=42)
    >>> df_clustered
       x  y  cluster
    0  1  1        2
    1  2  1        0
    4  3  3        1
    5  4  3        1
    >>> duplicates
    Counter({(2, 1): 3})
    """
    # Identify duplicates
    duplicates = df[df.duplicated(subset=["x", "y"], keep=False)]
    duplicates_counter = Counter(map(tuple, duplicates[["x", "y"]].values))

    # Remove duplicates and perform KMeans clustering on unique points
    unique_df = df.drop_duplicates(subset=["x", "y"]).copy()

    # Adjust n_clusters if unique data points are fewer than desired clusters
    n_clusters = min(n_clusters, len(unique_df))

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    unique_df["cluster"] = kmeans.fit_predict(unique_df[["x", "y"]])

    # Plot clustered data
    fig, ax = plt.subplots()
    scatter = ax.scatter(unique_df["x"], unique_df["y"], c=unique_df["cluster"])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("KMeans Clusters")

    return duplicates_counter, unique_df, ax


import unittest
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic functionality with duplicates
        df = pd.DataFrame({"x": [1, 2, 2, 2, 3, 4], "y": [1, 1, 1, 1, 3, 3]})
        duplicates, df_clustered, ax = f_419(df, random_state=42)
        self.assertEqual(duplicates, Counter({(2, 1): 3}))
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")
        self.assertFalse(df_clustered["cluster"].isna().any())

    def test_case_2(self):
        # Test functionality without duplicates
        df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 6], "y": [1, 2, 3, 4, 5, 6]})
        duplicates, df_clustered, ax = f_419(df, random_state=42)
        self.assertEqual(duplicates, Counter())
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")

    def test_case_3(self):
        # Test functionality with all points being duplicates
        df = pd.DataFrame({"x": [1, 1, 1, 1, 1, 1], "y": [1, 1, 1, 1, 1, 1]})
        duplicates, df_clustered, ax = f_419(df, random_state=42)
        self.assertEqual(duplicates, Counter({(1, 1): 6}))
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")

    def test_case_4(self):
        # Test with specified number of clusters
        df = pd.DataFrame({"x": [1, 2, 3, 40, 50, 60], "y": [1, 2, 3, 40, 50, 60]})
        duplicates, df_clustered, ax = f_419(df, n_clusters=2, random_state=42)
        self.assertEqual(duplicates, Counter())
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")

    def test_case_5(self):
        # Test functionality with multiple duplicates
        df = pd.DataFrame(
            {"x": [1, 2, 3, 4, 5, 5, 5, 5], "y": [1, 2, 3, 4, 5, 5, 5, 5]}
        )
        duplicates, df_clustered, ax = f_419(df, random_state=42)
        self.assertEqual(duplicates, Counter({(5, 5): 4}))
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")
        self.assertFalse(df_clustered["cluster"].isna().any())

    def test_case_6(self):
        # Test with a mix of unique points and duplicates
        df = pd.DataFrame(
            {"x": [1, 2, 3, 3, 3, 4, 5, 6], "y": [1, 2, 3, 3, 3, 4, 5, 6]}
        )
        duplicates, df_clustered, ax = f_419(df, random_state=42)
        self.assertEqual(duplicates, Counter({(3, 3): 3}))
        self.assertIn("cluster", df_clustered.columns)
        self.assertEqual(ax.get_title(), "KMeans Clusters")
        self.assertFalse(df_clustered["cluster"].isna().any())

    def test_case_7(self):
        # Easily separable data
        df = pd.DataFrame(
            {
                "x": [1, 2, 3, 10, 11, 12, 20, 21, 22],
                "y": [1, 2, 3, 10, 11, 12, 20, 21, 22],
            }
        )

        # We expect 3 clusters because of the natural separation in data
        duplicates, df_clustered, _ = f_419(df, n_clusters=3, random_state=42)
        self.assertEqual(duplicates, Counter())

        # Check that all points in a specific region belong to the same cluster
        cluster_1 = df_clustered[df_clustered["x"] <= 3]["cluster"].nunique()
        cluster_2 = df_clustered[(df_clustered["x"] > 3) & (df_clustered["x"] <= 12)][
            "cluster"
        ].nunique()
        cluster_3 = df_clustered[df_clustered["x"] > 12]["cluster"].nunique()

        self.assertEqual(
            cluster_1, 1
        )  # All points in this region should belong to the same cluster
        self.assertEqual(
            cluster_2, 1
        )  # All points in this region should belong to the same cluster
        self.assertEqual(
            cluster_3, 1
        )  # All points in this region should belong to the same cluster

    def test_case_8(self):
        # Test effects of random state on clustering outcome
        df = pd.DataFrame(
            {"x": [10, 20, 20, 40, 50, 60], "y": [10, 20, 20, 40, 50, 60]}
        )
        _, df_clustered_1, _ = f_419(df, n_clusters=2, random_state=42)
        _, df_clustered_2, _ = f_419(df, n_clusters=2, random_state=42)

        # Clusters should be the same for the same random state
        self.assertTrue((df_clustered_1["cluster"] == df_clustered_2["cluster"]).all())

    def tearDown(self):
        plt.close("all")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
