import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def f_113(df):
    """
    Describe a dataframe and draw a distribution chart for each numeric column after replacing the NaN values with the average of the column.

    Parameters:
    df (DataFrame): The pandas DataFrame.

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame with statistics. This includes count, mean, standard deviation (std), min, 25%, 50%, 75%, and max values for each numeric column.
        - List[Axes]: A list of matplotlib Axes objects representing the distribution plots for each numeric column.
                    Each plot visualizes the distribution of data in the respective column with 10 bins.

    Requirements:
    - numpy
    - seaborn
    - matplotlib.pyplot

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> df = pd.DataFrame([[1,2,3],[4,5,6],[7.0,np.nan,9.0]], columns=["c1","c2","c3"])
    >>> description, plots = f_113(df)
    >>> print(description)
            c1    c2   c3
    count  3.0  3.00  3.0
    mean   4.0  3.50  6.0
    std    3.0  1.50  3.0
    min    1.0  2.00  3.0
    25%    2.5  2.75  4.5
    50%    4.0  3.50  6.0
    75%    5.5  4.25  7.5
    max    7.0  5.00  9.0
    """
    df = df.fillna(df.mean(axis=0))
    description = df.describe()
    plots = []
    for col in df.select_dtypes(include=[np.number]).columns:
        plot = sns.displot(df[col], bins=10)
        plots.append(plot.ax)
    return description, plots


import unittest
import pandas as pd


class TestCases(unittest.TestCase):
    """Test cases for the f_112 function."""

    def setUp(self):
        # Generating more complex data for testing
        self.df1 = pd.DataFrame(
            {"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10], "C": [11, 12, 13, 14, 15]}
        )

        self.df2 = pd.DataFrame({"X": [1, None, 9, 13], "Y": [None, 3, 4, 8]})

        self.df3 = pd.DataFrame(
            {"M": [7, 13, 21, 11, 22, 8, None, 17], "N": [None, 2, 3, 4, 10, 0, 27, 12]}
        )

        self.df4 = pd.DataFrame(
            {"P": [None, None, 4], "Q": [7, None, 3], "R": [2, None, 6]}
        )

        self.df5 = pd.DataFrame({"W": [1, 2], "Z": [2, 1]})

        self.df6 = pd.DataFrame(
            {
                "A": [1, 2, 3, 4, 5, 6],
                "B": [None, 8, 9, 10, 11, None],
                "C": [13, None, None, None, None, 18],
                "D": [19, None, 21, None, 23, None],
            }
        )

    def test_case_1(self):
        description, plots = f_113(self.df1)
        self.assertFalse(description.isna().any().any())
        self.assertIsInstance(description, pd.DataFrame)
        self.assertListEqual(list(description.columns), ["A", "B", "C"])
        self.assertEqual(len(plots), 3)

    def test_case_2(self):
        description, plots = f_113(self.df2)
        self.assertFalse(description.isna().any().any())
        self.assertIsInstance(description, pd.DataFrame)
        self.assertListEqual(list(description.columns), ["X", "Y"])
        self.assertEqual(len(plots), 2)

    def test_case_3(self):
        description, plots = f_113(self.df3)
        self.assertFalse(description.isna().any().any())
        self.assertIsInstance(description, pd.DataFrame)
        self.assertListEqual(list(description.columns), ["M", "N"])
        self.assertEqual(len(plots), 2)

    def test_case_4(self):
        description, plots = f_113(self.df4)
        self.assertFalse(description.isna().any().any())
        self.assertIsInstance(description, pd.DataFrame)
        self.assertListEqual(list(description.columns), ["P", "Q", "R"])
        self.assertEqual(len(plots), 3)

    def test_case_5(self):
        description, plots = f_113(self.df5)
        self.assertFalse(description.isna().any().any())
        self.assertIsInstance(description, pd.DataFrame)
        self.assertListEqual(list(description.columns), ["W", "Z"])
        self.assertEqual(len(plots), 2)

    def test_case_6(self):
        description, plots = f_113(self.df6)
        self.assertFalse(description.isna().any().any())
        self.assertIsInstance(description, pd.DataFrame)
        self.assertListEqual(list(description.columns), ["A", "B", "C", "D"])
        self.assertEqual(len(plots), 4)
        self.assertEqual(description.loc["mean", "A"], 3.5)
        self.assertEqual(description.loc["std", "B"], 1.0)
        self.assertEqual(description.loc["25%", "A"], 2.25)
        self.assertEqual(description.loc["50%", "C"], 15.5)
        self.assertEqual(description.loc["75%", "A"], 4.75)
        self.assertEqual(description.loc["max", "D"], 23.0)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
