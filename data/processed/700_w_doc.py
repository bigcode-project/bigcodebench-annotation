import pandas as pd
from sklearn.cluster import KMeans

def task_func(x_list, y_list):
    """
    Perform K-Means clustering on the given data by first turning it into a DataFrame with two columns "x" and "y" and then return the labels and centroids.

    Parameters:
    - x_list (list): List of data corresponding to 'x'
    - y_list (list): List of data corresponding to 'y'

    Returns:
    tuple: The labels and centroids as numpy arrays.
        - kmeans.labels_: A NumPy array where each element is the cluster label assigned to each data point. 
        - kmeans.cluster_centers_: A NumPy array containing the coordinates of the cluster centers.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6], 'y': [2, 3, 4, 5, 6, 7]})
    >>> labels, centroids = task_func([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7])
    """
    df = pd.DataFrame({'x': x_list, 'y': y_list})
    kmeans = KMeans(n_clusters=2, random_state=0).fit(df)
    return kmeans.labels_, kmeans.cluster_centers_

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        labels, centroids = task_func([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7])
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
        labels, centroids = task_func([1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2])
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
        self.assertEqual(labels[2], 0)
        self.assertEqual(labels[3], 0)
        self.assertEqual(labels[4], 0)
        self.assertEqual(labels[5], 0)
        self.assertEqual(centroids[0][0], 1.)
        self.assertEqual(centroids[0][1], 2.)
    def test_case_3(self):
        labels, centroids = task_func([1, 2, 3, 4, 5, 6], [2, 2, 2, 2, 2, 2])
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
        labels, centroids = task_func([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])
        self.assertEqual(labels[0], 0)
        self.assertEqual(labels[1], 0)
    def test_case_5(self):
        labels, centroids = task_func([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
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
