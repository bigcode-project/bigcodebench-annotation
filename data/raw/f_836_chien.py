import re
import pandas as pd
from scipy.stats import gaussian_kde
from scipy import linalg
import matplotlib.pyplot as plt


def f_836(text):
    """
    This code takes a text input, calculates the lengths of the words, 
    and visualizes the distribution of word lengths using a histogram and a KDE curve (if applicable) on a matplotlib subplot.

    Parameters:
    text (str): The text string to be analyzed. The function can handle strings with various types 
                of characters and punctuation.

    Returns:
    matplotlib.axes._subplots.AxesSubplot: An Axes object showing the histogram and optionally the KDE 
                                           plot of word lengths. This visual representation helps in 
                                           understanding the distribution of word lengths in the given text.

    Requirements:
    - re
    - matplotlib
    - scipy
    - matplotlib

    Example:
    >>> ax = f_836('Hello world! This is a test.')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    words = re.split(r"\W+", text)
    word_counts = [len(word) for word in words if word]

    _, ax = plt.subplots()

    if word_counts:  # Check if word_counts is not empty
        ax.hist(word_counts, bins=30, edgecolor='black', alpha=0.7)

        # Add KDE plot if applicable
        if len(word_counts) > 1 and np.var(word_counts) != 0:
            try:
                kde = gaussian_kde(word_counts)
                x_range = np.linspace(min(word_counts), max(word_counts), 100)
                ax.plot(x_range, kde(x_range), color='red')  # KDE line in red
            except linalg.LinAlgError:
                # Handle the singular matrix error
                pass

    return ax


import unittest
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class TestCases(unittest.TestCase):
    """Tests for the f_836 function"""

    def test_simple_sentence(self):
        """Test a simple sentence"""
        ax1 = f_836("This is a test")
        self.assertIsInstance(ax1, plt.Axes)
        # The number of bars might differ due to matplotlib's binning strategy
        unique_word_lengths = {len(word) for word in "This is a test".split() if word}
        self.assertTrue(
            len(ax1.patches) >= len(unique_word_lengths),
            "Incorrect number of bars for a simple sentence",
        )

    def test_empty_string(self):
        """Test an empty string"""
        ax2 = f_836("")
        self.assertIsInstance(ax2, plt.Axes)
        self.assertEqual(
            len(ax2.patches), 0, "There should be no bars for an empty string"
        )

    def test_special_characters(self):
        """Test special characters and numbers"""
        ax3 = f_836("Hello, world! 1234")
        self.assertIsInstance(ax3, plt.Axes)
        # The number of bars might differ due to matplotlib's binning strategy
        unique_word_lengths = {
            len(word) for word in "Hello, world! 1234".split() if word
        }
        self.assertTrue(
            len(ax3.patches) >= len(unique_word_lengths),
            "Incorrect handling of special characters and numbers",
        )

    def test_repeated_words(self):
        """Test repeated words"""
        ax4 = f_836("repeat repeat repeat")
        self.assertIsInstance(ax4, plt.Axes)
        # Only one unique word length: 6
        self.assertTrue(len(ax4.patches) >= 1, "Incorrect handling of repeated words")

    def test_long_text(self):
        """Test a long text"""
        text = "A long text with multiple words of different lengths"
        ax5 = f_836(text)
        self.assertIsInstance(ax5, plt.Axes)
        # Adjust expectation for number of bars due to matplotlib's binning
        words = re.split(r"\W+", text)
        word_counts = pd.Series([len(word) for word in words if word])
        expected_unique_lengths = len(set(word_counts))
        self.assertTrue(
            len(ax5.patches) >= expected_unique_lengths,
            "Incorrect plot for a long text",
        )

    def tearDown(self):
        plt.clf()


def run_tests():
    """Run all testscases"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
