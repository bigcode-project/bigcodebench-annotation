import re
import pandas as pd


def f_381(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    """
    Reverse the order of words in a specific column of a pandas DataFrame where the words
    match a user-specified regular expression pattern, using a nested helper function.
    Words are considered to be whitespace-separated strings. This function maintains the
    original order of non-matching words.

    Parameters:
    - df (pd.DataFrame): The pandas DataFrame.
    - column_name (str): The name of the column to be modified.
    - pattern (str), the regular expression pattern to match words against.

    Returns:
    - pd.DataFrame: A new pandas DataFrame with the specified column's words reordered
    if they match the pattern, maintaining the original order of words that do not match,
    and returning a copy of the unaltered DataFrame if the pattern is empty.

    Requirements:
    - pandas
    - re

    Example:
    >>> df = pd.DataFrame({'A': ['apple orange', 'red yellow green'], 'B': [1, 2]})
    >>> pattern = r'\b(?:apple|yellow)\b'
    >>> reversed_df = f_381(df, 'A', pattern)
    >>> reversed_df
                      A  B
    0      apple orange  1
    1  red yellow green  2
    >>> df = pd.DataFrame({'A': ['yellow car red', 'green apple yellow'], 'B': [3, 4]})
    >>> pattern = r'\b(?:car|apple|yellow)\b'
    >>> reversed_df = f_381(df, 'A', pattern)
    >>> reversed_df
                        A  B
    0      yellow car red  3
    1  green apple yellow  4
    """

    def reverse_matched_words(text):
        words = text.split()
        matched_words = [word for word in words if re.search(pattern, word)][::-1]
        new_words = [
            matched_words.pop(0) if re.search(pattern, word) else word for word in words
        ]
        return " ".join(new_words)

    new_df = df.copy()
    if not pattern:
        return new_df
    new_df[column_name] = new_df[column_name].apply(reverse_matched_words)
    return new_df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # Example df to test for error handling
        self.df = pd.DataFrame(
            {"A": ["blue car red", "green apple yellow"], "B": [3, 4]}
        )
    def test_case_1(self):
        # Test case where no words match the pattern
        df = pd.DataFrame({"Text": ["apple orange", "blue red"], "Number": [1, 2]})
        pattern = r"\b(?:banana|green)\b"
        expected = df.copy()
        result = f_381(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_2(self):
        # Test case where all words in a column match the pattern
        df = pd.DataFrame({"Text": ["apple banana", "banana apple"], "Number": [1, 2]})
        pattern = r"\b(?:apple|banana)\b"
        expected = pd.DataFrame(
            {"Text": ["banana apple", "apple banana"], "Number": [1, 2]}
        )
        result = f_381(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_3(self):
        # Test case with a mix of matching and non-matching words
        df = pd.DataFrame(
            {"Text": ["apple orange banana", "blue apple green"], "Number": [1, 2]}
        )
        pattern = r"\b(?:apple|banana)\b"
        expected = pd.DataFrame(
            {"Text": ["banana orange apple", "blue apple green"], "Number": [1, 2]}
        )
        result = f_381(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_4(self):
        # Test case where the column contains an empty string
        df = pd.DataFrame({"Text": ["", "apple banana"], "Number": [1, 2]})
        pattern = r"\b(?:apple|banana)\b"
        expected = pd.DataFrame({"Text": ["", "banana apple"], "Number": [1, 2]})
        result = f_381(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_5(self):
        # Test case where the pattern is an empty string (matches nothing)
        df = pd.DataFrame({"Text": ["apple orange", "banana apple"], "Number": [1, 2]})
        pattern = ""
        expected = df.copy()
        result = f_381(df, "Text", pattern)
        pd.testing.assert_frame_equal(expected, result)
    def test_case_6(self):
        # Test the function with a column name that does not exist in the DataFrame
        with self.assertRaises(KeyError):
            f_381(self.df, "NonexistentColumn", r"\b(?:car|apple|yellow)\b")
    def test_case_7(self):
        # Test the function with a non-string column name
        with self.assertRaises(KeyError):
            f_381(self.df, 123, r"\b(?:car|apple|yellow)\b")
    def test_case_8(self):
        # Test the function with an invalid regular expression pattern
        with self.assertRaises(re.error):
            f_381(self.df, "A", r"\b(?:car|apple|yellow")
