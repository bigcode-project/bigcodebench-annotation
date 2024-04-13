import nltk
from string import punctuation
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
PUNCTUATION = set(punctuation)


def f_102(text):
    """
    Draw a bar chart of the frequency of words in a text beginning with the "$" character. Words that start with the '$' character but consist only of punctuation (e.g., '$$') are not included in the frequency count.
    - If there is no word respecting the above conditions, the plot should be None.
    - The barplot x words on the x-axis and frequencies on the y-axis.

    Parameters:
        - text (str): The input text.
    Returns:
        - matplotlib.axes._subplots.AxesSubplot: The plot showing the frequency of words beginning with the '$' character.

    Requirements:
        - nltk
        - string
        - seaborn
        - matplotlib

    Example:
    >>> text = "$child than resource indicate star $community station onto best green $exactly onto then age charge $friend than ready child really $let product coach decision professional $camera life off management factor $alone beat idea bit call $campaign fill stand Congress stuff $performance follow your resource road $data performance himself school here"
    >>> ax = f_102(text)
    """
    words = text.split()
    dollar_words = [
        word
        for word in words
        if word.startswith("$")
        and not all(c in PUNCTUATION for c in word)
        and len(word) > 1
    ]
    freq = nltk.FreqDist(dollar_words)
    if not freq:  # If frequency distribution is empty, return None
        return None
    plt.figure(figsize=(10, 5))
    sns.barplot(x=freq.keys(), y=freq.values())
    return plt.gca()


import unittest


class TestCases(unittest.TestCase):
    """Test cases for the f_102 function."""

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
        # Randomly generated sentence with $ words
        text = "This is the $first $first sentence."
        plot = f_102(text)
        self.assertIsInstance(plot, plt.Axes, "Return type should be a plot (Axes).")
        self.is_bar(plot, expected_categories=["$first"], expected_values=[2.0])

    def test_case_2(self):
        # Another randomly generated sentence with $ words
        text = "This $is $is $is the $second $sentence $sentence"
        plot = f_102(text)
        self.assertIsInstance(plot, plt.Axes, "Return type should be a plot (Axes).")
        self.is_bar(
            plot,
            expected_categories=["$is", "$second", "$sentence"],
            expected_values=[3.0, 1.0, 2.0],
        )

    def test_case_3(self):
        # Sentence without any $ words
        text = "This is the third sentence."
        plot = f_102(text)
        self.assertIsNone(plot, "The plot should be None since there are no $ words.")

    def test_case_4(self):
        # Sentence with all $ words being single characters or punctuation
        text = "$ $! $@ $$"
        plot = f_102(text)
        self.assertIsNone(
            plot,
            "The plot should be None since all $ words are single characters or punctuation.",
        )

    def test_case_5(self):
        # Mix of valid $ words and punctuation-only $ words with some repeated words
        text = "$apple $apple $banana $!$ $@ fruit $cherry"
        plot = f_102(text)
        self.assertIsInstance(plot, plt.Axes, "Return type should be a plot (Axes).")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()