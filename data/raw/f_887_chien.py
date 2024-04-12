import pandas as pd
import matplotlib.pyplot as plt

# Constants
CATEGORIES = ["A", "B", "C", "D", "E"]


def f_887(data_list):
    """
    Processes a list of category labels to create a histogram that visualizes their distribution.
    This histogram compares the distribution of a predefined set of categories (A, B, C, D, E)
    with any additional categories found in the input list.

    Parameters:
    - data_list (list): A list containing category labels (strings).

    Returns:
    - Axes object (matplotlib.axes._subplots.AxesSubplot): The histogram displaying the distribution of categories.

    Requirements:
    - pandas
    - matplotlib

    Notes:
    - The function evaluates the distribution of predefined categories ('A', 'B', 'C', 'D', 'E') and checks for uniformity.
    - Categories in the data_list that are not among the predefined categories are identified and included in the histogram.
    - The ax.bar call in the function creates a bar plot on the axes object. It uses the following parameters:
        * all_categories: The categories to be displayed on the x-axis, including both predefined and extra categories.
        * category_counts.reindex(all_categories, fill_value=0): The counts of each category, where categories not found
          in the data_list are assigned a count of 0.
        * width=0.8: Sets the width of the bars in the bar plot.
        * align="center": Aligns the bars with the center of the x-ticks.

    Raises:
    - ValueError: If the input data_list is empty, the function raises a ValueError with the message "The data list is empty."
      In this case, no histogram is generated and the function terminates.


    Example:
    >>> data = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    >>> ax = f_887(data)
    >>> ax.get_xticks()
    array([0., 1., 2., 3., 4., 5., 6.])
    """

    if not data_list:
        raise ValueError("The data list is empty.")

    data_series = pd.Series(data_list)
    category_counts = data_series.value_counts()

    # Prepare data for predefined categories
    predefined_counts = category_counts.reindex(CATEGORIES, fill_value=0)

    # Check for uniformity in predefined categories
    if not all(x == predefined_counts.iloc[0] for x in predefined_counts):
        print("The distribution of predefined categories is not uniform.")

    # Handling extra categories not in predefined list
    extra_categories = category_counts.drop(CATEGORIES, errors="ignore").index.tolist()
    all_categories = CATEGORIES + extra_categories

    _, ax = plt.subplots()
    ax.bar(
        all_categories,
        category_counts.reindex(all_categories, fill_value=0),
        width=0.8,
        align="center",
    )
    ax.set_xticks(all_categories)

    return ax


import unittest
from unittest.mock import patch
import io


class TestCases(unittest.TestCase):
    """Tests for the function."""

    def test_empty_list(self):
        """
        Test the function with an empty list. Expects ValueError.
        """
        with self.assertRaises(ValueError):
            f_887([])

    def test_uniform_distribution(self):
        """
        Test the function with a uniform distribution of predefined categories.
        Expects no printed warning about non-uniform distribution.
        """
        data = ["A", "B", "C", "D", "E"] * 2
        with patch("sys.stdout", new=io.StringIO()) as fake_output:
            f_887(data)
        self.assertNotIn(
            "The distribution of predefined categories is not uniform.",
            fake_output.getvalue(),
        )

    def test_non_uniform_distribution(self):
        """
        Test the function with a non-uniform distribution of predefined categories.
        Expects a printed warning about non-uniform distribution.
        """
        data = ["A", "A", "B", "C", "D", "E"]
        with patch("sys.stdout", new=io.StringIO()) as fake_output:
            f_887(data)
        self.assertIn(
            "The distribution of predefined categories is not uniform.",
            fake_output.getvalue(),
        )

    def test_extra_categories(self):
        """
        Test the function with extra categories not in the predefined list.
        Expects extra categories to be included in the histogram.
        """
        data = ["A", "B", "C", "D", "E", "F", "G"]
        ax = f_887(data)
        self.assertIn("F", [tick.get_text() for tick in ax.get_xticklabels()])
        self.assertIn("G", [tick.get_text() for tick in ax.get_xticklabels()])

    def test_no_extra_categories(self):
        """
        Test the function with no extra categories.
        Expects only predefined categories to be included in the histogram.
        """
        data = ["A", "B", "C", "D", "E"]
        ax = f_887(data)
        for extra_cat in ["F", "G"]:
            self.assertNotIn(
                extra_cat, [tick.get_text() for tick in ax.get_xticklabels()]
            )

    def tearDown(self):
        plt.clf()

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
