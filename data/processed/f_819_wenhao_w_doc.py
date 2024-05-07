import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def f_575(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    """
    Randomly shuffle the given array's features, normalize its values, then convert to a DataFrame
    with shuffled feature names.

    Parameters:
    - records (np.ndarray): A 2D numpy array with each row as a record and each column as a feature.
    - random_seed (int, optional): Seed for random operations to ensure reproducibility.

    Returns:
    - pd.DataFrame: A pandas DataFrame containing the preprocessed data, with shuffled feature names.

    Raises:
    - ValueError: If records is not 2D.

    Requirements:
    - numpy
    - pandas
    - sklearn

    Notes:
    - This function normalizes data by subtracting the mean and scaling to unit variance.
    - Feature names are of format f{n}; for example, if the records have 5 features, feature
      names will be ["f1", "f2", "f3", "f4", "f5"] shuffled.

    Examples:
    >>> data = np.array([[1, 2, 3], [4, 5, 6]])
    >>> df = f_575(data, random_seed=42)
    >>> df.shape
    (2, 3)
    >>> df.columns
    Index(['f2', 'f3', 'f1'], dtype='object')
    >>> data = np.array([[-1, -2, -3, -4, -5], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5]])
    >>> df = f_575(data, random_seed=24)
    >>> df
             f3        f1        f4        f5        f2
    0 -1.224745 -1.224745 -1.224745 -1.224745 -1.224745
    1  0.000000  0.000000  0.000000  0.000000  0.000000
    2  1.224745  1.224745  1.224745  1.224745  1.224745
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    if not (records.ndim == 2):
        raise ValueError("Input must be a 2D numpy array.")
    records_copy = records.copy()
    np.random.shuffle(records_copy.T)
    scaler = StandardScaler()
    normalized_records = scaler.fit_transform(records_copy)
    features = [f"f{i+1}" for i in range(records[0].shape[0])]
    np.random.shuffle(features)
    df = pd.DataFrame(normalized_records, columns=features)
    return df

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.expected_shape = (2, 5)
    def test_case_1(self):
        # Test basic shape and columns
        df = f_575(self.data, random_seed=1)
        self.assertEqual(df.shape, self.expected_shape)
        self.assertTrue(set(df.columns) == set(["f1", "f2", "f3", "f4", "f5"]))
        # assert last row values
        self.assertEqual(df.iloc[-1].tolist(), [1.0, 1.0, 1.0, 1.0, 1.0])
        self.assertEqual(df.iloc[0].tolist(), [-1.0, -1.0, -1.0, -1.0, -1.0])
        
    def test_case_2(self):
        # Test normalization
        df = f_575(self.data, random_seed=2)
        np.testing.assert_array_almost_equal(
            df.mean(axis=0), np.zeros(self.expected_shape[1]), decimal=5
        )
        np.testing.assert_array_almost_equal(
            df.std(axis=0, ddof=0), np.ones(self.expected_shape[1]), decimal=5
        )
        
    def test_case_3(self):
        # Test random seed effect
        df1 = f_575(self.data, random_seed=3)
        df2 = f_575(self.data, random_seed=3)
        pd.testing.assert_frame_equal(df1, df2)
    def test_case_4(self):
        # Test handling invalid inputs
        with self.assertRaises(ValueError):
            f_575(np.array([1, 2, 3]), random_seed=4)
        with self.assertRaises(ValueError):
            f_575(np.array([[1, 2, 3], [4, 5]], dtype=object), random_seed=4)
    def test_case_5(self):
        # Test handling zero variance
        data = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
        df = f_575(data, random_seed=42)
        # In cases of zero variance, StandardScaler will set values to 0
        np.testing.assert_array_equal(df.values, np.zeros(data.shape))
