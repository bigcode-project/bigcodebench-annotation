import pandas as pd
import random


def f_676(df, item, seed):
    """
    Find the locations of a particular item in a pandas DataFrame.
    Counts the number of occurences and adds a random integer x, where 0 <=x < 10, to it.

    Parameters:
    df (DataFrame): The DataFrame to search.
    item (str): The item to find.
    seed(int): seed for random number generation.

    Returns:
    list: A list of tuples. Each tuple contains the row-index and column-name where the item is found.
    int: The number of occurences with the added random number.

    Requirements:
    - pandas
    - random

    Example:
    >>> df = pd.DataFrame({'A': ['apple', 'banana'], 'B': ['orange', 'apple']})
    >>> f_676(df, 'apple', seed=12)
    ([(0, 'A'), (1, 'B')], 9)

    >>> df = pd.DataFrame({'A': ['a', 'b', 'e'], 'B': ['c', 'd', 'd'], '2': ['asdf', 'ddd', 'aaaa'], '12': ['e', 'e', 'd']})
    >>> f_676(df, 'e', seed=2)
    ([(2, 'A'), (0, '12'), (1, '12')], 3)
    """
    random.seed(seed)
    random_int = random.randint(0, 9)
    positions = [(index, col) for col in df for index, val in enumerate(df[col]) if val == item]
    return positions, len(positions) + random_int 

import unittest
import pandas as pd
from faker import Faker

fake = Faker()

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Simple DataFrame
        df = pd.DataFrame({'A': ['apple', 'banana'], 'B': ['orange', 'apple']})
        result, count = f_676(df, 'apple', 2222)
        expected_result = [(0, 'A'), (1, 'B')]
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 5)

    def test_case_2(self):
        # No occurrence of the item
        df = pd.DataFrame({'A': ['orange', 'banana'], 'B': ['orange', 'banana']})
        result, count = f_676(df, 'apple', seed=12)
        expected_result = []
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 7)
  
    def test_case_3(self):
        # Larger DataFrame
        fake.random.seed(111)
        df = pd.DataFrame({
            'A': [fake.random_element(elements=('apple', 'banana', 'orange')) for _ in range(10)],
            'B': [fake.random_element(elements=('apple', 'banana', 'orange')) for _ in range(10)],
            'C': [fake.random_element(elements=('apple', 'banana', 'orange')) for _ in range(10)]
        })
        result, count = f_676(df, 'apple', seed=22)
        expected_result = [(index, col) for col in df for index, val in enumerate(df[col]) if val == 'apple']
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 10)
    
    def test_case_4(self):
        # Empty DataFrame
        df = pd.DataFrame()
        result, count = f_676(df, 'apple', seed=112)
        expected_result = []
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 7)

    def test_case_5(self):
        # DataFrame with non-string values
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [2, 3, 4, 5, 6]
        })
        result, count = f_676(df, 3, seed=32)
        expected_result = [(2, 'A'), (1, 'B')]
        self.assertCountEqual(result, expected_result)
        self.assertEqual(count, 3)
if __name__ == "__main__":
    run_tests()