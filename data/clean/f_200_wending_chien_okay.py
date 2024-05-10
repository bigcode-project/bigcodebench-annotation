import pandas as pd
from sklearn.preprocessing import LabelEncoder


def f_200(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Encrypt the categorical data in a specific column of a DataFrame using LabelEncoder.

    Parameters:
    df (pd.DataFrame): The DataFrame that contains the data.
    column_name (str): The name of the column to encode.

    Returns:
    pd.DataFrame: The DataFrame with the encoded column.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> df = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry', 'apple', 'banana']})
    >>> encoded_df = f_200(df, 'fruit')
    >>> encoded_df['fruit'].tolist()
    [0, 1, 2, 0, 1]
    """
    le = LabelEncoder()
    df[column_name] = le.fit_transform(df[column_name])
    return df


import unittest
import pandas as pd


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_case_1(self):
        df = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry', 'apple', 'banana']})
        encoded_df = f_200(df, 'fruit')
        self.assertEqual(encoded_df['fruit'].tolist(), [0, 1, 2, 0, 1])

    def test_case_2(self):
        df = pd.DataFrame({'animal': ['cat', 'dog', 'bird', 'cat', 'bird']})
        encoded_df = f_200(df, 'animal')
        self.assertEqual(encoded_df['animal'].tolist(), [1, 2, 0, 1, 0])

    def test_case_3(self):
        df = pd.DataFrame({'color': ['red', 'blue', 'green', 'red', 'green']})
        encoded_df = f_200(df, 'color')
        self.assertEqual(encoded_df['color'].tolist(), [2, 0, 1, 2, 1])

    def test_case_4(self):
        df = pd.DataFrame({'vehicle': ['car', 'bus', 'train', 'car', 'train']})
        encoded_df = f_200(df, 'vehicle')
        self.assertEqual(encoded_df['vehicle'].tolist(), [1, 0, 2, 1, 2])

    def test_case_5(self):
        df = pd.DataFrame({'city': ['NYC', 'LA', 'SF', 'NYC', 'SF']})
        encoded_df = f_200(df, 'city')
        self.assertEqual(encoded_df['city'].tolist(), [1, 0, 2, 1, 2])


if __name__ == "__main__":
    run_tests()
