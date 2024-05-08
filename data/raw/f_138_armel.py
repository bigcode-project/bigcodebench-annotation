import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def f_138(df):
    """
    Analyze a Pandas DataFrame by counting different values in a column "col3," grouped by "col1" and "col2," and creating a bar chart to visualize the data distribution.

    Parameters:
    - df (pandas.DataFrame): The DataFrame to be analyzed.

    Returns:
    - pandas.DataFrame: The DataFrame of the analyzed data.
    - matplotlib.axes.Axes: The bar chart visualizing the data distribution.

    Requirements:
    - pandas
    - numpy
    - matplotlib

    Example:
    >>> data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
    >>> df = pd.DataFrame(data, columns=COLUMNS)
    >>> analyzed_df = f_138(df)
    >>> print(analyzed_df)
    (   col1  col2  col3
    0     1     1     2
    1     1     2     1
    2     2     1     3
    3     2     2     1, <Axes: xlabel='col1'>)
    """
    analyzed_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()
    ax = analyzed_df.plot(kind='bar', x='col1', y='col3', secondary_y='col2')
    return analyzed_df, ax

import unittest
import pandas as pd
import matplotlib

class TestCases(unittest.TestCase):
    """Test cases for the f_138 function."""
    @staticmethod
    def is_barplot(ax, expected_values, expected_categories):
        extracted_values = [bar.get_height() for bar in ax.patches] # extract bar height
        extracted_categories = [tick.get_text() for tick in ax.get_xticklabels()] # extract category label

        for actual_value, expected_value in zip(extracted_values, expected_values):
            assert actual_value == expected_value, f"Expected value '{expected_value}', but got '{actual_value}'"

        for actual_category, expected_category in zip(extracted_categories, expected_categories):
            assert actual_category == expected_category, f"Expected category '{expected_category}', but got '{actual_category}'"

    def test_case_1(self):
        # Input 1
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
        df = pd.DataFrame(data, columns=COLUMNS)
        analyzed_df, ax = f_138(df)

        # Assertions
        self.assertIsInstance(analyzed_df, pd.DataFrame)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(analyzed_df), 4)
        self.assertTrue("col1" in analyzed_df.columns)
        self.assertTrue(all([col in analyzed_df.columns for col in ["col1", "col2", "col3"]]))

    def test_case_2(self):
        # Input 2
        data = [[1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 1], [2, 1, 2]]
        df = pd.DataFrame(data, columns=COLUMNS)
        analyzed_df, ax = f_138(df)

        # Assertions
        self.assertIsInstance(analyzed_df, pd.DataFrame)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(analyzed_df), 3)
        self.assertTrue(all([col in analyzed_df.columns for col in ["col1", "col2", "col3"]]))
        self.is_barplot(
            ax=ax,
            expected_values=[2, 2, 2],
            expected_categories=['1', '1', '2']
        )

    def test_case_3(self):
        # Input 3
        data = [[1, 1, 1], [1, 1, 1]]
        df = pd.DataFrame(data, columns=COLUMNS)
        analyzed_df, ax = f_138(df)
        self.is_barplot(
            ax=ax,
            expected_values=[1],
            expected_categories=["1"]
        )
        # Assertions
        self.assertIsInstance(analyzed_df, pd.DataFrame)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(analyzed_df), 1)
        self.assertTrue(all([col in analyzed_df.columns for col in ["col1", "col2", "col3"]]))

    def test_case_4(self):
        # Input 3
        data = [[1, 1, 2], [1, 1, 2]]
        df = pd.DataFrame(data, columns=COLUMNS)
        analyzed_df, ax = f_138(df)

        # Assertions
        self.assertIsInstance(analyzed_df, pd.DataFrame)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(analyzed_df), 1)
        self.assertTrue(all([col in analyzed_df.columns for col in ["col1", "col2", "col3"]]))

    def test_case_5(self):
        # Input 3
        data = [[1, 2, 1], [1, 1, 3]]
        df = pd.DataFrame(data, columns=COLUMNS)
        analyzed_df, ax = f_138(df)

        # Assertions
        self.assertIsInstance(analyzed_df, pd.DataFrame)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(analyzed_df), 2)
        self.assertTrue(all([col in analyzed_df.columns for col in ["col1", "col2", "col3"]]))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
