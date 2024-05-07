import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def f_769(P, T):
    """
    Calculate the product of matrix "P" and 3D tensor "T" then return dataframe of normalized results.

    This function performs matrix-tensor multiplication between a matrix "P" and a 3D tensor "T" using numpy.
    It checks if the shapes of P and T are compatible for multiplication, raising a ValueError if they are not.
    The function then normalizes the resulting 2D array using sklearn's StandardScaler. The final output
    is returned as a pandas DataFrame, with columns named feature_0, feature_1, ..., feature_n,
    where n is the number of features in the flattened result of the matrix-tensor multiplication.

    Parameters:
    - P (numpy.ndarray): The input matrix. Must not be empty.
    - T (numpy.ndarray): The input tensor. Must not be empty.

    Returns:
    pandas.DataFrame: A DataFrame with the normalized result.

    Requirements:
    - numpy
    - pandas
    - sklearn.preprocessing

    Example:
    >>> np.random.seed(0)
    >>> P = np.array([[6, 2, 7], [1, 1, 8], [8, 7, 1], [9, 6, 4], [2, 1, 1]])
    >>> T = np.random.rand(3, 5, 5)
    >>> result = f_769(P, T)
    >>> type(result)
    <class 'pandas.core.frame.DataFrame'>
    >>> result.head(2)
       feature_0  feature_1  feature_2  ...  feature_22  feature_23  feature_24
    0   0.214791   0.220904   1.697850  ...    1.768847   -1.759510   -0.003527
    1  -0.652336   1.064228  -0.707134  ...   -0.036116    1.002544   -0.813796
    <BLANKLINE>
    [2 rows x 25 columns]
    """
    if P.size == 0 or T.size == 0:
        raise ValueError("Inputs cannot be empty.")
    if P.shape[1] != T.shape[0]:
        raise ValueError(
            f"Matrix P shape {P.shape[1]} and Tensor T shape {T.shape[0]} are incompatible for tensor multiplication."
        )
    result = np.tensordot(P, T, axes=[1, 0]).swapaxes(0, 1)
    result = result.reshape(result.shape[0], -1)
    scaler = StandardScaler()
    result = scaler.fit_transform(result)
    adjusted_feature_names = [f"feature_{i}" for i in range(result.shape[1])]
    result = pd.DataFrame(result, columns=adjusted_feature_names)
    return result

import unittest
import numpy as np
from sklearn.preprocessing import StandardScaler
class TestCases(unittest.TestCase):
    def tensor_product_manual(self, P, T):
        """Manually compute the tensor product without any normalization."""
        result = np.tensordot(P, T, axes=[1, 0]).swapaxes(0, 1)
        result = result.reshape(result.shape[0], -1)
        return result
    def test_case_1(self):
        np.random.seed(0)
        P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        T = np.random.rand(3, 4, 4)
        result = f_769(P, T)
        manual_result = self.tensor_product_manual(P, T)
        # Reverse normalization for comparison
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (4, 12))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-5))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-5))
    def test_case_2(self):
        np.random.seed(0)
        P = np.array([[1, 2], [3, 4], [5, 6]])
        T = np.random.rand(3, 5, 5)
        with self.assertRaises(ValueError):
            f_769(P, T)
    def test_case_3(self):
        np.random.seed(0)
        P = np.eye(4)
        T = np.random.rand(4, 6, 6)
        result = f_769(P, T)
        manual_result = self.tensor_product_manual(P, T)
        # Reverse normalization for comparison
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (6, 24))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-5))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-5))
    def test_case_4(self):
        np.random.seed(0)
        P = np.ones((5, 5))
        T = np.random.rand(5, 7, 7)
        result = f_769(P, T)
        manual_result = self.tensor_product_manual(P, T)
        # Reverse normalization for comparison
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (7, 35))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-5))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-5))
    def test_case_5(self):
        np.random.seed(0)
        P = np.diag(np.arange(1, 7))
        T = np.random.rand(6, 8, 8)
        result = f_769(P, T)
        manual_result = self.tensor_product_manual(P, T)
        # Reverse normalization for comparison
        scaler = StandardScaler().fit(manual_result)
        reversed_result = scaler.inverse_transform(result)
        self.assertEqual(result.shape, (8, 48))
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-5))
        self.assertTrue(np.allclose(manual_result, reversed_result, atol=1e-5))
    def test_case_6(self):
        # Test with an empty matrix and tensor, expecting a ValueError due to incompatible shapes
        P = np.array([])
        T = np.array([])
        with self.assertRaises(ValueError):
            f_769(P, T)
    def test_case_7(self):
        # Test with non-numeric inputs in matrices/tensors to verify type handling
        P = np.array([["a", "b"], ["c", "d"]])
        T = np.random.rand(2, 2, 2)
        with self.assertRaises(Exception):
            f_769(P, T)
    def test_case_8(self):
        # Test with zero matrix and tensor to verify handling of all-zero inputs
        P = np.zeros((5, 5))
        T = np.zeros((5, 3, 3))
        result = f_769(P, T)
        self.assertTrue(np.allclose(result, np.zeros((3, 15))))
    def test_case_9(self):
        # Test DataFrame output for correct column names, ensuring they match expected feature naming convention
        P = np.random.rand(3, 3)
        T = np.random.rand(3, 4, 4)
        result = f_769(P, T)
        expected_columns = [
            "feature_0",
            "feature_1",
            "feature_2",
            "feature_3",
            "feature_4",
            "feature_5",
            "feature_6",
            "feature_7",
            "feature_8",
            "feature_9",
            "feature_10",
            "feature_11",
        ]
        self.assertListEqual(list(result.columns), expected_columns)
    def test_case_10(self):
        # Test to ensure DataFrame indices start from 0 and are sequential integers
        P = np.random.rand(2, 3)
        T = np.random.rand(3, 5, 5)
        result = f_769(P, T)
        expected_indices = list(range(5))  # Expected indices for 5 rows
        self.assertListEqual(list(result.index), expected_indices)
