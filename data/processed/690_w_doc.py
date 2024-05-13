import pandas as pd
from sklearn.linear_model import LinearRegression

ROWS = 100
COLUMNS = ['X', 'Y']

def task_func(df):
    """
    Given a Pandas DataFrame with random numeric values and columns X & Y, use sklearn's linear regression to match the data to a linear model.

    Parameters:
    - df (DataFrame): The DataFrame to use.

    Returns:
    - model (LinearRegression): The fitted linear model.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.normal(size=(100, 2)), columns=['X', 'Y'])
    >>> model = task_func(df)
    >>> print(model)
    LinearRegression()
    """
    X = pd.DataFrame(df[['X']])  # Extracting column 'X' as a DataFrame
    y = pd.Series(df['Y'])       # Extracting column 'Y' as a Series
    model = LinearRegression().fit(X, y)
    return model

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
    
    def test_case_2(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
    def test_case_3(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
    def test_case_4(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) is not None)
    def test_case_5(self):
        df = pd.DataFrame(np.random.normal(size=(ROWS, len(COLUMNS))), columns=COLUMNS)
        model = task_func(df)
        self.assertTrue(model is not None)
        self.assertTrue(model.coef_ is not None)
        self.assertTrue(model.intercept_ is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) is not None)
        self.assertTrue(model.score(df[['X']], df['Y']) >= 0)
