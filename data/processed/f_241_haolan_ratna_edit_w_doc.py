import pandas as pd
from sklearn.preprocessing import LabelEncoder

def f_311(df, dct, columns=None):
    """
    This function preprocesses a pandas DataFrame by replacing specified values, encoding categorical attributes, 
    and standardizing numerical attributes. It's designed to be flexible for data preprocessing in machine learning tasks.

    Parameters:
    - df (DataFrame): The input DataFrame to be preprocessed.
    - dct (dict): A dictionary for replacing values in the DataFrame. Keys are existing values, and values are new values.
    - columns (list of str, optional): Specific column names to be encoded. If None, all object-type columns in the DataFrame are encoded.

    Returns:
    - DataFrame: The preprocessed DataFrame with encoded categorical attributes and standardized numerical attributes.

    Requirements:
    - pandas
    - sklearn.preprocessing.LabelEncoder

    Example:
    >>> df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1, 2, 3]})
    >>> dct = {'a': 'x', 'b': 'y'}
    >>> result = f_311(df, dct)
    >>> result.shape == df.shape
    True
    >>> result['col1'].mean() == 0.0
    True

    Note:
    - The function assumes that the DataFrame and the dictionary are well-formed and relevant to each other.
    - The encoding of categorical columns is done using LabelEncoder, which encodes labels with value between 0 and n_classes-1.
    - Numerical standardization is performed by subtracting the mean and dividing by the standard deviation of each column.

    Raises:
    - The function will raise a ValueError is input df is not a DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    df = df.replace(dct)
    if columns is None:
        columns = df.select_dtypes(include=['object']).columns.tolist()
    for column in columns:
        if df[column].dtype == 'object':
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
    df = (df - df.mean()) / df.std()
    return df

import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with a mix of categorical and numerical columns
        df = pd.DataFrame({'cat': ['a', 'b', 'c'], 'num': [1, 2, 3]})
        dct = {'a': 'x', 'b': 'y', 'c': 'z'}
        result = f_311(df, dct)
        # Assertions
        self.assertEqual(result.shape, df.shape)
        self.assertTrue('cat' in result.columns)
        self.assertTrue('num' in result.columns)
    def test_case_2(self):
        # Testing with only numerical columns
        df = pd.DataFrame({'num1': [10, 20, 30], 'num2': [40, 50, 60]})
        dct = {}
        result = f_311(df, dct)
        # Assertions
        self.assertEqual(result.shape, df.shape)
        self.assertAlmostEqual(result['num1'].mean(), 0, places=5)
        self.assertAlmostEqual(result['num2'].mean(), 0, places=5)
    def test_case_3(self):
        # Testing with only categorical columns
        df = pd.DataFrame({'cat1': ['u', 'v', 'w'], 'cat2': ['x', 'y', 'z']})
        dct = {'u': 'a', 'v': 'b', 'w': 'c', 'x': 'd', 'y': 'e', 'z': 'f'}
        result = f_311(df, dct)
        # Assertions
        self.assertEqual(result.shape, df.shape)
        self.assertIn(result['cat1'].dtype, [np.float64])
        self.assertIn(result['cat2'].dtype, [np.float64])
    def test_case_4(self):
        # Testing with an empty DataFrame
        df = pd.DataFrame({})
        dct = {}
        result = f_311(df, dct)
        # Assertions
        self.assertEqual(result.empty, True)
    def test_case_5(self):
        # Testing with complex DataFrame and no changes through dictionary
        df = pd.DataFrame({'num': [100, 200, 300], 'cat': ['alpha', 'beta', 'gamma']})
        dct = {'delta': 400}
        result = f_311(df, dct)
        # Assertions
        self.assertEqual(result.shape, df.shape)
        self.assertAlmostEqual(result['num'].std(), 1, places=5)
        self.assertIn(result['cat'].dtype, [np.float64])
    
    def test_case_6(self):
        with self.assertRaises(ValueError):
            f_311("non_df", {})
