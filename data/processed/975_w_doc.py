import numpy as np
import pandas as pd

def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    """
    Create a Pandas DataFrame with a specified number of rows filled with random
    values in [0, 1) and shuffled columns.
    
    Note:
    - The columns should be unique and sorted in the ascending order.

    Parameters:
    rows (int): The number of rows for the DataFrame. Must not be negative.
    columns (list of str): Column names for the DataFrame.
                           Defaults to ['A', 'B', 'C', 'D', 'E'].
                           If it contains repeated columns, the function deduplicates
                           it in a case and spacing sensitive way. If it is empty,
                           the function returns an empty DataFrame.
    seed (int): The random seed for reproducibility.
    
    Returns:
    pd.DataFrame: A pandas DataFrame with shuffled columns.

    Requirements:
    - numpy
    - pandas

    Example:
    >>> df = task_func(10)
    >>> df.head(2)
              D         E         A         C         B
    0  0.548814  0.715189  0.602763  0.544883  0.423655
    1  0.645894  0.437587  0.891773  0.963663  0.383442
    """

    np.random.seed(seed)
    columns = sorted(list(set(columns)))
    data = np.random.rand(rows, len(columns))
    np.random.shuffle(columns)
    df = pd.DataFrame(data, columns=columns)
    return df

import unittest
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case - data and format correctness
        df = task_func(10, seed=0)
        default_columns = ["A", "B", "C", "D", "E"]
        self.assertEqual(df.shape, (10, 5))
        for column in default_columns:
            self.assertEqual(df.dtypes[column], np.float64)
        self.assertEqual(len(set(df.columns)), len(default_columns))
    def test_case_2(self):
        # Test custom columns
        custom_columns = ["X", "Y", "Z"]
        df = task_func(5, columns=custom_columns, seed=0)
        self.assertTrue(all(column in custom_columns for column in df.columns))
        # assert first 2 rows data
        self.assertEqual(set(df.iloc[0].tolist()), {0.5488135039273248, 0.7151893663724195, 0.6027633760716439})
        
    def test_case_3(self):
        # Test custom rows
        for n_rows in [1, 10, 50]:
            df = task_func(n_rows)
            self.assertEqual(len(df), n_rows)
    def test_case_4(self):
        df = task_func(5, seed=42)
        self.assertEqual(set(df.iloc[0].tolist()), {0.3745401188473625, 0.9507143064099162, 0.7319939418114051, 0.5986584841970366, 0.15601864044243652})
    def test_case_5(self):
        # Test handling edge cases - negative rows
        with self.assertRaises(ValueError):
            task_func(-1)
    def test_case_6(self):
        # Test handling empty columns
        df = task_func(5, columns=[])
        self.assertTrue(df.empty)
    def test_case_7(self):
        # Test handling duplicate columns
        df = task_func(5, columns=["A", "A", "B", "B", "C"], seed=0)
        self.assertEqual(len(df.columns), 3)
