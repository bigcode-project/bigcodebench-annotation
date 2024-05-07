import pandas as pd
import matplotlib.pyplot as plt

def f_180(matrix):
    """
    Visualize a 2D numeric array (matrix) as a heatmap using matplotlib.
    
    Parameters:
    matrix (array): The 2D numpy array.
    
    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object with the heatmap.
    
    Requirements:
    - pandas
    - matplotlib.pyplot
    
    Example:
    >>> import numpy as np
    >>> matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> ax = f_180(matrix)
    """
    df = pd.DataFrame(matrix)
    fig, ax = plt.subplots()
    ax.imshow(df, cmap='hot', interpolation='nearest')
    return ax

import unittest
import numpy as np
import matplotlib
class TestCases(unittest.TestCase):
    def test_case_1(self):
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        ax = f_180(matrix)
        
        # Asserting the return type
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        
        # Asserting the colormap used
        self.assertEqual(ax.images[0].get_cmap().name, 'hot')
    def test_case_2(self):
        matrix = np.array([[10, 20], [30, 40]])
        ax = f_180(matrix)
        
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(ax.images[0].get_cmap().name, 'hot')
    def test_case_3(self):
        matrix = np.array([[1, 1], [1, 1], [1, 1]])
        ax = f_180(matrix)
        
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(ax.images[0].get_cmap().name, 'hot')
    def test_case_4(self):
        matrix = np.array([[1]])
        ax = f_180(matrix)
        
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(ax.images[0].get_cmap().name, 'hot')
    def test_case_5(self):
        matrix = np.random.rand(5, 5)  # Random 5x5 matrix
        ax = f_180(matrix)
        
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(ax.images[0].get_cmap().name, 'hot')
