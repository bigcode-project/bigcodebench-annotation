
import re
import numpy as np
from scipy.stats import ttest_rel

def f_108(text1, text2):
    """
    Perform a paired t-test for the number of words in two strings.
    
    Parameters:
    text1 (str), text2 (str): The two text strings.
    
    Returns:
    float: The t-statistic.
    float: The p-value.
    
    Requirements:
    - re
    - numpy
    - scipy.stats.ttest_rel
    
    Example:
    >>> f_108('Words, words, words.', 'And more words!')
    (t-statistic value, p-value)
    """
    word_counts1 = np.array([len(word) for word in re.split(r'\W+', text1) if word])
    word_counts2 = np.array([len(word) for word in re.split(r'\W+', text2) if word])
    t_statistic, p_value = ttest_rel(word_counts1, word_counts2)
    return t_statistic, p_value
