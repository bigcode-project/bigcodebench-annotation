import pandas as pd
import matplotlib.pyplot as plt


def f_380(df: pd.DataFrame, column_name: str) -> (str, plt.Axes):
    """
    This function assesses whether the distribution of values in a specified column of a DataFrame is
    uniform and visualizes this distribution using a histogram.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - column_name (str): The name of the column to be evaluated.

    Returns:
    - str: A message indicating whether the distribution in the column is uniform or not. The message is one of the following:
        - "The distribution of values is uniform."
        - "The distribution of values is not uniform."
    - plt.Axes: An Axes object displaying the histogram of the value distribution in the specified column.

    The function handles the following cases:
    - If the DataFrame is empty, the specified column does not exist in the DataFrame, or
        if the specified column contains only null values, the function returns a message
        "The DataFrame is empty or the specified column has no data."
        In this case, a blank histogram with a title "Distribution of values in [column_name] (No Data)" is generated.
    - If the DataFrame and column are valid, the function calculates if the distribution of values is uniform.
        It returns a message stating whether the distribution is uniform or not.
        A histogram is generated to visualize the distribution of values in the specified column.
        This histogram displays the frequency of each value, with the number of bins set to the number
        of unique values in the column, an edge color of black, and a transparency alpha value of 0.7.
        The x-axis is labeled "Values", the y-axis is labeled "Frequency", and
        the title of the plot is "Distribution of values in [column_name]".

    Requirements:
    - pandas
    - matplotlib

    Example:
    >>> df = pd.DataFrame({'Category': ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'E', 'E']})
    >>> message, ax = f_380(df, 'Category')
    >>> print(message)
    The distribution of values is not uniform.
    """
    if df.empty or column_name not in df.columns or df[column_name].isnull().all():
        message = "The DataFrame is empty or the specified column has no data."
        _, ax = plt.subplots()
        ax.set_title(f"Distribution of values in {column_name} (No Data)")
        return message, ax
    unique_values_count = df[column_name].nunique()
    total_values = len(df[column_name])
    is_uniform = total_values % unique_values_count == 0 and all(
        df[column_name].value_counts() == total_values / unique_values_count
    )
    message = (
        "The distribution of values is uniform."
        if is_uniform
        else "The distribution of values is not uniform."
    )
    _, ax = plt.subplots()
    ax.hist(df[column_name], bins=unique_values_count, edgecolor="black", alpha=0.7)
    ax.set_xticks(range(unique_values_count))
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Distribution of values in {column_name}")
    return message, ax

import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Tests for `f_380`."""
    def test_uniform_distribution(self):
        """Test the distribution of values in a column with a uniform distribution."""
        df = pd.DataFrame({"Category": ["A", "A", "B", "B", "C", "C"]})
        message, _ = f_380(df, "Category")
        self.assertEqual(message, "The distribution of values is uniform.")
    def test_non_uniform_distribution(self):
        """Test the distribution of values in a column with a non-uniform distribution."""
        df = pd.DataFrame({"Category": ["A", "A", "B", "B", "B", "C", "C", "C", "C"]})
        message, _ = f_380(df, "Category")
        self.assertEqual(message, "The distribution of values is not uniform.")
    def test_single_value(self):
        """Test the distribution of values in a column with a single value."""
        df = pd.DataFrame({"Category": ["A", "A", "A", "A", "A", "A"]})
        message, _ = f_380(df, "Category")
        self.assertEqual(message, "The distribution of values is uniform.")
    def test_multi_column(self):
        """Test the distribution of values in a column with a multi-column DataFrame."""
        df = pd.DataFrame(
            {
                "Category": ["A", "A", "B", "B", "C", "C"],
                "Type": ["X", "X", "Y", "Y", "Z", "Z"],
            }
        )
        message, _ = f_380(df, "Type")
        self.assertEqual(message, "The distribution of values is uniform.")
    def test_empty_dataframe(self):
        """Test the distribution of values in a column with an empty DataFrame."""
        df = pd.DataFrame({"Category": []})
        message, _ = f_380(df, "Category")
        self.assertEqual(
            message, "The DataFrame is empty or the specified column has no data."
        )
    def tearDown(self):
        plt.close()
