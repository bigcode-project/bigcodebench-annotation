import pandas as pd
import matplotlib.pyplot as plt


def f_35(array):
    """
    Create a Pandas DataFrame from a 2D list and plot the sum of each column.

    Parameters:
    array (list of list of int): The 2D list representing the data.

    Returns:
    DataFrame, Axes: A pandas DataFrame with the data and a matplotlib Axes object showing the sum of each column.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Internal Constants:
    COLUMNS: List of column names used for the DataFrame ['A', 'B', 'C', 'D', 'E']

    Example:
    >>> df, ax = f_35([[1,2,3,4,5], [6,7,8,9,10]])
    >>> print(df)
       A  B  C  D   E
    0  1  2  3  4   5
    1  6  7  8  9  10
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    COLUMNS = ["A", "B", "C", "D", "E"]
    df = pd.DataFrame(array, columns=COLUMNS)
    sums = df.sum()
    fig, ax = plt.subplots()
    sums.plot(kind="bar", ax=ax)
    return df, ax

import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df, ax = f_35([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.assertEqual(df.values.tolist(), [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.assertEqual(df.columns.tolist(), ["A", "B", "C", "D", "E"])
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_2(self):
        df, ax = f_35(
            [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [5, 15, 25, 35, 45]]
        )
        self.assertEqual(
            df.values.tolist(),
            [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [5, 15, 25, 35, 45]],
        )
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_3(self):
        # Test handling uniform data
        df, ax = f_35([[1, 1, 1, 1, 1]])
        self.assertEqual(df.values.tolist(), [[1, 1, 1, 1, 1]])
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_4(self):
        # Test handling all zero
        df, ax = f_35([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        self.assertEqual(df.values.tolist(), [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_5(self):
        # Handle negatives
        df, ax = f_35([[-1, -2, -3, -4, -5], [1, 2, 3, 4, 5]])
        self.assertEqual(df.values.tolist(), [[-1, -2, -3, -4, -5], [1, 2, 3, 4, 5]])
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_6(self):
        # Handle empty
        df, ax = f_35([])
        self.assertEqual(df.values.tolist(), [])
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_7(self):
        # Handle invalid input
        with self.assertRaises(TypeError):
            f_35([["a", "b", "c", "d", "e"]])
    def test_case_8(self):
        # Handle large numbers
        df, _ = f_35([[1000000, 2000000, 3000000, 4000000, 5000000]])
        self.assertTrue(
            all(
                df.sum()
                == pd.Series(
                    [1000000, 2000000, 3000000, 4000000, 5000000],
                    index=["A", "B", "C", "D", "E"],
                )
            )
        )
    def test_case_9(self):
        # Test plot details
        _, ax = f_35([[1, 2, 3, 4, 5]])
        self.assertEqual(len(ax.patches), 5)  # Checks if there are exactly 5 bars
        bar_labels = [bar.get_x() for bar in ax.patches]
        self.assertEqual(len(bar_labels), 5)
    def test_case_10(self):
        # Test column sums with plot check
        data = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6]]
        df, ax = f_35(data)
        column_sums = df.sum().tolist()
        bar_heights = [bar.get_height() for bar in ax.patches]
        self.assertEqual(column_sums, bar_heights)
        self.assertEqual(
            len(ax.patches), len(data[0])
        )  # Ensure there's a bar for each column
    def tearDown(self):
        plt.close("all")
