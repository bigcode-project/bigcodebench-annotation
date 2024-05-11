import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
# Constants for configuration
RANGE = 100
SIZE = 1000
CLUSTERS = 5


def task_func():
    """
    Generates a set of 2D random points within a specified range and size,
    applies KMeans clustering to these points, and plots the results with
    cluster centroids.

    The function creates a scatter plot of the clustered points with each
    cluster displayed in a different color and the centroids of these clusters
    highlighted.

    Requirements:
        - numpy
        - sklearn.cluster
        - matplotlib.pyplot

    Returns:
        A tuple containing the numpy array of data points and the fitted KMeans model.

    Example:
    >>> data, kmeans = task_func()
    >>> isinstance(data, np.ndarray)  # Check if data is a numpy array
    True
    >>> data.shape == (1000, 2)  # Verify the shape of the data array
    True
    >>> isinstance(kmeans, KMeans)  # Confirm kmeans is an instance of KMeans
    True
    >>> len(kmeans.cluster_centers_) == 5  # Check the number of clusters
    True
    """
    data = np.array([(np.random.randint(0, RANGE), np.random.randint(0, RANGE)) for _ in range(SIZE)])
    kmeans = KMeans(n_clusters=CLUSTERS)
    kmeans.fit(data)
    plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='viridis', marker='.')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='x')
    plt.title("KMeans Clustering of Random 2D Points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    return data, kmeans

import unittest
class TestCases(unittest.TestCase):
    def test_data_size(self):
        """Ensure the generated data has the correct size."""
        data, _ = task_func()
        self.assertEqual(data.shape, (SIZE, 2))
    def test_cluster_centers_shape(self):
        """Check the shape of the cluster centers array."""
        _, kmeans = task_func()
        self.assertEqual(kmeans.cluster_centers_.shape, (CLUSTERS, 2))
    def test_fitted_model(self):
        """Verify the model is a KMeans instance and is fitted."""
        _, kmeans = task_func()
        self.assertIsInstance(kmeans, KMeans)
        self.assertTrue(hasattr(kmeans, 'labels_'))
    def test_data_range(self):
        """Ensure that generated data points fall within the specified range."""
        data, _ = task_func()
        self.assertTrue((data >= 0).all() and (data <= RANGE).all())
    def test_cluster_labels(self):
        """Verify that cluster labels are assigned to each data point."""
        _, kmeans = task_func()
        self.assertEqual(len(kmeans.labels_), SIZE)
