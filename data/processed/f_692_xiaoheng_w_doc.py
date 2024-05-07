import re
from nltk.stem import PorterStemmer

def f_766(text_series):
    """
    Process a pandas Series of text data by lowercasing all letters, removing non-alphanumeric 
    characters (except spaces), removing punctuation, and stemming each word to its root form.
    
    Stemming is done using the NLTK's PorterStemmer, which applies a series of rules to find the stem of each word.
    
    Parameters:
    - text_series (pandas.Series): A Series object containing string entries representing text data.

    Requirements:
    - re
    - nltk

    Returns:
    - pandas.Series: A Series where each string has been processed to remove non-alphanumeric characters,
      punctuation, converted to lowercase, and where each word has been stemmed.
    
    Examples:
    >>> input_series = pd.Series(["This is a sample text.", "Another example!"])
    >>> output_series = f_766(input_series)
    >>> print(output_series.iloc[0])
    thi is a sampl text
    >>> print(output_series.iloc[1])
    anoth exampl

    """
    stemmer = PorterStemmer()
    def process_text(text):
        text = re.sub('[^\sa-zA-Z0-9]', '', text).lower().strip()
        text = " ".join([stemmer.stem(word) for word in text.split()])
        return text
    return text_series.apply(process_text)

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    
    def test_lowercase_and_stemming(self):
        """
        Test case to ensure that all text is converted to lowercase and words are stemmed properly.
        """
        input_series = pd.Series(["THIS IS A TEST.", "Test, case number 2!"])
        expected_output = pd.Series(["thi is a test", "test case number 2"])
        processed_series = f_766(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)
    def test_numerics_and_special_characters(self):
        """
        Test case to verify that numeric characters are retained and special characters are removed.
        """
        input_series = pd.Series(["Another Test 123.", "456 Anoth3r one!"])
        expected_output = pd.Series(["anoth test 123", "456 anoth3r one"])
        processed_series = f_766(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)
    def test_empty_strings(self):
        """
        Test case to check the function's handling of empty strings.
        """
        input_series = pd.Series(["", " "])
        expected_output = pd.Series(["", ""])
        processed_series = f_766(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)
    def test_punctuation(self):
        """
        Test case to check that punctuation is removed from the text.
        """
        input_series = pd.Series(["Punctuation! Should, be: removed; right?"])
        expected_output = pd.Series(["punctuat should be remov right"])
        processed_series = f_766(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)
    def test_stemconsistency(self):
        """
        Test case to ensure that stemming is consistent across different forms of words.
        """
        input_series = pd.Series(["Stemming should work on words like running", "stemmed works on stemmed"])
        expected_output = pd.Series(["stem should work on word like run", "stem work on stem"])
        processed_series = f_766(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)
