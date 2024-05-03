import pandas as pd


def f_676(df, item):
    """
    Find the locations of a particular item in a pandas DataFrame.

    Parameters:
    df (DataFrame): The DataFrame to search.
    item (str): The item to find.

    Returns:
    list: A list of tuples. Each tuple contains the row-index and column-name where the item is found.

    Requirements:
    - pandas

    Example:
    >>> df = pd.DataFrame({'A': ['apple', 'banana'], 'B': ['orange', 'apple']})
    >>> f_676(df, 'apple')
    [(0, 'A'), (1, 'B')]
    """
    positions = [(index, col) for col in df for index, val in enumerate(df[col]) if val == item]
    return positions

import unittest
import pandas as pd
from faker import Faker
fake = Faker()
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Simple DataFrame
        df = pd.DataFrame({'A': ['apple', 'banana'], 'B': ['orange', 'apple']})
        result = f_676(df, 'apple')
        expected_result = [(0, 'A'), (1, 'B')]
        self.assertCountEqual(result, expected_result)
    
    def test_case_2(self):
        # No occurrence of the item
        df = pd.DataFrame({'A': ['orange', 'banana'], 'B': ['orange', 'banana']})
        result = f_676(df, 'apple')
        expected_result = []
        self.assertCountEqual(result, expected_result)
    
    def test_case_3(self):
        # Larger DataFrame
        df = pd.DataFrame({
            'A': [fake.random_element(elements=('apple', 'banana', 'orange')) for _ in range(10)],
            'B': [fake.random_element(elements=('apple', 'banana', 'orange')) for _ in range(10)],
            'C': [fake.random_element(elements=('apple', 'banana', 'orange')) for _ in range(10)]
        })
        result = f_676(df, 'apple')
        expected_result = [(index, col) for col in df for index, val in enumerate(df[col]) if val == 'apple']
        self.assertCountEqual(result, expected_result)
    
    def test_case_4(self):
        # Empty DataFrame
        df = pd.DataFrame()
        result = f_676(df, 'apple')
        expected_result = []
        self.assertCountEqual(result, expected_result)
    
    def test_case_5(self):
        # DataFrame with non-string values
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [2, 3, 4, 5, 6]
        })
        result = f_676(df, 3)
        expected_result = [(2, 'A'), (1, 'B')]
        self.assertCountEqual(result, expected_result)
