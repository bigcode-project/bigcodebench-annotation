import pandas as pd
from sklearn.cluster import DBSCAN

def f_537(data, cols):
    """
    Perform DBSCAN clustering on the data by transforming it into a DataFrame and recording the clusters in a new column named 'Cluster'.
    Please choose the parameters eps=3 and min_samples=2.
    
    Parameters:
    - data (list): List of lists with the data, where the length of the inner list equals the number of columns
    - cols (list): List of column names
    
    Returns:
    - df (DataFrame): The DataFrame with a new 'Cluster' column.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> data = [[5.1, 3.5], [4.9, 3.0], [4.7, 3.2]]
    >>> cols = ['x', 'y']
    >>> df = f_537(data, cols)
    >>> print(df)
         x    y  Cluster
    0  5.1  3.5        0
    1  4.9  3.0        0
    2  4.7  3.2        0
    """
    df = pd.DataFrame(data, columns=cols)
    dbscan = DBSCAN(eps=3, min_samples=2)
    df['Cluster'] = dbscan.fit_predict(df)
    return df

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = f_537([[5.1, 3.5], [4.9, 3.0], [4.7, 3.2]], ['x', 'y'])
        print(df)
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0])))
    def test_case_2(self):
        df = f_537([[1, 2], [3, 4], [5, 6]], ['x', 'y'])
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0])))
    def test_case_3(self):
        df = f_537([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]], ['x', 'y'])
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0, 1, 1, -1])))
    def test_case_4(self):
        df = f_537([[1, 2, 3], [2, 2, 2], [2, 3, 4], [8, 7, 6], [8, 8, 8], [25, 80, 100]], ['x', 'y', 'z'])
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0, 1, 1, -1])))
    def test_case_5(self):
        df = f_537([[-1, -2], [-2, -2], [-2, -3], [-8, -7], [-8, -8], [-25, -80]], ['x', 'y'])
        self.assertTrue('Cluster' in df.columns)
        self.assertTrue(np.array_equal(df['Cluster'], np.array([0, 0, 0, 1, 1, -1])))
