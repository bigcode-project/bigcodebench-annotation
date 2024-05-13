import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist


def task_func(example_str, top_n=30):
    """
    Extract all texts that are not enclosed in square brackets from the given string and plot 
    a frequency distribution of the words. Also return the top_n most common words in the frequency distribution
    as a dictionary.

    Parameters:
    - example_str (str): The input string.
    - top_n (int, Optional): The number of most common words to display in the frequency distribution plot. Default is 30.

    Returns:
    - Axes: A matplotlib Axes object representing the frequency distribution plot.
    - dict: A dictionary containing the top_n most common words and their frequencies.

    Requirements:
    - re
    - nltk.probability.FreqDist
    - matplotlib.pyplot

    Example:
    >>> ax, top_n_words = task_func("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]")
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    text = ' '.join(re.findall('(.*?)\\[.*?\\]', example_str))
    words = text.split()
    fdist = FreqDist(words)
    if top_n > len(fdist):
        top_n = len(fdist)
    plt.figure()
    ax = fdist.plot(top_n, cumulative=False, show=False)
    plt.close()
    top_n_words = dict(fdist.most_common(top_n))
    return ax, top_n_words

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        example_str = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
        ax, top_n_words = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
        # Test the number of words in the plot
        self.assertEqual(len(ax.get_xticklabels()), 4, "The number of words in the plot is not 30.")
        # Test the top_n_words dictionary
        self.assertEqual(top_n_words, {'Smith': 2, 'Josie': 1, 'Mugsy': 1, 'Dog': 1}, "The top_n_words dictionary is incorrect.")
    def test_case_2(self):
        example_str = "Hello [1234 STREET, CITY, STATE 12345] World [5678 LANE, TOWN, PROVINCE 67890]"
        ax, _ = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
    def test_case_3(self):
        example_str = "[IGNORE THIS] This is a simple test string [ANOTHER IGNORE]"
        ax, top_n_words = task_func(example_str, top_n=5)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
        # Test the histogram data
        #self.assertEqual(len(ax.patches), 5, "The number of words in the plot is not 5.")
        # Test the top_n_words dictionary
        self.assertEqual(top_n_words, {'This': 1, 'is': 1, 'a': 1, 'simple': 1, 'test': 1}, "The top_n_words dictionary is incorrect.")
    
    def test_case_4(self):
        example_str = "[BEGIN] Testing the function with different [MIDDLE] types of input strings [END]"
        ax, _ = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
    
    def test_case_5(self):
        example_str = "Example without any brackets so all words should be considered."
        ax, _ = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
