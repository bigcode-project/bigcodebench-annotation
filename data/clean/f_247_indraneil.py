import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def f_247(data, save_plot=False, plot_path=None):
    """
    Unzip a list of objects and their 3D coordinates, run PCA to reduce the dimensionality to 2D, 
    and depending on the value of save_plot parameter, either save the plot to the provided path and 
    return the 2D coordinates or return the 2D coordinates and the plot's Axes.

    Parameters:
    - data (list of tuple): A list containing tuples of an object and its 3D coordinates.
    - save_plot (bool, optional): If True, the plot will be saved. Defaults to False.
    - plot_path (str, optional): The path where the plot will be saved. Required if save_plot is True.

    Returns:
    - coordinates_2d (numpy.ndarray): The 2D coordinates after applying PCA.
    - ax (matplotlib.axes._subplots.AxesSubplot, optional): The plot's Axes if save_plot is True.

    Requirements:
    - numpy
    - sklearn.decomposition.PCA
    - matplotlib.pyplot

    Raises:
    - ValueError: If save_plot is True but plot_path is not provided.

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.gettempdir()
    >>> f_247([('A', 1, 1, 1), ('B', 2, 2, 2)], save_plot=True, plot_path=f"{temp_dir}/temp_plot.png")[0]
    array([[ 8.66025404e-01,  4.09680598e-17],
           [-8.66025404e-01,  4.09680598e-17]])
    """
    items, x_values, y_values, z_values = zip(*data)
    coordinates = np.array(list(zip(x_values, y_values, z_values)))

    pca = PCA(n_components=2)
    coordinates_2d = pca.fit_transform(coordinates)

    # Initialize a fresh plot
    plt.figure()
    fig, ax = plt.subplots()
    ax.scatter(*zip(*coordinates_2d))

    if save_plot:
        if plot_path:
            plt.savefig(plot_path)
            plt.close(fig)
            return coordinates_2d, ax
        else:
            raise ValueError("plot_path is required if save_plot is True")
    else:
        return coordinates_2d


import unittest
import os
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Basic functionality test
        data = [('A', 1, 1, 1), ('B', 2, 2, 2)]
        result = f_247(data)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (2, 2))
        # Test the return value
        self.assertTrue(np.allclose(result, [[0.866, 0], [-0.866, 0]], atol=0.1))

    def test_case_2(self):
        # Test with save_plot=True without providing plot_path
        data = [('A', 1, 1, 1), ('B', 2, 2, 2)]
        with self.assertRaises(ValueError):
            f_247(data, save_plot=True)

    def test_case_3(self):
        # Test with save_plot=True and providing plot_path
        data = [('A', 1, 1, 1), ('B', 2, 2, 2)]
        plot_path = "temp_plot.png"
        result, ax = f_247(data, save_plot=True, plot_path=plot_path)
        self.assertTrue(os.path.exists(plot_path))
        os.remove(plot_path)

    def test_case_4(self):
        # Test with different data
        data = [('A', 3, 2, 1), ('B', 5, 6, 7), ('C', 8, 9, 10)]
        result = f_247(data)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (3, 2))

    def test_case_5(self):
        # Test with larger data
        data = [('A', i, i+1, i+2) for i in range(10)]
        result = f_247(data)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (10, 2))
        # Test the return value
        self.assertTrue(
            np.allclose(
                result, 
                [
                    [-7.79, 0.], [-6.06, 0.], [-4.33, -0.], [-2.6, -0.], [-0.87, -0.], 
                    [0.87, 0.], [2.6, 0.], [4.33, 0.], [6.06, -0.], [7.79, 0.]
                ], 
                atol=0.1
            )
        )


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
