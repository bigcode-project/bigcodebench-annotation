import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def task_func(df, target_column, target_values=None):
    """
    Replace all elements in DataFrame columns that are not present in the target_values array with zeros, and then perform a linear regression using the target column.

    Parameters:
        df (DataFrame): The input pandas DataFrame.
        target_column (str): The target column for the linear regression.
        target_values (array-like, optional): An array of target values to keep in the DataFrame. 
        All other values will be replaced with zeros. Defaults to None.


    Returns:
        LinearRegression: The trained Linear Regression model.

    Raises:
        ValueError: If df is not a DataFrame or if target_column is not a string or if target_values is not an array-like object

    Requirements:
        - numpy
        - pandas
        - sklearn.linear_model.LinearRegression

    Example:
        >>> rng = np.random.default_rng(seed=0)
        >>> df = pd.DataFrame(rng.integers(0, 100, size=(1000, 2)), columns=['A', 'predict'])
        >>> model = task_func(df, 'predict')
        >>> print(model.coef_)
        [-0.04934205]
        >>> print(model.intercept_)  
        53.67665840020308

        >>> rng = np.random.default_rng(seed=0)
        >>> df = pd.DataFrame(rng.integers(0, 100, size=(1000, 5)), columns=['A', 'B', 'C', 'D', 'predict'])
        >>> model = task_func(df, 'predict')
        >>> print(model.coef_)
        [-0.00173703 -0.02190392 -0.03304266  0.00759771]
        >>> print(model.intercept_)
        53.362739257681035
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df should be a DataFrame.")
    if df.empty:
        raise ValueError("df should contain at least one row")
    if target_column not in df.columns:
        raise ValueError("target_column should be in DataFrame")
    if not all(np.issubdtype(dtype, np.number) for dtype in df.dtypes):
        raise ValueError("df values should be numeric only")
    if target_values != None:
        df = df.applymap(lambda x: x if x in target_values else 0)
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    model = LinearRegression().fit(X, y)
    return model

import unittest
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
class TestCases(unittest.TestCase):
    
    def lin_relation_1d(self, x, w0, w1):
        '''1-d linear relation for testing'''
        return w0 + w1*x
    
    def lin_relation_nd(self, row, w0, w):
        '''n-dimension linear relation for testing'''
        result = 0
        for i, x in enumerate(row.values):
            result += x * w[i]
        return w0 + result 
    def test_case_df(self):
        '''non DataFrame input'''
        df = 3
        target_column = 'test'
        self.assertRaises(Exception, task_func, df, target_column)
    def test_case_target_column(self):
        '''target column not in DataFrame'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.integers(0, 10, size=(5, 2)), columns=['test', 'python'])
        target_column = 'not'
        self.assertRaises(Exception, task_func, df, target_column)
    def test_case_empty_df(self):
        '''empty df as input'''
        df = pd.DataFrame(columns=['A', 'B'])
        target_column = 'A'
        self.assertRaises(Exception, task_func, df, target_column)
    
    def test_case_non_numeric_values(self):
        '''df not numeric'''
        data = {
            'A': [1, 2, 'test'],
            'B': [3, 3, 3]
        }
        df = pd.DataFrame(data)
        target_column = 'A'
        self.assertRaises(Exception, task_func, df, target_column)
    def test_case_1(self):
        '''prediction for one column'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.integers(0, 100, size=(1000, 1)), columns=list('A'))
        df['predict'] = df.apply(self.lin_relation_1d, args=(2, 4))
        model = task_func(df, 'predict')
        self.assertIsInstance(model, LinearRegression, "Returned value is not a LinearRegression model.")
        # make sure predictions work as expected
        pred = model.predict(df.drop('predict', axis=1))
        self.assertTrue(np.allclose(pred.tolist(), df['predict'].tolist()))
        # assert model params
        self.assertAlmostEqual(model.coef_[0], 4, places=4)
        self.assertAlmostEqual(model.intercept_, 2, places=4)
        
    def test_case_2(self):
        '''multiple column prediction'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.integers(0, 100, size=(1000, 5)), columns=list('ABCDE'))
        df['predict'] = df.apply(self.lin_relation_nd, axis=1, args=(4, [2.5, 5.8, 6, 4, -1]))
        model = task_func(df, 'predict')
        self.assertIsInstance(model, LinearRegression, "Returned value is not a LinearRegression model.")
        # make sure predictions work as expected
        pred = model.predict(df.drop('predict', axis=1))
        self.assertTrue(np.allclose(pred.tolist(), df['predict'].tolist()))
        # assert model params
        self.assertTrue(np.allclose(model.coef_, [2.5, 5.8, 6, 4, -1]))
        self.assertAlmostEqual(model.intercept_, 4, places=4)
    def test_case_3(self):
        '''test working target value --> with target value linear regression can't deliver good results'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.integers(0, 10, size=(1000, 1)), columns=list('A'))
        df['predict'] = df.apply(self.lin_relation_1d, args=(0, 2))
        model = task_func(df, 'predict', target_values=[1, 2, 4, 8])
        self.assertIsInstance(model, LinearRegression, "Returned value is not a LinearRegression model.")
        
        # make sure predictions work as expected
        masked_df = df.applymap(lambda x: x if x in [1, 2, 4, 8] else 0)
        masked_predict = masked_df['predict']
        pred = model.predict(masked_df.drop('predict', axis=1))
        self.assertTrue(not np.allclose(pred.tolist(), masked_predict.tolist()))
        # assert model params
        self.assertAlmostEqual(model.coef_[0], 0.2921456, places=2)
        self.assertAlmostEqual(model.intercept_, 0.81175, places=4)
        
    def test_case_4(self):
        '''df with constant values'''
        df = pd.DataFrame(np.full((10, 10), 3), columns=list('ABCDEFGHIJ'))
        model = task_func(df, 'J')
        self.assertTrue(all(coef == 0 for coef in model.coef_), "Model coefficients are not correct.")
        self.assertAlmostEqual(model.intercept_, 3, places=4)
    def test_case_5(self):
        '''df filled with random floats'''
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.random(size=(1000, 5)) * 10, columns=list('ABCDE'))
        df['predict'] = df.apply(self.lin_relation_nd, axis=1, args=(-1, [15, -4.8, 12, 40.2, -2]))
        model = task_func(df, 'predict')
        self.assertIsInstance(model, LinearRegression, "Returned value is not a LinearRegression model.")
        # make sure predictions work as expected
        pred = model.predict(df.drop('predict', axis=1))
        self.assertTrue(np.allclose(pred.tolist(), df['predict'].tolist()))
        # assert model params
        self.assertTrue(np.allclose(model.coef_, [15, -4.8, 12, 40.2, -2]))
        self.assertAlmostEqual(model.intercept_, -1, places=4)
