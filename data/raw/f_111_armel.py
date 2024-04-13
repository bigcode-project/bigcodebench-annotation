import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def f_111(data_matrix, n_components):
    """
    Apply PCA with n_components components to a 2D data matrix, calculate the mean value of each component, and then return the cumulative explained variance of the components in a plot.
    - The function returns a dataframe with columns 'Component 1', 'Component 2' etc.
    - Each row of the dataframe correspond to a row of the original matrix mapped in the PCA space.
    - The dataframe should also include a column 'Mean' which is the average value of each component value per row
    - Create a plot of the cumulative explained variance.
        - the xlabel should be 'Number of Components' and the ylabel 'Cumulative Explained Variance'

    Parameters:
    data_matrix (numpy.array): The 2D data matrix.

    Returns:
    tuple:
        - pandas.DataFrame: A DataFrame containing the PCA transformed data and the mean of each component.
        - matplotlib.axes._subplots.AxesSubplot: A plot showing the cumulative explained variance of the components.

    Requirements:
    - numpy
    - pandas
    - matplotlib.pyplot
    - sklearn.decomposition.PCA

    Example:
    >>> data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
    >>> df, ax = f_111(data)
    >>> print(df)
    """
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data_matrix)

    df = pd.DataFrame(
        transformed_data,
        columns=[f"Component {i+1}" for i in range(transformed_data.shape[1])],
    )
    df["Mean"] = df.mean(axis=1)

    fig, ax = plt.subplots()
    ax.plot(np.cumsum(pca.explained_variance_ratio_))
    ax.set_xlabel("Number of Components")
    ax.set_ylabel("Cumulative Explained Variance")
    return df, ax


import unittest


class TestCases(unittest.TestCase):
    """Test cases for the f_111 function."""

    def test_case_1(self):
        data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
        df, ax = f_111(data)
        self.assertEqual(df.shape, (2, 3))
        self.assertTrue("Mean" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")

    def test_case_2(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        df, ax = f_111(data)
        self.assertEqual(df.shape, (3, 3))
        self.assertTrue("Mean" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")

    # Additional test cases
    def test_case_3(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        df, ax = f_111(data)
        expected_columns = min(data.shape) + 1
        self.assertEqual(df.shape[1], expected_columns)
        self.assertTrue("Mean" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")

    def test_case_4(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        df, ax = f_111(data)
        expected_columns = min(data.shape) + 1
        self.assertEqual(df.shape[1], expected_columns)
        self.assertTrue("Mean" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")

    def test_case_5(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        df, ax = f_111(data)
        expected_columns = min(data.shape) + 1
        self.assertEqual(df.shape[1], expected_columns)
        self.assertTrue("Mean" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
