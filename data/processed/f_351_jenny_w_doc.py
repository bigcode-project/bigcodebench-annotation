import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


def f_174(n_samples=100, centers=3, n_features=2, random_seed=42):
    """
    Create isotropic Gaussian blobs to form clusters and visualize them.

    Parameters:
    - n_samples (int): The total number of points divided among clusters.
    - centers (int): The number of centers to generate.
    - n_features (int): The number of features for each sample.
    - random_seed (int): The seed for the random number generator.

    Returns:
    tuple: A tuple containing:
        - X (numpy.ndarray): The matrix of blob points.
        - y (numpy.ndarray): The vector of blob labels.
        - ax (matplotlib.axes.Axes): The Axes object with the scatter plot.

    Requirements:
    - matplotlib.pyplot
    - sklearn

    Example:
    >>> X, y, ax = f_174(n_samples=500, centers=5, random_seed=0)
    >>> type(X), type(y), type(ax)
    (<class 'numpy.ndarray'>, <class 'numpy.ndarray'>, <class 'matplotlib.axes._axes.Axes'>)
    >>> ax
    <Axes: >
    """
    X, y = make_blobs(
        n_samples=n_samples,
        centers=centers,
        n_features=n_features,
        random_state=random_seed,
    )

    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=y)

    return X, y, ax

import unittest
import matplotlib
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test default case
        n_samples, n_features, centers = 100, 2, 3
        X, y, ax = f_174()
        self.assertEqual(X.shape, (n_samples, n_features))
        self.assertEqual(y.shape, (n_samples,))
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(set(y)), centers)
    def test_case_2(self):
        # Test n_samples
        for n_samples in [1, 50, 100]:
            X, y, _ = f_174(n_samples=n_samples)
            self.assertEqual(X.shape[0], n_samples)
            self.assertEqual(y.shape[0], n_samples)
    def test_case_3(self):
        # Test centers
        for centers in [1, 50, 100]:
            _, y, _ = f_174(centers=centers)
        self.assertEqual(len(set(y)), centers)
    def test_case_4(self):
        # Test n_features
        for n_features in [2, 50, 100]:
            X, y, _ = f_174(n_features=n_features)
            self.assertEqual(X.shape[1], n_features)
    def test_case_5(self):
        # Test random seed
        X1, y1, _ = f_174(n_samples=100, centers=3, n_features=2, random_seed=42)
        X2, y2, _ = f_174(n_samples=100, centers=3, n_features=2, random_seed=42)
        self.assertTrue((X1 == X2).all())
        self.assertTrue((y1 == y2).all())
    def test_case_6(self):
        # Test with the minimum possible values that are still valid
        n_samples, n_features, centers = 1, 2, 1
        X, y, ax = f_174(
            n_samples=1, centers=centers, n_features=n_features, random_seed=0
        )
        self.assertEqual(X.shape, (n_samples, n_features))
        self.assertEqual(y.shape, (n_samples,))
        self.assertEqual(len(set(y)), centers)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_7(self):
        # Example of handling an expected failure due to invalid input
        with self.assertRaises(ValueError):
            f_174(n_samples=-100)
        with self.assertRaises(ValueError):
            f_174(centers=-10)
        with self.assertRaises(Exception):
            f_174(n_features=0)
        with self.assertRaises(ValueError):
            f_174(random_seed="invalid")
    def tearDown(self):
        plt.close("all")
