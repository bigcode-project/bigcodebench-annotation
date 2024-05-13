import pandas as pd
import random

def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    """
    Create a Pandas DataFrame from a list of tuples, each representing a row.
    Tuples of unequal lengths are allowed, and missing elements are filled with None.
    Optionally, missing numeric values can be filled with random data.

    Parameters:
    data (list of tuples): Each tuple contains the data for each row.
                           Elements in tuples represent values corresponding to the columns parameter.
    columns (list of str): List of column names for the DataFrame.
                           Defaults to ['Name', 'Age', 'Occupation'].
    fill_missing (bool): If True, fill missing numeric values with random data.
                         Defaults to False.
    num_range (tuple): Range (min, max) of random numbers for filling missing values.
                       Defaults to (0, 100).
    seed (int): Optional seed for random number generator for reproducibility.
                Defaults to None.

    Returns:
    DataFrame: A pandas DataFrame with specified columns.
               Missing elements are represented as None or filled with random data.

    Requirements:
    - pandas
    - random

    Example:
    >>> data = [('John', 25, 'Engineer'), ('Alice', ), ('Bob', )]
    >>> df = task_func(data, fill_missing=True, num_range=(0, 10), seed=42)
    >>> print(df)
        Name   Age Occupation
    0   John  25.0   Engineer
    1  Alice  10.0       None
    2    Bob   1.0       None

    >>> data = [('Mango', 20), ('Apple', ), ('Banana', )]
    >>> df = task_func(data, columns=['Fruit', 'Quantity'], fill_missing=False, seed=42)
    >>> print(df)
        Fruit  Quantity
    0   Mango      20.0
    1   Apple       NaN
    2  Banana       NaN
    """

    if seed is not None:
        random.seed(seed)
    df = pd.DataFrame(data, columns=columns)
    if fill_missing:
        for col in df.columns:
            if df[col].dtype in ['float64', 'int64']:
                df[col] = df[col].apply(lambda x: random.randint(*num_range) if pd.isnull(x) else x)
    return df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_basic_functionality(self):
        # Testing basic functionality with complete data for each column
        data = [('John', 25, 'Engineer'), ('Alice', 30, 'Doctor')]
        df = task_func(data)
        expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_uneven_tuples(self):
        # Handling tuples of uneven length, missing elements should be filled with None
        data = [('John', 25, 'Engineer'), ('Alice', 30, 'Doctor'), ('Bob', )]
        df = task_func(data)
        expected_df = pd.DataFrame([['John', 25, 'Engineer'], ['Alice', 30, 'Doctor'], ['Bob', None, None]], columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_custom_columns(self):
        # Specifying custom column names
        data = [('Mango', 20), ('Apple', 30)]
        df = task_func(data, columns=['Fruit', 'Quantity'])
        expected_df = pd.DataFrame(data, columns=['Fruit', 'Quantity'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_empty_list(self):
        # Providing an empty list, resulting in an empty DataFrame with only the specified columns
        data = []
        df = task_func(data)
        expected_df = pd.DataFrame(columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_all_none(self):
        # All elements missing for a particular record
        data = [('John', 25, 'Engineer'), (None, None, None)]
        df = task_func(data)
        expected_df = pd.DataFrame([['John', 25, 'Engineer'], [None, None, None]], columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(df, expected_df)
    def test_random_fill(self):
        # Testing random data filling functionality
        data = [('John', 25, None), (None, None, None)]
        df = task_func(data, fill_missing=True, num_range=(1, 100), seed=42)
        # Check if missing values are filled and if the filled values are within the specified range
        self.assertTrue(df.loc[0, 'Occupation'] is None)
        self.assertTrue(df.loc[1, 'Name'] is None)
        self.assertTrue(df.loc[1, 'Age'] is not None and 1 <= df.loc[1, 'Age'] <= 100)
    def test_seed_reproducibility(self):
        # Testing if the seed parameter provides reproducible results
        data = [('John', None, None)]
        df1 = task_func(data, fill_missing=True, num_range=(1, 100), seed=42)
        df2 = task_func(data, fill_missing=True, num_range=(1, 100), seed=42)
        pd.testing.assert_frame_equal(df1, df2)
