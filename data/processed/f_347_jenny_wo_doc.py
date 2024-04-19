import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def f_347(P, T, tensor_shape=(3, 3, 3)):
    """
    Calculate the product of a matrix "P" and a 3D tensor "T" with numpy and then apply PCA to reduce the
    dimensionality of the result. The resulting 2D data is then visualized.
    Note: This function only accepts numpy matrices/arrays.

    Parameters:
    P (numpy.ndarray): The input matrix.
    T (numpy.ndarray): The input tensor. Must have same shape as tensor_shape.
    tensor_shape (tuple, optional): The shape of the tensor. Must be same as T.shape. Default is (3, 3, 3).

    Returns:
    pca_result (numpy.ndarray): The result of PCA of shape (N, 2), where N is the number of rows in matrix P.
    ax (matplotlib.axes.Axes): Plot of 'PCA Result Visualization', with 'Principal Component 1' on the x-axis
                               and 'Principal Component 2' on the y-axis.



    Requirements:
    - numpy
    - sklearn.decomposition
    - matplotlib.pyplot

    Example:
    >>> P = np.array([[6, 2, 7], [1, 1, 8], [8, 7, 1], [9, 6, 4], [2, 1, 1]])
    >>> T = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
    >>> pca_result, ax = f_347(P, T)
    >>> pca_result.shape
    (3, 2)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    if not (isinstance(P, np.ndarray) and isinstance(T, np.ndarray)):
        raise TypeError("Expected inputs to be numpy arrays")

    if not T.shape == tensor_shape:
        raise ValueError("Provided tensor does not match the specified tensor_shape.")

    result = np.tensordot(P, T, axes=[1, 1]).swapaxes(0, 1)

    # Reshape the result for PCA
    result = result.reshape(result.shape[0], -1)
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(result)

    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1])
    ax.set_title("PCA Result Visualization")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")

    return pca_result, ax

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        # Set up common matrices and tensors for testing
        self.TENSOR_SHAPE = (3, 3, 3)
        self.P = np.array([[6, 2, 7], [1, 1, 8], [8, 7, 1]])
        self.T = np.random.rand(*self.TENSOR_SHAPE)
        self.T_zeros = np.zeros(self.TENSOR_SHAPE)
        self.T_ones = np.ones(self.TENSOR_SHAPE)
    def test_case_1(self):
        # Test results and plot correctness
        pca_result, ax = f_347(self.P, self.T)
        self._common_assertions(pca_result, ax)
    def test_case_2(self):
        # Function should fail when input types are invalid
        with self.assertRaises(Exception):
            f_347("not a numpy array", self.T, self.TENSOR_SHAPE)
        with self.assertRaises(Exception):
            f_347(self.P, "not a numpy array", self.TENSOR_SHAPE)
        with self.assertRaises(Exception):
            f_347([], [], self.TENSOR_SHAPE)
    def test_case_3(self):
        # Function should fail when input shapes are invalid
        T_incorrect_shape = np.random.rand(2, 2, 2)
        with self.assertRaises(Exception):
            f_347(self.P, T_incorrect_shape, self.TENSOR_SHAPE)
        with self.assertRaises(Exception):
            f_347(np.array([]), np.array([]), self.TENSOR_SHAPE)
    def test_case_4(self):
        # Test custom shapes
        P = np.random.rand(5, 4)
        T = np.random.rand(5, 4, 4)
        pca_result, ax = f_347(P, T, tensor_shape=T.shape)
        self._common_assertions(pca_result, ax)
    def test_case_5(self):
        # Test with zeros
        pca_result, ax = f_347(self.P, self.T_zeros)
        self._common_assertions(pca_result, ax)
    def test_case_6(self):
        # Adjusting the matrix and tensor to have a slight variation
        P = np.array([[1.01, 0.01, 0.01], [0.01, 1.01, 0.01], [0.01, 0.01, 1.01]])
        T = np.ones(self.TENSOR_SHAPE) + 0.01 * np.random.rand(*self.TENSOR_SHAPE)
        pca_result, ax = f_347(P, T)
        # Assert that the PCA results don't produce NaN values and that there's a reduction in dimensionality
        self.assertFalse(np.isnan(pca_result).any())
        self.assertEqual(pca_result.shape[1], 2)
        # Also check common assertions
        self._common_assertions(pca_result, ax)
    def _common_assertions(self, pca_result, ax):
        # Common assertions for shape and plot labels
        self.assertEqual(pca_result.shape[1], 2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "PCA Result Visualization")
        self.assertEqual(ax.get_xlabel(), "Principal Component 1")
        self.assertEqual(ax.get_ylabel(), "Principal Component 2")
    def tearDown(self):
        plt.close("all")
