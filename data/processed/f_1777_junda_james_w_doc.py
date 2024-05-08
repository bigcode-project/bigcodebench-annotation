import pandas as pd
from scipy.stats import skew

def f_95(df):
    """
    Calculate the skewness of the last column of the dataframe.

    Parameters:
    df (DataFrame): The input dataframe.

    Returns:
    float: The skewness of the last column of the dataframe.

    Raises:
    ValueError: If the input is not a DataFrame or has no columns.

    Requirements:
    - pandas
    - scipy.stats
    
    Example:
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
    >>> skewness = f_95(df)
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty pandas DataFrame.")
    last_col = df.columns[-1]
    skewness = skew(df[last_col].dropna())  # dropna() to handle NaN values
    return skewness

import unittest
import numpy as np
import pandas as pd 
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    def test_skewness_calculation(self):
        skewness = f_95(self.df)
        # print(skewness)
        self.assertIsInstance(skewness, float)
        self.assertAlmostEqual(-0.1670862308059806, skewness)
    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            f_95("not a dataframe")
    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_95(pd.DataFrame())
    def test_with_nan_values(self):
        self.df.iloc[::10, -1] = np.nan
        skewness = f_95(self.df)
        self.assertIsInstance(skewness, float)
    def test_single_column_df(self):
        df_single_col = pd.DataFrame(self.df.iloc[:, 0])
        skewness = f_95(df_single_col)
        self.assertIsInstance(skewness, float)
