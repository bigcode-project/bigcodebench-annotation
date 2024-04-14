import matplotlib.pyplot as plt
import numpy as np


def f_366(n, seed=0):
    """
    Generates a simple scatter plot with 'n' points.

    Parameters:
    - n (int): The number of points to be plotted.
    - seed (int, optional): The seed for the random number generator. Defaults to None.

    Returns:
    - plot (matplotlib.figure.Figure): The generated plot titled "Scatter plot of random points".
    - points (list of tuples): List containing the (x, y) coordinates of the plotted points.

    Requirements:
    - numpy
    - matplotlib.pyplot
    
    Example:
    >>> f_366(5)
    (<Figure size 640x480 with 1 Axes>, [(0.5488135039273248, 0.6458941130666561), (0.7151893663724195, 0.4375872112626925), (0.6027633760716439, 0.8917730007820798), (0.5448831829968969, 0.9636627605010293), (0.4236547993389047, 0.3834415188257777)])
    """
    # Setting the random seed for reproducibility
    np.random.seed(seed)

    # Generating random points
    x = np.random.rand(n)
    y = np.random.rand(n)

    # Plotting
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("Scatter plot of random points")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    return fig, list(zip(x, y))

import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic point type and structure
        _, points = f_366(5)
        self.assertTrue(
            all(
                isinstance(point, tuple)
                and len(point) == 2
                and all(isinstance(coord, float) for coord in point)
                for point in points
            ),
            "Points should be a list of tuples with float coordinates",
        )
    def test_case_2(self):
        # Test parameter 'n'
        for n in [0, 1, 5, 100]:
            plot, points = f_366(n)
            self.assertEqual(len(points), n)
            self.assertTrue(isinstance(plot, type(plt.figure())))
    def test_case_3(self):
        # Test random seed - reproduction
        _, points1 = f_366(5, seed=1)
        _, points2 = f_366(5, seed=1)
        self.assertEqual(
            points1, points2, "Points generated with the same seed should match exactly"
        )
    def test_case_4(self):
        # Test random seed - differences
        _, points1 = f_366(5, seed=1)
        _, points2 = f_366(5, seed=10)
        self.assertNotEqual(
            points1, points2, "Points generated with the same seed should match exactly"
        )
    def test_case_5(self):
        # Test invalid inputs
        with self.assertRaises(ValueError):
            f_366(-5)
        with self.assertRaises(TypeError):
            f_366(5.5)
        with self.assertRaises(TypeError):
            f_366("5")
    def test_case_6(self):
        # Test visualization
        fig, _ = f_366(1)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), "Scatter plot of random points")
        self.assertEqual(ax.get_xlabel(), "X")
        self.assertEqual(ax.get_ylabel(), "Y")
    def tearDown(self):
        plt.close("all")
