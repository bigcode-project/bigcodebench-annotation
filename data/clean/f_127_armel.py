import re
import pandas as pd

STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]


def f_127(text):
    """
    Given a text as input, the function should split it into multiple sentences and build a dictionary where each key is associated with a sentence and the corresponding value is the number of words in the sentence. The function returns a pandas Series built from the dictionary.
    - The keys of the dictionary (which correspond to the Index of the pandas Series) should be named "Sentence 1", "Sentence 2" etc.
    - When counting the words in a sentence, do not consider those included in the constant STOPWORDS.
    - Do not consider empty sentences.

    Parameters:
    text (str): The text to analyze.

    Returns:
    pandas.core.series.Series: A pandas Series each sentence and its number of words that are not in STOPWORDS.

    Requirements:
    - pandas
    - regex

    Example:
    >>> text = "This is a sample sentence. This sentence contains sample words."
    >>> df = f_127("I am good at programming. I learned it in college.")
    >>> print(df)
    Sentence 1    5
    Sentence 2    5
    dtype: int64
    """
    sentences = re.split(r"\.\s*", text)
    sentence_counts = {}

    for i, sentence in enumerate(sentences):
        if sentence.strip() == "":
            continue
        words = re.split(r"\s+", sentence.lower())
        words = [word for word in words if word not in STOPWORDS]
        sentence_counts[f"Sentence {i+1}"] = len(words)

    sentence_counts = pd.Series(sentence_counts)
    return sentence_counts


import unittest


class TestCases(unittest.TestCase):
    """Test cases for the f_127 function."""

    def test_case_1(self):
        text = "This is a sample sentence. This sentence contains sample words."
        expected_output = pd.Series({"Sentence 1": 5, "Sentence 2": 4})
        result = f_127(text)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_2(self):
        text = "Hello. My name is Marc. I'm here to help. How can I assist you today?"
        expected_output = pd.Series(
            {"Sentence 1": 1, "Sentence 2": 4, "Sentence 3": 3, "Sentence 4": 6}
        )
        result = f_127(text)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_3(self):
        text = "This is a test. Stopwords are words which do not contain important meaning."
        expected_output = pd.Series({"Sentence 1": 4, "Sentence 2": 7})
        result = f_127(text)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_4(self):
        text = "Hello! How are you? I'm fine, thanks."
        expected_output = pd.Series(
            {"Sentence 1": 6}
        )  # Only the last sentence is split by a period
        result = f_127(text)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_5(self):
        text = ""
        expected_output = pd.Series()
        result = f_127(text)
        pd.testing.assert_series_equal(result, expected_output)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
