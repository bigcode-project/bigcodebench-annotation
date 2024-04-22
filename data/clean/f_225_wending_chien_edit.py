import pandas as pd
import numpy as np
from random import choice

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]


def f_225(rows, columns):
    """
    Generates a DataFrame with a specified number of rows and columns, populated with randomly generated data.
    Each column's data type is randomly selected from a set of Python data types,
    including primitive and complex structures.

    Parameters:
    rows (int): Number of rows in the generated DataFrame.
    columns (int): Number of columns in the generated DataFrame. Each column is assigned a random data type.

    DataFrame: A DataFrame in which each column's data type could be one of the following,
    with random content generated accordingly:
    - str: Random strings of 5 lowercase alphabetic characters.
    - int: Random integers from 0 to 9.
    - float: Random floats derived by converting integers from 0 to 9 into float.
    - list: Lists of random length (1 to 5) containing integers from 0 to 9.
    - tuple: Tuples of random length (1 to 5) containing integers from 0 to 9.
    - dict: Dictionaries with a random number (1 to 5) of key-value pairs, keys and values are integers from 0 to 9.
    - set: Sets of random size (1 to 5) containing unique integers from 0 to 9.

    Returns:
    pd.DataFrame: A DataFrame with the specified number of rows and columns containing randomly generated data.

    Requirements:
    - pandas
    - numpy
    - random

    Example:
    >>> df = f_225(2, 3)
    >>> print(df.shape)
    (2, 3)
    >>> isinstance(df, pd.DataFrame)
    True
    """
    data = {}
    for col in range(columns):
        data_type = choice(DATA_TYPES)
        if data_type == str:
            data['col' + str(col)] = [''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=5)) for _ in
                                      range(rows)]
        elif data_type in [int, float]:
            data['col' + str(col)] = np.random.choice([data_type(i) for i in range(10)], size=rows)
        elif data_type == list:
            data['col' + str(col)] = [list(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in
                                      range(rows)]
        elif data_type == tuple:
            data['col' + str(col)] = [tuple(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in
                                      range(rows)]
        elif data_type == dict:
            data['col' + str(col)] = [dict(zip(np.random.choice(range(10), size=np.random.randint(1, 6)),
                                               np.random.choice(range(10), size=np.random.randint(1, 6)))) for _ in
                                      range(rows)]
        elif data_type == set:
            data['col' + str(col)] = [set(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in
                                      range(rows)]

    df = pd.DataFrame(data)
    return df


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def setUp(self):
        """Setup a predictable random seed for numpy to ensure deterministic tests."""
        np.random.seed(42)

    def test_dataframe_dimensions(self):
        """Test the generated DataFrame has the correct dimensions."""
        rows, columns = 5, 3
        df = f_225(rows, columns)
        self.assertEqual(df.shape, (rows, columns), "DataFrame should have the specified dimensions.")

    def test_dataframe_data_types(self):
        """Test that each column in the DataFrame has data of the correct type and validates mixed data types."""
        df = f_225(5, 5)
        for col in df.columns:
            values = df[col]
            unique_types = set(type(v) for v in values)
            self.assertTrue(len(unique_types) <= 2, "Each column should contain no more than two distinct data types.")

    def test_dataframe_size(self):
        """Test that the DataFrame has the correct dimensions."""
        rows, columns = 5, 4
        df = f_225(rows, columns)
        self.assertEqual(df.shape, (rows, columns), "DataFrame should have the specified dimensions.")

    def test_column_names(self):
        """Test that the column names are correctly formatted."""
        columns = 3
        df = f_225(5, columns)
        expected_columns = ['col' + str(i) for i in range(columns)]
        self.assertListEqual(list(df.columns), expected_columns, "Column names are not formatted correctly.")

    def test_collection_sizes(self):
        """Test the size constraints of collections like lists, tuples, dicts, and sets."""
        df = f_225(10, 10)
        for col in df.columns:
            if isinstance(df[col][0], (list, tuple, set, dict)):
                if isinstance(df[col][0], dict):
                    sizes = [len(v.keys()) for v in df[col]]
                else:
                    sizes = [len(v) for v in df[col]]
                self.assertTrue(all(1 <= s <= 5 for s in sizes), f"Sizes in column {col} should be between 1 and 5.")


if __name__ == "__main__":
    run_tests()
