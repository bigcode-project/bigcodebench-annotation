import numpy as np
import pandas as pd

def f_792(rows, columns, seed=None):
    """
    Generate a DataFrame with random values within a specified range.
    
    This function creates a matrix of given dimensions filled with random values between 0 and 1 and returns it as a Pandas DataFrame. Users have the option to set a random seed for reproducible results.
    
    Parameters:
    - rows (int): The number of rows for the matrix.
    - columns (int): The number of columns for the matrix.
    - seed (int, optional): The seed for the random number generator. Default is None.
    
    Returns:
    - DataFrame: A Pandas DataFrame containing the generated random values.
    
    Examples:
    >>> df = f_792(3, 2, seed=42)
    >>> print(df.shape)
    (3, 2)
    
    >>> df = f_792(1, 1, seed=24)
    >>> print(df.shape)
    (1, 1)
    """
    if seed is not None:
        np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    df = pd.DataFrame(matrix)
    
    return df

import unittest

class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.seed = 42

    def test_case_1(self):
        df = f_792(3, 2, seed=self.seed)
        self.assertEqual(df.shape, (3, 2))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())
        
    def test_case_2(self):
        df = f_792(5, 5, seed=self.seed)
        self.assertEqual(df.shape, (5, 5))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())
        
    def test_case_3(self):
        df = f_792(1, 1, seed=self.seed)
        self.assertEqual(df.shape, (1, 1))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())
        
    def test_case_4(self):
        df = f_792(4, 3, seed=self.seed)
        self.assertEqual(df.shape, (4, 3))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())
        
    def test_case_5(self):
        df = f_792(2, 2, seed=self.seed)
        self.assertEqual(df.shape, (2, 2))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
