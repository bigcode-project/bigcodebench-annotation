import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def f_659(num_samples=1000, k=5, d=2,  random_seed=None):
    """
    Generate a dataset consisting of random numbers sampled from a gaussian
    normal distribution that are transformed by applying a linear
    transformation. Standardize it with the StandardScaler of sklearn,
    and calculate the average square error between the original dataset
    and the standardized dataset.

    Parameters:
    - num_samples (int): The number of samples to generate. Default is 1000.
    - k (float): Multiplicative Factor in linear transformation. Default is 5.
    - d (float): Offset in linear transformation. Default is 2.
    - random_seed (int): The random seed for reproducibility. Default is None.

    Returns:
    float: The mean squared error between the original and standardized data.
           This value represents the average squared difference between each
           original value and its standardized counterpart. The MSE can vary
           significantly depending on the random seed and the specified 
           parameters of the linear transformation.

    Requirements:
    - numpy
    - sklearn.preprocessing.StandardScaler
    - sklearn.metrics.mean_squared_error

    Example:
    >>> mse = f_659(num_samples=123, k=-6.4, d=12.1, random_seed=2)
    >>> print(mse)
    193.04172078372736

    >>> mse = f_659()
    >>> print(mse)
    19.03543917135251

    >>> mse = f_659(k=1, d=0)
    >>> print(mse)
    0.001113785307245742
    """

    if random_seed is not None:
        np.random.seed(random_seed)
    data = np.random.randn(num_samples, 1)*k + d
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    mse = mean_squared_error(data, scaled_data)

    return mse

import unittest
class TestCases(unittest.TestCase):
    def test_case_rng(self):
        'test rng reproducability'
        result1 = f_659(random_seed=23)
        result2 = f_659(random_seed=23)
        self.assertEqual(result1, result2)
    def test_case_1(self):
        'low mse + mse decreasing with num_samples'
        result1 = f_659(num_samples=1000000, k=1, d=0, random_seed=1)
        self.assertAlmostEqual(result1, 0, places=5)
        result2 = f_659(num_samples=1000, k=1, d=0, random_seed=1)
        result3 = f_659(num_samples=10000, k=1, d=0, random_seed=1)
        self.assertTrue(result2 > result3)
    def test_case_2(self):
        'deterministic mse'
        result = f_659(num_samples=100, k=0, d=10, random_seed=42)
        self.assertAlmostEqual(result, 100, places=5)
    def test_case_3(self):
        'random input'
        result = f_659(num_samples=10000, k=10, d=0, random_seed=42)
        self.assertAlmostEqual(result, 81.61581766096013, places=5)
    def test_case_5(self):
        'floats'
        result = f_659(num_samples=340, k=-3.4, d=123.4, random_seed=42)
        self.assertAlmostEqual(result, 15220.804873417765, places=5)
