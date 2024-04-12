import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Constants
N_COMPONENTS = 2

def f_485(L):
    """
    Convert a list of lists 'L' into a 2D numeric array, apply PCA to it and return the PCA result and scatter plot.
    
    Requirements:
    - numpy
    - sklearn.decomposition
    - matplotlib.pyplot

    Parameters:
    L (list of lists): A list of lists where each sublist contains integers.
    
    Returns:
    tuple: A tuple containing the PCA result (numpy array) and the scatter plot (matplotlib Axes object).

    Example:
    >>> pca_result, plot = f_485([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> type(pca_result)
    <class 'numpy.ndarray'>
    >>> type(plot)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """
    data = np.array(L)

    pca = PCA(n_components=N_COMPONENTS)
    pca_result = pca.fit_transform(data)

    fig, ax = plt.subplots()
    ax.scatter(pca_result[:,0], pca_result[:,1])

    return pca_result, ax

import unittest
import numpy as np
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        test_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        pca_result, plot = f_485(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))

    def test_case_2(self):
        test_input = [[1, 1], [1, 1], [1, 1]]
        pca_result, plot = f_485(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))

    def test_case_3(self):
        test_input = [[1, 2], [3, 4], [5, 6], [7, 8]]
        pca_result, plot = f_485(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (4, 2))

    def test_case_4(self):
        test_input = [[-1, -2], [-3, -4], [-5, -6]]
        pca_result, plot = f_485(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))

    def test_case_5(self):
        test_input = [[-1, 2], [3, -4], [5, -6]]
        pca_result, plot = f_485(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))


if __name__ == "__main__":
    run_tests()