import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


def f_732(array, seed=None):
    """
    Shuffles the columns of a numpy array randomly, performs Principal Component Analysis (PCA)
    to reduce the dimensionality to 2 principal components, and returns these components as a pandas DataFrame.

    Parameters:
    - array (numpy.ndarray): A 2D numpy array where each row is an observation and each column is a feature.
    - seed (int, optional): Seed for the random number generator. Defaults to None (not set).

    Returns:
    - pandas.DataFrame: DataFrame with columns 'PC1' and 'PC2' representing the two principal components.

    Raises:
    - ValueError: If the input array is not 2D.

    Requirements:
    - numpy
    - pandas
    - sklearn

    Note:
    - PCA reduction will default to the number of features if fewer than 2.
    - An named but empty DataFrame is returned for arrays without features or with empty content.

    Examples:
    >>> array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    >>> df = f_732(array, seed=42)
    >>> df["PC1"]
    0    5.59017
    1   -5.59017
    Name: PC1, dtype: float64
    >>> df.shape
    (2, 2)
    """
    if seed is not None:
        np.random.seed(seed)

    if not isinstance(array, np.ndarray) or len(array.shape) != 2:
        raise ValueError("Input must be a 2D numpy array.")

    if array.size == 0 or array.shape[1] == 0:
        return pd.DataFrame(columns=["PC1", "PC2"])

    shuffled_array = np.copy(array)
    np.random.shuffle(np.transpose(shuffled_array))

    n_components = min(2, shuffled_array.shape[1])
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(shuffled_array)

    column_labels = ["PC1", "PC2"][:n_components]
    df = pd.DataFrame(data=principal_components, columns=column_labels)

    return df

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.array2x5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.array5x1 = np.array([[1], [2], [3], [4], [5]])
    def test_with_empty_array(self):
        """Test handling of an empty array."""
        array = np.empty((0, 0))
        df = f_732(array, seed=42)
        self.assertTrue(df.empty, "The returned DataFrame should be empty.")
        self.assertTrue(
            (df.columns == ["PC1", "PC2"]).all(),
            "Column names should be 'PC1' and 'PC2' even for an empty DataFrame.",
        )
    def test_with_2x5_array(self):
        """Test PCA on a 2x5 array with shuffled columns."""
        df = f_732(self.array2x5, seed=42)
        self.assertEqual(df.shape, (2, 2), "DataFrame shape should be (2, 2).")
        self.assertTrue(
            (df.columns == ["PC1", "PC2"]).all(),
            "Column names should be 'PC1' and 'PC2'.",
        )
    def test_with_5x1_array(self):
        """Test PCA on a 5x1 array."""
        df = f_732(self.array5x1, seed=0)
        self.assertEqual(
            df.shape, (5, 1), "DataFrame shape should be (5, 1) for a single component."
        )
        self.assertTrue(
            (df.columns == ["PC1"]).all(),
            "Column name should be 'PC1' for a single component.",
        )
    def test_invalid_input(self):
        """Test handling of invalid input."""
        with self.assertRaises(ValueError):
            f_732(np.array([1, 2, 3]), seed=42)
    def test_reproducibility(self):
        """Test if the function is reproducible with the same seed."""
        df1 = f_732(self.array2x5, seed=42)
        df2 = f_732(self.array2x5, seed=42)
        pd.testing.assert_frame_equal(
            df1, df2, "Results should be identical when using the same seed."
        )
    def test_pca_correctness(self):
        """
        Test PCA correctness by ensuring that the variance is captured correctly
        in the principal components.
        """
        # Creating a simple array where variance is higher in one dimension
        # This dataset is designed so that the first principal component should
        # capture the majority of the variance.
        array = np.array(
            [
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [10, 10, 10, 10, 10],
            ]
        )  # Increased variance in the last row
        df = f_732(array, seed=0)
        # The PCA should be able to capture the variance in the first principal component
        # significantly more than in the second, if applicable.
        # Asserting that the first PC values are not all the same,
        # which indicates it captured the variance.
        self.assertFalse(
            df["PC1"].std() == 0,
            "PCA should capture variance along the first principal component.",
        )
