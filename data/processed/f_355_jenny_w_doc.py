from scipy.spatial.distance import cdist
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt


def f_551(n_samples=200, centers=4, plot_path=None, random_seed=None):
    """
    Generate a synthetic 2D dataset using make_blobs, visualize the dataset, and then calculate
    the Euclidean distance between individual samples of the dataset.

    Parameters:
    - n_samples (int): Number of samples to generate. Default is 200.
    - centers (int): Number of centers to generate. Default is 4.
    - plot_path (str, optional): Path to save the plot. If None, the plot will be returned.
    - random_seed (int, optional): Seed for random number generation. Default is None.

    Returns:
    - tuple:
        - ndarray: A 2D array with distances between each sample.
        - Axes or None: If plot_path is None, returns the matplotlib Axes object of the plot.
                        Otherwise, saves the plot to the provided path and return None.
                        Plot shows values of the first feature dimension on the x-axis, values
                        of the second feature dimension on the y-axis, and labels of the synthetic
                        examples as color.

    Requirements:
    - scipy.spatial.distance.cdist
    - sklearn.datasets.make_blobs
    - matplotlib.pyplot

    Example:
    >>> distances, plot = f_551(random_seed=42)
    >>> distances.shape
    (200, 200)
    >>> plot
    <Axes: >
    """
    X, y = make_blobs(
        n_samples=n_samples,
        n_features=2,
        centers=centers,
        random_state=random_seed,
    )

    fig, ax = plt.subplots()

    ax.scatter(X[:, 0], X[:, 1], c=y)

    if plot_path:
        plt.savefig(plot_path)
        plt.close(fig)
        return cdist(X, X), None

    return cdist(X, X), ax

import unittest
import tempfile
import os
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.seed = 42
        self.temp_dir = tempfile.TemporaryDirectory()
    def test_case_1(self):
        # Default parameters
        distances, plot = f_551()
        self.assertEqual(distances.shape, (200, 200))
        self.assertEqual(len(plot.collections[0].get_offsets()), 200)
        self.assertEqual(len(set(plot.collections[0].get_array())), 4)
    def test_case_2(self):
        # Custom parameters
        n_samples, centers = 50, 5
        distances, plot = f_551(
            random_seed=self.seed, n_samples=n_samples, centers=centers
        )
        self.assertEqual(distances.shape, (n_samples, n_samples))
        self.assertEqual(len(plot.collections[0].get_offsets()), n_samples)
        self.assertEqual(len(set(plot.collections[0].get_array())), centers)
    def test_case_3(self):
        # Saving the plot to a path
        plot_path = os.path.join(self.temp_dir.name, "test_plot.png")
        distances, plot = f_551(random_seed=self.seed, plot_path=plot_path)
        self.assertEqual(distances.shape, (200, 200))
        self.assertTrue(os.path.exists(plot_path))
        self.assertIsNone(plot)
    def test_case_4(self):
        # Test reproducibility with the same seed
        distances1, _ = f_551(random_seed=self.seed)
        distances2, _ = f_551(random_seed=self.seed)
        np.testing.assert_array_equal(distances1, distances2)
        # Test different outputs with different seeds
        distances3, _ = f_551(random_seed=43)
        with self.assertRaises(AssertionError):
            np.testing.assert_array_equal(distances1, distances3)
    def test_case_5(self):
        # Test negative parameters for n_samples
        with self.assertRaises(ValueError):
            f_551(n_samples=-100, random_seed=self.seed)
    def test_case_6(self):
        # Test non-integer inputs for n_samples
        with self.assertRaises(TypeError):
            f_551(n_samples=200.5, random_seed=self.seed)
    def tearDown(self):
        plt.close("all")
        self.temp_dir.cleanup()
