import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def f_820(array, features=None, seed=None):
    """
    Shuffles the columns of a given 2D numpy array and visualizes it as a heatmap.

    Parameters:
    - array (ndarray): The 2D numpy array to shuffle and plot. It must not be empty.
    - features (list of str, optional): Custom labels for the columns after shuffling.
                                        If not specified, default numerical labels are used.
                                        The list must match the number of columns in 'array'.
    - seed (int, optional): Seed for the random number generator to ensure reproducibility of the shuffle.

    Returns:
    - Axes: The matplotlib Axes object containing the heatmap.

    Raises:
    - ValueError: If 'features' is provided and does not match the number of columns in 'array'; and
                  if 'array' is empty or not 2-dimensional.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - seaborn

    Notes:
    - This function uses the features list as labels for the heatmap's x-axis if features is provided;
      otherwise, it defaults to strings of the numerical labels starting from 1 up to the number of
      columns in the array.

    Example:
    >>> np.random.seed(0)
    >>> array = np.random.rand(2, 5)
    >>> ax = f_820(array, features=['A', 'B', 'C', 'D', 'E'], seed=1)
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    >>> ax.collections[0].get_array().data.flatten()
    array([0.60276338, 0.71518937, 0.4236548 , 0.5488135 , 0.54488318,
           0.891773  , 0.43758721, 0.38344152, 0.64589411, 0.96366276])
    """

    if seed is not None:
        np.random.seed(seed)

    if array.size == 0 or len(array.shape) != 2:
        raise ValueError("Input array must be 2-dimensional and non-empty.")

    if features is not None and len(features) != array.shape[1]:
        raise ValueError("Features list must match the number of columns in the array.")

    shuffled_array = np.random.permutation(array.T).T

    fig, ax = plt.subplots()
    sns.heatmap(
        shuffled_array,
        xticklabels=features if features is not None else np.arange(array.shape[1]) + 1,
        ax=ax,
    )

    return ax


import unittest
import numpy as np
import matplotlib.pyplot as plt


class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.expected_labels = ["1", "2", "3", "4", "5"]

    def test_default_features(self):
        """Test heatmap with default features."""
        ax = f_820(self.array)
        xticklabels = [tick.get_text() for tick in ax.get_xticklabels()]
        self.assertEqual(xticklabels, self.expected_labels)
        self.assertTrue(len(ax.collections), 1)

    def test_custom_features(self):
        """Test heatmap with custom features."""
        custom_labels = ["A", "B", "C", "D", "E"]
        ax = f_820(self.array, features=custom_labels)
        xticklabels = [tick.get_text() for tick in ax.get_xticklabels()]
        self.assertEqual(xticklabels, custom_labels)
        self.assertTrue(len(ax.collections), 1)

    def test_features_mismatch(self):
        """Test for error when features list does not match array dimensions."""
        with self.assertRaises(ValueError):
            f_820(self.array, features=["A", "B"])

    def test_seed_reproducibility(self):
        """Test if seeding makes shuffling reproducible."""
        ax1 = f_820(self.array, seed=42)
        ax2 = f_820(self.array, seed=42)
        heatmap_data1 = ax1.collections[0].get_array().data
        heatmap_data2 = ax2.collections[0].get_array().data
        np.testing.assert_array_equal(heatmap_data1, heatmap_data2)

    def test_empty_array(self):
        """Test for handling an empty array."""
        with self.assertRaises(ValueError):
            f_820(np.array([]))

    def tearDown(self):
        """Cleanup plot figures after each test."""
        plt.close("all")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
