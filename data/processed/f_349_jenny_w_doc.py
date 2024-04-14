import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f_349(n_points=100, random_seed=None):
    """
    Generate an array of random 3D dots in the range [0, 1) for each dimension
    and draw them in a 3D scatter plot.

    Parameters:
    n_points (int): The number of points to generate and plot. Default is 100.
    random_seed (int, optional): Seed for the random number generator. Default is None.

    Returns:
    tuple: A tuple containing:
        - points (ndarray): A numpy ndarray of shape (n_points, 3) with the coordinates of the points.
        - plot (Axes3D): A 3D scatter plot of the generated points.

    Requirements:
    - numpy
    - matplotlib.pyplot

    Example:
    >>> points, plot = f_349(200, random_seed=42)
    >>> type(points)
    <class 'numpy.ndarray'>
    >>> type(plot)
    <class 'mpl_toolkits.mplot3d.axes3d.Axes3D'>
    """
    np.random.seed(random_seed)
    points = np.random.random((n_points, 3))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(points[:, 0], points[:, 1], points[:, 2])

    return points, ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test default parameters - values
        points, _ = f_349()
        self.assertEqual(points.shape, (100, 3))
        self.assertTrue(
            (points >= 0).all() and (points < 1).all(),
            "All points should be in the range [0, 1)",
        )
    def test_case_2(self):
        # Test default parameters - plot
        _, plot = f_349()
        self.assertTrue(isinstance(plot, Axes3D))
    def test_case_3(self):
        # Test controlling number of points
        points1, _ = f_349(n_points=1)
        points10, _ = f_349(n_points=10)
        points100, _ = f_349(n_points=100)
        self.assertEqual(points1.shape, (1, 3))
        self.assertEqual(points10.shape, (10, 3))
        self.assertEqual(points100.shape, (100, 3))
    def test_case_4(self):
        # Test random seed
        points1, _ = f_349(random_seed=42)
        points2, _ = f_349(random_seed=42)
        self.assertTrue(
            np.array_equal(points1, points2),
            "The points should be identical for the same seed",
        )
    def test_case_5(self):
        # Test handling invalid inputs
        with self.assertRaises(ValueError):
            f_349(-1)
        for invalid in [0.5, "invalid", None, []]:
            with self.assertRaises(TypeError):
                f_349(invalid)
    def tearDown(self):
        plt.close("all")
