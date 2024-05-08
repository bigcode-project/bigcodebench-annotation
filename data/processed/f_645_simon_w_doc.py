import nltk
from string import punctuation
import pandas as pd


def f_607(text):
    """
    Finds all words in a text, that are seperated by whitespace, 
    beginning with the "$" character and computes their number of occurences.

    Parameters:
    text (str): The input text.

    Returns:
    DataFrame: A pandas DataFrame with two columns: "Word" and "Frequency". 
               "Word" contains the '$' prefixed words, and "Frequency" contains their occurrences.

               
    Raises:
    ValueError: if text is not a string
    
    Requirements:
    - nltk
    - string
    - pandas

    Note:
    The function ignores words that are entirely made up of punctuation, even if they start with a '$'.

    Example:
    >>> text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
    >>> f_607(text)
       Word  Frequency
    0  $abc          3
    1  $efg          1
    2  $hij          3

    >>> text = "$hello this i$s a $test $test $test"
    >>> f_607(text)
         Word  Frequency
    0  $hello          1
    1   $test          3
    """
    if not isinstance(text, str):
        raise ValueError("The input should be a string.")
    tk = nltk.WhitespaceTokenizer()
    words = tk.tokenize(text)    
    dollar_words = [word for word in words if word.startswith('$') and not all(c in set(punctuation) for c in word)]
    freq = nltk.FreqDist(dollar_words)
    df = pd.DataFrame(list(freq.items()), columns=["Word", "Frequency"])
    return df

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
        result = f_607(text)
        expected_words = ["$abc", "$efg", "$hij"]
        expected_freqs = [3, 1, 3]
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_2(self):
        text = "This is a test without dollar words."
        result = f_607(text)
        self.assertEqual(len(result), 0)
    def test_case_3(self):
        text = "$test1 $test2 $test1 $test3"
        result = f_607(text)
        expected_words = ["$test1", "$test2", "$test3"]
        expected_freqs = [2, 1, 1]
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_4(self):
        text = "$! $$ $a $a $a"
        result = f_607(text)
        expected_words = ["$a"]
        expected_freqs = [3]
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_5(self):
        text = "$word1 word2 $word2 $word1 $word3 $word1"
        result = f_607(text)
        expected_words = ["$word1", "$word2", "$word3"]
        expected_freqs = [3, 1, 1]
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_6(self):
        '''empty input string'''
        text = ""
        result = f_607(text)
        expected_words = []
        expected_freqs = []
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    
    def test_case_7(self):
        '''check for correct return type'''
        text = "$test 123 abcd.aef"
        result = f_607(text)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Word' in result.columns)
        self.assertTrue('Frequency' in result.columns)
    def test_case_8(self):
        '''word with $ in the middle'''
        text = "asdfj;alskdfj;$kjhkjhdf"
        result = f_607(text)
        expected_words = []
        expected_freqs = []
        self.assertListEqual(result["Word"].tolist(), expected_words)
        self.assertListEqual(result["Frequency"].tolist(), expected_freqs)
    def test_case_9(self):
        '''non string input'''
        input = 24
        self.assertRaises(Exception, f_607, input)
