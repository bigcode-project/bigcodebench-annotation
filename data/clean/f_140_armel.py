import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ['col1', 'col2', 'col3']

def f_140(data):
    """
    You are given a list of elements. Each element is a list with the same length as COLUMNS, representing one row a dataframe df to create. Draw a line chart with unique values in the COLUMNS[-1] of the pandas DataFrame "df", grouped by the rest of the columns.
    - The x-label should be set to the string obtained by joining all the column names (except the last one) by the character "-".
    - The y-label should be set to the last column name.

    Parameters:
    - df (pandas.DataFrame): The DataFrame to be plotted.

    Returns:
    - tuple: A tuple containing:
        - pandas.DataFrame: The DataFrame of the analyzed data.
        - plt.Axes: The Axes object of the plotted line chart.

    Requirements:
    - pandas
    - matplotlib

    Example:
    >>> data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
    >>> analyzed_df, ax = f_140(data)
    >>> print(analyzed_df)
       col1  col2  col3
    0     1     1     2
    1     1     2     1
    2     2     1     3
    3     2     2     1
    """
    df = pd.DataFrame(data, columns=COLUMNS)
    analyzed_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()

    # Adjusting the plotting logic
    fig, ax = plt.subplots()
    ax.plot(analyzed_df[COLUMNS[:-1]].astype(str).agg('-'.join, axis=1), analyzed_df[COLUMNS[-1]])
    ax.set_xlabel('-'.join(COLUMNS[:-1]))
    ax.set_ylabel(COLUMNS[-1])

    return analyzed_df, ax

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_140 function."""
    def test_case_1(self):
        # Using the provided example as the first test case
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
        analyzed_df, ax = f_140(data)

        # Assertions for the returned DataFrame
        expected_data = [[1, 1, 2], [1, 2, 1], [2, 1, 3], [2, 2, 1]]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df)

        # Assertions for the returned plot
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [2, 1, 3, 1])
    def test_case_2(self):
        data = [
            [1, 1, 2],
            [1, 1, 3],
            [1, 2, 4],
            [1, 1, 5],
            [1, 3, 7]
        ]
        analyzed_df, ax = f_140(data)
        expected_data = [
            [1, 1, 3],
            [1, 2, 1],
            [1, 3, 1]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [3, 1, 1])

    def test_case_3(self):
        data = [
            [1, 1, 1],
            [1, 2, 3],
            [2, 1, 4],
            [2, 2, 5]
        ]
        analyzed_df, ax = f_140(data)
        expected_data = [
            [1, 1, 1],
            [1, 2, 1],
            [2, 1, 1],
            [2, 2, 1]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [1, 1, 1, 1])

    def test_case_4(self):
        data = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        analyzed_df, ax = f_140(data)
        expected_data = [
            [1, 1, 1],
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [1])

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
        analyzed_df, ax = f_140(data)
        expected_data = [
            [0, 0, 2],
            [0, 1, 2],
            [1, 0, 2],
            [1, 1, 2]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')
        self.assertEqual(ax.get_ylabel(), 'col3')
        self.assertListEqual(list(ax.lines[0].get_ydata()), [2, 2, 2, 2])

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
