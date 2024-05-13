import math
import pandas as pd

def task_func(tuples_list):
    """
    Given a list of tuples turn them into a Pandas DataFrame with math.sin applied to each number.

    Parameters:
    - tuples_list (list): The list of tuples.
    
    Returns:
    - df (DataFrame): A pandas DataFrame. Each row of df corresponds to a tuple from tuples_list, with the values being the sine of the original values in the tuple.

    Requirements:
    - math
    - pandas

    Example:
    >>> df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])
    >>> print(df)
              0         1         2         3
    0  0.841471  0.909297  0.141120 -0.756802
    1 -0.958924 -0.279415  0.656987  0.989358
    2  0.412118 -0.544021 -0.999990 -0.536573
    """
    df = pd.DataFrame([(math.sin(n) for n in t) for t in tuples_list])
    return df

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.iloc[0, 0], math.sin(1))
        self.assertEqual(df.iloc[0, 1], math.sin(2))
        self.assertEqual(df.iloc[0, 2], math.sin(3))
        self.assertEqual(df.iloc[0, 3], math.sin(4))
        self.assertEqual(df.iloc[1, 0], math.sin(5))
        self.assertEqual(df.iloc[1, 1], math.sin(6))
        self.assertEqual(df.iloc[1, 2], math.sin(7))
        self.assertEqual(df.iloc[1, 3], math.sin(8))
        self.assertEqual(df.iloc[2, 0], math.sin(9))
        self.assertEqual(df.iloc[2, 1], math.sin(10))
        self.assertEqual(df.iloc[2, 2], math.sin(11))
        self.assertEqual(df.iloc[2, 3], math.sin(12))
    def test_case_2(self):
        df = task_func([(1, 2, 3, 4)])
        self.assertEqual(df.shape, (1, 4))
        self.assertEqual(df.iloc[0, 0], math.sin(1))
        self.assertEqual(df.iloc[0, 1], math.sin(2))
        self.assertEqual(df.iloc[0, 2], math.sin(3))
        self.assertEqual(df.iloc[0, 3], math.sin(4))
    def test_case_3(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8)])
        self.assertEqual(df.shape, (2, 4))
        self.assertEqual(df.iloc[0, 0], math.sin(1))
        self.assertEqual(df.iloc[0, 1], math.sin(2))
        self.assertEqual(df.iloc[0, 2], math.sin(3))
        self.assertEqual(df.iloc[0, 3], math.sin(4))
        self.assertEqual(df.iloc[1, 0], math.sin(5))
        self.assertEqual(df.iloc[1, 1], math.sin(6))
        self.assertEqual(df.iloc[1, 2], math.sin(7))
        self.assertEqual(df.iloc[1, 3], math.sin(8))
    def test_case_4(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16)])
        self.assertEqual(df.shape, (4, 4))
        self.assertEqual(df.iloc[0, 0], math.sin(1))
        self.assertEqual(df.iloc[0, 1], math.sin(2))
        self.assertEqual(df.iloc[0, 2], math.sin(3))
        self.assertEqual(df.iloc[0, 3], math.sin(4))
        self.assertEqual(df.iloc[1, 0], math.sin(5))
        self.assertEqual(df.iloc[1, 1], math.sin(6))
        self.assertEqual(df.iloc[1, 2], math.sin(7))
        self.assertEqual(df.iloc[1, 3], math.sin(8))
        self.assertEqual(df.iloc[2, 0], math.sin(9))
        self.assertEqual(df.iloc[2, 1], math.sin(10))
        self.assertEqual(df.iloc[2, 2], math.sin(11))
        self.assertEqual(df.iloc[2, 3], math.sin(12))
        self.assertEqual(df.iloc[3, 0], math.sin(13))
        self.assertEqual(df.iloc[3, 1], math.sin(14))
        self.assertEqual(df.iloc[3, 2], math.sin(15))
        self.assertEqual(df.iloc[3, 3], math.sin(16))
    def test_case_5(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16), (17, 18, 19, 20)])
        self.assertEqual(df.shape, (5, 4))
        self.assertEqual(df.iloc[0, 0], math.sin(1))
        self.assertEqual(df.iloc[0, 1], math.sin(2))
        self.assertEqual(df.iloc[0, 2], math.sin(3))
        self.assertEqual(df.iloc[0, 3], math.sin(4))
        self.assertEqual(df.iloc[1, 0], math.sin(5))
        self.assertEqual(df.iloc[1, 1], math.sin(6))
        self.assertEqual(df.iloc[1, 2], math.sin(7))
        self.assertEqual(df.iloc[1, 3], math.sin(8))
        self.assertEqual(df.iloc[2, 0], math.sin(9))
        self.assertEqual(df.iloc[2, 1], math.sin(10))
        self.assertEqual(df.iloc[2, 2], math.sin(11))
        self.assertEqual(df.iloc[2, 3], math.sin(12))
        self.assertEqual(df.iloc[3, 0], math.sin(13))
        self.assertEqual(df.iloc[3, 1], math.sin(14))
        self.assertEqual(df.iloc[3, 2], math.sin(15))
        self.assertEqual(df.iloc[3, 3], math.sin(16))
        self.assertEqual(df.iloc[4, 0], math.sin(17))
        self.assertEqual(df.iloc[4, 1], math.sin(18))
        self.assertEqual(df.iloc[4, 2], math.sin(19))
        self.assertEqual(df.iloc[4, 3], math.sin(20))
