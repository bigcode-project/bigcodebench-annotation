from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def f_174(l):
    """
    Perform Principal Component Analysis (PCA) on the given array and record the first two main components.

    Parameters:
    l (numpy array): The input array.

    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object of the generated plot

    Note:
    - This function use "PCA Result" as the title of the plot.
    - This function use "First Principal Component" and "Second Principal Component" as the xlabel 
    and ylabel of the plot, respectively.

    Requirements:
    - sklearn.decomposition.PCA
    - matplotlib.pyplot

    Example:
    >>> import numpy as np
    >>> l = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    >>> ax = f_174(l)
    >>> len(ax.collections[0].get_offsets())
    4
    >>> print(ax.get_title())
    PCA Result
    >>> plt.close()
    """
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(l)
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    plt.scatter(principalComponents[:, 0], principalComponents[:, 1])
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.title('PCA Result')
    return ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: simple 2D array
        l = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        ax = f_174(l)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(ax.get_title(), "PCA Result")
        self.assertEqual(ax.get_xlabel(), "First Principal Component")
        self.assertEqual(ax.get_ylabel(), "Second Principal Component")
        # Check the number of points
        self.assertEqual(len(ax.collections[0].get_offsets()), len(l))
        plt.close()
    def test_case_2(self):
        # Input 2: another simple 2D array
        l = np.array([[2, 3], [4, 5], [6, 7], [8, 9]])
        ax = f_174(l)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(ax.get_title(), "PCA Result")
        self.assertEqual(ax.get_xlabel(), "First Principal Component")
        self.assertEqual(ax.get_ylabel(), "Second Principal Component")
        # Check the number of points
        self.assertEqual(len(ax.collections[0].get_offsets()), len(l))
        plt.close()
    def test_case_3(self):
        # Input 3: larger array
        np.random.seed(0)
        l = np.random.rand(10, 2)
        ax = f_174(l)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(ax.get_title(), "PCA Result")
        self.assertEqual(ax.get_xlabel(), "First Principal Component")
        self.assertEqual(ax.get_ylabel(), "Second Principal Component")
        # Check the number of points
        self.assertEqual(len(ax.collections[0].get_offsets()), len(l))
        plt.close()
    def test_case_4(self):
        # Input 4: array with similar values (less variance)
        l = np.array([[1, 2], [1, 2.1], [1.1, 2], [1.1, 2.1]])
        ax = f_174(l)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(ax.get_title(), "PCA Result")
        self.assertEqual(ax.get_xlabel(), "First Principal Component")
        self.assertEqual(ax.get_ylabel(), "Second Principal Component")
        # Check the number of points
        self.assertEqual(len(ax.collections[0].get_offsets()), len(l))
        plt.close()
    def test_case_5(self):
        # Input 5: array with larger values
        l = np.array([[100, 200], [300, 400], [500, 600], [700, 800]])
        ax = f_174(l)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(ax.get_title(), "PCA Result")
        self.assertEqual(ax.get_xlabel(), "First Principal Component")
        self.assertEqual(ax.get_ylabel(), "Second Principal Component")
        # Check the number of points
        self.assertEqual(len(ax.collections[0].get_offsets()), len(l))
        plt.close()
