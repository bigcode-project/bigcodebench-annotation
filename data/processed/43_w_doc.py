import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def task_func(data_matrix, n_components=2):
    """
    Apply PCA with n_components components to a 2D data matrix, calculate the mean value of each component, and then return the cumulative explained variance of the components in a plot.
    - The function returns a dataframe with columns 'Component 1', 'Component 2', ... etc.
    - Each row of the dataframe correspond to a row of the original matrix mapped in the PCA space.
    - The dataframe should also include a column 'Mean' which is the average value of each component value per row
    - Create a plot of the cumulative explained variance.
        - the xlabel should be 'Number of Components' and the ylabel 'Cumulative Explained Variance'

    Parameters:
    data_matrix (numpy.array): The 2D data matrix.

    Returns:
    tuple:
        - pandas.DataFrame: A DataFrame containing the PCA transformed data and the mean of each component.
        - matplotlib.axes._axes.Axes: A plot showing the cumulative explained variance of the components.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - sklearn.decomposition

    Example:
    >>> import numpy as np
    >>> data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
    >>> df, ax = task_func(data)
    >>> print(df["Mean"])
    0    2.850439
    1   -2.850439
    Name: Mean, dtype: float64
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
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
        df, ax = task_func(data)
        self.assertEqual(df.shape, (2, 3))
        self.assertTrue("Mean" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")
    def test_case_2(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        df, ax = task_func(data)
        self.assertEqual(df.shape, (3, 3))
        self.assertTrue("Mean" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")
    # Additional test cases
    def test_case_3(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        df, ax = task_func(data)
        expected_columns = min(data.shape) + 1
        self.assertEqual(df.shape[1], expected_columns)
        self.assertTrue("Mean" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")
    def test_case_4(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        df, ax = task_func(data)
        expected_columns = min(data.shape) + 1
        self.assertEqual(df.shape[1], expected_columns)
        self.assertTrue("Mean" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")
    def test_case_5(self):
        data = np.array([[1, 2], [3, 4], [5, 6]])
        df, ax = task_func(data)
        expected_columns = min(data.shape) + 1
        self.assertEqual(df.shape[1], expected_columns)
        self.assertTrue("Mean" in df.columns)
        self.assertTrue("Component 1" in df.columns)
        self.assertTrue("Component 2" in df.columns)
        self.assertEqual(ax.get_xlabel(), "Number of Components")
        self.assertEqual(ax.get_ylabel(), "Cumulative Explained Variance")
