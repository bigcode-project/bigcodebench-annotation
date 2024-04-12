import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']


def f_522(x, y, labels):
    """
    Create a heatmap using the seaborn library for "x" and "y" numpy arrays with labels.

    Parameters:
    x (list): List of numpy arrays representing the x-values of the data points.
    y (list): List of numpy arrays representing the y-values of the data points.
    labels (list): List of strings representing the labels for the chemical compounds.

    Returns:
    ax (AxesSubplot): A seaborn heatmap object.
df (DataFrame): The dataframe used to create the heatmap.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - pandas
    - seaborn

    Example:
    >>> x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
    >>> y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
    >>> labels = ['H\u2082O', 'O\u2082', 'CO\u2082']
    >>> ax = f_522(x, y, labels)
    >>> plt.show()
    """
    data = []

    for i in range(len(x)):
        data.append(np.concatenate((x[i], y[i])))

    df = pd.DataFrame(data, index=labels)
    ax = sns.heatmap(df, cmap='coolwarm')
    
    return ax, df

import unittest
import numpy as np

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    # (test cases will be same as above)

    def test_case_1(self):
        x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
        y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
        labels = ['H₂O', 'O₂', 'CO₂']
        ax, df = f_522(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (3, 6))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[1,2,3,4,5,6], [4,5,6,7,8,9], [7,8,9,10,11,12]])
        np.testing.assert_array_equal(df.values, expected_data)

    def test_case_2(self):
        x = [np.array([1,1]), np.array([2,2])]
        y = [np.array([3,3]), np.array([4,4])]
        labels = ['H₂O', 'O₂']
        ax, df = f_522(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (2, 4))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[1,1,3,3], [2,2,4,4]])
        np.testing.assert_array_equal(df.values, expected_data)

    def test_case_3(self):
        x = [np.array([10])]
        y = [np.array([20])]
        labels = ['H₂O']
        ax, df = f_522(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (1, 2))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[10, 20]])
        np.testing.assert_array_equal(df.values, expected_data)

    def test_case_4(self):
        x = [np.array([5,6,7]), np.array([8,9,10]), np.array([11,12,13])]
        y = [np.array([15,16,17]), np.array([18,19,20]), np.array([21,22,23])]
        labels = ['A', 'B', 'C']
        ax, df = f_522(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (3, 6))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[5,6,7,15,16,17], [8,9,10,18,19,20], [11,12,13,21,22,23]])
        np.testing.assert_array_equal(df.values, expected_data)

    def test_case_5(self):
        x = [np.array([2,3]), np.array([5,6])]
        y = [np.array([8,9]), np.array([11,12])]
        labels = ['X', 'Y']
        ax, df = f_522(x, y, labels)
        
        # Assert the shape of the dataframe
        self.assertEqual(df.shape, (2, 4))
        
        # Assert the data values of the dataframe
        expected_data = np.array([[2,3,8,9], [5,6,11,12]])
        np.testing.assert_array_equal(df.values, expected_data)


if __name__ == "__main__":
    run_tests()