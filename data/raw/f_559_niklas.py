import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

ROWS = 100
COLUMNS = ['X', 'Y']

def f_559(df):
    """
    Given a Pandas DataFrame with random numeric values and columns X & Y, use sklearn's linear regression to match the data to a linear model.

    Parameters:
    df (DataFrame): The DataFrame to use.

    Returns:
    LinearRegression: The fitted linear model.

    Requirements:
    - numpy
    - pandas
    - sklearn

    Example:
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.normal(size=(100, 2)), columns=['X', 'Y'])
    >>> model = f_559(df)
    >>> print(model)
    LinearRegression()
    """
    model = LinearRegression().fit(df[['X']], df['Y'])
    return model

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = f_559(df)
        self.assertTrue(model is not None)
    
    def test_case_2(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = f_559(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)

    def test_case_3(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = f_559(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)

    def test_case_4(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = f_559(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) is not None)

    def test_case_5(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = f_559(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) >= 0)

run_tests()
if __name__ == "__main__":
    run_tests()