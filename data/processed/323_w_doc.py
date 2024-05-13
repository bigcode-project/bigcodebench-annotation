import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture


def task_func(text, num_gaussians=1, seed=42):
    '''
    Extract names from a string that aren't enclosed by square brackets, 
    tokenize the names into words, and count the frequency of each word.
    Finally, fit a mixture of num_gaussians 1-D Gaussian distributions to 
    the word frequencies and return the means and variances of the fitted 
    Gaussians.
    
    Parameters:
    text (str): The text from which to extract names and count word frequencies.
    num_gaussians (int, Optional): The number of Gaussian distributions to fit to 
                                   the word frequencies. Defaults to 1.
    seed (int, Optional): The seed for the random number generator. Defaults to 42.
    
    Returns:
    dict: A dictionary with the frequency of each word.
    
    Requirements:
    - re module for regular expression operations.
    - numpy for setting the random seed.
    - collections.Counter for counting word frequencies.
    - scipy.stats.gmm for fitting Gaussian mixture models.

    Raises:
    ValueError: If num_gaussians is less than or equal to 0.
    Exception: If num_gaussians is greater than the number of unique words.
    
    Examples:
    >>> freqs, means = task_func("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]")
    >>> freqs
    {'Josie': 1, 'Smith': 2, 'Mugsy': 1, 'Dog': 1}
    '''

    np.random.seed(seed)
    names = re.findall(r'(.*?)(?:\[.*?\]|$)', text)
    words = ' '.join(names).split()
    word_freqs = Counter(words)
    if num_gaussians <= 0:
        raise ValueError('Number of Gaussians must be greater than 0.')
    if len(word_freqs) < num_gaussians:
        raise Exception('Number of Gaussians must be less than or equal to the number of unique words.')
    mixture = GaussianMixture(n_components=num_gaussians)
    mixture.fit([[freq] for freq in word_freqs.values()])
    means = mixture.means_
    return dict(word_freqs), means

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        text = "John Doe [1234 Elm St, Springfield, IL 12345]Jane Smith [5678 Maple Dr, Anytown, CA 67890]"
        result, _ = task_func(text)
        expected = {'John': 1, 'Doe': 1, 'Jane': 1, 'Smith': 1}
        self.assertDictEqual(result, expected)
    def test_case_2(self):
        text = "Alice [7890 Oak Ln, Someplace, TX 23456]Bob Charlie Bob [2345 Birch Rd, Otherplace, NY 34567]"
        result, means = task_func(text, 2)
        expected = {'Alice': 1, 'Bob': 2, 'Charlie': 1}
        self.assertDictEqual(result, expected)
        self.assertAlmostEquals(means[0][0], 2.00, places=2)
        self.assertAlmostEquals(means[1][0], 1.00, places=2)
    def test_case_3(self):
        text = "Eve [3456 Cedar St, Thisplace, WA 45678]"
        self.assertRaises(Exception, task_func, text)
    def test_case_4(self):
        text = "Frank Grace Holly [4567 Pine Pl, Thatplace, NV 56789]"
        result, _ = task_func(text)
        expected = {'Frank': 1, 'Grace': 1, 'Holly': 1}
        self.assertDictEqual(result, expected)
    def test_case_5(self):
        text = "Ivy Jack [5678 Spruce Way, Hereplace, ME 67890]Katherine [6789 Fir Blvd, Thereplace, VT 78901]Leo"
        result, _ = task_func(text)
        expected = {'Ivy': 1, 'Jack': 1, 'Katherine': 1, 'Leo': 1}
        self.assertDictEqual(result, expected)
        # Long test case
        long_text = "Antony [2345 Elm St, Thiscity, CA 34567]Barbara [3456 Oak Dr, Thatcity, NY 45678]" + \
                    "Barbara [4567 Maple Ave, Othercity, TX 56789]Diana [5678 Birch Rd, Newcity, WA 67890]" + \
                    "Edward [6789 Cedar Ln, Oldcity, NV 78901]Antony [7890 Pine St, Anytown, ME 89012]" + \
                    "George [8901 Spruce Dr, Someplace, VT 90123]Helen [9012 Fir Ave, Anywhere, MD 01234]" + \
                    "Ian [0123 Elm Blvd, Nowhere, WI 12345]Jessica [1234 Oak Way, Everywhere, IL 23456]" + \
                    "Kevin [2345 Maple Pl, Somewhere, CA 34567]Laura [3456 Birch St, Thisplace, NY 45678]" + \
                    "Michael [4567 Cedar Dr, Thatplace, TX 56789]Barbara [5678 Pine Ave, Otherplace, WA 67890]" + \
                    "Oliver [6789 Spruce Rd, Newplace, NV 78901]Patricia [7890 Fir St, Oldplace, ME 89012]" + \
                    "Quentin [8901 Elm Dr, Anyplace, VT 90123]Rachel [9012 Oak Ln, Somecity, MD 01234]" + \
                    "Samuel [0123 Maple Dr, Thatcity, WI 12345]Antony [1234 Birch St, Othercity, IL 23456]" + \
                    "Ursula [2345 Cedar Ave, Newcity, CA 34567]Victor [3456 Pine Rd, Oldcity, NY 45678]" + \
                    "Wendy [4567 Spruce St, Anytown, TX 56789]John [5678 Fir Dr, Someplace, WA 67890]" + \
                    "Zachary [6789 Elm Way, Anywhere, NV 78901]Zachary [7890 Oak Pl, Nowhere, ME 89012]"
        result, means = task_func(long_text, 2)
        self.assertAlmostEquals(means[0][0], 1.05, places=2)
        self.assertAlmostEquals(means[1][0], 3.00, places=2)
