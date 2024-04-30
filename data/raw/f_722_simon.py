import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def f_722(data, n_clusters=3, seed=None):
    """
    Perform K-Means clustering on the given DataFrame using the sklearn KMeans algorithm. 

    The function expects a DataFrame with numerical values, as KMeans cannot handle categorical data. 
    It applies standard KMeans clustering from the sklearn library to form clusters. The number of clusters is 
    configurable via the 'n_clusters' parameter, defaulting to 3. The Number of times the k-means algorithm is run with 
    different centroid seeds (n_init) is set to 10. The function returns an array of cluster labels 
    corresponding to each data point in the input as well as the fitted KMeans model.

    Parameters:
    data (pandas.DataFrame): A DataFrame consisting of only numerical data. Each row represents a distinct data point.
    n_clusters (int, optional): The number of clusters to form. Defaults to 3.
    seed (int, optional): The seed used for setting the random stat in the KMeans clustering algorith.
                          Used for making results reproducable.

    Returns:
    numpy.ndarray: An array of integers (cluster labels) corresponding to the input data. Each label is an integer 
                   representing the cluster to which a row of data has been assigned.
    sklearn.cluster.KMeans: The fitted KMeans Model.

    Raises:
    - ValueError: If the DataFrame contains non numeric entries.

    Requirements:
    - pandas
    - numpy
    - sklearn.cluster.KMeans

    Example:
    >>> np.random.seed(12)
    >>> data = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
    >>> labels, model = f_722(data, n_clusters=4, seed=12)
    >>> print(labels) 
    [2 0 2 1 3 3 3 3 2 2 3 2 0 2 2 1 1 2 0 0 3 1 1 0 3 3 0 1 3 2 2 1 0 1 2 3 0
     2 1 1 1 0 1 3 0 3 1 1 1 3 3 1 2 1 1 2 3 1 3 2 3 0 2 1 3 3 2 1 1 1 0 2 0 3
     1 2 3 2 3 3 1 0 0 1 3 0 3 3 2 0 2 1 1 3 1 1 3 0 1 2]
    >>> print(model)
    KMeans(n_clusters=4, random_state=12)


    >>> data = pd.DataFrame({
    ...     'a': [1, 20, 2, 22, 100],
    ...     'b': [1, 20, 2, 22, 100]
    ... })
    >>> labels, model = f_722(data, seed=213)
    >>> print(labels)
    [2 0 2 0 1]
    >>> print(model)
    KMeans(n_clusters=3, random_state=213)
    """
    if not data.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).all():
        raise ValueError("DataFrame should only contain numeric values.")

    kmeans = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10)
    kmeans.fit(data)

    return kmeans.labels_, kmeans

import unittest
import pandas as pd
import numpy as np


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_nonnumeric(self):
        data = pd.DataFrame({
            'a': [1, 2, 3],
            'b': ['a', 2, 4]
        })
        self.assertRaises(Exception, f_722, data)


    def test_case_1(self):
        np.random.seed(12)
        data = pd.DataFrame(np.random.randint(0, 20, size=(20, 4)), columns=list('ABCD'))
        labels, kmeans = f_722(data, n_clusters=4, seed=1)
        unique_labels = np.unique(labels)
        assert all(label in range(4) for label in unique_labels)
        self.assertTrue(isinstance(labels, np.ndarray))
        self.assertIsInstance(kmeans, KMeans)
        np.testing.assert_equal(labels, [3, 0, 3, 1, 2, 1, 2, 0, 2, 1, 1, 3, 3, 1, 0, 0, 0, 0, 1, 3])

    def test_case_2(self):
        data = pd.DataFrame(np.zeros((100, 4)), columns=list('ABCD'))
        labels, kmeans = f_722(data, n_clusters=3, seed=12)
        self.assertIsInstance(kmeans, KMeans)
        assert len(np.unique(labels)) == 1
        self.assertTrue(isinstance(labels, np.ndarray))

        self.assertCountEqual(labels, np.zeros(100))

    def test_case_3(self):
        data = pd.DataFrame({'A': range(100), 'B': range(100), 'C': range(100)})
        labels, kmeans = f_722(data, seed=42)
        self.assertIsInstance(kmeans, KMeans)

        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        np.testing.assert_equal(labels, expected)
        self.assertTrue(isinstance(labels, np.ndarray))

    def test_case_4(self):
        np.random.seed(5)
        data = pd.DataFrame(np.random.rand(100, 20))
        labels, kmeans = f_722(data, n_clusters=12, seed=12)
        self.assertIsInstance(kmeans, KMeans)
        expected = [ 4,  5,  5,  9, 10,  1,  0,  3,  4,  7,  7,  2, 11, 11,  3,  0,  4,
                    2,  3,  2,  2, 10, 10,  8,  5,  9, 11,  5,  0,  8, 11,  5,  7,  0,
                    8, 11,  7, 11,  6,  1,  1,  7,  0,  9,  3,  7,  8,  0,  4,  1,  7,
                    2, 10,  3, 11,  9,  1,  1,  7,  4,  5,  7,  6,  9,  8,  6,  5,  9,  0,
                    11 , 1 , 1,  4,  2,  1,  0,  7,  5,  1,  9,  6,  7, 10, 10,  4,  4,  9,
                    1,  9,  5,  6,  3, 10,  7, 11,  8,  1,  8,  6, 11]
        np.testing.assert_equal(labels, expected)
        self.assertTrue(isinstance(labels, np.ndarray))

    def test_case_5(self):
        data = pd.DataFrame([])
        self.assertRaises(Exception, f_722, data)


if __name__ == "__main__":
    run_tests()