import pandas as pd
import numpy as np

def f_285(df, col):
    """
    Process a Pandas DataFrame by removing a specific column and adding a 'IsEvenIndex' column.
    The 'IsEvenIndex' column is a boolean flag indicating if the index of each row is even.
    
    Parameters:
    - df (pd.DataFrame): The pandas DataFrame to process.
    - col (str): The column to remove.

    Returns:
    - df (pd.DataFrame): The processed pandas DataFrame with the specified column removed and a new 'IsEvenIndex' column added.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(5, 4)), columns=list('ABCD'))
    >>> df = f_285(df, 'C')
    >>> print(df)
        A   B   D  IsEvenIndex
    0  51  92  71         True
    1  60  20  86        False
    2  74  74  99         True
    3  23   2  52        False
    4   1  87  37         True
    """
    updated_df = pd.DataFrame(df).drop(col, axis=1)
    updated_df['IsEvenIndex'] = np.arange(len(updated_df)) % 2 == 0
    return updated_df

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = f_285(df, 'A')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('A' in df.columns)
    def test_case_2(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = f_285(df, 'B')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('B' in df.columns)
    def test_case_3(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = f_285(df, 'C')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('C' in df.columns)
    def test_case_4(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = f_285(df, 'D')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('D' in df.columns)
    def test_case_5(self):
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        df = f_285(df, 'A')
        self.assertEqual(df.shape, (100, 4))
        self.assertFalse('A' in df.columns)
