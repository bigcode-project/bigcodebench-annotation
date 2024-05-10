import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def task_func(list_of_pairs):
    """
    Create a Pandas DataFrame from a list of pairs and visualize the data using a bar chart.
    - The title of the barplot should be set to 'Category vs Value'`.

    Parameters:
    list_of_pairs (list of tuple): Each tuple contains:
        - str: Category name.
        - int: Associated value.

    Returns:
    tuple:
        - DataFrame: A pandas DataFrame with columns 'Category' and 'Value'.
        - Axes: A matplotlib Axes displaying a bar chart of categories vs. values.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - seaborn

    Example:
    >>> list_of_pairs = [('Fruits', 5), ('Vegetables', 9)]
    >>> df, ax = task_func(list_of_pairs)
    >>> print(df)
         Category  Value
    0      Fruits      5
    1  Vegetables      9
    """
    df = pd.DataFrame(list_of_pairs, columns=["Category", "Value"])
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Category", y="Value", data=df)
    plt.title("Category vs Value")
    ax = plt.gca()
    return df, ax

import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    @staticmethod
    def is_bar(ax, expected_values, expected_categories):
        extracted_values = [
            bar.get_height() for bar in ax.patches
        ]  # extract bar height
        extracted_categories = [
            tick.get_text() for tick in ax.get_xticklabels()
        ]  # extract category label
        for actual_value, expected_value in zip(extracted_values, expected_values):
            assert (
                actual_value == expected_value
            ), f"Expected value '{expected_value}', but got '{actual_value}'"
        for actual_category, expected_category in zip(
            extracted_categories, expected_categories
        ):
            assert (
                actual_category == expected_category
            ), f"Expected category '{expected_category}', but got '{actual_category}'"
    def test_case_1(self):
        df, ax = task_func(
            [
                ("Allison", 49),
                ("Cassidy", 72),
                ("Jamie", -74),
                ("Randy", -25),
                ("Joshua", -85),
            ]
        )
        # Testing the DataFrame
        self.assertEqual(
            df["Category"].tolist(), ["Allison", "Cassidy", "Jamie", "Randy", "Joshua"]
        )
        self.assertEqual(df["Value"].tolist(), [49, 72, -74, -25, -85])
        # Testing the plot title
        self.assertEqual(ax.get_title(), "Category vs Value")
        self.is_bar(
            ax=ax,
            expected_categories=["Allison", "Cassidy", "Jamie", "Randy", "Joshua"],
            expected_values=[49, 72, -74, -25, -85],
        )
    def test_case_2(self):
        df, ax = task_func(
            [
                ("Jonathan", 36),
                ("Maureen", 47),
                ("Zachary", -32),
                ("Kristen", 39),
                ("Donna", -23),
            ]
        )
        # Testing the DataFrame
        self.assertEqual(
            df["Category"].tolist(),
            ["Jonathan", "Maureen", "Zachary", "Kristen", "Donna"],
        )
        self.assertEqual(df["Value"].tolist(), [36, 47, -32, 39, -23])
        # Testing the plot title
        self.assertEqual(ax.get_title(), "Category vs Value")
    def test_case_3(self):
        df, ax = task_func(
            [
                ("Eric", -91),
                ("Jennifer", 52),
                ("James", -79),
                ("Matthew", 25),
                ("Veronica", 2),
            ]
        )
        # Testing the DataFrame
        self.assertEqual(
            df["Category"].tolist(),
            ["Eric", "Jennifer", "James", "Matthew", "Veronica"],
        )
        self.assertEqual(df["Value"].tolist(), [-91, 52, -79, 25, 2])
        # Testing the plot title
        self.assertEqual(ax.get_title(), "Category vs Value")
    def test_case_4(self):
        df, ax = task_func(
            [
                ("Caitlin", -82),
                ("Austin", 64),
                ("Scott", -11),
                ("Brian", -16),
                ("Amy", 100),
            ]
        )
        # Testing the DataFrame
        self.assertEqual(
            df["Category"].tolist(), ["Caitlin", "Austin", "Scott", "Brian", "Amy"]
        )
        self.assertEqual(df["Value"].tolist(), [-82, 64, -11, -16, 100])
        # Testing the plot title
        self.assertEqual(ax.get_title(), "Category vs Value")
    def test_case_5(self):
        df, ax = task_func(
            [
                ("Justin", 96),
                ("Ashley", 33),
                ("Daniel", 41),
                ("Connie", 26),
                ("Tracy", 10),
            ]
        )
        # Testing the DataFrame
        self.assertEqual(
            df["Category"].tolist(), ["Justin", "Ashley", "Daniel", "Connie", "Tracy"]
        )
        self.assertEqual(df["Value"].tolist(), [96, 33, 41, 26, 10])
        # Testing the plot title
        self.assertEqual(ax.get_title(), "Category vs Value")
    def test_case_6(self):
        df, ax = task_func(
            [
                ("Vanessa", -115),
                ("Roberto", -267),
                ("Barbara", 592),
                ("Amanda", 472),
                ("Rita", -727),
                ("Christopher", 789),
                ("Brandon", 457),
                ("Kylie", -575),
                ("Christina", 405),
                ("Dylan", 265),
            ]
        )
        # Testing the DataFrame
        self.assertEqual(
            df["Category"].tolist(),
            [
                "Vanessa",
                "Roberto",
                "Barbara",
                "Amanda",
                "Rita",
                "Christopher",
                "Brandon",
                "Kylie",
                "Christina",
                "Dylan",
            ],
        )
        self.assertEqual(
            df["Value"].tolist(), [-115, -267, 592, 472, -727, 789, 457, -575, 405, 265]
        )
        # Testing the plot title
        self.assertEqual(ax.get_title(), "Category vs Value")
    def test_case_7(self):
        df, ax = task_func(
            [
                ("Kevin", -896),
                ("Kirk", 718),
                ("Cathy", -328),
                ("Ryan", -605),
                ("Peter", -958),
                ("Brenda", -266),
                ("Laura", 117),
                ("Todd", 807),
                ("Ann", 981),
                ("Kimberly", -70),
            ]
        )
        # Testing the DataFrame
        self.assertEqual(
            df["Category"].tolist(),
            [
                "Kevin",
                "Kirk",
                "Cathy",
                "Ryan",
                "Peter",
                "Brenda",
                "Laura",
                "Todd",
                "Ann",
                "Kimberly",
            ],
        )
        self.assertEqual(
            df["Value"].tolist(),
            [-896, 718, -328, -605, -958, -266, 117, 807, 981, -70],
        )
        # Testing the plot title
        self.assertEqual(ax.get_title(), "Category vs Value")
    def test_case_8(self):
        df, ax = task_func(
            [
                ("Samuel", -366),
                ("Kathy", -267),
                ("Michael", -379),
                ("Teresa", 926),
                ("Stephanie", -73),
                ("Joy", -892),
                ("Robert", 988),
                ("Jenna", -362),
                ("Jodi", 816),
                ("Carlos", 981),
            ]
        )
        # Testing the DataFrame
        self.assertEqual(
            df["Category"].tolist(),
            [
                "Samuel",
                "Kathy",
                "Michael",
                "Teresa",
                "Stephanie",
                "Joy",
                "Robert",
                "Jenna",
                "Jodi",
                "Carlos",
            ],
        )
        self.assertEqual(
            df["Value"].tolist(),
            [-366, -267, -379, 926, -73, -892, 988, -362, 816, 981],
        )
        # Testing the plot title
        self.assertEqual(ax.get_title(), "Category vs Value")
