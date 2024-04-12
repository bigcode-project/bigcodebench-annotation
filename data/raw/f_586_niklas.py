import pandas as pd
from sklearn.linear_model import LinearRegression

def f_586(df, target):
    """
    Perform a linear regression analysis on a given DataFrame.
    
    Parameters:
    - df (DataFrame): The pandas DataFrame.
    - target (str): The target variable.
    
    Returns:
    - score (float): The R-squared score of the model.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> df = pd.DataFrame([[5.1, 1.4], [4.9, 1.4], [4.7, 1.3]], columns = ['x', 'y'])
    >>> r_squared = f_586(df, 'y')
    >>> print(r_squared)
    0.7500000000000011
    """
    X = df.drop(target, axis=1)
    y = df[target]
    
    model = LinearRegression()
    model.fit(X, y)

    return model.score(X, y)

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]], columns = ['x', 'y', 'z'])
        r_squared = f_586(df, 'z')
        self.assertEqual(r_squared, 1.0)
        
    def test_case_2(self):
        df = pd.DataFrame([[-1, 1, 2], [3, 4, 5], [6, 7, 8]], columns = ['x', 'y', 'z'])
        r_squared = f_586(df, 'z')
        self.assertEqual(r_squared, 1.0)
    
    def test_case_3(self):
        df = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]], columns = ['x', 'y', 'z'])
        r_squared = f_586(df, 'z')
        self.assertEqual(r_squared, 1.0)

    def test_case_4(self):
        df = pd.DataFrame([[0, 0, 9], [1, 1, 35], [2, 2, 78]], columns = ['x', 'y', 'z'])
        r_squared = f_586(df, 'z')
        self.assertFalse(r_squared == 1.0)

    def test_case_5(self):
        df = pd.DataFrame([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]], columns = ['x', 'y', 'z', 'w'])
        r_squared = f_586(df, 'w')
        self.assertEqual(r_squared, 1.0)
        
run_tests()
if __name__ == "__main__":
    run_tests()