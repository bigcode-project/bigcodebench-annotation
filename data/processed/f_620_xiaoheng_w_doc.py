import re
import numpy as np
from scipy.stats import ttest_rel

def f_832(text1, text2):
    """
    Perform a paired t-test for the number of words in two strings, only if the strings produce the same number of words.
    
    Parameters:
    - text1 (str), text2 (str): The two text strings.
    
    Returns:
    - t_statistic (float): The t-statistic, or NaN if tests cannot be performed due to unequal lengths.
    - p_value (float): The p-value, or NaN if tests cannot be performed due to unequal lengths.
    
    Requirements:
    - re
    - numpy
    - scipy
    
    Example:
    >>> f_832('Words, words, words.', 'And more words!')
    (1.7320508075688774, 0.22540333075851657)
    """
    word_counts1 = np.array([len(word) for word in re.split(r'\W+', text1) if word])
    word_counts2 = np.array([len(word) for word in re.split(r'\W+', text2) if word])
    if len(word_counts1) != len(word_counts2):
        return (np.nan, np.nan)
    t_statistic, p_value = ttest_rel(word_counts1, word_counts2)
    return t_statistic, p_value

import unittest
import re
import numpy as np
from scipy.stats import ttest_rel
class TestCases(unittest.TestCase):
    def test_1(self):
        t_stat, p_val = f_832("Hello, world!", "Hi, universe!")
        self.assertTrue(isinstance(t_stat, float))
        self.assertTrue(isinstance(p_val, float))
    def test_2(self):
        t_stat, p_val = f_832("Short text.", "This is a slightly longer text.")
        self.assertTrue(isinstance(t_stat, float))
        self.assertTrue(isinstance(p_val, float))
    def test_3(self):
        t_stat, p_val = f_832("A, B, C, D, E.", "F, G, H, I, J.")
        self.assertTrue(isinstance(t_stat, float))
        self.assertTrue(isinstance(p_val, float))
        
    def test_4(self):
        t_stat, p_val = f_832("", "")
        self.assertTrue(np.isnan(t_stat))
        self.assertTrue(np.isnan(p_val))
    def test_5(self):
        t_stat, p_val = f_832("Testing with similar lengths.", "Testing with similar lengths.")
        self.assertTrue(np.isnan(t_stat))  # Since the lengths are the same, t-statistic should be NaN
        self.assertTrue(np.isnan(p_val))
    def test_unequal_lengths(self):
        t_stat, p_val = f_832("Short text.", "This is a slightly longer text.")
        self.assertTrue(np.isnan(t_stat))
        self.assertTrue(np.isnan(p_val))
