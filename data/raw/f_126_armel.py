import pandas as pd
import regex as re
from sklearn.feature_extraction.text import CountVectorizer


def f_126(text):
    """
    Analyze a text by creating a document term matrix with CountVectorizer. The text contains several sentences, each separated by a period.
    Ignore empty sentences.

    Parameters:
    text (str): The text to analyze.

    Returns:
    DataFrame: A pandas DataFrame with the document-term matrix. It column names should be adapted from the vectorizer feature names.

    Requirements:
    - pandas
    - regex
    - sklearn.feature_extraction.text.CountVectorizer

    Example:
    >>> text = "This is a sample sentence. This sentence contains sample words."
    >>> dtm = f_126(text)
    >>> print(dtm)
    """
    sentences = re.split(r"\.\s*", text)
    sentences = [sentence for sentence in sentences if len(sentence.strip()) != 0]
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(sentences)
    df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    return df


import unittest


class TestCases(unittest.TestCase):
    """Test cases for the f_126 function."""

    def test_case_1(self):
        # Test with a basic input
        text = "This is a sample sentence. This sentence contains sample words."
        dtm = f_126(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (2, 6)
        )  # Expected 2 rows (sentences) and 6 unique words
        self.assertEqual(dtm["sample"].tolist(), [1, 1])
        self.assertEqual(dtm["this"].tolist(), [1, 1])

    def test_case_2(self):
        # Test with a single sentence (with a trailing period)
        text = "A single sentence."
        dtm = f_126(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (1, 2)
        )  # Expected 1 rows (sentences) and 2 unique words
        self.assertEqual(dtm["single"].tolist(), [1])

    def test_case_3(self):
        # Test with no periods (still should consider it as one sentence)
        text = "No periods in this text"
        dtm = f_126(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (1, 5)
        )  # Expected 1 row (sentence) and 5 unique words
        self.assertEqual(dtm["text"].tolist(), [1])

    def test_case_4(self):
        # Test with a single sentence (with same word multiple times)
        text = ("test test test test test test test test test test test " * 3).strip()
        dtm = f_126(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (1, 1)
        )  # Expected 1 row (sentence) and 1 unique words
        self.assertEqual(dtm["test"].tolist(), [33])

    def test_case_5(self):
        # Test with no periods (still should consider it as one sentence)
        text = "This is the first sentence. This is the second sentence. This is the third sentence. This is the fourth sentence. This is the fith and last sentence."
        dtm = f_126(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (5, 11)
        )  # Expected 5 rows (sentence) and 11 unique words
        self.assertEqual(dtm["this"].tolist(), [1, 1, 1, 1, 1])
        self.assertEqual(dtm["is"].tolist(), [1, 1, 1, 1, 1])
        self.assertEqual(dtm["the"].tolist(), [1, 1, 1, 1, 1])
        self.assertEqual(dtm["sentence"].tolist(), [1, 1, 1, 1, 1])


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
