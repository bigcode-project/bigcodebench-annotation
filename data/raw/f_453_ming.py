import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Constants for configuration
RANGE = 100
SIZE = 1000
CLUSTERS = 5


def f_453():
    """
    Generates a set of 2D random points within a specified range and size,
    applies KMeans clustering to these points, and plots the results with
    cluster centroids.

    The function creates a scatter plot of the clustered points with each
    cluster displayed in a different color and the centroids of these clusters
    highlighted.

    Requirements:
        - numpy for array operations.
        - sklearn.cluster for applying KMeans clustering.
        - matplotlib.pyplot for plotting the clustered points and centroids.

    Returns:
        A tuple containing the numpy array of data points and the fitted KMeans model.

    Example:
        >>> data, kmeans_model = f_453()
        This will display a scatter plot of clustered points and return the
        data points and the KMeans model used for clustering.
    """
    # Generate random 2D points
    data = np.array([(np.random.randint(0, RANGE), np.random.randint(0, RANGE)) for _ in range(SIZE)])

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=CLUSTERS)
    kmeans.fit(data)

    # Plot the clustered data points
    plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='viridis', marker='.')
    # Plot the cluster centroids
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='x')
    plt.title("KMeans Clustering of Random 2D Points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    return data, kmeans


import unittest
import numpy as np
from sklearn.cluster import KMeans

class TestF453(unittest.TestCase):
    def test_data_size(self):
        """Ensure the generated data has the correct size."""
        data, _ = f_453()
        self.assertEqual(data.shape, (SIZE, 2))

    def test_cluster_centers_shape(self):
        """Check the shape of the cluster centers array."""
        _, kmeans = f_453()
        self.assertEqual(kmeans.cluster_centers_.shape, (CLUSTERS, 2))

    def test_fitted_model(self):
        """Verify the model is a KMeans instance and is fitted."""
        _, kmeans = f_453()
        self.assertIsInstance(kmeans, KMeans)
        self.assertTrue(hasattr(kmeans, 'labels_'))

    def test_data_range(self):
        """Ensure that generated data points fall within the specified range."""
        data, _ = f_453()
        self.assertTrue((data >= 0).all() and (data <= RANGE).all())

    def test_cluster_labels(self):
        """Verify that cluster labels are assigned to each data point."""
        _, kmeans = f_453()
        self.assertEqual(len(kmeans.labels_), SIZE)


if __name__ == "__main__":
    unittest.main()
