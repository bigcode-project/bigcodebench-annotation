import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def f_293(myList, n_clusters):
    """
    Cluster a list of 2D points using KMeans and visualize the clusters.

    Note: This function raises ValueError if it encounters invalid inputs.
    KMeans is performed with random_state = 42 and n_init = 10. Scatterplot
    uses red 'x' markers for cluster centers.

    Parameters:
    - myList (list): List of 2D points.
    - n_clusters (int): Number of clusters to form.

    Returns:
    - matplotlib.axes._axes.Axes: Axes object with the plotted clusters.

    Requirements:
    - matplotlib.pyplot
    - sklearn.cluster.KMeans

    Example:
    >>> myList = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    >>> ax = f_293(myList, 2)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(0.0, 0, '0'), Text(1.0, 0, '1'), Text(2.0, 0, '2'), Text(3.0, 0, '3'), Text(4.0, 0, '4'), Text(5.0, 0, '5'), Text(6.0, 0, '6'), Text(7.0, 0, '7'), Text(8.0, 0, '8'), Text(9.0, 0, '9'), Text(10.0, 0, '10')]
    """
    if not myList or n_clusters <= 0:
        raise ValueError("Invalid inputs")

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(myList)

    fig, ax = plt.subplots()
    ax.scatter(*zip(*myList), c=kmeans.labels_)
    ax.scatter(*zip(*kmeans.cluster_centers_), marker="x", color="red")
    return ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_list = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    def test_case_1(self):
        # Test single cluster
        myList = [[1, 1], [1, 1], [1, 1], [1, 1]]
        ax = f_293(myList, 1)
        self.assertEqual(len(set(ax.collections[0].get_array())), 1)
    def test_case_2(self):
        # Test arbitrary number of clusters
        myList = self.test_list
        for n in range(1, 6):
            ax = f_293(myList, n)
            self.assertEqual(len(set(ax.collections[0].get_array())), n)
    def test_case_3(self):
        # Test visualization
        myList = self.test_list
        ax = f_293(myList, 2)
        red_collection = next(
            coll
            for coll in ax.collections
            if (
                coll.get_facecolor()[0][0] == 1.0
                and coll.get_facecolor()[0][1] == 0.0
                and coll.get_facecolor()[0][2] == 0.0
            )
        )
        red_x_markers_count = len(red_collection.get_offsets())
        self.assertEqual(red_x_markers_count, 2)
    def test_case_4(self):
        # Test handling invalid inputs
        with self.assertRaises(ValueError):
            f_293([], 1)
        with self.assertRaises(ValueError):
            f_293([[1, 1], [2, 2]], 0)
        with self.assertRaises(ValueError):
            f_293(self.test_list, len(self.test_list) + 1)
    def test_case_5(self):
        # Test consistency across runs with built-in random seed
        myList = self.test_list
        ax1 = f_293(myList, 2)
        ax2 = f_293(myList, 2)
        colors1 = ax1.collections[0].get_array()
        colors2 = ax2.collections[0].get_array()
        self.assertTrue(all(c1 == c2 for c1, c2 in zip(colors1, colors2)))
    def tearDown(self):
        plt.close("all")
