import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def f_763(df, columns):
    """
    Normalizes specified columns of a DataFrame using min-max scaling.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing numerical data.
    columns (list of str): A list of column names to be normalized.

    Returns:
    pandas.DataFrame: A new DataFrame with the specified columns normalized between 0 and 1.

    Requirements:
    - pandas for DataFrame operations
    - sklearn.preprocessing for MinMaxScaler

    Constants:
    - A MinMaxScaler object from sklearn.preprocessing is used internally for scaling.

    Example:
    >>> df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    >>> normalized_df = f_763(df, ['a', 'b'])
    >>> print(normalized_df)
         a    b
    0  0.0  0.0
    1  0.5  0.5
    2  1.0  1.0
    """
    # Create a local MinMaxScaler object
    scaler = MinMaxScaler()
    
    # Create a copy of the DataFrame to avoid modifying the original DataFrame
    df_copy = df.copy()

    # Normalize the specified columns
    df_copy[columns] = scaler.fit_transform(df_copy[columns])

    return df_copy

import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from sklearn.preprocessing import MinMaxScaler
import sys

# Import the function f_763 from the refined_function.py file
sys.path.append('/mnt/data/')

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input: DataFrame with two columns 'a' and 'b' with integer values
        # Output: DataFrame with 'a' and 'b' normalized
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        expected_df = pd.DataFrame({'a': [0.0, 0.5, 1.0], 'b': [0.0, 0.5, 1.0]})
        result_df = f_763(df, ['a', 'b'])
        assert_frame_equal(expected_df, result_df)

    def test_case_2(self):
        # Input: DataFrame with one column 'x' with float values
        # Output: DataFrame with 'x' normalized
        df = pd.DataFrame({'x': [1.1, 2.2, 3.3]})
        expected_df = pd.DataFrame({'x': [0.0, 0.5, 1.0]})
        result_df = f_763(df, ['x'])
        assert_frame_equal(expected_df, result_df)

    def test_case_3(self):
        # Input: DataFrame with multiple columns, but only one column 'y' to normalize
        # Output: DataFrame with 'y' normalized, other columns unchanged
        df = pd.DataFrame({'y': [10, 20, 30], 'z': [1, 2, 3]})
        expected_df = pd.DataFrame({'y': [0.0, 0.5, 1.0], 'z': [1, 2, 3]})
        result_df = f_763(df, ['y'])
        assert_frame_equal(expected_df, result_df)

    def test_case_4(self):
        # Input: DataFrame with negative numbers in column 'm'
        # Output: DataFrame with 'm' normalized
        df = pd.DataFrame({'m': [-1, 0, 1]})
        expected_df = pd.DataFrame({'m': [0.0, 0.5, 1.0]})
        result_df = f_763(df, ['m'])
        assert_frame_equal(expected_df, result_df)

    def test_case_5(self):
        # Input: DataFrame with all zeros in column 'n'
        # Output: DataFrame with 'n' normalized (all zeros)
        df = pd.DataFrame({'n': [0, 0, 0]})
        expected_df = pd.DataFrame({'n': [0.0, 0.0, 0.0]})
        result_df = f_763(df, ['n'])
        assert_frame_equal(expected_df, result_df)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()