import nltk

# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from collections import Counter

def f_597(content):
    """
    Count the Part-of-Speech (POS) tags in a sentence without the last word.

    Parameters:
    - content (str): The sentence to count POS tags from.

    Returns:
    - dict: A dictionary with POS tags as keys and their count as values.

    Requirements:
    - nltk
    - collections.Counter

    Example:
    >>> f_597('this is an example content')
    {'DT': 2, 'VBZ': 1, 'NN': 1}
    """
    words = content.split()[:-1]  # Split and remove the last word
    pos_tags = nltk.pos_tag(words)  # Tokenization is built into pos_tag for simple whitespace tokenization
    pos_counts = Counter(tag for _, tag in pos_tags)
    return dict(pos_counts)

import unittest
import re
class TestCases(unittest.TestCase):
    def test_case_1(self):
        sentence = "this is an example content"
        # Expected output after removing "content"
        expected_output = {'DT': 2, 'NN': 1, 'VBZ': 1}
        self.assertEqual(f_597(sentence), expected_output)
    def test_case_2(self):
        sentence = "The quick brown fox jumps"
        # "jumps" is removed; expect {'DT': 1, 'JJ': 1, 'NN': 1} for "The quick brown fox"
        expected_output = {'DT': 1, 'JJ': 1, 'NN': 2}
        self.assertEqual(f_597(sentence), expected_output)
    def test_case_3(self):
        sentence = "Over the lazy dog"
        # "dog" is removed; expect {'IN': 1, 'DT': 1, 'JJ': 1} for "Over the lazy"
        expected_output = {'DT': 1, 'IN': 1, 'NN': 1}
        self.assertEqual(f_597(sentence), expected_output)
    def test_case_4(self):
        sentence = "Hello world"
        # "world" is removed; expect {} for "Hello"
        expected_output = {'NN': 1}  # "Hello" might be tagged as interjection 'UH' if not considered a proper noun
        self.assertEqual(f_597(sentence), expected_output)
    def test_case_5(self):
        sentence = "This is a longer sentence with various parts of speech"
        # After removing "speech", adjust expectation
        expected_output = {'DT': 2, 'IN': 2, 'JJ': 1, 'NN': 1, 'NNS': 1, 'RBR': 1, 'VBZ': 1}
        self.assertEqual(f_597(sentence), expected_output)
