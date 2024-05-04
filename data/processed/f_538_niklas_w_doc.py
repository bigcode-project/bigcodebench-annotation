import numpy as np
import pandas as pd
from scipy.stats import linregress


def f_304(df):
    """
    Analyze the relationship between two variables in a DataFrame.
    The function performs a linear regression on the two variables and adds a 'predicted' column to the DataFrame.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame with columns 'var1', 'var2'.
    
    Returns:
    - df (pandas.DataFrame): The DataFrame with the added 'predicted' column.

    Requirements:
    - numpy
    - pandas
    - scipy

    Example:
    >>> df = pd.DataFrame({'var1': np.random.randn(10),
    ...                    'var2': np.random.randn(10)})
    >>> df = f_304(df)
    >>> assert 'predicted' in df.columns
    >>> assert len(df) == 10
    >>> assert len(df.columns) == 3
    """
    regression = linregress(df['var1'], df['var2'])
    predictions = np.array(regression.slope) * np.array(df['var1']) + np.array(regression.intercept)
    df['predicted'] = pd.Series(predictions, index=df.index)
    return df

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'var1': np.random.randn(10),
                           'var2': np.random.randn(10)})
        df = f_304(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 10)
        self.assertEqual(len(df.columns), 3)
    def test_case_2(self):
        df = pd.DataFrame({'var1': [1, 2, 3, 4, 5],
                            'var2': [1, 2, 3, 4, 5]})
        df = f_304(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 5)
        self.assertEqual(len(df.columns), 3)
        self.assertTrue(np.all(df['predicted'] == df['var2']))
    
    def test_case_3(self):
        df = pd.DataFrame({'var1': [1, 2, 3, 4, 5],
                            'var2': [5, 4, 3, 2, 1]})
        df = f_304(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 5)
        self.assertEqual(len(df.columns), 3)
        self.assertTrue(np.all(df['predicted'] == df['var2']))
    def test_case_4(self):
        df = pd.DataFrame({'var1': [1, 2, 3, 4, 5],
                            'var2': [1, 1, 1, 1, 1]})
        df = f_304(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 5)
        self.assertEqual(len(df.columns), 3)
        self.assertTrue(np.all(df['predicted'] == df['var2']))
    def test_case_5(self):
        df = pd.DataFrame({'var1': [0, 1, 2, 3, 4, 5],
                            'var2': [1, 1, 1, 1, 1, 1]})
        df = f_304(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 6)
        self.assertEqual(len(df.columns), 3)
        self.assertTrue(np.all(df['predicted'] == df['var2']))
