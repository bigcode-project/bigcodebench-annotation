import nltk
import re
from collections import Counter


# Constants
STOPWORDS = nltk.corpus.stopwords.words('english')

def f_310(text):
    """
    Calculate the frequency of continuous words in a text string. The function splits the text into words, 
    converts them to lowercase, removes punctuation marks and common stopwords (provided as a constant), 
    and then calculates the frequency of each word.

    Parameters:
    text (str): The input text string.

    Returns:
    dict: A dictionary with words as keys and their frequencies as values.

    Requirements:
    - nltk for stopwords (ensure the stopwords dataset is downloaded using nltk.download('stopwords'))
    - re for regular expressions
    - collections.Counter for counting occurrences

    Example:
    >>> f_310('This is a sample text. This text is for testing.')
    {'sample': 1, 'text': 2, 'testing': 1}
    """
    words = re.split(r'\W+', text.lower())
    words = [word for word in words if word not in STOPWORDS and word != '']
    word_freq = dict(Counter(words))

    return word_freq


import unittest
import doctest


class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Basic test
        text = 'This is a sample text. This text is for testing.'
        expected_output = {'sample': 1, 'text': 2, 'testing': 1}
        self.assertEqual(f_310(text), expected_output)

    def test_case_2(self):
        # Test with stopwords
        text = 'The quick brown fox jumped over the lazy dog.'
        expected_output = {'quick': 1, 'brown': 1, 'fox': 1, 'jumped': 1, 'lazy': 1, 'dog': 1}
        self.assertEqual(f_310(text), expected_output)

    def test_case_3(self):
        # Test with punctuation
        text = 'Hello, world! How are you today?'
        expected_output = {'hello': 1, 'world': 1, 'today': 1}
        self.assertEqual(f_310(text), expected_output)

    def test_case_4(self):
        # Test with empty string
        text = ''
        expected_output = {}
        self.assertEqual(f_310(text), expected_output)

    def test_case_5(self):
        # Test with numeric values and special characters
        text = 'Python3 is better than Python2. I love Python3.5!'
        expected_output = {'python3': 2, 'better': 1, 'python2': 1, 'love': 1, '5': 1}
        self.assertEqual(f_310(text), expected_output)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
