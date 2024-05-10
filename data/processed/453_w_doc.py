import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def task_func(n_samples=100, n_features=10, random_seed=None):
    """
    Generate synthetic data using a simple regression model, fit a linear regression model to the data,
    and return the predicted values along with the coefficients and intercept of the model.

    Parameters:
    - n_samples (int): The number of samples for the synthetic data. Default is 100.
    - n_features (int): The number of features for the synthetic data. Default is 10.
    - random_seed (int, optional): The seed for reproducibility. Default is None.

    Returns:
    - tuple: A tuple containing:
        - predictions (numpy.ndarray): The predicted values of the test set.
        - coefficients (numpy.ndarray): Coefficients of the linear regression model.
        - intercept (float): Intercept of the linear regression model.
        - mse (float): Mean squared error of the model predictions.

    Requirements:
    - numpy
    - sklearn.datasets.make_regression
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LinearRegression
    
    Example:
    >>> predictions, coefficients, intercept, mse = task_func(100, 5, random_seed=42)
    >>> predictions[:3]
    array([ 180.79207843, -295.0210232 ,  118.23799221])
    >>> round(mse, 4)
    0.0113
    """
    X, y = datasets.make_regression(
        n_samples=n_samples, n_features=n_features, noise=0.1, random_state=random_seed
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_seed
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    coefficients = model.coef_
    intercept = model.intercept_
    mse = np.mean((predictions - y_test) ** 2)
    return predictions, coefficients, intercept, mse

import unittest
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import datasets
from numpy.testing import assert_array_equal
import numpy as np
class TestCases(unittest.TestCase):
    def generate_data(self, n_samples, n_features, random_seed=None):
        # Generate data for testing
        X, y = datasets.make_regression(
            n_samples=n_samples,
            n_features=n_features,
            noise=0.1,
            random_state=random_seed,
        )
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=random_seed
        )
        return X_train, X_test, y_train, y_test
    def test_case_1(self):
        # Basic test for different inputs
        random_seed = 1
        for n_samples, n_features in [
            [100, 5],
            [500, 8],
            [1000, 10],
            [5000, 15],
            [10000, 20],
        ]:
            predictions, _, _, mse = task_func(n_samples, n_features, random_seed=random_seed)
            _, _, _, y = self.generate_data(
                n_samples, n_features, random_seed=random_seed
            )
            self.assertEqual(mse, mean_squared_error(y, predictions))
    def test_case_2(self):
        # Test default parameters
        predictions, coefficients, intercept, mse = task_func(random_seed=42)
        self.assertEqual(
            predictions.shape[0], 20
        )  # Default split leaves 20% of 100 samples for testing
        self.assertEqual(coefficients.shape[0], 10)  # Default number of features
        self.assertIsInstance(intercept, float)
        _, _, _, y = self.generate_data(
                100, 10, 42
            )
        self.assertEqual(mse, mean_squared_error(y, predictions))
    def test_case_3(self):
        # Test different random seeds for reproducibility
        _, coefficients_1, intercept_1, mse_1 = task_func(random_seed=1)
        _, coefficients_2, intercept_2, mse_2 = task_func(random_seed=2)
        with self.assertRaises(AssertionError):
            assert_array_equal(coefficients_1, coefficients_2)
            self.assertEqual(intercept_1, intercept_2)
            
    def test_case_4(self):
        # Test zero and negative samples and features
        with self.assertRaises(ValueError):
            task_func(n_samples=0, n_features=10)
        with self.assertRaises(ValueError):
            task_func(n_samples=100, n_features=0)
        with self.assertRaises(ValueError):
            task_func(n_samples=-100, n_features=10)
        with self.assertRaises(ValueError):
            task_func(n_samples=100, n_features=-10)
    def test_case_5(self):
        # Test extreme values for parameters
        predictions, _, _, mse = task_func(n_samples=100000, n_features=100, random_seed=42)
        self.assertEqual(
            predictions.shape[0], 20000
        )  # 20% of 100000 samples for testing
        self.assertAlmostEqual(mse, 0.010142327812255192, places=4)
        
    def test_case_6(self):
        # Test output shapes
        predictions, coefficients, _, mse = task_func(
            n_samples=100, n_features=5, random_seed=42
        )
        self.assertEqual(predictions.shape[0], 20)
        self.assertEqual(coefficients.shape[0], 5)
    def test_case_7(self):
        # Test output types
        predictions, coefficients, intercept, mse = task_func()
        self.assertIsInstance(predictions, np.ndarray)
        self.assertIsInstance(coefficients, np.ndarray)
        self.assertIsInstance(intercept, float)
        self.assertIsInstance(mse, float)
        
    def test_case_8(self):
        # Test determinism with the same random seed
        predictions_1, _, _, mse_1 = task_func(random_seed=42)
        predictions_2, _, _, mse_2 = task_func(random_seed=42)
        assert_array_equal(predictions_1, predictions_2)
        self.assertEqual(mse_1, mse_2)
        
    def test_case_9(self):
        # Test without random seed (non-deterministic outcomes)
        predictions_1, _, _, _ = task_func()
        predictions_2, _, _, _ = task_func()
        with self.assertRaises(AssertionError):
            assert_array_equal(predictions_1, predictions_2)
