import numpy as np
import pandas as pd
import random

def f_810(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    """
    Creates a matrix of specified dimensions with random integers within a given range,
    and then converts it into a pandas DataFrame.
    
    Parameters:
    - rows (int): Number of rows in the matrix. Default is 3.
    - cols (int): Number of columns in the matrix. Default is 2.
    - min_val (int): Minimum integer value for the random integers. Default is 0.
    - max_val (int): Maximum integer value for the random integers. Default is 100.
    
    Returns:
    DataFrame: A pandas DataFrame containing random integers within the specified range.
    
    Requirements:
    - numpy
    - pandas
    - random

    Example:
    >>> df = f_810(3, 2, 0, 100)
    >>> print(type(df))
    <class 'pandas.core.frame.DataFrame'>
    >>> print(df.shape)
    (3, 2)
    """
    random.seed(seed)
    if min_val == max_val:
        matrix = np.full((rows, cols), min_val)
    else:
        matrix = np.array([[random.randrange(min_val, max_val) for j in range(cols)] for i in range(rows)])
    df = pd.DataFrame(matrix)
    return df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = f_810()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.iloc[:, 0].tolist(), [49, 53, 33])
        self.assertEqual(df.iloc[:, 1].tolist(), [97, 5, 65])
        
    def test_case_2(self):
        df = f_810(rows=5, cols=4)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.iloc[:, 0].tolist(), [49, 33, 38, 27, 17])
        self.assertEqual(df.iloc[:, 1].tolist(), [97, 65, 61, 64, 96])
        self.assertEqual(df.iloc[:, 2].tolist(), [53, 62, 45, 17, 12])
    def test_case_3(self):
        df = f_810(min_val=10, max_val=20)
        self.assertEqual(df.iloc[:, 0].tolist(), [16, 10, 18])
        self.assertEqual(df.iloc[:, 1].tolist(), [16, 14, 17])
        
    def test_case_4(self):
        df = f_810(min_val=50, max_val=50)
        self.assertEqual(df.iloc[:, 0].tolist(), [50, 50, 50])
        self.assertEqual(df.iloc[:, 1].tolist(), [50, 50, 50])
    def test_case_5(self):
        df = f_810(rows=0, cols=2)
        self.assertTrue(df.empty)
