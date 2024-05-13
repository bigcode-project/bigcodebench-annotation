import pandas as pd
from sklearn.preprocessing import StandardScaler


def task_func(tuples_list, columns):
    """
    Convert a list of tuples into a Pandas DataFrame, perform a default scaling in each column, and return the transformed DataFrame.
    
    Parameters:
    - tuples_list (list): The list of tuples.
    - columns (list): The list of column names.
    
    Returns:
    - df_scaled (DataFrame): A pandas DataFrame containing the scaled versions of the original data.

    Requirements:
    - pandas
    - sklearn
    
    Example:
    >>> df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
    >>> print(df)
              A         B         C         D
    0 -1.224745 -1.224745 -1.224745 -1.224745
    1  0.000000  0.000000  0.000000  0.000000
    2  1.224745  1.224745  1.224745  1.224745
    """

    df = pd.DataFrame(tuples_list, columns=columns)
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df_scaled

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['A'].tolist(), [-1.224744871391589, 0.0, 1.224744871391589])
    def test_case_2(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['B'].tolist(), [-1.224744871391589, 0.0, 1.224744871391589])
    def test_case_3(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['C'].tolist(), [-1.224744871391589, 0.0, 1.224744871391589])
    def test_case_4(self):
        df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['D'].tolist(), [-1.224744871391589, 0.0, 1.224744871391589])
    def test_case_5(self):
        df = task_func([(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], ['A', 'B', 'C', 'D'])
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df.columns.tolist(), ['A', 'B', 'C', 'D'])
        self.assertEqual(df['A'].tolist(), [0.0, 0.0, 0.0])
