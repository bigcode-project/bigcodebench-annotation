import pandas as pd
from itertools import combinations

# Constants
MIN_PERCENTAGE = 0.75

def f_724(data, cols, percentage):
    """
    Find all combinations of columns from a given DataFrame so that the absolute correlation between them is greater than a certain threshold.

    Parameters:
    - data (list): List of lists with the data, where the length of the inner list equals the number of columns
    - cols (list): List of column names
    - percentage (float): The threshold for the absolute correlation.

    Returns:
    - corr_combinations (list): A list of tuples where each tuple contains two column names.

    Requirements:
    - pandas
    - itertools

    Example:
    >>> result = f_724([[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]], ['x', 'y', 'z'], 0.9)
    >>> print(result)
    [('x', 'y')]
    """
    if not 0 <= percentage <= 1:
        raise ValueError('Percentage must be between 0 and 1')
    df = pd.DataFrame(data, columns=cols)
    corr_matrix = df.corr().abs()
    columns = corr_matrix.columns
    corr_combinations = []
    for col1, col2 in combinations(columns, 2):
        if corr_matrix.loc[col1, col2] > percentage:
            corr_combinations.append((col1, col2))
    return corr_combinations

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(f_724([[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]], ['x', 'y', 'z'], 0.9), [('x', 'y')])
    def test_case_2(self):
        self.assertEqual(f_724([[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]], ['x', 'y', 'z'], 0.5), [('x', 'y'), ('x', 'z'), ('y', 'z')])
    def test_case_3(self):
        self.assertEqual(f_724([[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]], ['x', 'y', 'z'], 0.1), [('x', 'y'), ('x', 'z'), ('y', 'z')])
    def test_case_4(self):
        self.assertEqual(f_724([[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]], ['x', 'y', 'z'], 0.0), [('x', 'y'), ('x', 'z'), ('y', 'z')])
    def test_case_5(self):
        self.assertEqual(f_724([[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]], ['x', 'y', 'z'], 1.0), [])
