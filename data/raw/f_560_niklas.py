import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def f_560(df):
    """
    Given a pandas DataFrame with random numeric values, run KMeans clusters on the data and return the labels.

    Parameters:
    - df (DataFrame): The DataFrame to use.

    Returns:
    - labels (np.array): The labels from the KMeans clustering.

    Requirements:
    - pandas
    - numpy
    - sklearn

    Example:
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.rand(500, 2) * 100, columns=['A', 'B'])
    >>> labels = f_560(df)
    >>> print(labels)
    [2 0 1 2 0 2 0 1 2 1 1 1 2 2 1 1 2 0 1 0 2 2 2 2 1 0 0 0 1 1 1 0 2 2 2 1 2
     0 1 1 0 1 1 0 0 2 0 0 1 1 2 2 0 2 1 1 0 0 1 0 0 1 1 0 2 1 1 0 0 2 0 1 1 0
     1 0 2 0 0 2 2 0 2 1 2 1 1 1 0 0 1 0 2 0 1 2 0 1 0 0 1 2 1 2 1 0 1 1 2 0 0
     1 1 0 0 0 0 2 1 1 0 0 2 2 0 1 0 2 0 1 0 2 0 0 1 0 0 0 0 0 0 1 1 2 2 1 0 2
     1 1 2 0 0 1 0 1 2 0 1 1 0 1 0 0 1 2 1 1 0 1 1 1 2 1 2 2 1 2 2 0 2 2 0 0 1
     1 2 1 1 0 2 0 0 1 0 0 2 2 0 0 2 2 2 1 1 2 0 0 1 0 0 2 2 2 1 2 1 2 2 1 2 1
     0 0 1 0 2 2 2 1 2 0 0 2 2 2 2 2 2 0 0 2 0 1 0 2 1 1 1 0 0 2 1 0 0 0 0 1 2
     0 1 0 0 1 2 0 0 0 0 1 0 2 1 2 2 2 0 0 1 0 1 1 2 1 0 2 2 0 2 1 2 1 1 1 1 2
     1 0 1 1 1 1 2 1 2 2 1 0 1 0 1 1 1 2 1 0 0 2 1 1 1 1 2 0 0 2 0 1 1 0 2 1 1
     1 1 2 2 2 1 0 0 2 0 1 1 1 1 2 2 2 1 1 2 2 2 0 1 2 0 2 0 2 0 2 1 2 0 2 2 1
     1 0 2 2 0 2 1 2 0 0 1 2 2 0 2 2 1 1 2 0 0 1 2 1 2 2 0 2 0 0 1 0 2 0 1 0 2
     0 1 1 1 1 2 1 0 1 1 1 0 0 2 2 1 2 0 2 2 1 2 1 0 1 2 1 0 1 0 1 0 1 2 1 1 1
     1 0 0 1 2 1 1 2 2 0 1 1 0 1 2 1 0 0 1 2 1 2 0 1 2 2 2 0 1 2 0 0 2 1 1 2 2
     1 1 0 0 0 1 1 1 0 2 1 0 0 2 0 2 1 0 0]
    """
    # Perform clustering
    kmeans = KMeans(n_clusters=3, random_state=0).fit(df)
    labels = kmeans.labels_
    return labels

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame(np.random.rand(500, 2) * 100, columns=['A', 'B'])
        labels = f_560(df)
        self.assertEqual(len(labels), 500)
        self.assertTrue(np.all(np.isin(labels, [0, 1, 2])))

    def test_case_2(self):
        df = pd.DataFrame(np.random.rand(10, 2) * 100, columns=['A', 'B'])
        labels = f_560(df)
        self.assertEqual(len(labels), 10)
        self.assertTrue(np.all(np.isin(labels, [0, 1, 2])))

    def test_case_3(self):
        df = pd.DataFrame(np.random.rand(5, 4) * 100, columns=['A', 'B', 'C', 'D'])
        labels = f_560(df)
        self.assertEqual(len(labels), 5)
        self.assertTrue(np.all(np.isin(labels, [0, 1, 2])))

    def test_case_4(self):
        df = pd.DataFrame(np.random.rand(20, 3) * 100, columns=['A', 'B', 'C'])
        labels = f_560(df)
        self.assertEqual(len(labels), 20)
        self.assertTrue(np.all(np.isin(labels, [0, 1, 2])))

    def test_case_5(self):
        df = pd.DataFrame(np.random.rand(42, 1) * 100, columns=['A'])
        labels = f_560(df)
        self.assertEqual(len(labels), 42)
        self.assertTrue(np.all(np.isin(labels, [0, 1, 2])))
        

run_tests()
if __name__ == "__main__":
    run_tests()