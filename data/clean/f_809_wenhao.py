import pandas as pd
import matplotlib.pyplot as plt


def f_809(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the cumulative sum for each column in a given DataFrame and plot
    the results in a bar chart.

    Args:
    df (pd.DataFrame): The input DataFrame with numerical values.
                       Must not be empty and must contain numeric data to plot.
    Returns:
    - tuple: A tuple containing:
             (1) A DataFrame with cumulative sums for each column.
             (2) A matplotlib bar chart Figure of these cumulative sums.

    Raises:
    - ValueError: If the DataFrame is empty or contains non-numeric data.

    Requirements:
    - pandas
    - matplotlib

    Note:
    - NaN values are ignored in the cumulative sum calculation, i.e. treated as
      zero for the purpose of the sum without changing existing values to NaN.
    - The plot title is set to 'Cumulative Sum per Column'.
    - X-axis label is 'Index' and Y-axis label is 'Cumulative Sum'.
    - A legend is included in the plot.

    Example:
    >>> input_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    >>> output_df, fig = f_809(input_df)
    >>> output_df
       A   B
    0  1   4
    1  3   9
    2  6  15
    >>> fig
    <Figure size 640x480 with 1 Axes>
    """
    cumsum_df = df.cumsum()

    fig, ax = plt.subplots()
    cumsum_df.plot(kind="bar", ax=ax)
    ax.set_title("Cumulative Sum per Column")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Sum")
    ax.legend()

    return cumsum_df, fig


import numpy as np
import pandas as pd
import unittest
import matplotlib.pyplot as plt


class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup common for all tests
        self.input_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        self.expected_df = pd.DataFrame({"A": [1, 3, 6], "B": [4, 9, 15]})

    def test_case_1(self):
        # Test basic case
        output_df, _ = f_809(self.input_df)
        pd.testing.assert_frame_equal(output_df, self.expected_df)

    def test_case_2(self):
        # Test cumulative sum correctness for a case with negative values
        input_df_neg = pd.DataFrame({"A": [1, -2, 3], "B": [-4, 5, -6]})
        expected_df_neg = pd.DataFrame({"A": [1, -1, 2], "B": [-4, 1, -5]})
        output_df_neg, _ = f_809(input_df_neg)
        pd.testing.assert_frame_equal(output_df_neg, expected_df_neg)

    def test_case_3(self):
        # Test bar chart properties
        _, fig = f_809(self.input_df)

        self.assertIsInstance(fig, plt.Figure)

        ax = fig.axes[0]  # Get the Axes object from the figure
        # Verify the title, x-label, and y-label
        self.assertEqual(ax.get_title(), "Cumulative Sum per Column")
        self.assertEqual(ax.get_xlabel(), "Index")
        self.assertEqual(ax.get_ylabel(), "Cumulative Sum")

        # Ensure that a legend is present and contains the correct labels
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        expected_labels = self.input_df.columns.tolist()
        self.assertEqual(legend_labels, expected_labels)

    def test_case_4(self):
        # Test with an empty DataFrame
        empty_df = pd.DataFrame()
        with self.assertRaises(Exception):
            f_809(empty_df)

    def test_case_5(self):
        # Test with DataFrame containing NaN values
        nan_df = pd.DataFrame({"A": [1, np.nan, 3], "B": [4, 5, np.nan]})
        nan_df_cumsum = nan_df.cumsum()
        output_nan_df, _ = f_809(nan_df)
        pd.testing.assert_frame_equal(output_nan_df, nan_df_cumsum)

    def test_case_6(self):
        # Test with DataFrame containing all zeros
        zeros_df = pd.DataFrame({"A": [0, 0, 0], "B": [0, 0, 0]})
        expected_zeros_df = pd.DataFrame({"A": [0, 0, 0], "B": [0, 0, 0]})
        output_zeros_df, _ = f_809(zeros_df)
        pd.testing.assert_frame_equal(output_zeros_df, expected_zeros_df)

    def test_case_7(self):
        # Test with a DataFrame containing only one row
        one_row_df = pd.DataFrame({"A": [1], "B": [2]})
        expected_one_row_df = pd.DataFrame({"A": [1], "B": [2]})
        output_one_row_df, _ = f_809(one_row_df)
        pd.testing.assert_frame_equal(output_one_row_df, expected_one_row_df)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
