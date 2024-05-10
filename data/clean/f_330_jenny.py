import pandas as pd
import numpy as np


def f_330(data, column="c"):
    """
    Remove a column from a data dictionary if it exists, and then plot the remaining data
    if it contains numeric data.

    Parameters:
    - data (dict): The input data dictionary.
    - column (str): Name of column to remove. Defaults to "c".

    Returns:
    - df (pd.DataFrame): The modified DataFrame after removing the specified column.
    - ax (matplotlib.axes._axes.Axes or None): The plot of the modified DataFrame if there's
      numeric data to plot, otherwise None.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    >>> modified_df, ax = f_330(data)
    >>> ax
    <Axes: >
    >>> modified_df
       a  b
    0  1  4
    1  2  5
    2  3  6
    """
    df = pd.DataFrame(data)
    if column in df.columns:
        df = df.drop(columns=column)

    # If there's no numeric data, return None for the plot.
    if df.empty or not np.any(df.dtypes.apply(pd.api.types.is_numeric_dtype)):
        return df, None

    ax = df.plot()
    return df, ax


import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Scenario: DataFrame with columns 'a', 'b', and 'c'.
        np.random.seed(0)
        data = {
                "a": np.random.randn(10),
                "b": np.random.randn(10),
                "c": np.random.randn(10),
            }
        df = pd.DataFrame(
            data
        )
        modified_df, ax = f_330(data)  # Remove default column 'c'.
        # Assert column 'c' removal and plot data verification.
        self.assertNotIn("c", modified_df.columns)
        plotted_data = [line.get_ydata() for line in ax.get_lines()]
        self.assertTrue(
            all(
                [
                    np.array_equal(data, modified_df[col].values)
                    for data, col in zip(plotted_data, modified_df.columns)
                ]
            )
        )

    def test_case_2(self):
        # Scenario: DataFrame with columns 'a' and 'b' (no 'c').
        np.random.seed(0)
        data = {"a": np.random.randn(10), "b": np.random.randn(10)}
        df = pd.DataFrame(data)
        modified_df, ax = f_330(data)
        # Assert that the modified DataFrame remains unchanged and plot is generated.
        self.assertEqual(list(df.columns), list(modified_df.columns))
        self.assertIsNotNone(ax)

    def test_case_3(self):
        # Scenario: Empty DataFrame
        data = {}
        df = pd.DataFrame(data)
        modified_df, ax = f_330(data)
        # Assert empty DataFrame and no plot.
        self.assertTrue(modified_df.empty)
        self.assertIsNone(ax)

    def test_case_4(self):
        # Scenario: DataFrame with single non-numeric column 'c'.
        data = {"c": ["apple", "banana", "cherry"]}
        df = pd.DataFrame(data)
        modified_df, ax = f_330(data)
        # Assert empty DataFrame after 'c' removal and no plot.
        self.assertTrue(modified_df.empty)
        self.assertIsNone(ax)

    def test_case_5(self):
        np.random.seed(0)
        # Scenario: DataFrame with columns 'a', 'b', 'c', and non-numeric column 'd'.
        data = {
                "a": np.random.randn(10),
                "b": np.random.randn(10),
                "c": np.random.randn(10),
                "d": [
                    "apple",
                    "banana",
                    "cherry",
                    "date",
                    "fig",
                    "grape",
                    "honeydew",
                    "kiwi",
                    "lime",
                    "mango",
                ],
            }
        df = pd.DataFrame(
            data
        )
        modified_df, ax = f_330(data)
        # Assert column 'c' removal and plot data verification excluding non-numeric column 'd'.
        self.assertNotIn("c", modified_df.columns)
        plotted_data = [line.get_ydata() for line in ax.get_lines()]
        self.assertTrue(
            all(
                [
                    np.array_equal(data, modified_df[col].values)
                    for data, col in zip(plotted_data, modified_df.columns)
                    if col != "d"
                ]
            )
        )

    def test_case_6(self):
        # Scenario: Remove specified column.
        np.random.seed(0)
        data = {
                "a": np.random.randn(10),
                "b": np.random.randn(10),
            }
        df = pd.DataFrame(
            data
        )
        modified_df, ax = f_330(df, column="a")
        self.assertNotIn("a", modified_df.columns)
        plotted_data = [line.get_ydata() for line in ax.get_lines()]
        self.assertTrue(
            all(
                [
                    np.array_equal(data, modified_df[col].values)
                    for data, col in zip(plotted_data, modified_df.columns)
                ]
            )
        )

    def test_case_7(self):
        # Scenario: Only non-numeric columns.
        data = {
                "a": ["apple", "banana"],
                "b": ["cherry", "date"],
                "c": ["fig", "grape"],
            }
        df = pd.DataFrame(
            data
        )
        modified_df, ax = f_330(data)
        self.assertNotIn("c", modified_df.columns)
        pd.testing.assert_frame_equal(df[["a", "b"]], modified_df)
        self.assertEqual(ax, None)

    def tearDown(self):
        plt.close("all")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
