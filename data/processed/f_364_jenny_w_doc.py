import pandas as pd
import random


def f_746(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    """
    Create a Pandas DataFrame with specified number of rows. Each row contains a randomly
    selected category from the provided categories list and a random integer between 1 and 100.

    The function also generates a bar chart visualizing the counts of each category in the DataFrame
    and returns both the DataFrame and the bar chart.

    Parameters:
    - num_rows (int): Number of rows in the DataFrame. Default is 100. Must be at least 1.
    - categories (list): List of categories to choose from. Default is ['a', 'b', 'c', 'd', 'e'].
    - random_seed (int): Seed for random number generation to ensure reproducibility. Default is 42.

    Returns:
    - pd.DataFrame: A pandas DataFrame with randomly generated category data.
    - matplotlib.pyplot.Axes: A bar chart visualizing the category counts, with the title 'Category Counts'.

    Raises:
    - ValueError: If num_rows is less than 1.
    
    Requirements:
    - pandas
    - random

    Example:
    >>> df, ax = f_746(num_rows=5)
    >>> df
      Category  Value
    0        a     18
    1        a     95
    2        c     14
    3        b     87
    4        b     95
    """
    if num_rows <= 0:
        raise ValueError("num_rows must not be negative")
    random.seed(random_seed)
    df = pd.DataFrame(
        {
            "Category": [
                categories[random.randint(0, len(categories) - 1)]
                for _ in range(num_rows)
            ],
            "Value": [random.randint(1, 100) for _ in range(num_rows)],
        }
    )
    ax = (
        df["Category"]
        .value_counts()
        .plot(kind="bar", title="Category Counts", figsize=(10, 6))
    )
    return df, ax

import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with default parameters
        df, ax = f_746()
        self.assertEqual(len(df), 100)
        self.assertTrue(
            set(df["Category"].unique()).issubset(set(["a", "b", "c", "d", "e"]))
        )
        self.assertTrue(df["Value"].min() >= 1)
        self.assertTrue(df["Value"].max() <= 100)
        self.assertEqual(ax.get_title(), "Category Counts")
    def test_case_2(self):
        # Test num_rows
        for num_rows in [10, 50, 100]:
            df, _ = f_746(num_rows=num_rows)
            self.assertEqual(len(df), num_rows)
    def test_case_3(self):
        # Test edge case - 0 rows
        with self.assertRaises(Exception):
            f_746(num_rows=0)
    def test_case_4(self):
        # Test edge case - invalid num_rows
        with self.assertRaises(Exception):
            f_746(num_rows=-1)
    def test_case_5(self):
        # Test categories
        df, _ = f_746(categories=["x", "y", "z"])
        self.assertTrue(set(df["Category"].unique()).issubset(set(["x", "y", "z"])))
    def test_case_6(self):
        # Test edge case - single category
        df, _ = f_746(categories=["unique"])
        self.assertTrue(
            set(["unique"]).issubset(df["Category"].unique()),
            "Should work with a single category",
        )
    def test_case_7(self):
        # Test edge case - empty categories
        with self.assertRaises(Exception):
            f_746(categories=[])
    def test_case_8(self):
        # Test random seed
        df1, _ = f_746(random_seed=123)
        df2, _ = f_746(random_seed=123)
        df3, _ = f_746(random_seed=124)
        self.assertTrue(
            df1.equals(df2), "DataFrames should be identical with the same seed"
        )
        self.assertFalse(
            df1.equals(df3), "DataFrames should differ with different seeds"
        )
    def test_case_9(self):
        # Test visualization
        categories = ["x", "y", "z"]
        _, ax = f_746(num_rows=100, categories=categories, random_seed=42)
        ax_categories = [tick.get_text() for tick in ax.get_xticklabels()]
        self.assertListEqual(
            sorted(categories),
            sorted(ax_categories),
            "X-axis categories should match input categories",
        )
    def tearDown(self):
        plt.close("all")
