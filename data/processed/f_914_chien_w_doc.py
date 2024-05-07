import pandas as pd
from random import shuffle

# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


def f_37(list_of_lists):
    """
    Generate a list of pandas DataFrames, each created from a sublist in 'list_of_lists'.
    Each DataFrame has columns named as per the elements of the sublist, and each column
    is filled with randomly shuffled values from 'POSSIBLE_VALUES'.

    Parameters:
    - list_of_lists (list of list): A list where each element is a list of strings
    representing column names for a DataFrame.

    Returns:
    - list of pandas.DataFrame: A list where each element is a DataFrame with columns as specified
    in 'list_of_lists', and each column contains shuffled values from 'POSSIBLE_VALUES'.

    Requirements:
    - pandas
    - random.shuffle

    Note:
    - The length of each DataFrame's columns is equal to the length of 'POSSIBLE_VALUES'.
    - Each column in the DataFrame has the same shuffled order of 'POSSIBLE_VALUES'.

    Example:
    >>> import random
    >>> random.seed(0)
    >>> dfs = f_37([['x', 'y', 'z'], ['a', 'b', 'c']])
    >>> dfs[0].head()
       x  y  z
    0  H  J  H
    1  I  E  A
    2  B  I  J
    3  F  G  D
    4  D  A  C
    """
    dataframes = []
    for list_ in list_of_lists:
        df_dict = {col: POSSIBLE_VALUES.copy() for col in list_}
        for col in df_dict:
            shuffle(df_dict[col])
        df = pd.DataFrame(df_dict)
        dataframes.append(df)
    return dataframes

import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    """Test cases for f_37 function."""
    def test_dataframe_count(self):
        """Test number of dataframes returned."""
        random.seed(0)
        input_data = [["x", "y"], ["a", "b", "c"], ["m"]]
        dfs = f_37(input_data)
        self.assertEqual(len(dfs), len(input_data))
    def test_dataframe_columns(self):
        """Test each dataframe has correct columns."""
        random.seed(1)
        input_data = [["x", "y"], ["a", "b", "c"], ["m"]]
        dfs = f_37(input_data)
        for idx, df in enumerate(dfs):
            self.assertListEqual(list(df.columns), input_data[idx])
    def test_dataframe_values(self):
        """Test values in each dataframe column are from the POSSIBLE_VALUES list."""
        random.seed(2)
        input_data = [["x", "y"], ["a", "b", "c"], ["m"]]
        dfs = f_37(input_data)
        for df in dfs:
            for col in df.columns:
                self.assertTrue(all(val in POSSIBLE_VALUES for val in df[col].values))
    def test_empty_input(self):
        """Test function with an empty list of lists."""
        random.seed(3)
        dfs = f_37([])
        self.assertEqual(len(dfs), 0)
    def test_single_list_input(self):
        """Test function with a single list input."""
        random.seed(4)
        input_data = [["x", "y", "z"]]
        dfs = f_37(input_data)
        self.assertEqual(len(dfs), 1)
        self.assertListEqual(list(dfs[0].columns), input_data[0])
        self.assertTrue(all(val in POSSIBLE_VALUES for val in dfs[0]["x"].values))
        self.assertTrue(all(val in POSSIBLE_VALUES for val in dfs[0]["y"].values))
        self.assertTrue(all(val in POSSIBLE_VALUES for val in dfs[0]["z"].values))
