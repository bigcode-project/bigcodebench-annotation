import pandas as pd
import random


def f_266(dictionary, item, seed):
    """
    Converts a dictionary to a pandas DataFrame and find the locations of a particular item in the resulting DataFrame.
    Counts the number of occurences and adds a random integer x, where 0 <=x < 10, to it.

    Parameters:
    dict (dictionary): The dictionary to search.
    item (str): The item to find.
    seed(int): seed for random number generation.

    Returns:
    list: A list of tuples. Each tuple contains the row-index and column-name where the item is found.
    int: The number of occurences with the added random number.
    DataFrame: The converted dictionary.

    Requirements:
    - pandas
    - random

    Example:
    >>> dict = {'A': ['apple', 'banana'], 'B': ['orange', 'apple']}
    >>> f_266(dict, 'apple', seed=12)
    ([(0, 'A'), (1, 'B')], 9,         A       B
    0   apple  orange
    1  banana   apple)
    
    >>> dict = {'A': ['a', 'b', 'e'], 'B': ['c', 'd', 'd'], '2': ['asdf', 'ddd', 'aaaa'], '12': ['e', 'e', 'd']}
    >>> f_266(dict, 'e', seed=2)
    ([(2, 'A'), (0, '12'), (1, '12')], 3,    A  B     2 12
    0  a  c  asdf  e
    1  b  d   ddd  e
    2  e  d  aaaa  d)
    """
    random.seed(seed)
    random_int = random.randint(0, 9)
    df = pd.DataFrame(dictionary)
    positions = [(index, col) for col in df for index, val in enumerate(df[col]) if val == item]
    return positions, len(positions) + random_int , df

import unittest
import pandas as pd
from faker import Faker
fake = Faker()
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Simple dict
        dictionary = {'A': ['apple', 'banana'], 'B': ['orange', 'apple']}
        result, count, df = f_266(dictionary, 'apple', 2222)
        expected_result = [(0, 'A'), (1, 'B')]
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 5)
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    def test_case_2(self):
        # No occurrence of the item
        dictionary = {'A': ['orange', 'banana'], 'B': ['orange', 'banana']}
        result, count, df = f_266(dictionary, 'apple', seed=12)
        expected_result = []
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 7)
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    def test_case_3(self):
        # Larger dict
        fake.random.seed(111)
        dictionary = {
            'A': [fake.random_element(elements=('apple', 'banana', 'orange')) for _ in range(10)],
            'B': [fake.random_element(elements=('apple', 'banana', 'orange')) for _ in range(10)],
            'C': [fake.random_element(elements=('apple', 'banana', 'orange')) for _ in range(10)]
        }
        result, count, df = f_266(dictionary, 'apple', seed=22)
        expected_result = [(index, col) for col in df for index, val in enumerate(df[col]) if val == 'apple']
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 10)
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    
    def test_case_4(self):
        # Empty dict
        dictionary = {}
        result, count, df = f_266(dictionary, 'apple', seed=112)
        expected_result = []
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 7)
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
    def test_case_5(self):
        # dict with non-string values
        dictionary = {
            'A': [1, 2, 3, 4, 5],
            'B': [2, 3, 4, 5, 6]
        }
        result, count, df = f_266(dictionary, 3, seed=32)
        expected_result = [(2, 'A'), (1, 'B')]
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 3)
        pd.testing.assert_frame_equal(pd.DataFrame(dictionary), df)
