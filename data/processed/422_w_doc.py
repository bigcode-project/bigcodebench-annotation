import pandas as pd
from sklearn.model_selection import train_test_split


def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    """
    Split the data into train and test datasets after removing a specified column if it exists.

    Parameters:
    - df (dict): The input dataframe.
    - target_column (str): The name of the target column.
    - column_to_remove (str): The name of the column to remove. Defaults to 'c'.
    - test_size (float): The ratio of test data in split output. Defaults to .2.

    Returns:
    - X_train (pd.DataFrame): Split features for training.
    - X_test  (pd.DataFrame): Split features for testing.
    - y_train    (pd.Series): Split target values for training.
    - y_test     (pd.Series): Split target values for testing.

    Requirements:
    - pandas
    - sklearn

    Examples:
    >>> data = {
    ... 'a': [1, 2, 3, 4],
    ... 'b': [5, 6, 7, 8],
    ... 'c': [9, 10, 11, 12],
    ... 'target': [0, 1, 0, 1]
    ... }
    >>> X_train, _, _, _ = task_func(data, 'target')
    >>> type(X_train), X_train.shape
    (<class 'pandas.core.frame.DataFrame'>, (3, 2))
    >>> data = {
    ... 'x1': [10, 20, 30, 40],
    ... 'x2': [50, 60, 70, 80],
    ... 'x3': [90, 100, 110, 120],
    ... 'outcome': [1, 2, 3, 4]
    ... }
    >>> df2 = pd.DataFrame(data)
    >>> _, _, _, y_test = task_func(df2, 'outcome', 'x3', .25)
    >>> type(y_test), y_test.shape
    (<class 'pandas.core.series.Series'>, (1,))
    """

    df = pd.DataFrame(df)
    if column_to_remove in df.columns:
        df = df.drop(columns=column_to_remove)
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(columns=target_column), df[target_column], test_size=test_size
    )
    return X_train, X_test, y_train, y_test

import unittest
import pandas as pd
from sklearn.utils._param_validation import InvalidParameterError
class TestCases(unittest.TestCase):
    def setUp(self):
        # basic test dataframe
        self.df = {"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8], "c": [7, 8, 9, 10, 11]}
    def shape_testing_helper(self, expected_train_len, expected_test_len, split_data):
        X_train, X_test, y_train, y_test = split_data
        self.assertTrue(len(X_train) == expected_train_len)
        self.assertTrue(len(y_train) == expected_train_len)
        self.assertTrue(len(X_test) == expected_test_len)
        self.assertTrue(len(y_test) == expected_test_len)
    def test_case_1(self):
        # Dataframe with a 'c' column to be removed
        X_train, X_test, y_train, y_test = task_func(self.df, "b")
        self.assertEqual("a", X_train.columns[0])
        self.assertEqual("b", y_train.name)
        self.assertNotIn("c", X_train.columns)
        self.shape_testing_helper(4, 1, (X_train, X_test, y_train, y_test))
    def test_case_2(self):
        # Specify removal of separate column
        X_train, X_test, y_train, y_test = task_func(self.df, "a", column_to_remove="b")
        self.assertEqual("c", X_train.columns[0])
        self.assertEqual("a", y_train.name)
        self.assertNotIn("b", X_train.columns)
        self.shape_testing_helper(4, 1, (X_train, X_test, y_train, y_test))
    def test_case_3(self):
        # Dataframe doesn't have column to be removed
        X_train, X_test, y_train, y_test = task_func(self.df, "a", column_to_remove="FOO")
        self.assertEqual("a", y_train.name)
        self.assertIn("b", X_train.columns)
        self.assertIn("c", X_train.columns)
        self.shape_testing_helper(4, 1, (X_train, X_test, y_train, y_test))
    def test_case_4(self):
        # Change testing ratio
        X_train, X_test, y_train, y_test = task_func(self.df, "a", test_size=0.8)
        self.shape_testing_helper(1, 4, (X_train, X_test, y_train, y_test))
    def test_case_5(self):
        # Should fail if specify invalid ratio
        with self.assertRaises(InvalidParameterError):
            task_func(self.df, "a", test_size=-999)
        with self.assertRaises(InvalidParameterError):
            task_func(self.df, "a", test_size="foo")
    def test_case_6(self):
        # Testing with a dataframe having mixed data types
        df = {
                "a": [pd.NA, 2.3, 3.4, 4.5, 5.5],
                "b": ["one", "two", pd.NA, "four", "five"],
                "c": [True, False, True, False, pd.NA],
            }
        X_train, X_test, y_train, y_test = task_func(df, "b")
        self.assertNotIn("c", X_train.columns)
        self.shape_testing_helper(4, 1, (X_train, X_test, y_train, y_test))
