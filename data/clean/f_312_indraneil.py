import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt


def f_312(text, n, top_k):
    """
    Visualize the uppermost K n-grams in a given text string.

    Parameters:
    text (str): The text string.
    n (int): The value of n for the n-grams.
    top_k (int): The number of top n-grams to visualize.

    Returns:
    None

    Requirements:
    - re
    - pandas
    - seaborn
    - textblob
    - matplotlib

    Example:
    >>> type(f_312('This is a sample text for testing.', 2, 5))
    <class 'matplotlib.axes._axes.Axes'>
    """
    blob = TextBlob(text.lower())
    words_freq = Counter([' '.join(list(span)) for span in blob.ngrams(n=n)])  # Get n-grams and count frequency
    words_freq_filtered = words_freq.most_common(top_k)  # Get top k n-grams
    top_df = pd.DataFrame(words_freq_filtered, columns=['n-gram', 'Frequency'])
    plt.figure()

    return sns.barplot(x='n-gram', y='Frequency', data=top_df)


import unittest
import matplotlib.pyplot as plt
import doctest


class TestCases(unittest.TestCase):
    def tearDown(self) -> None:
        plt.close('all')
        return super().tearDown()

    def test_case_1(self):
        # Test with a simple text, bigram (n=2) and top 2 n-grams
        ax = f_312('This is a sample text for testing.', 2, 2)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertNotIn('sample text', ngrams)
        self.assertIn('is a', ngrams)

    def test_case_2(self):
        # Test with a longer text, trigram (n=3) and top 3 n-grams
        text = 'The sun shines bright in the clear blue sky. The sky is blue and beautiful.'
        ax = f_312(text, 3, 3)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertNotIn('the clear blue', ngrams)
        self.assertNotIn('sky the sky', ngrams)
        self.assertIn('the sun shines', ngrams)

    def test_case_3(self):
        # Test with no repeating n-grams, unigram (n=1) and top 3 n-grams
        text = 'Each word is unique.'
        ax = f_312(text, 1, 3)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertEqual(len(ngrams), 3)  # Only 4 unique words bu top 3 n-grams

    def test_case_4(self):
        # Test with a repeated word, bigram (n=2) and top 1 n-grams
        text = 'Repeat repeat repeat again.'
        ax = f_312(text, 2, 1)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertIn('repeat repeat', ngrams)

    def test_case_5(self):
        # Test with punctuation in text, bigram (n=2) and top 3 n-grams
        text = 'Hello, world! How are you, world?'
        ax = f_312(text, 2, 3)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertIn('hello world', ngrams)
        self.assertNotIn('you world', ngrams)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
