from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    """
    Calculate the Euclidean distances between consecutive points in a provided 
    list of 2D coordinates.

    This function takes a list of tuples, where each tuple contains two numbers
    representing a point in 2D space. It computes the Euclidean distance between
    each consecutive pair of points.

    If an empty list or a single point is passed, the function returns an empty list.
    If a tuple contains just one number it is assumed that both coordinates are equal to this number.
    Example: (2) == (2, 2)

    Parameters:
    points (list of tuples): A list of tuples where each tuple contains two 
                             numbers (x, y), representing a point in 2D space.

    Returns:
    list of floats: A list containing the Euclidean distances between 
                    consecutive points. Each distance is a float.
    
    Requirements:
    - itertools
    - scipy.spatial

    Example:
    >>> task_func([(1, 2), (3, 4), (5, 6), (7, 8)])
    [2.8284271247461903, 2.8284271247461903, 2.8284271247461903]

    >>> task_func([(1, 2), (4), (-1.2, 4)])
    [3.605551275463989, 5.2]
    """
    distances = []
    for point1, point2 in zip_longest(points, points[1:]):
        if point2 is not None:
            distances.append(distance.euclidean(point1, point2))
    return distances

import unittest
class TestCases(unittest.TestCase):
    def test_empty_list(self):
        # Testing with no points
        self.assertEqual(task_func([]), [])
    def test_single_point(self):
        # Testing with a single point (no distances can be calculated)
        self.assertEqual(task_func([(0, 0)]), [])
    def test_zero_distance(self):
        # Testing with multiple points at the same location (zero distance)
        self.assertEqual(task_func([(3, 4), (3, 4)]), [0.0])
    def test_various_distances(self):
        # Testing with points at various distances
        points = [(1, 2), (4, 6), (4, 6), (10, 20)]
        # The distances between the points are approximately:
        results = task_func(points)
        self.assertTrue(all(isinstance(x, float) for x in results))
        self.assertAlmostEqual(results[0], 5.0, places=4)
        self.assertAlmostEqual(results[1], 0.0, places=4)
        self.assertAlmostEqual(results[2], 15.2315421, places=4)
    def test_negative_coordinates(self):
        # Testing with points in negative coordinates
        points = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
        results = task_func(points)
        expected = [1.4142135623730951] * 3  # repeating 3 times
        self.assertEqual(results, expected)
