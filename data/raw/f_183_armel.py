import pandas as pd
import numpy as np
from itertools import zip_longest

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def f_183(l1, l2, seed):
    '''
    Create a DataFrame using two input lists by alternating their elements and assign a random category for each row. The set of possible category is
    stored in the constant CATEGORIES.
    
    Parameters:
    - l1 (list): The first list.
    - l2 (list): The second list.
    - seed (int) : Seed to initialize the random number generator with.

    Returns:
    DataFrame: A pandas DataFrame with combined data from l1 and l2 and random categories. The dataframe should have 2 column, 'Value' and 'Category'.
    
    Requirements:
    - pandas
    - numpy
    - itertools
    
    Example:
    >>> l1 = list(range(10))
    >>> l2 = list(range(10, 20))
    >>> df = f_183(l1, l2)
    >>> print(df)
    >>> df['Category'].value_counts().plot(kind='bar')
    '''
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    rng = np.random.default_rng(seed)
    categories = rng.choice(CATEGORIES, len(combined))
    df = pd.DataFrame.from_dict({'Value': combined, 'Category': categories})
    return df

import unittest
import pandas as pd


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_183 function."""
    def setUp(self):
        self.seed = 122

    def test_case_1(self):
        l1 = list(range(10))
        l2 = list(range(10, 20))
        df = f_183(l1, l2, self.seed)
        
        # Asserting the shape of the returned DataFrame
        self.assertEqual(df.shape, (20, 2))
        
        # Asserting the columns of the dataframe are 'Value' and 'Category'
        self.assertEqual(list(df.columns.values), ['Value', 'Category'])
        
        # Asserting the values in the 'Value' column of the DataFrame
        self.assertEqual(list(df['Value']), [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19])
        
        # Asserting that the 'Category' column only contains values from CATEGORIES
        self.assertTrue(set(df['Category']).issubset(set(['A', 'B', 'C', 'D', 'E'])))

    def test_case_2(self):
        l1 = []
        l2 = list(range(5))
        df = f_183(l1, l2, self.seed)
        
        # Asserting the shape of the returned DataFrame
        self.assertEqual(df.shape, (5, 2))
        
        # Asserting the values in the 'Value' column of the DataFrame
        self.assertEqual(list(df['Value']), [0, 1, 2, 3, 4])
        
        # Asserting that the 'Category' column only contains values from CATEGORIES
        self.assertTrue(set(df['Category']).issubset(set(['A', 'B', 'C', 'D', 'E'])))

    def test_case_3(self):
        l1 = list(range(5))
        l2 = []
        df = f_183(l1, l2, self.seed)
        
        # Asserting the shape of the returned DataFrame
        self.assertEqual(df.shape, (5, 2))
        
        # Asserting the values in the 'Value' column of the DataFrame
        self.assertEqual(list(df['Value']), [0, 1, 2, 3, 4])
        
        # Asserting that the 'Category' column only contains values from CATEGORIES
        self.assertTrue(set(df['Category']).issubset(set(['A', 'B', 'C', 'D', 'E'])))

    def test_case_4(self):
        l1 = []
        l2 = []
        df = f_183(l1, l2, self.seed)
        
        # Asserting the shape of the returned DataFrame
        self.assertEqual(df.shape, (0, 2))

    def test_case_5(self):
        l1 = list(range(3))
        l2 = list(range(5, 8))
        df = f_183(l1, l2, self.seed)
        
        # Asserting the shape of the returned DataFrame
        self.assertEqual(df.shape, (6, 2))
        
        # Asserting the values in the 'Value' column of the DataFrame
        self.assertEqual(list(df['Value']), [0, 5, 1, 6, 2, 7])
        
        # Asserting that the 'Category' column only contains values from CATEGORIES
        self.assertTrue(set(df['Category']).issubset(set(['A', 'B', 'C', 'D', 'E'])))

if __name__ == "__main__" :
    run_tests()