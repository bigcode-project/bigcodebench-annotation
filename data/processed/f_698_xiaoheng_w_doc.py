import re
from nltk.corpus import stopwords
from collections import Counter

STOPWORDS = set(stopwords.words('english'))

def f_713(input_string):
    """
    Divide a multi-line string into individual lines, remove stopwords, and count the frequency of each word.

    Parameters:
    - input_string (str): The multi-line string.

    Returns:
    - dict: A dictionary with word frequencies where each key is a unique word and the value is its frequency.

    Requirements:
    - re
    - nltk.corpus
    - collections

    Example:
    >>> f_713('line a\\nfollows by line b\\n...bye\\n')
    {'line': 2, 'follows': 1, 'b': 1, 'bye': 1}
    """
    lines = input_string.split('\n')
    word_count = Counter()
    for line in lines:
        words = re.findall(r'\b\w+\b', line)
        words = [word for word in words if word not in STOPWORDS]
        word_count.update(words)
    return dict(word_count)

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_string = "This is line one.\nThis is line two."
        expected_output = {'This': 2, 'line': 2, 'one': 1, 'two': 1}
        self.assertEqual(f_713(input_string), expected_output)
    def test_case_2(self):
        input_string = "apple orange apple\norange apple\napple"
        expected_output = {'apple': 4, 'orange': 2}
        self.assertEqual(f_713(input_string), expected_output)
    def test_case_3(self):
        input_string = "This\nThis\nThis"
        expected_output = {'This': 3}
        self.assertEqual(f_713(input_string), expected_output)
    def test_case_4(self):
        input_string = "This is a test.\nThis is only a test."
        expected_output = {'This': 2, 'test': 2}
        self.assertEqual(f_713(input_string), expected_output)
    def test_case_5(self):
        input_string = "Stop this\nStop"
        expected_output = {'Stop': 2}
        self.assertEqual(f_713(input_string), expected_output)
