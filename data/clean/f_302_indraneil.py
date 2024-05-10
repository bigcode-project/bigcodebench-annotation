import collections
import matplotlib.pyplot as plt
import pandas as pd


# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def f_302(sentences_dict, word_keys):
    """
    Calculate the occurrence of certain words in a collection of sentences and return a bar chart.

    Parameters:
    sentences_dict (dict): The dictionary containing sentences.
    word_keys (list): The list of words.

    Returns:
    - matplotlib.axes._subplots.AxesSubplot: Axes object of the bar chart displaying the frequencies.

    Requirements:
    - collections
    - matplotlib.pyplot
    - pandas

    Example:
    >>> sentences_dict = {'Sentence1': 'the quick brown fox', 'Sentence2': 'jumps over the lazy dog', 'Sentence3': 'the dog is brown'}
    >>> word_keys = ['the', 'dog']
    >>> type(f_302(sentences_dict, word_keys))
    <class 'matplotlib.axes._axes.Axes'>
    """
    word_counts = collections.Counter(' '.join(sentences_dict.values()).split())
    frequencies = [word_counts[word] for word in word_keys]
    word_series = pd.Series(frequencies, index=word_keys)
    plt.figure()
    word_series.plot(kind='bar')
    return word_series.plot(kind='bar')


import unittest
import doctest


class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        sentences_dict = {
            'Sentence1': 'the quick brown fox',
            'Sentence2': 'jumps over the lazy dog',
            'Sentence3': 'the dog is brown'
        }
        word_keys = ['the', 'dog']
        ax = f_302(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 2, 3, 2])
        
    def test_case_2(self):
        sentences_dict = {
            'Sentence1': 'apple orange banana',
            'Sentence2': 'apple apple',
            'Sentence3': 'banana orange orange'
        }
        word_keys = ['apple', 'orange', 'banana']
        ax = f_302(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 3, 2, 3, 3, 2])
        
    def test_case_3(self):
        sentences_dict = {
            'Sentence1': 'cat mouse',
            'Sentence2': 'dog cat',
            'Sentence3': 'mouse mouse cat'
        }
        word_keys = ['cat', 'mouse', 'dog']
        ax = f_302(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 3, 1, 3, 3, 1])

    def test_case_4(self):
        sentences_dict = {
            'Sentence1': 'sun moon stars',
            'Sentence2': 'sun sun',
            'Sentence3': 'moon stars stars'
        }
        word_keys = ['sun', 'stars', 'moon']
        ax = f_302(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 3, 2, 3, 3, 2])

    def test_case_5(self):
        sentences_dict = {
            'Sentence1': 'car bus bike',
            'Sentence2': 'bus bus bike',
            'Sentence3': 'car car bus'
        }
        word_keys = ['car', 'bus', 'bike']
        ax = f_302(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 4, 2, 3, 4, 2])


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
