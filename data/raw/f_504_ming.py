import re
import pandas as pd
import numpy as np

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

def f_504(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Extract numeric data from a Pandas DataFrame based on a specific pattern. The function searches 
    each cell for occurrences of the regex pattern '>number<number>' (e.g., '>1.23<') and replaces 
    the cell content with the extracted numeric value. If no match is found, the cell is replaced with NaN.
    
    Parameters:
    - dataframe (pd.DataFrame): A pandas DataFrame containing data to be processed.
    
    Returns:
    - pd.DataFrame: A modified DataFrame with cells containing the extracted numeric values or NaN.
    
    Requirements:
    - Libraries: re, pandas, numpy.
    
    Example:
    >>> df = pd.DataFrame({'A': ['>1.23<', '>4.56<'], 'B': ['>7.89<', '>0.12<']})
    >>> f_504(df)
       A     B
    0  1.23  7.89
    1  4.56  0.12
    """
    for col in dataframe.columns:
        dataframe[col] = dataframe[col].apply(lambda x: float(re.search(DATA_PATTERN, x).group(0)[1:-1]) 
                                              if pd.notnull(x) and re.search(DATA_PATTERN, x) else np.nan)
    return dataframe

import unittest
import pandas as pd
import numpy as np

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        df = pd.DataFrame({'A': ['>1.23<', '>4.56<'], 'B': ['>7.89<', '>0.12<']})
        result = f_504(df)
        expected = pd.DataFrame({'A': [1.23, 4.56], 'B': [7.89, 0.12]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_case_2(self):
        df = pd.DataFrame({'A': ['1.23', '4.56'], 'B': ['7.89', '0.12']})
        result = f_504(df)
        expected = pd.DataFrame({'A': [np.nan, np.nan], 'B': [np.nan, np.nan]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_case_3(self):
        df = pd.DataFrame({'A': ['>1.23<', '4.56'], 'B': ['>7.89<', '0.12']})
        result = f_504(df)
        expected = pd.DataFrame({'A': [1.23, np.nan], 'B': [7.89, np.nan]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_case_4(self):
        df = pd.DataFrame({'A': ['>1.23<', None], 'B': [None, '>0.12<']})
        result = f_504(df)
        expected = pd.DataFrame({'A': [1.23, np.nan], 'B': [np.nan, 0.12]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_case_5(self):
        df = pd.DataFrame()
        result = f_504(df)
        expected = pd.DataFrame()
        pd.testing.assert_frame_equal(result, expected)

if __name__ == "__main__":
    run_tests()