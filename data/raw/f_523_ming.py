import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def f_523(x, y, labels):
    """ 
    Perform Principal Component Analysis (PCA) on "x" and "y" numpy arrays and record the results with labels.

    Parameters:
    x (list): List of numpy arrays representing the x-values of the data points.
    y (list): List of numpy arrays representing the y-values of the data points.
    labels (list): List of strings representing the labels for the chemical compounds.

    Returns:
    fig: Matplotlib figure object.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - sklearn.decomposition

    Example:
    >>> x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
    >>> y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
    >>> labels = ['H₂O', 'O₂', 'CO₂']
    >>> fig = f_523(x, y, labels)
    >>> plt.show(fig)
    """
    pca = PCA(n_components=2)

    fig, ax = plt.subplots()

    for i in range(len(x)):
        xy = np.vstack((x[i], y[i])).T
        xy_transformed = pca.fit_transform(xy)
        ax.plot(xy_transformed[:, 0], xy_transformed[:, 1], label=labels[i])
    
    ax.legend()
    
    return fig

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import unittest

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # Generate sample data for testing
        self.x_data = [
            np.array([1, 2, 3, 4]),
            np.array([5, 6, 7, 8]),
            np.array([9, 10, 11, 12]),
            np.array([13, 14, 15, 16]),
            np.array([17, 18, 19, 20])
        ]
        
        self.y_data = [
            np.array([21, 22, 23, 24]),
            np.array([25, 26, 27, 28]),
            np.array([29, 30, 31, 32]),
            np.array([33, 34, 35, 36]),
            np.array([37, 38, 39, 40])
        ]
        
        self.labels = ['H₂O', 'O₂', 'CO₂', 'N₂', 'Ar']

    def test_case_1(self):
        fig = f_523(self.x_data, self.y_data, self.labels)
        # Check if returned object is a matplotlib figure
        self.assertIsInstance(fig, plt.Figure)

    def test_case_2(self):
        # Testing with different data lengths
        x_data = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
        y_data = [np.array([10, 11, 12]), np.array([13, 14, 15]), np.array([16, 17, 18])]
        fig = f_523(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)

    def test_case_3(self):
        # Testing with data of length 2 (to avoid PCA error)
        x_data = [np.array([1, 2]), np.array([4, 5]), np.array([7, 8])]
        y_data = [np.array([10, 11]), np.array([13, 14]), np.array([16, 17])]
        fig = f_523(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)
        
    def test_case_4(self):
        # Testing with longer data
        x_data = [np.array(range(10)), np.array(range(10, 20)), np.array(range(20, 30))]
        y_data = [np.array(range(30, 40)), np.array(range(40, 50)), np.array(range(50, 60))]
        fig = f_523(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)
        
    def test_case_5(self):
        # Testing with random data
        x_data = [np.random.randn(10) for _ in range(3)]
        y_data = [np.random.randn(10) for _ in range(3)]
        fig = f_523(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)


if __name__ == "__main__":
    run_tests()