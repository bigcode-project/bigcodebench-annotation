import pandas as pd
import numpy as np
import itertools

def task_func(T1, row_num=50, seed=None):
    """
    Convert elements in 'T1' to integers and create a Pandas DataFrame with random numbers. 
    The number of columns in the DataFrame is determined by the sum of the integers in 'T1', 
    and the number of rows is defined by the 'row_num' parameter.

    Parameters:
    T1 (tuple): A tuple of tuples, each containing string representations of integers.
    row_num (int, optional): Number of rows for the DataFrame. Defaults to 50.
    seed (int, optional): Seed for random number generation. Defaults to None.

    Returns:
    DataFrame: A pandas DataFrame with random numbers.

    Requirements:
    - pandas
    - numpy
    - itertools

    Example:
    >>> T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
    >>> df = task_func(T1, row_num=5, seed=2022)
    >>> print(df)
       Col_1  Col_2  Col_3  Col_4  ...  Col_222  Col_223  Col_224  Col_225
    0     92     45     49     55  ...        6       60       45       99
    1     51     17     38     83  ...       63       86       82       59
    2     27     64     73     92  ...       39       25       91       95
    3     52     40     35     22  ...       71       34       52       13
    4     54      1     79     61  ...       41       78       97       27
    <BLANKLINE>
    [5 rows x 225 columns]

    >>> df = task_func(('1', ('1', '3')), row_num=2, seed=32)
    >>> print(df)
       Col_1  Col_2  Col_3  Col_4  Col_5
    0     87     43      5     54     62
    1     88     19     71     89      3

    >>> T1 = (('1', '12'), ('1', '-12'))
    >>> df = task_func(T1, row_num=6, seed=21)
    >>> print(df)
       Col_1  Col_2
    0     73     79
    1     56      4
    2     48     35
    3     60     98
    4     74     72
    5     63     44
    """

    np.random.seed(seed)
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_cols = sum(flattened_list)
    data = np.random.randint(0, 100, size=(row_num, total_cols))
    df = pd.DataFrame(data, columns=[f'Col_{i+1}' for i in range(total_cols)])
    return df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_rng(self):
        T1 = (('13', '17', '18', '21', '32'))
        df1 = task_func(T1, row_num=50, seed=2022)
        df2 = task_func(T1, row_num=50, seed=2022)
        pd.testing.assert_frame_equal(df1, df2)
        df4 = task_func(T1, row_num=50, seed=12)
        try:
            pd.testing.assert_frame_equal(df1, df4)
        except AssertionError:
            pass
        else:
            raise AssertionError('frames are equal but should not be')
    def test_case_1(self):
        T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
        df = task_func(T1, row_num=50, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, sum([13, 17, 18, 21, 32, 7, 11, 13, 14, 28, 1, 5, 6, 8, 15, 16])))
    def test_case_2(self):
        T1 = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'))
        df = task_func(T1, row_num=50, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, sum([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    def test_case_3(self):
        T1 = (('10', '20', '30'), ('40', '50', '60'), ('70', '80', '90'))
        df = task_func(T1, row_num=70, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (70, sum([10, 20, 30, 40, 50, 60, 70, 80, 90])))
    def test_case_4(self):
        T1 = ()
        df = task_func(T1, row_num=50, seed=2022)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, 0))
    def test_case_5(self):
        T1 = (('1', '2', '3'), (), ('7', '8', '9'))
        df = task_func(T1, row_num=50, seed=21)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (50, sum([1, 2, 3, 7, 8, 9])))
    def test_non_int(self):
        a = (('1', '2.45'))
        self.assertRaises(Exception, task_func, a, 120, 21)
