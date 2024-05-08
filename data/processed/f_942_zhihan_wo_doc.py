import re
from collections import Counter


def f_962(text, top_n):
    """
    Count the N most common words in a text after removing URLs.

    Parameters:
    text (str): The text to analyze.
    top_n (int): The number of top words to return.

    Returns:
    list: A list of tuples where each tuple contains a word and its frequency.

    Requirements:
    - re
    - collections.Counter

    Example:
    >>> f_962('Visit https://www.python.org for more info. Python is great. I love Python.', 2)
    [('Python', 2), ('Visit', 1)]

    Note:
    - Valid url is start with http or https
    """
    text = re.sub('http[s]?://\S+', '', text)
    words = re.findall(r'\b\w+\b', text)
    word_freq = Counter(words)
    return word_freq.most_common(top_n)

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_962('Python is great. I love Python.', 2)
        expected = [('Python', 2), ('is', 1)]
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = f_962('Visit https://www.python.org for more info. Python is great. I love Python.', 2)
        expected = [('Python', 2), ('Visit', 1)]
        self.assertEqual(result, expected)
    def test_case_3(self):
        text = 'Visit https://www.python.org and http://www.example.com. Python é ótimo! Adoro Python!'
        result = f_962(text, 2)
        expected = [('Python', 2), ('Visit', 1)]
        self.assertEqual(result, expected)
    def test_case_4(self):
        result = f_962('', 2)
        expected = []
        self.assertEqual(result, expected)
    def test_case_5(self):
        result = f_962('Hello, world! How are you?', 2)
        expected = [('Hello', 1), ('world', 1)]
        self.assertEqual(result, expected)
