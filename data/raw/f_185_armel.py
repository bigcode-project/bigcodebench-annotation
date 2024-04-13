import pandas as pd
from itertools import zip_longest
import seaborn as sns
import matplotlib.pyplot as plt

def f_185(l1, l2):
    """
    Combine two lists by alternating their elements and create a DataFrame. 
    Additionally, visualize the distribution of the first column's values in the DataFrame using a histogram.
    
    Parameters:
    l1 (list): The first list.
    l2 (list): The second list.
    
    Returns:
    tuple: A tuple containing:
        - pandas.DataFrame: A pandas DataFrame with combined data from l1 and l2. The dataframe should have one column which name is 'a'.
        - Axes: A histogram plot showing the distribution of the first column's values.
    
    Requirements:
    - pandas
    - itertools
    - seaborn
    - matplotlib
    
    Example:
    >>> l1 = list(range(10))
    >>> l2 = list(range(10, 20))
    >>> df, ax = f_185(l1, l2)
    >>> plt.show()
    """
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    df = pd.DataFrame(combined, columns=["a"])
    plt.figure()
    ax = sns.histplot(df["a"])
    return df, ax

import unittest
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_185 function."""
    def test_case_1(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [6, 7, 8, 9, 10]
        df, ax = f_185(l1, l2)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), len(l1) + len(l2))
        self.assertEqual(list(df['a']), [1, 6, 2, 7, 3, 8, 4, 9, 5, 10])
    
    def test_case_2(self):
        l1 = [1, 2, 3, 4, 5, 11, 12]
        l2 = [6, 7, 8, 9, 10]
        df, ax = f_185(l1, l2)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), len(l1) + len(l2))
        self.assertEqual(list(df['a']), [1, 6, 2, 7, 3, 8, 4, 9, 5, 10, 11, 12])
    
    def test_case_3(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6, 7, 8, 9, 10]
        df, ax = f_185(l1, l2)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), len(l1) + len(l2))
        self.assertEqual(list(df['a']), [1, 4, 2, 5, 3, 6, 7, 8, 9, 10])
    
    def test_case_4(self):
        l1 = []
        l2 = [1, 2, 3]
        df, ax = f_185(l1, l2)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), len(l2))
        self.assertEqual(list(df['a']), [1, 2, 3])
    
    def test_case_5(self):
        l1 = [1, 2, 3]
        l2 = []
        df, ax = f_185(l1, l2)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), len(l1))
        self.assertEqual(list(df['a']), [1, 2, 3])

if __name__ == "__main__" :
    run_tests()