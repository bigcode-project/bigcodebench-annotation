import numpy as np
import pandas as pd


def f_691(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generate a DataFrame with columns 'columns' and fill them with random 
    integer values between 0 and 100. Remove some columns based on the provided indexes.
    
    Parameters:
    n_rows (int): The number of rows in the DataFrame.
    remove_cols (list of int): The indices of columns to be removed.
    columns (list of str, optional): The columns to be included in the DataFrame. Defaults to ['A', 'B', 'C', 'D', 'E'].
    random_seed (int): Seed for the rng. Default is None.

    Returns:
    DataFrame: The resulting DataFrame after removal of columns.
    
    Requirements:
    - numpy
    - pandas
    
    Example:
    >>> df = f_691(10, [1, 3], random_seed=1)
    >>> print(df)
        A   C   E
    0  37  72  75
    1   5  64   1
    2  76   6  50
    3  20  84  28
    4  29  50  87
    5  87  96  13
    6   9  63  22
    7  57   0  81
    8   8  13  72
    9  30   3  21

    >>> df = f_691(3, [1, 3], columns=['test', 'rem1', 'apple', 'remove'], random_seed=12)
    >>> print(df)
       test  apple
    0    75      6
    1     3     76
    2    22     52

    """
    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.randint(0, 100, size=(n_rows, len(columns))), columns=columns)
    df = df.drop(df.columns[remove_cols], axis=1)

    return df

import unittest
import numpy as np
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = f_691(5, [1, 3], random_seed=1)
        expected = pd.DataFrame({
            'A': {0: 37, 1: 5, 2: 76, 3: 20, 4: 29},
            'C': {0: 72, 1: 64, 2: 6, 3: 84, 4: 50},
            'E': {0: 75, 1: 1, 2: 50, 3: 28, 4: 87}
        })
        pd.testing.assert_frame_equal(df, expected, check_dtype=False)

    def test_case_2(self):
        df = f_691(10, [], columns=['X', 'Y', 'Z'], random_seed=12)
        expected = pd.DataFrame({
            'X': {0: 75, 1: 2, 2: 76, 3: 49, 4: 13, 5: 75, 6: 76, 7: 89, 8: 35, 9: 63},
            'Y': {0: 27, 1: 3, 2: 48, 3: 52, 4: 89, 5: 74, 6: 13, 7: 35, 8: 33, 9: 96},
            'Z': {0: 6, 1: 67, 2: 22, 3: 5, 4: 34, 5: 0, 6: 82, 7: 62, 8: 30, 9: 18}
        })
        pd.testing.assert_frame_equal(df, expected, check_dtype=False)

    def test_case_3(self):
        df = f_691(0, remove_cols=[], random_seed=42)
        expected = pd.DataFrame(
            {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}}
        )
        pd.testing.assert_frame_equal(df, expected, check_dtype=False, check_index_type=False)

    def test_case_4(self):
        df1 = f_691(10, [], random_seed=12)
        df2 = f_691(10, [], random_seed=12)

        pd.testing.assert_frame_equal(df1, df2, check_dtype=False, check_index_type=False)

    def test_case_5(self):
        df = f_691(6, [0, 1, 2, 3, 4], random_seed=1)
        self.assertEqual(list(df.columns), [])

if __name__ == "__main__":
    run_tests()