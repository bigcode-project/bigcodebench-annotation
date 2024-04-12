import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def f_580(df):
    """
    Use a linear regression model to predict the "value" of "feature" in the given dataframe and return the coefficients and section.

    Parameters:
    - df (DataFrame): pandas DataFrame that contains columns named 'feature' and 'value'.

    Returns:
    - unittest (dict): A dictionary with the coefficients and the intercept of the fitted linear regression model.

    Requirements:
    - pandas
    - numpy
    - sklearn

    Example:
    >>> np.random.seed(42)
    >>> df = pd.DataFrame({'feature': np.random.rand(100), 'value': np.random.rand(100)})
    >>> coefficients = f_580(df)
    >>> print(coefficients)
    {'coefficients': [[-0.03353164387961974]], 'intercept': [0.5135976564010359]}
    """
    X = df['feature'].values.reshape(-1,1)
    y = df['value'].values.reshape(-1,1)

    # Fit linear regression
    model = LinearRegression().fit(X, y)

    return {'coefficients': model.coef_.tolist(), 'intercept': model.intercept_.tolist()}

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'feature': np.random.rand(100), 'value': np.random.rand(100)})
        coefficients = f_580(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)

    def test_case_2(self):
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [1, 2, 3, 4, 5]})
        coefficients = f_580(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 1.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 0.0)

    def test_case_3(self):
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [2, 4, 6, 8, 10]})
        coefficients = f_580(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 2.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 0.0)

    def test_case_4(self):
        df = pd.DataFrame({'feature': [0, 0, 0, 0, 0], 'value': [1, 2, 3, 4, 5]})
        coefficients = f_580(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 0.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 3.0)

    def test_case_5(self):
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [0, 0, 0, 0, 0]})
        coefficients = f_580(df)
        self.assertEqual(len(coefficients['coefficients']), 1)
        self.assertEqual(len(coefficients['coefficients'][0]), 1)
        self.assertEqual(len(coefficients['intercept']), 1)
        self.assertAlmostEqual(coefficients['coefficients'][0][0], 0.0)
        self.assertAlmostEqual(coefficients['intercept'][0], 0.0)

run_tests()
if __name__ == "__main__":
    run_tests()