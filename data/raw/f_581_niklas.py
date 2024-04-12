import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def f_581(df):
    """
    Divide the given DataFrame into a training set and a test set (70%: 30% split), separate the "Target" column and return the four resulting dataframs.

    Parameters:
    - df (DataFrame): pandas DataFrame that contains a column named 'target'.

    Returns:
    - tuple: A tuple containing four DataFrames: X_train, X_test, y_train, y_test.

    Requirements:
    - pandas
    - sklearn
    - numpy
    
    Example:
    >>> df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=list('ABCDE'))
    >>> df['target'] = np.random.randint(0, 2, size=100)
    >>> X_train, X_test, y_train, y_test = f_581(df)
    >>> print(X_train.shape)
    (70, 5)
    """
    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=list('ABCDE'))
        df['target'] = np.random.randint(0, 2, size=100)
        X_train, X_test, y_train, y_test = f_581(df)
        self.assertEqual(X_train.shape, (70, 5))
        self.assertEqual(X_test.shape, (30, 5))
        self.assertEqual(y_train.shape, (70,))
        self.assertEqual(y_test.shape, (30,))

    def test_case_2(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'target': [0, 1, 0]})
        X_train, X_test, y_train, y_test = f_581(df)
        self.assertEqual(X_train.shape, (2, 2))
        self.assertEqual(X_test.shape, (1, 2))
        self.assertEqual(y_train.shape, (2,))
        self.assertEqual(y_test.shape, (1,))

    def test_case_3(self):
        df = pd.DataFrame({'A': [0, 0, 0], 'B': [0, 0, 0], 'target': [0, 0, 0]})
        X_train, X_test, y_train, y_test = f_581(df)
        self.assertEqual(X_train.shape, (2, 2))
        self.assertEqual(X_test.shape, (1, 2))
        self.assertEqual(y_train.shape, (2,))
        self.assertEqual(y_test.shape, (1,))
        self.assertEqual(X_train.iloc[0, 0], 0)
        self.assertEqual(X_train.iloc[0, 1], 0)
        self.assertEqual(X_train.iloc[1, 0], 0)
        self.assertEqual(X_train.iloc[1, 1], 0)
        self.assertEqual(X_test.iloc[0, 0], 0)
        self.assertEqual(X_test.iloc[0, 1], 0)
        self.assertEqual(y_train.iloc[0], 0)
        self.assertEqual(y_train.iloc[1], 0)
        self.assertEqual(y_test.iloc[0], 0)

    def test_case_4(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'target': [1, 1, 1]})
        X_train, X_test, y_train, y_test = f_581(df)
        self.assertEqual(X_train.shape, (2, 2))
        self.assertEqual(X_test.shape, (1, 2))
        self.assertEqual(y_train.shape, (2,))
        self.assertEqual(y_test.shape, (1,))
    
    def test_case_5(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'target': [0, 0, 0]})
        X_train, X_test, y_train, y_test = f_581(df)
        self.assertEqual(X_train.shape, (2, 2))
        self.assertEqual(X_test.shape, (1, 2))
        self.assertEqual(y_train.shape, (2,))
        self.assertEqual(y_test.shape, (1,))


run_tests()
if __name__ == "__main__":
    run_tests()