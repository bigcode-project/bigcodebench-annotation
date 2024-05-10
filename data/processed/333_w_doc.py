import re
from collections import Counter
from nltk.corpus import stopwords


def task_func(text: str) -> dict:
    """
    Count the number of non-stop words in a given text.
    
    Parameters:
    - text (str): The input text for word counting.
    
    Returns:
    dict: A dictionary with the words (as keys) and their counts (as values).
    
    Requirements:
    - re
    - collections.Counter
    
    Example:
    >>> count = task_func("This is a sample text. Some words are repeated.")
    >>> print(count)
    {'sample': 1, 'text': 1, 'words': 1, 'repeated': 1}
    """
    words = re.findall(r'\b\w+\b', text)
    non_stopwords = [word for word in words if word.lower() not in set(stopwords.words('english'))]
    count = dict(Counter(non_stopwords))
    return count

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Simple sentence with some stopwords
        input_text = "This is a simple test."
        expected_output = {'simple': 1, 'test': 1}
        self.assertDictEqual(task_func(input_text), expected_output)
    def test_case_2(self):
        # Longer sentence with repeated words
        input_text = "Some words are repeated more than once. Repeated words are common."
        expected_output = {'words': 2, 'repeated': 1, 'Repeated': 1, 'common': 1}
        self.assertDictEqual(task_func(input_text), expected_output)
        
    def test_case_3(self):
        # Text with no stopwords
        input_text = "Python programming language."
        expected_output = {'Python': 1, 'programming': 1, 'language': 1}
        self.assertDictEqual(task_func(input_text), expected_output)
        
    def test_case_4(self):
        # Text with all stopwords
        input_text = "This is an and the with"
        expected_output = {}
        self.assertDictEqual(task_func(input_text), expected_output)
        
    def test_case_5(self):
        # Empty text
        input_text = ""
        expected_output = {}
        self.assertDictEqual(task_func(input_text), expected_output)
