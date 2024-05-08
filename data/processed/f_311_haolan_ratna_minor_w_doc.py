import pandas as pd
import numpy as np

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def f_255(length):
    """
    Generate a Pandas DataFrame with specified length and random data and then record the data.

    Parameters:
    length (int): The length of the DataFrame to be generated.

    Returns:
    DataFrame: A pandas DataFrame with random data.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> np.random.seed(0)
    >>> df = f_255(5)
    >>> df.shape
    (5, 5)
    """
    data = np.random.randint(0,100,size=(length, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)
    return df

import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Testing basic functionality
        np.random.seed(0)
        df = f_255(5)
        self.assertIsInstance(df, pd.DataFrame, "Output should be a DataFrame.")
        self.assertEqual(df.shape, (5, 5), "DataFrame shape mismatch.")
        
    def test_case_2(self):
        # Testing custom columns
        np.random.seed(0)
        custom_columns = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
        df = f_255(3)
        self.assertListEqual(list(df.columns), custom_columns, "Column names mismatch.")
        
    def test_case_3(self):
        # Testing return plot
        np.random.seed(0)
        df = f_255(4)
        self.assertIsInstance(df, pd.DataFrame, "Output should be a DataFrame.")
        
    def test_case_4(self):
        # Testing data range
        np.random.seed(0)
        df = f_255(10)
        self.assertTrue((df.values >= 0).all() and (df.values < 100).all(), "Data values should be between 0 and 99.")
        
    def test_case_5(self):
        # Testing default columns
        np.random.seed(0)
        df = f_255(7)
        default_columns = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
        self.assertListEqual(list(df.columns), default_columns, "Default column names mismatch.")
