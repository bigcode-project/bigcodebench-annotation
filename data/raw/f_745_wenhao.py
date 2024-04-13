import pandas as pd
from sklearn.linear_model import LinearRegression

def f_745(d, target='z'):
    """
    Perform linear regression to "x," "y," against "z" from a list of dictionaries "d."

    Parameters:
    d (list): A list of dictionaries.
    target (str): The target variable for the regression.

    Returns:
    LinearRegression: A LinearRegression model.

    Requirements:
    - pandas
    - sklearn.linear_model.LinearRegression

    Examples:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
    >>> model = f_745(data)
    >>> isinstance(model, LinearRegression)
    True

    >>> data = [{'x': 4, 'y': 20, 'z': 10}, {'x': 5, 'y': 25, 'z': 15}, {'x': 6, 'y': 5, 'z': 20}]
    >>> model = f_745(data, target='y')
    >>> isinstance(model, LinearRegression)
    True
    """
    df = pd.DataFrame(d)
    predictors = [k for k in df.columns if k != target]

    X = df[predictors]
    y = df[target]

    model = LinearRegression().fit(X, y)

    return model

import unittest

class TestCases(unittest.TestCase):
    
    def test_basic_regression(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        model = f_745(data)
        self.assertIsInstance(model, LinearRegression)
        self.assertEqual(len(model.coef_), 2)

    def test_negative_values(self):
        data = [{'x': -1, 'y': -10, 'z': -5}, {'x': -3, 'y': -15, 'z': -6}, {'x': -2, 'y': -1, 'z': -7}]
        model = f_745(data)
        self.assertIsInstance(model, LinearRegression)
        self.assertEqual(len(model.coef_), 2)
    
    def test_zero_values(self):
        data = [{'x': 0, 'y': 0, 'z': 0}, {'x': 0, 'y': 0, 'z': 0}, {'x': 0, 'y': 0, 'z': 0}]
        model = f_745(data)
        self.assertIsInstance(model, LinearRegression)
        self.assertEqual(len(model.coef_), 2)
    
    def test_different_target(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        model = f_745(data, target='y')
        self.assertIsInstance(model, LinearRegression)
        self.assertEqual(len(model.coef_), 2)
    
    def test_single_predictor(self):
        data = [{'x': 1, 'z': 5}, {'x': 3, 'z': 6}, {'x': 2, 'z': 7}]
        model = f_745(data, target='z')
        self.assertIsInstance(model, LinearRegression)
        self.assertEqual(len(model.coef_), 1)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
