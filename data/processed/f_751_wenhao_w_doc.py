import pandas as pd
import itertools
from random import shuffle

def f_521(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    """
    Create a Pandas DataFrame by associating each element from a list of letters to a category from a list of categories.
    The categories are randomly shuffled.

    Parameters:
    letters (List[str]): A list of letters to be included in the DataFrame. Default is ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'].
    categories (List[str]): A list of categories to be included in the DataFrame. Default is ['Category 1', 'Category 2', 'Category 3'].

    Returns:
    DataFrame: A Pandas DataFrame with two columns: 'Letter' and 'Category'. Each letter is randomly associated with a category.

    Requirements:
    - pandas
    - itertools
    - random.shuffle

    Example:
    >>> import random
    >>> random.seed(0)
    >>> df = f_521(['A', 'B'], ['Cat 1', 'Cat 2'])
    >>> print(df)
      Letter Category
    0      A    Cat 2
    1      B    Cat 1
    2      A    Cat 1
    3      B    Cat 2
    >>> random.seed(1)
    >>> df = f_521()
    >>> print(df.head())
      Letter    Category
    0      A  Category 3
    1      B  Category 3
    2      C  Category 2
    3      D  Category 2
    4      E  Category 3
    """
    
    flattened_list = list(itertools.chain(*[letters for _ in range(len(categories))]))
    expanded_categories = list(itertools.chain(*[[category] * len(letters) for category in categories]))
    shuffle(expanded_categories)

    df = pd.DataFrame({'Letter': flattened_list, 'Category': expanded_categories})

    return df

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with default parameters
        df = f_521()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 27)  # 9 letters * 3 categories
    def test_case_2(self):
        # Testing with custom parameters
        df = f_521(['X', 'Y'], ['Cat 1'])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 2)  # 2 letters * 1 category
    def test_case_3(self):
        # Testing with empty categories list
        df = f_521(['X', 'Y'], [])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)  # 2 letters * 0 categories
    def test_case_4(self):
        # Testing with empty letters list
        df = f_521([], ['Cat 1', 'Cat 2'])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)  # 0 letters * 2 categories
    def test_case_5(self):
        # Testing with both empty lists
        df = f_521([], [])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)  # 0 letters * 0 categories
