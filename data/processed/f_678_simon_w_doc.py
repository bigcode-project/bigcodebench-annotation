import numpy as np
from sklearn.cluster import KMeans


def f_423(data, n_clusters):
    """
    Apply KMeans clustering to a 2D numeric array and find the indices of the data points in each cluster.

    Parameters:
    data (numpy array): The 2D numpy array for clustering.
    n_clusters (int): The number of clusters to form.

    Returns:
    dict: A dictionary where keys are cluster labels and values are lists of indices for data points in the cluster.

    Requirements:
    - numpy
    - sklearn.cluster

    Example:
    >>> data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    >>> cluster = f_423(data, 2)
    >>> cluster_list = list(cluster.values())
    >>> cluster_list.sort(key=lambda x: x[0])
    >>> print(cluster_list)
    [array([0, 1]), array([2, 3])]

    >>> data = np.array([[1, 1], [2, 2]])
    >>> cluster = f_423(data, 2)
    >>> cluster_list = list(cluster.values())
    >>> cluster_list.sort(key=lambda x: x[0])
    >>> print(cluster_list)
    [array([0]), array([1])]
    """
    kmeans = KMeans(n_clusters=n_clusters).fit(data)
    labels = kmeans.labels_
    clusters = {i: np.where(labels == i)[0] for i in range(n_clusters)}
    return clusters

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data = np.array([[1, 1], [1.1, 1.1], [5, 5], [5.1, 5.1]])
        result = f_423(data, 2)
        self.assertEqual(len(result), 2)
        self.assertTrue(isinstance(result[0], np.ndarray))
        self.assertTrue(isinstance(result[1], np.ndarray))
        result_list = [x.tolist() for x in result.values()]
        self.assertCountEqual(result_list, [[0, 1], [2, 3]])
    def test_case_2(self):
        data = np.array([[1, 2], [1, 3],[1, 4], [1, 5], [200, 1], [200, 2], [200, 3], [3000, 1], [3000, 3]])
        result = f_423(data, 3)
        self.assertEqual(len(result), 3)
        self.assertTrue(isinstance(result[0], np.ndarray))
        self.assertTrue(isinstance(result[1], np.ndarray))
        result_list = [x.tolist() for x in result.values()]
        self.assertCountEqual(result_list, [[0, 1, 2, 3], [4, 5, 6], [7, 8]])
    def test_case_3(self):
        data = np.array([[1, 2]])
        result = f_423(data, 1)
        self.assertEqual(len(result), 1)
        self.assertTrue(isinstance(result[0], np.ndarray))
        self.assertCountEqual(list(result.values()), [0])
    def test_case_4(self):
        '''wrong input'''
        self.assertRaises(Exception, f_423, [])
        self.assertRaises(Exception, f_423, 2)
        self.assertRaises(Exception, f_423, [['asv', 1]])
        self.assertRaises(Exception, f_423, {})
    def test_case_5(self):
        data = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
        result = f_423(data, 5)
        self.assertEqual(len(result), 5)
        for i in range(5):
            self.assertTrue(isinstance(result[i], np.ndarray))
        result_list = [x.tolist() for x in result.values()]
        self.assertCountEqual(result_list, [[0], [1], [2], [3], [4]])
