import heapq
from sklearn.linear_model import LinearRegression

def f_655(df, feature, target, n=10):
    """
    Fit a simple linear regression model to two columns of a DataFrame 
    specified by feature and target. 
    return the indices of the n largest residuals as well as the linear 
    regression model.
    
    Parameters:
    df (pandas.DataFrame): A DataFrame with at least two numerical columns named 'col1' and 'col2'.
    feature (str): The DataFrame column used as feature.
    target (str): The DataFrame column used as target.
    n (int, optional): Number of largest residuals to return. Default is 10.
    
    Returns:
    list[int]: Indices of the n largest residuals.
    LinearRegression: The LinearRegression model.
    
    Raises:
    ValueError: If specified columns are not in the provided DataFrame.

    Requirements:
    - heapq
    - sklearn.linear_model
    
    Example:
    >>> df = pd.DataFrame({
    ...     'col1': [99, 86, 90, 70, 86, 95, 56, 98, 80, 81],
    ...     'col2': [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
    ... })
    >>> indices, model = f_655(df, 'col1', 'col2', n=5)
    >>> print(indices)
    [0, 1, 9, 7, 8]
    >>> print(model)
    LinearRegression()

    >>> df = pd.DataFrame({
    ...     'a': [1, 2, 3, 4, 5],
    ...     'b': [1, 2, 3, 4, 5]
    ... })
    >>> indices, model = f_655(df, 'a', 'b', n=3)
    >>> print(indices)
    [0, 1, 2]
    >>> print(model)
    LinearRegression()
    """
    if feature not in df.columns or target not in df.columns:
        raise ValueError(f"Columns {feature} or {target} not found in the DataFrame.")
    X = df[feature].values.reshape(-1, 1)
    y = df[target].values
    model = LinearRegression()
    model.fit(X, y)
    residuals = y - model.predict(X)
    largest_residual_indices = heapq.nlargest(n, range(len(residuals)), key=lambda i: abs(residuals[i]))
    return largest_residual_indices, model

import unittest
from faker import Faker
import pandas as pd
fake = Faker()
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.sample_data = {
            'col1': [fake.random_int(min=1, max=100) for _ in range(100)],
            'col2': [fake.random_int(min=1, max=100) for _ in range(100)]
        }
    def test_wrong_columns(self):
        # test with wrong columns
        data = {
            'col1': [1, 2, 3, 4, 5],
            'col2': [2, 3, 4, 5, 6]
        }
        df = pd.DataFrame(data)
        self.assertRaises(Exception, f_655, df, 'a', 'col2')
        self.assertRaises(Exception, f_655, df, 'col1', 'a')
        self.assertRaises(Exception, f_655, df, 'a', 'b')
    # tests with random data
    def test_case_1(self):
        indices, model = f_655(pd.DataFrame(self.sample_data), 'col1', 'col2')
        self.assertTrue(isinstance(model, LinearRegression))
        self.assertEqual(len(indices), 10)
    def test_case_2(self):
        indices, model = f_655(pd.DataFrame(self.sample_data), 'col1', 'col2', n=5)
        self.assertTrue(isinstance(model, LinearRegression))
        self.assertEqual(len(indices), 5)
    def test_case_3(self):
        random_length = fake.random_int(min=5, max=20)
        df = pd.DataFrame({
            'col1': [fake.random_int(min=1, max=100) for _ in range(random_length)],
            'col2': [fake.random_int(min=1, max=100) for _ in range(random_length)]
        })
        indices, model = f_655(df, 'col1', 'col2', n=3)
        self.assertTrue(isinstance(model, LinearRegression))
        self.assertEqual(len(indices), 3)
    def test_case_4(self):
        df = pd.DataFrame({
            'col1': [fake.random_int(min=1, max=100) for _ in range(10)],
            'col2': [50 for _ in range(10)]
        })
        indices, model = f_655(df, 'col1', 'col2')
        self.assertTrue(isinstance(model, LinearRegression))
        self.assertEqual(len(indices), 10)
    def test_case_5(self):
        df = pd.DataFrame({
            'col1': list(range(10)),
            'col2': list(range(10))
        })
        indices, model = f_655(df, 'col1', 'col2')
        self.assertTrue(isinstance(model, LinearRegression))
        self.assertEqual(len(indices), 10)
    # deterministic tests
    def test_deterministic_case_1(self):
        df = pd.DataFrame({
            'col1': [10, 20, 30, 40, 50],
            'col2': [1, 2, 3, 4, 5]
        })
        indices, model = f_655(df, 'col1', 'col2')
        self.assertTrue(isinstance(model, LinearRegression))
        # Given the linear relationship, the residuals should be close to zero.
        # Hence, any index could be in the top N residuals.
        # check if model was used to generate indices
        y = df['col2'].values
        X = df['col1'].values.reshape(-1, 1)
        residuals = y - model.predict(X)
        largest_residual_indices = heapq.nlargest(10, range(len(residuals)), key=lambda i: abs(residuals[i]))
        self.assertListEqual(largest_residual_indices, indices)
    def test_deterministic_case_2(self):
        df = pd.DataFrame({
            'col1': [10, 20, 30, 40, 50],
            'col2': [10, 40, 90, 160, 250]
        })
        indices, model = f_655(df, 'col1', 'col2')
        self.assertTrue(isinstance(model, LinearRegression))
        # Given the data, the residuals will vary. 
        # We're predicting the largest residuals based on known data.
        expected_indices = [0, 2, 4, 1, 3]  # This is based on a manual observation.
        self.assertEqual(indices, expected_indices)
        # check if model was used to generate indices
        y = df['col2'].values
        X = df['col1'].values.reshape(-1, 1)
        residuals = y - model.predict(X)
        largest_residual_indices = heapq.nlargest(10, range(len(residuals)), key=lambda i: abs(residuals[i]))
        self.assertListEqual(largest_residual_indices, indices)
    def test_deterministic_case_3(self):
        df = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5],
            'col2': [5, 4, 3, 2, 1]
        })
        indices, model = f_655(df, 'col1', 'col2')
        self.assertTrue(isinstance(model, LinearRegression))
        # Given the inverse linear relationship, the residuals should be close to zero.
        # Hence, any index could be in the top N residuals.
        self.assertEqual(len(indices), 5)
        # check if model was used to generate indices
        y = df['col2'].values
        X = df['col1'].values.reshape(-1, 1)
        residuals = y - model.predict(X)
        largest_residual_indices = heapq.nlargest(10, range(len(residuals)), key=lambda i: abs(residuals[i]))
        self.assertListEqual(largest_residual_indices, indices)
