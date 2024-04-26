import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def f_719(data, n_components=2):
    """
    Perform PCA (Principal Component Analysis) on the provided DataFrame.

    This function takes a pandas DataFrame, scales the data using sklearn 
    StandardScaler, and then applies PCA to reduce 
    the number of dimensions of the data to the number specified by n_components, 
    maintaining as much information as possible.

    Parameters:
    data (DataFrame): A pandas DataFrame containing numerical data. Each column represents a 
                      different variable, and each row represents a different observation.
    n_components (int): The number of principal components to retain after transformation. 
                        Default is 2.

    Returns:
    DataFrame: A new DataFrame with the original data transformed into 'n_components' principal 
               components.

    Raises:
    ValueError: If input data is not a DataFrame or contains non-numeric data.
    ValueError: If n_components is greater than the number of columns in the data.
    ValueError: If input data is empty.

    Requirements:
    pandas
    sklearn.preprocessing
    sklearn.decomposition

    Example:
    >>> data = pd.DataFrame({
    ...     'A': [1, 2, 3, 4, 5],
    ...     'B': [6, 7, 8, 9, 10],
    ...     'C': [11, 12, 13, 14, 15],
    ...     'D': [16, 17, 18, 19, 20]
    ... })
    >>> result = f_719(data, n_components=2)
    >>> print(result)
              0             1
    0  2.828427  3.648565e-16
    1  1.414214 -1.216188e-16
    2 -0.000000  0.000000e+00
    3 -1.414214  1.216188e-16
    4 -2.828427  2.432377e-16

    >>> data = pd.DataFrame({
    ...         'A': [-43, 212, 1, -12, 5],
    ...         'B': [-1, 0, 0, 9.76, 12.34],
    ...         'C': [1, 42, -13.2, 31, 1.23],
    ... })
    >>> res = f_719(data, n_components=1)
    >>> print(res)        
              0
    0 -0.793152
    1  2.511947
    2 -0.940253
    3  0.069179
    4 -0.847722
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data should be a DataFrame.")

    if not data.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).all():
        raise ValueError("DataFrame should only contain numeric values.")
    
    if n_components > len(data.columns):
        raise ValueError("n_components should not be greater than the number of columns in data.")
    
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    pca = PCA(n_components=n_components)
    data_reduced = pca.fit_transform(data_scaled)
    return pd.DataFrame(data_reduced)

import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.data_small = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [6, 7, 8, 9, 10],
            'C': [11, 12, 13, 14, 15],
            'D': [16, 17, 18, 19, 20]
        })
        self.data_large = pd.DataFrame(np.random.randint(0, 100, size=(1000, 50)))
    def test_basic_functionality(self):
        result = f_719(self.data_small)
        self.assertEqual(result.shape, (5, 2))
    def test_varying_components(self):
        for components in [1, 3, 4]:
            result = f_719(self.data_small, n_components=components)
            self.assertEqual(result.shape, (5, components))
    def test_large_dataset(self):
        result = f_719(self.data_large, n_components=10)
        self.assertEqual(result.shape, (1000, 10))
    def test_invalid_input(self):
        data_invalid = self.data_small.copy()
        data_invalid['E'] = ['non-numeric'] * 5
        with self.assertRaises(ValueError):
            f_719(data_invalid)
    def test_empty_dataframe(self):
        data_empty = pd.DataFrame()
        with self.assertRaises(ValueError):
            f_719(data_empty)
    def test_known_input(self):
        expected_output = np.array([
            [ 2.82842712e+00,  3.64856517e-16],
            [ 1.41421356e+00, -1.21618839e-16],
            [-0.00000000e+00,  0.00000000e+00],
            [-1.41421356e+00,  1.21618839e-16],
            [-2.82842712e+00,  2.43237678e-16]
       ])
        actual_output = f_719(self.data_small, n_components=2).values
        np.testing.assert_almost_equal(actual_output, expected_output, decimal=5)
