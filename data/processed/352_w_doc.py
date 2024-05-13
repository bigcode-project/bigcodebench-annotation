import pandas as pd
from collections import Counter


def task_func(text_dict, word_keys, top_k=2):
    """
    Calculate the frequency of certain words in a text dictionary and return a bar chart's Axes object and a dictionary
    containing the frequencies of the top_k most common words in text_dict. 
    
    The function takes a dictionary containing word frequencies and a list of words. It calculates the frequency 
    of the provided words in the dictionary and returns the Axes object of the bar chart displaying the frequencies
    along with the top_k most common words and their frequencies as a dictionary. If a word in word_keys is not present 
    in text_dict, its frequency is considered to be 0.
    
    Parameters:
    - text_dict (dict): The dictionary containing word frequencies. Key is the word and value is its frequency.
    - word_keys (list of str): The list of words to consider.
    - top_k (int, Optional): A positive integer denoting the number of most common words to return. Default is 2.
    
    Returns:
    - matplotlib.axes._axes.Axes: Axes object of the bar chart displaying the frequencies.
    - dict: Dictionary containing the frequencies of the top_k most common words. Key is the word and value is 
    its frequency.
    
    Requirements:
    - pandas
    - collections.Counter

    Raises:
    - ValueError: If top_k is a negative integer.
    
    Example:
    >>> import collections
    >>> text_dict = collections.Counter(['the', 'be', 'to', 'the', 'that', 'and', 'a', 'in', 'the', 'that', 'have', 'I'])
    >>> word_keys = ['the', 'and', 'I']
    >>> ax, frequencies = task_func(text_dict, word_keys, 3)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> frequencies
    {'the': 3, 'that': 2, 'be': 1}
    """

    if top_k < 0:
        raise ValueError('top_k must be a positive integer.')
    elif top_k >= len(text_dict):
        top_k = len(text_dict)
    frequencies = [text_dict.get(word, 0) for word in word_keys]
    freq_dict = Counter(text_dict)
    top_k_words = freq_dict.most_common(top_k)
    word_series = pd.Series(frequencies, index=word_keys)
    ax = word_series.plot(kind='bar')
    return ax, dict(top_k_words)

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        text_dict = Counter(['the', 'be', 'to', 'the', 'and', 'that', 'a', 'in', 'the', 'that', 'have', 'I'])
        word_keys = ['the', 'and', 'I']
        ax, top_k_dict = task_func(text_dict, word_keys, 3)
        self.assertDictContainsSubset(top_k_dict, {'the': 3, 'that': 2, 'be': 1})
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
    def test_case_2(self):
        text_dict = Counter(['apple', 'banana', 'apple', 'orange', 'grape', 'apple', 'banana'])
        word_keys = ['apple', 'banana', 'cherry']
        ax, top_k_dict = task_func(text_dict, word_keys)
        self.assertDictContainsSubset(top_k_dict, {'apple': 3, 'banana': 2})
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
    def test_case_3(self):
        text_dict = Counter([])
        word_keys = ['apple', 'banana', 'cherry']
        ax, top_k_dict = task_func(text_dict, word_keys)
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
    def test_case_4(self):
        text_dict = Counter(['a', 'a', 'b', 'b', 'b', 'c', 'c'])
        word_keys = ['a', 'b', 'c', 'd']
        ax, top_k_dict = task_func(text_dict, word_keys)
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
    def test_case_5(self):
        text_dict = Counter(['cat', 'dog', 'cat', 'fish', 'fish', 'fish', 'bird'])
        word_keys = ['cat', 'dog', 'bird', 'elephant']
        ax, top_k_dict = task_func(text_dict, word_keys,9)
        self.assertDictContainsSubset(top_k_dict, {'fish': 3, 'cat': 2, 'dog': 1, 'bird': 1})
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
