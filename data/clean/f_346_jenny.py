import numpy as np
import matplotlib.pyplot as plt


def f_346(P, T):
    """
    Calculate the product of a matrix "P" and a 3D tensor "T" with numpy and then visualize the
    result in 3D with matplotlib. The product of the matrix and tensor is based on the Einstein summation.
    
    Note:
    This function only accepts numpy matrices/arrays.

    Parameters:
    P (numpy.ndarray): The input matrix with shape (N, 3), where N is the number of rows.
    T (numpy.ndarray): The input tensor with shape (3, 3, 3).

    Returns:
    tuple:
        - result (numpy.ndarray): The product of matrix P and tensor T with shape (N, 3).
        - ax (mpl_toolkits.mplot3d.axes3d.Axes3D): The 3D visualization of the result.

    Requirements:
    - numpy
    - matplotlib.pyplot

    Example:
    >>> P = np.array([[6, 2, 7], [1, 1, 8], [8, 7, 1]])
    >>> T = np.random.rand(3, 3, 3)
    >>> result, ax = f_346(P, T)
    >>> type(result)
    <class 'numpy.ndarray'>
    >>> type(ax)
    <class 'mpl_toolkits.mplot3d.axes3d.Axes3D'>
    """
    if not (isinstance(P, np.ndarray) and isinstance(T, np.ndarray)):
        raise TypeError("Expected inputs to be numpy arrays")

    # Compute the matrix-tensor product to ensure the result has the desired shape
    result = np.einsum("ij,jkl->ik", P, T)

    # Visualize the result in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(result[:, 0], result[:, 1], result[:, 2])

    # Return the result and the 3D visualization
    return result, ax


import unittest
import numpy as np
import matplotlib.pyplot as plt


class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.test_P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.test_T = np.random.rand(3, 3, 3)

    def check_result_correctness(self, P, T, result):
        # Manually compute the expected result for the matrix-tensor product
        expected_result = np.einsum("ij,jkl->ik", P, T)
        return np.allclose(result, expected_result)

    def test_case_1(self):
        # Test output visualization
        _, ax = f_346(self.test_P, self.test_T)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_2(self):
        # Test result correctness
        result, _ = f_346(self.test_P, self.test_T)
        self.assertTrue(self.check_result_correctness(self.test_P, self.test_T, result))
        self.assertEqual(result.shape, (self.test_P.shape[0], 3))

    def test_case_3(self):
        # Test with zeros and negative values
        P = np.array([[0, 0, 0]])
        T = np.random.rand(3, 3, 3) - 0.5
        result, _ = f_346(P, T)
        self.assertTrue(np.all(result == 0))

    def test_case_4(self):
        # Test with non-numeric data
        P = np.array([["a", "b", "c"], [1, 2, 3]])
        with self.assertRaises(Exception):
            f_346(P, self.test_T)

    def test_case_5(self):
        # Test incompatible shapes
        P = np.array([[1, 2], [3, 4]])
        with self.assertRaises(Exception):
            f_346(P, self.test_T)

    def test_case_6(self):
        # Test incompatible input types
        with self.assertRaises(Exception):
            f_346([1, 2], [2, 1])

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
