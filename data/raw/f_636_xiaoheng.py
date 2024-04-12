import nltk

# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

import string
import re
from collections import Counter

def f_636(content):
    """
    Count the Part-of-Speech (POS) tags in a sentence without the last word.

    Parameters:
    - content (str): The sentence to count POS tags from.

    Returns:
    - dict: A dictionary with POS tags as keys and their count as values.

    Requirements:
    - nltk
    - string
    - re
    - collections.Counter

    Example:
    >>> f_636('this is an example content')
    {'DT': 2, 'VBZ': 1, 'NN': 1}
    """
    content = content.split(' ')[:-1]
    words = nltk.word_tokenize(' '.join(content))
    pos_tags = nltk.pos_tag(words)
    pos_counts = Counter(tag for word, tag in pos_tags)

    return dict(pos_counts)

import unittest

class TestF_178(unittest.TestCase):
    def test_case_1(self):
        sentence = "this is an example content"
        expected_output = {'DT': 2, 'VBZ': 1, 'NN': 1}
        self.assertEqual(f_636(sentence), expected_output)

    def test_case_2(self):
        sentence = "The quick brown fox jumps"
        expected_output = {'DT': 1, 'JJ': 1, 'NN': 2}
        self.assertEqual(f_636(sentence), expected_output)

    def test_case_3(self):
        sentence = "Over the lazy dog"
        expected_output = {'IN': 1, 'DT': 1, 'JJ': 1}
        self.assertEqual(f_636(sentence), expected_output)

    def test_case_4(self):
        sentence = "Hello world"
        expected_output = {'NN': 1}
        self.assertEqual(f_636(sentence), expected_output)

    def test_case_5(self):
        sentence = "This is a longer sentence with various parts of speech"
        expected_output = {'DT': 2, 'VBZ': 1, 'DT': 1, 'JJR': 1, 'NN': 3, 'IN': 1, 'NNS': 1}
        self.assertEqual(f_636(sentence), expected_output)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestF_178))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()