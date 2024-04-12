import re
import string
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

from collections import Counter
import random

# Constants
STOPWORDS = set(stopwords.words('english'))

def f_676(text, n=2):
    """
    Remove duplicate and stopwords from a string "text."
    Then, generate a count of n-grams (default is bigrams) in the text.

    Parameters:
    - text (str): The text string to analyze.
    - n (int): The size of the n-grams.

    Returns:
    - dict: The count of the n-grams in the text.

    Requirements:
    - re
    - string
    - nltk.corpus.stopwords
    - collections.Counter

    Example:
    >>> text = "The quick brown fox jumps over the lazy dog and the dog was not that quick to respond."
    >>> ngrams = f_676(text)
    >>> print(ngrams)
    Counter({('quick', 'brown'): 1, ('brown', 'fox'): 1, ('fox', 'jumps'): 1, ('jumps', 'lazy'): 1, ('lazy', 'dog'): 1, ('dog', 'dog'): 1, ('dog', 'quick'): 1, ('quick', 'respond'): 1})
    """
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    words = [word for word in re.findall(r'\b\w+\b', text.lower()) if word not in STOPWORDS]
    ngrams = zip(*[words[i:] for i in range(n)])

    return Counter(ngrams)

import unittest
from collections import Counter

class TestCases(unittest.TestCase):

    def test_case_1(self):
        """
        Test Case 1: Simple Text
        - Input: A simple text string with no duplicated words or stopwords
        - Expected Output: A Counter object with the count of each bigram
        """
        text = "The quick brown fox jumps over the lazy dog."
        result = f_676(text)
        expected = Counter({('quick', 'brown'): 1, ('brown', 'fox'): 1, ('fox', 'jumps'): 1, ('jumps', 'lazy'): 1, ('lazy', 'dog'): 1})
        self.assertEqual(result, expected)

    def test_case_2(self):
        """
        Test Case 2: Text with Duplicated Words
        - Input: A text string with duplicated consecutive words
        - Expected Output: A Counter object with the count of each bigram, excluding duplicated words
        """
        text = "This is is a simple simple test test."
        result = f_676(text)
        expected = Counter({('simple', 'test'): 1})
        self.assertEqual(result, expected)

    def test_case_3(self):
        """
        Test Case 3: Text with Stopwords
        - Input: A text string with common English stopwords
        - Expected Output: A Counter object with the count of each bigram, excluding stopwords
        """
        text = "This is a test of the function."
        result = f_676(text)
        expected = Counter({('test', 'function'): 1})
        self.assertEqual(result, expected)

    def test_case_4(self):
        """
        Test Case 4: Text with Special Characters
        - Input: A text string with punctuation and special characters
        - Expected Output: A Counter object with the count of each bigram, excluding special characters
        """
        text = "Hello, world! This is a test. Testing, one, two, three."
        result = f_676(text)
        expected = Counter({('hello', 'world'): 1, ('test', 'testing'): 1, ('testing', 'one'): 1, ('one', 'two'): 1, ('two', 'three'): 1})
        self.assertEqual(result, expected)

    def test_case_5(self):
        """
        Test Case 5: Empty Text
        - Input: An empty text string
        - Expected Output: An empty Counter object
        """
        text = ""
        result = f_676(text)
        expected = Counter()
        self.assertEqual(result, expected)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()