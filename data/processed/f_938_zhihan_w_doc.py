from nltk.tokenize import RegexpTokenizer
from collections import Counter


def f_958(text):
    """
    Identifies and counts words in a given text that start with the "$" symbol. It returns the five most frequent
    dollar-prefixed words along with their counts. Words solely consisting of "$" symbols without any following
    alphanumeric characters are ignored in the frequency count.

    Parameters:
    - text (str): The input text to analyze.

    Returns:
    - list of tuples: Each tuple contains a dollar-prefixed word (excluding the "$" symbol) and its frequency,
                      ordered by most to least common.

    Requirements:
    - nltk.tokenize.RegexpTokenizer
    - collections.Counter

    Example:
    >>> text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
    >>> f_958(text)
    [('abc', 3), ('hij', 3), ('efg', 1)]
    """
    tokenizer = RegexpTokenizer(r'\$\$+\w*|\$\w+')
    dollar_prefixed_words = tokenizer.tokenize(text)
    normalized_words = [word.lstrip("$") if len(word.lstrip("$")) > 0 else word for word in dollar_prefixed_words]
    word_counts = Counter(normalized_words)
    return word_counts.most_common(5)

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
        expected_output = [('abc', 3), ('hij', 3), ('efg', 1)]
        result = f_958(text)
        self.assertEqual(result, expected_output)
    def test_case_2(self):
        text = "This is a test without any $ prefixed words."
        expected_output = []
        result = f_958(text)
        self.assertEqual(result, expected_output)
    def test_case_3(self):
        text = "$apple $banana $apple $cherry $cherry $cherry"
        expected_output = [('cherry', 3), ('apple', 2), ('banana', 1)]
        result = f_958(text)
        self.assertEqual(result, expected_output)
    def test_case_4(self):
        text = "$$ $$ $$ $$"
        expected_output = [('$$', 4)]
        result = f_958(text)
        self.assertEqual(result, expected_output)
    def test_case_5(self):
        text = "$word1 $word2 $word3 $word4 $word5 $word6"
        expected_output = [('word1', 1), ('word2', 1), ('word3', 1), ('word4', 1), ('word5', 1)]
        result = f_958(text)
        self.assertEqual(result, expected_output)
