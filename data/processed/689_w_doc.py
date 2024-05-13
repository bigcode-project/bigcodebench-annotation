import numpy as np
from scipy import stats

def task_func(df):
    """
    Given a Pandas DataFrame with random numeric values test if the data in each column is normally distributed using the Shapiro-Wilk test.

    Parameters:
    - df (DataFrame): A Pandas DataFrame with random numeric values.
    
    Returns:
    - dict: A dictionary with p-values from the Shapiro-Wilk test for each column.

    Requirements:
    - numpy
    - scipy

    Example:
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.normal(size=(100, 5)))
    >>> p_values = task_func(df)
    >>> print(p_values)
    {0: 0.3595593273639679, 1: 0.23594242334365845, 2: 0.7625704407691956, 3: 0.481273353099823, 4: 0.13771861791610718}
    """

    p_values = {}
    for col in df.columns:
        column_data = np.array(df[col])
        test_stat, p_value = stats.shapiro(column_data)
        p_values[col] = p_value
    return p_values

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
    
    def test_case_1(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        p_values = task_func(df)
        self.assertEqual(len(p_values), 2)
        self.assertTrue('a' in p_values)
        self.assertTrue('b' in p_values)
        self.assertTrue(p_values['a'] > 0.05)
        self.assertTrue(p_values['b'] > 0.05)
    def test_case_2(self):
        df = pd.DataFrame({'a': [-1, 0, 1], 'b': [4, 5, 6]})
        p_values = task_func(df)
        self.assertEqual(len(p_values), 2)
        self.assertTrue('a' in p_values)
        self.assertTrue('b' in p_values)
        self.assertTrue(p_values['a'] > 0.05)
        self.assertTrue(p_values['b'] > 0.05)
    def test_case_3(self):
        df = pd.DataFrame(np.random.normal(size=(100, 5)))
        p_values = task_func(df)
        self.assertEqual(len(p_values), 5)
        for col in df.columns:
            self.assertTrue(col in p_values)
            self.assertTrue(p_values[col] > 0.05)
    def test_case_4(self):
        df = pd.DataFrame(np.random.normal(size=(100, 5)))
        df['a'] = np.random.uniform(size=100)
        p_values = task_func(df)
        self.assertEqual(len(p_values), 6)
        for col in df.columns:
            self.assertTrue(col in p_values)
            if col == 'a':
                self.assertTrue(p_values[col] < 0.05)
            else:
                self.assertTrue(p_values[col] > 0.05)
    def test_case_5(self):
        df = pd.DataFrame(np.random.normal(size=(100, 5)))
        df['a'] = np.random.uniform(size=100)
        df['b'] = np.random.uniform(size=100)
        p_values = task_func(df)
        self.assertEqual(len(p_values), 7)
        for col in df.columns:
            self.assertTrue(col in p_values)
            if col in ['a', 'b']:
                self.assertTrue(p_values[col] < 0.05)
            else:
                self.assertTrue(p_values[col] > 0.05)
