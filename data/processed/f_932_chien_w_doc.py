import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def f_274(data=None):
    """
    Pre-process a dataset by converting it to a Pandas DataFrame,
    replacing values less than 0.5 with zeros, and
    standardizing the data using StandardScaler.

    Parameters:
    - data (numpy.ndarray, optional): A numpy array representing the dataset. If not provided, a random dataset
      of shape (100, 5) is generated.

    Returns:
    - pandas.DataFrame: The preprocessed dataset. Original values less than 0.5 are replaced with zeros, and the
      entire dataset is standardized.

    Requirements:
    - numpy
    - pandas
    - sklearn.preprocessing.StandardScaler

    Example:
    >>> np.random.seed(0)
    >>> dataset = np.random.rand(10, 5)
    >>> preprocessed_data = f_274(dataset)
    >>> preprocessed_data.head(2)
              0         1         2        3         4
    0  0.175481  1.062315  0.244316 -0.17039 -0.647463
    1  0.461851 -0.978767  1.052947  1.06408 -0.647463
    """
    if data is None:
        data = np.random.rand(100, 5)
    df = pd.DataFrame(data)
    df[df < 0.5] = 0
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    standardized_df = pd.DataFrame(scaled_data, columns=df.columns)
    return standardized_df

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the function f_274."""
    def test_default_dataset(self):
        """Test the function with default dataset."""
        result = f_274()
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (100, 5))
    def test_small_dataset(self):
        """Test the function with a small dataset."""
        data = np.array([[0.1, 0.9], [0.4, 0.8]])
        result = f_274(data)
        self.assertEqual(result.shape, (2, 2))
    def test_replacement(self):
        """Test the replacement of values less than 0.5."""
        data = np.array([[0.1, 0.9], [0.4, 0.8]])
        result = f_274(data)
        self.assertNotIn(0.1, result.values)
        self.assertNotIn(0.4, result.values)
    def test_no_replacement(self):
        """Test no replacement for values greater than 0.5."""
        data = np.array([[0.6, 0.9], [0.7, 0.8]])
        result = f_274(data)
        self.assertNotIn(0.6, result.values)
        self.assertNotIn(0.7, result.values)
        self.assertNotIn(0.8, result.values)
        self.assertNotIn(0.9, result.values)
    def test_standardization(self):
        """Test the standardization of the dataset."""
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = f_274(data)
        self.assertTrue(np.isclose(result.mean().mean(), 0, atol=1e-5))
        self.assertTrue(np.isclose(result.std().mean(), 1.225, atol=0.01))
        """Test the replacement of values less than 0.5."""
        data = np.array([[0.1, 0.9], [0.4, 0.8]])
        result = f_274(data)
        self.assertNotIn(0.1, result.values)
        self.assertNotIn(0.4, result.values)
