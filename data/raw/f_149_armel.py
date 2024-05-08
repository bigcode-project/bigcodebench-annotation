import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import ast

def f_149(directory):
    """
    Traverse a directory for CSV files a get the file with the longest filename. From that CSV file, load e-mail data, convert it into a Pandas DataFrame, calculate the sum, mean and median of the list associated with each e-mail, and then draw a histogram of the median.
    - The column names of each CSV files are 'email' and 'list'.
    - The column 'list' contains a string representation of a list. It should be converted before usage.
    - If there is not csv file in the directory, return an empty dataframe with the columns expected.
    - If there is not csv file in the directory, return None instead of an empty plot.

    Parameters:
    - directory (str): The path to the directory.

    Returns:
    - pandas.DataFrame : DataFrame containing the data from the CSV file with the longest filename augmented with the columns 'sum', 'mean' and 'median'.
    - matplotlib.axes._axes.Axes : Histogram of the median. None if there is no data to plot.

    Requirements:
    - pandas
    - os
    - numpy
    - ast
    - matplotlib.pyplot

    Example:
    >>> f_149('data_directory')
    """
    name = None
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            if name is None :
                name = filename
            else :
                name = filename if len(filename) > len(name) else name
    if name is None :
        return pd.DataFrame({}, columns = ['email', 'list'] + ['sum', 'mean', 'median']), None

    df = pd.read_csv(os.path.join(directory, name))
    df["list"] = df["list"].map(ast.literal_eval)
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)

    return df, df["median"].hist()

import unittest
import shutil
import pandas as pd

class TestCases(unittest.TestCase):
    """Test cases for the f_149 function."""
    def setUp(self):
        self.test_dir = "data/f_149"
        os.makedirs(self.test_dir, exist_ok=True)

        self.dir_1 = os.path.join(self.test_dir, "dir_1")
        os.makedirs(self.dir_1, exist_ok=True)
        df = pd.DataFrame(
            {
                "email" : ["first@example.com", "second@example.com", "third@example.com"],
                "list" : [[12, 17, 29, 45, 7, 3], [1, 1, 3, 73, 21, 19, 12], [91, 23, 7, 14, 66]]
            }
        )
        df.to_csv(os.path.join(self.dir_1, "csv.csv"), index=False)

        self.dir_2 = os.path.join(self.test_dir, "dir_2")
        os.makedirs(self.dir_2, exist_ok=True)
        df = pd.DataFrame(
            {
                "email" : ["fourth@example.com", "fifth@example.com", "sixth@example.com", "seventh@example.com"],
                "list" : [[12, 21, 35, 2, 1], [13, 4, 10, 20], [82, 23, 7, 14, 66], [111, 23, 4]]
            }
        )
        df.to_csv(os.path.join(self.dir_2, "csv.csv"), index=False)

        self.dir_3 = os.path.join(self.test_dir, "dir_3")
        os.makedirs(self.dir_3, exist_ok=True)
        df = pd.DataFrame(
            {
                "email" : ["eight@example.com", "ninth@example.com"],
                "list" : [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
            }
        )
        df.to_csv(os.path.join(self.dir_3, "csv.csv"), index=False)
        df = pd.DataFrame(
            {
                "email" : ["tenth@example.com", "eleventh@example.com"],
                "list" : [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
            }
        )
        df.to_csv(os.path.join(self.dir_3, "long_csv.csv"), index=False)

        self.dir_4 = os.path.join(self.test_dir, "dir_4")
        os.makedirs(self.dir_4, exist_ok=True)

        self.dir_5 = os.path.join(self.test_dir, "dir_5")
        os.makedirs(self.dir_5, exist_ok=True)
        df = pd.DataFrame(
            {
                "email": [
                    "first@example.com",
                ],
                "list": [
                    [12],
                ],
            }
        )
        df.to_csv(os.path.join(self.dir_5, "csv.csv"), index=False)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_case_1(self):
        # Test if the function correctly processes the CSV files and returns the appropriate DataFrame and histogram
        df, ax = f_149(self.dir_1)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass
        # Check DataFrame structure and content
        self.assertTrue(
            all(
                [
                    col in df.columns
                    for col in ["email", "list", "sum", "mean", "median"]
                ]
            )
        )

        # Check specific values in the DataFrame
        self.assertEqual(df.loc[0, 'email'], 'first@example.com')
        self.assertEqual(df.loc[1, 'email'], 'second@example.com')
        self.assertEqual(df.loc[2, 'email'], 'third@example.com')
        self.assertEqual(df.loc[1, 'sum'], 130)
        self.assertEqual(df.loc[1, 'mean'], 130.0/7.0)
        self.assertEqual(df.loc[1, 'median'], 12.0)

        # Check attributes of the histogram
        self.assertTrue(hasattr(ax, 'figure'))

    def test_case_2(self):
        # Test if the function correctly processes the CSV files and returns the appropriate DataFrame and histogram
        df, ax = f_149(self.dir_2)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass
        # Check DataFrame structure and content
        self.assertTrue(
            all(
                [
                    col in df.columns
                    for col in ["email", "list", "sum", "mean", "median"]
                ]
            )
        )

        # Check specific values in the DataFrame
        self.assertEqual(df.loc[1, 'email'], 'fifth@example.com')
        self.assertEqual(df.loc[1, 'sum'], 47)
        self.assertEqual(df.loc[1, 'mean'], 11.75)
        self.assertEqual(df.loc[2, 'median'], 23.0)

        # Check attributes of the histogram
        self.assertTrue(hasattr(ax, 'figure'))

    def test_case_3(self):
        # Test if the function correctly processes the CSV files and returns the appropriate DataFrame and histogram
        df, ax = f_149(self.dir_3)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass
        # Check DataFrame structure and content
        self.assertTrue(
            all(
                [
                    col in df.columns
                    for col in ["email", "list", "sum", "mean", "median"]
                ]
            )
        )

        # Check specific values in the DataFrame
        self.assertEqual(df.loc[1, 'email'], 'eleventh@example.com')
        self.assertEqual(df.loc[0, 'sum'], 65)
        self.assertEqual(df.loc[1, 'sum'], 90)

        self.assertEqual(df.loc[0, 'mean'], 13.0)
        self.assertEqual(df.loc[1, 'mean'], 18.0)

        self.assertEqual(df.loc[0, 'median'], 13.0)
        self.assertEqual(df.loc[1, 'median'], 18.0)

        # Check attributes of the histogram
        self.assertTrue(hasattr(ax, 'figure'))

    def test_case_4(self):
        # Test with a directory without csv files
        df, ax = f_149(self.dir_4)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass
        # Check DataFrame structure and content
        self.assertTrue(
            all(
                [
                    col in df.columns
                    for col in ["email", "list", "sum", "mean", "median"]
                ]
            )
        )
        self.assertIsNone(ax)

    def test_case_5(self):
        # Test if the function correctly processes the CSV files and returns the appropriate DataFrame and histogram
        df, ax = f_149(self.dir_5)
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass
        # Check DataFrame structure and content
        self.assertTrue(
            all(
                [
                    col in df.columns
                    for col in ["email", "list", "sum", "mean", "median"]
                ]
            )
        )

        # Check specific values in the DataFrame
        self.assertEqual(df.loc[0, "email"], "first@example.com")
        self.assertEqual(df.loc[1, "sum"], 12)
        self.assertEqual(df.loc[1, "mean"], 12.0)
        self.assertEqual(df.loc[1, "median"], 12.0)

        # Check attributes of the histogram
        self.assertTrue(hasattr(ax, "figure"))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
