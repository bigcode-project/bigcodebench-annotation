import pandas as pd
import numpy as np


def task_func(rows=100, columns=3):
    """
    Create a Pandas DataFrame with random alphabets in each cell.
    The DataFrame will have a specified number of rows and columns.
    Each column is named with a string from the list ['a', 'b', 'c', ...]
    depending on the number of columns specified.

    Parameters:
    - rows (int, optional): Number of rows in the DataFrame. Defaults to 100.
    - columns (int, optional): Number of columns in the DataFrame. Defaults to 3.

    Returns:
    DataFrame: A pandas DataFrame with random alphabets.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> np.random.seed(0)
    >>> df = task_func(5, 3)
    >>> print(df)
       a  b  c
    0  m  p  v
    1  a  d  d
    2  h  j  t
    3  v  s  e
    4  x  g  y
    >>> df['a'].value_counts()
    a
    m    1
    a    1
    h    1
    v    1
    x    1
    Name: count, dtype: int64
    """

    column_names = [
        chr(97 + i) for i in range(columns)
    ]  # generate column names based on the number of columns
    values = list("abcdefghijklmnopqrstuvwxyz")
    data = np.random.choice(values, size=(rows, columns))
    df = pd.DataFrame(data, columns=column_names)
    return df

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    """Tests case for function `task_func`."""
    def test_dataframe_shape_default(self):
        """Test if the DataFrame has default shape (100 rows, 3 columns) with default parameters."""
        np.random.seed(1)
        df_test = task_func()
        self.assertEqual(df_test.shape, (100, 3))
    def test_dataframe_shape_custom_rows(self):
        """Test if the DataFrame has the correct shape when a custom number of rows is specified."""
        np.random.seed(2)
        df_test = task_func(50)
        self.assertEqual(df_test.shape, (50, 3))
    def test_dataframe_shape_custom_columns(self):
        """Test if the DataFrame has the correct shape with a custom number of columns."""
        np.random.seed(3)
        df_test = task_func(50, 5)
        self.assertEqual(df_test.shape, (50, 5))
    def test_dataframe_columns_default(self):
        """Test if the DataFrame has default column names ['a', 'b', 'c'] with default parameters."""
        np.random.seed(4)
        df_test = task_func()
        self.assertListEqual(list(df_test.columns), ["a", "b", "c"])
    def test_dataframe_columns_custom(self):
        """Test if the DataFrame has the correct column names when a custom number of columns is specified."""
        np.random.seed(5)
        df_test = task_func(columns=5)
        expected_columns = ["a", "b", "c", "d", "e"]
        self.assertListEqual(list(df_test.columns), expected_columns)
    def test_dataframe_values(self):
        """Test if each cell in the DataFrame contains a letter from the English alphabet."""
        np.random.seed(6)
        df_test = task_func()
        for col in df_test.columns:
            self.assertTrue(
                set(df_test[col].unique()).issubset(set("abcdefghijklmnopqrstuvwxyz"))
            )
    def test_dataframe_empty(self):
        """Test if an empty DataFrame is created when 0 rows are specified."""
        np.random.seed(7)
        df_test = task_func(0)
        self.assertEqual(df_test.shape, (0, 3))
