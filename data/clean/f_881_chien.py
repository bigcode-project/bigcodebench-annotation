import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def f_881(s1, s2, n_clusters=3):
    """
    Perform K-Means clustering on data points from two pandas Series and visualize the clusters.

    Parameters:
    - s1 (pandas.Series): The first series of data. Each value in the series represents a data point's coordinate along one dimension.
    - s2 (pandas.Series): The second series of data. Each value corresponds to a data point's coordinate along another dimension. The length of s2 must match that of s1.
    - n_clusters (int, optional): The number of clusters to form as well as the number of centroids to generate. Defaults to 3.

    Returns:
    - tuple: A tuple containing the following elements:
        - ndarray: An array of cluster labels indicating the cluster each data point belongs to.
        - matplotlib.axes.Axes: The Axes object of the plot, which shows the data points colored according to their cluster labels.

    Raises:
    - ValueError: If either s1 or s2 is not a pandas Series, raise "s1 and s2 must be pandas Series"
    - ValueError: If s1 and s2 have different lengths, raise "s1 and s2 must have the same length"

    Requirements:
    - pandas
    - scikit-learn
    - matplotlib

    Notes:
    - The function needs to ensure that s1 and s2 are pandas Series of equal length. 
    - It then performs K-Means clustering on the combined data points from s1 and s2. 
    - After clustering, it creates a scatter plot where each cluster is visualized with a different color. 
    - The plot title is set to "K-Means Clustering" to describe the visualization technique. 
    - A legend is added, which uses elements from the scatter plot to describe each cluster.
        
    Example:
    >>> s1 = pd.Series(np.random.rand(100), name='feature1')
    >>> s2 = pd.Series(np.random.rand(100), name='feature2')
    >>> labels, ax = f_881(s1, s2, n_clusters=4)
    >>> print(ax.get_title())
    K-Means Clustering

   
    """
    if not isinstance(s1, pd.Series) or not isinstance(s2, pd.Series):
        raise ValueError("s1 and s2 must be pandas Series")

    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have the same length")

    # Create a DataFrame from the series
    df = pd.concat([s1, s2], axis=1)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df)

    # Visualize the clusters
    _, ax = plt.subplots()
    scatter = ax.scatter(df[s1.name], df[s2.name], c=labels)
    ax.set_xlabel(s1.name)
    ax.set_ylabel(s2.name)
    ax.set_title("K-Means Clustering")
    plt.legend(*scatter.legend_elements(), title="Clusters")

    return labels, ax


import pandas as pd
import numpy as np
import unittest
import os
from sklearn.datasets import make_blobs


class TestCases(unittest.TestCase):
    """Tests for f_881."""

    def setUp(self) -> None:
        os.environ["LOKY_MAX_CPU_COUNT"] = "2"

    def test_random_data_size_100(self):
        """Test with random data of size 100 and default number of clusters"""
        np.random.seed(42)
        s1 = pd.Series(np.random.rand(100), name="feature1")
        np.random.seed(0)
        s2 = pd.Series(np.random.rand(100), name="feature2")
        labels, ax = f_881(s1, s2)

        # Check if labels are ndarray
        self.assertIsInstance(labels, np.ndarray)

        # Check the plot's title
        self.assertEqual(ax.get_title(), "K-Means Clustering")

    def test_random_data_custom_clusters(self):
        """Test with random data of size 100 and custom number of clusters"""
        np.random.seed(42)
        s1 = pd.Series(np.random.rand(100), name="feature1")
        np.random.seed(0)
        s2 = pd.Series(np.random.rand(100), name="feature2")
        labels, ax = f_881(s1, s2, n_clusters=5)

        # Check if labels are ndarray
        self.assertIsInstance(labels, np.ndarray)
        self.assertEqual(len(set(labels)), 5)

        # Check the plot's title
        self.assertEqual(ax.get_title(), "K-Means Clustering")

    def test_invalid_input_non_series(self):
        """Test with invalid input types (non-Series)"""
        with self.assertRaises(ValueError):
            f_881([1, 2, 3], pd.Series([4, 5, 6]))

    def test_invalid_input_mismatched_length(self):
        """Test with mismatched length of Series"""
        s1 = pd.Series([1, 2, 3], name="feature1")
        s2 = pd.Series([4, 5], name="feature2")
        with self.assertRaises(ValueError):
            f_881(s1, s2)

    def test_custom_clusters_with_synthetic_data(self):
        """Test with synthetic data and custom number of clusters using make_blobs"""
        # Generate synthetic data with 2 distinct clusters
        X, _ = make_blobs(n_samples=100, centers=2, random_state=42)

        # Convert to pandas Series
        s1 = pd.Series(X[:, 0], name="feature1")
        s2 = pd.Series(X[:, 1], name="feature2")

        # Run the clustering function
        labels, ax = f_881(s1, s2, n_clusters=2)

        # Check if labels are ndarray
        self.assertIsInstance(labels, np.ndarray)

        # Check the number of unique labels (should be 2 for 2 clusters)
        self.assertEqual(len(set(labels)), 2)

        # Check the plot's title
        self.assertEqual(ax.get_title(), "K-Means Clustering")

    def tearDown(self):
        plt.clf()


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
