import pandas as pd
from sklearn.cluster import KMeans


def f_582(x_list, y_list, n_clusters=2, random_state=0):
    """
    Perform K-Means clustering on the given data by first turning it into a DataFrame with two columns "x" and "y" and then return the labels and centroids.

    Parameters:
    - x_list (list): List of data corresponding to 'x'
    - y_list (list): List of data corresponding to 'y'
    - n_clusters (int): Number of clusters to form, default to 2
    - random_state (int): Initial random state of k-means, default to 0

    Returns:
    tuple: The labels and centroids as numpy arrays.
        - kmeans.labels_: A NumPy array where each element is the cluster label assigned to each data point. 
        - kmeans.cluster_centers_: A NumPy array containing the coordinates of the cluster centers.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6], 'y': [2, 3, 4, 5, 6, 7]})
    >>> labels, centroids = f_582([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], 2, 0)
    """
    df = pd.DataFrame({'x': x_list, 'y': y_list})
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(df)
    return kmeans.labels_, kmeans.cluster_centers_


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.random_state = 0
        self.n_clusters = 2

    def test_case_1(self):
        labels, centroids = f_582([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
        self.assertEqual(labels[2], 0)
        self.assertEqual(labels[3], 1)
        self.assertEqual(labels[4], 1)
        self.assertEqual(labels[5], 1)
        self.assertEqual(centroids[0][0], 2.)
        self.assertEqual(centroids[0][1], 3.)
        self.assertEqual(centroids[1][0], 5.)
        self.assertEqual(centroids[1][1], 6.)

    def test_case_2(self):
        labels, centroids = f_582([1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
        self.assertEqual(labels[2], 0)
        self.assertEqual(labels[3], 0)
        self.assertEqual(labels[4], 0)
        self.assertEqual(labels[5], 0)
        self.assertEqual(centroids[0][0], 1.)
        self.assertEqual(centroids[0][1], 2.)

    def test_case_3(self):
        labels, centroids = f_582([1, 2, 3, 4, 5, 6], [2, 2, 2, 2, 2, 2],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
        self.assertEqual(labels[2], 0)
        self.assertEqual(labels[3], 1)
        self.assertEqual(labels[4], 1)
        self.assertEqual(labels[5], 1)
        self.assertEqual(centroids[0][0], 2.)
        self.assertEqual(centroids[0][1], 2.)
        self.assertEqual(centroids[1][0], 5.)
        self.assertEqual(centroids[1][1], 2.)

    def test_case_4(self):
        labels, centroids = f_582([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)

    def test_case_5(self):
        labels, centroids = f_582([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6],
                                  self.n_clusters, self.random_state)
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
        self.assertEqual(labels[2], 0)
        self.assertEqual(labels[3], 1)
        self.assertEqual(labels[4], 1)
        self.assertEqual(labels[5], 1)
        self.assertEqual(centroids[0][0], 2.)
        self.assertEqual(centroids[0][1], 2.)
        self.assertEqual(centroids[1][0], 5.)
        self.assertEqual(centroids[1][1], 5.)


run_tests()
if __name__ == "__main__":
    run_tests()
