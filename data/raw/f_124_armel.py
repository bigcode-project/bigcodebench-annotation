import pandas as pd
import regex as re

# Constants
STOPWORDS = ["a", "an", "the", "in", "is", "are"]


def f_124(text):
    """
    Count the frequency of each word in a text after removing specific stopwords.

    Parameters:
    text (str): The text to analyze.

    Returns:
    Series: A pandas Series with word frequencies excluding the words in STOPWORDS list.

    Requirements:
    - pandas
    - regex

    Example:
    >>> text = "This is a sample text. This text contains sample words."
    >>> word_counts = f_124(text)
    >>> print(word_counts)
    this        2
    sample      2
    text        2
    contains    1
    words       1
    dtype: int64
    """
    words = re.findall(r"\b\w+\b", text.lower())
    words = [word for word in words if word not in STOPWORDS]
    word_counts = pd.Series(words).value_counts().rename(None)
    return word_counts


import unittest


class TestCases(unittest.TestCase):
    """Test cases for the f_124 function."""

    def test_case_1(self):
        text = "This is a sample text This text contains sample words"
        word_counts = f_124(text).to_dict()
        expected_counts = {"this": 2, "sample": 2, "text": 2, "contains": 1, "words": 1}
        self.assertDictEqual(word_counts, expected_counts)

    def test_case_2(self):
        text = "Hello world Hello everyone"
        word_counts = f_124(text).to_dict()
        expected_counts = {"hello": 2, "world": 1, "everyone": 1}
        self.assertDictEqual(word_counts, expected_counts)

    def test_case_3(self):
        text = "a an the in is are"
        word_counts = f_124(text).to_dict()
        expected_counts = {}
        self.assertDictEqual(word_counts, expected_counts)

    def test_case_4(self):
        text = "This is a test sentence which has a bunch of words and no period"
        word_counts = f_124(text).to_dict()
        expected_counts = {
                "this": 1,
                "test": 1,
                "sentence": 1,
                "which": 1,
                "has": 1,
                "bunch": 1,
                "of": 1,
                "words": 1,
                "and": 1,
                "no": 1,
                "period": 1,
            }

        self.assertDictEqual(word_counts, expected_counts)

    def test_case_5(self):
        text = (
            "I I I want want to to to to to go to to to the olympics olympics this year"
        )
        word_counts = f_124(text).to_dict()
        expected_counts = {"i": 3, "want": 2, "to": 8, "go": 1, "olympics": 2, "this": 1, "year": 1}
        self.assertDictEqual(word_counts, expected_counts)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
