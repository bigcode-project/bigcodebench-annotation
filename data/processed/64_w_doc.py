import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    """
    You are given a list of elements. Each element is a list with the same length as COLUMNS, representing one row a dataframe df to create. Visualize the distribution of different values in a column "col3" of a pandas DataFrame df, grouped by "col1" and "col2," using a heatmap.

    Parameters:
    - data (list): A list of elements. Each element is a list with the same length as COLUMNS, representing one row of the dataframe to build.

    Returns:
    - tuple:
        pandas.DataFrame: The DataFrame of the analyzed data.
        plt.Axes: The heatmap visualization.

    Requirements:
    - pandas
    - seaborn
    - matplotlib

    Example:
    >>> data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
    >>> analyzed_df, ax = task_func(data)
    >>> print(analyzed_df)
    col2  1  2
    col1      
    1     2  1
    2     3  1
    """

    df = pd.DataFrame(data, columns=COLUMNS)
    analyzed_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()
    analyzed_df = analyzed_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
    ax = sns.heatmap(analyzed_df, annot=True)
    plt.show()
    return analyzed_df, ax

import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
        df = pd.DataFrame(data, columns=COLUMNS)
        analyzed_df, ax = task_func(df)
        expected_data = [[1, 1, 2], [1, 2, 1], [2, 1, 3], [2, 2, 1]]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_2(self):
        data = [
            [1, 1, 2],
            [1, 1, 3],
            [1, 2, 4],
            [1, 1, 5],
            [1, 3, 7]
        ]
        analyzed_df, ax = task_func(data)
        expected_data = [
            [1, 1, 3],
            [1, 2, 1],
            [1, 3, 1]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_3(self):
        data = [
            [1, 1, 1],
            [1, 2, 3],
            [2, 1, 4],
            [2, 2, 5]
        ]
        analyzed_df, ax = task_func(data)
        expected_data = [
            [1, 1, 1],
            [1, 2, 1],
            [2, 1, 1],
            [2, 2, 1]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_4(self):
        data = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        analyzed_df, ax = task_func(data)
        expected_data = [
            [1, 1, 1],
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_5(self):
        data = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        analyzed_df, ax = task_func(data)
        expected_data = [
            [0, 0, 2],
            [0, 1, 2],
            [1, 0, 2],
            [1, 1, 2]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        expected_df = expected_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
        # Assertions
        self.assertTrue(isinstance(analyzed_df, pd.DataFrame))
        pd.testing.assert_frame_equal(analyzed_df, expected_df, check_dtype=False)
        self.assertTrue(isinstance(ax, plt.Axes))
