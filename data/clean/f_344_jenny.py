import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def f_344(P, T):
    """
    Calculate the product of a matrix 'P' and a 3D tensor 'T' using numpy and visualize the results as a heatmap.
    Note: This function only accepts numpy matrices/arrays.

    Parameters:
    - P (numpy.ndarray): Input matrix of shape (M, 3), where M can be any positive integer.
    - T (numpy.ndarray): Input tensor of shape (3, 3, 3).

    Returns:
    - numpy.ndarray: Resultant product after matrix-tensor multiplication.
    - matplotlib.axes.Axes: Axes object displaying the heatmap of the 2D result.

    Requirements:
    - numpy
    - seaborn

    Example:
    >>> np.random.seed(0)
    >>> P = np.array([[6, 2, 7], [1, 1, 8]])
    >>> T = np.random.rand(3, 3, 3)
    >>> product, heatmap = f_344(P, T)
    >>> product
    array([[[ 9.50686132, 11.96467131, 11.52469849],
            [ 9.99949817,  7.62347761,  9.48114103],
            [ 3.62770285,  9.87052195,  8.45068927]],
    <BLANKLINE>
           [[ 7.15750903,  8.46701159,  8.96060503],
            [ 7.50619626,  5.04108634,  6.96116358],
            [ 1.47091192,  6.03135957,  2.94310891]]])
    >>> type(heatmap)
    <class 'matplotlib.axes._axes.Axes'>
    """
    if not (isinstance(P, np.ndarray) and isinstance(T, np.ndarray)):
        raise TypeError("Expected inputs to be numpy arrays")

    result = np.tensordot(P, T, axes=[1, 0])
    # Sum along the last dimension to get a 2D matrix
    result_2D = np.sum(result, axis=-1)
    heatmap = sns.heatmap(result_2D)
    return result, heatmap


import unittest
import numpy as np
import matplotlib.pyplot as plt


class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.test_P = np.array([[6, 2, 7], [1, 1, 8]])
        self.test_P_zeros = np.zeros((2, 3))
        self.test_T = np.array(
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[2, 3, 4], [5, 6, 7], [8, 9, 10]],
                [[3, 4, 5], [6, 7, 8], [9, 10, 11]],
            ]
        )

    def test_case_1(self):
        # Test return types
        product, heatmap = f_344(self.test_P, self.test_T)
        self.assertIsInstance(product, np.ndarray)
        self.assertIsInstance(heatmap, plt.Axes)

    def test_case_2(self):
        # Test output correctness
        product, _ = f_344(self.test_P, self.test_T)
        expected_product = np.tensordot(self.test_P, self.test_T, axes=[1, 0])
        self.assertTrue(np.allclose(product, expected_product))

    def test_case_3(self):
        # Test output correctness with zeros
        product, _ = f_344(self.test_P_zeros, self.test_T)
        self.assertTrue(np.all(product == 0))

    def test_case_4(self):
        # Test return shape
        product, _ = f_344(self.test_P, self.test_T)
        expected_shape = (2, 3, 3)
        self.assertEqual(product.shape, expected_shape, "Output shape is incorrect")

    def test_case_5(self):
        # Test handling invalid input types
        with self.assertRaises(TypeError):
            f_344([1, 2], [2, 1])

    def test_case_6(self):
        # Test handling invalid shape
        P = np.array([[1, 2], [3, 4]])
        T = np.random.rand(3, 3, 3)
        with self.assertRaises(ValueError):
            f_344(P, T)

    def tearDown(self):
        plt.close("all")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
