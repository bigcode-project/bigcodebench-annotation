from collections import Counter

def f_776(word: str) -> dict:
    """
    Count the occurrence of each adjacent pair of letters in a word.

    Functionality:
    This function counts the occurrences of each adjacent pair of letters in a given word.

    Parameters:
    - word (str): The word in which to count the adjacent letter pairs.

    Returns:
    - dict: A dictionary where keys are adjacent letter pairs and values are their counts.

    Required Libraries:
    - collections.Counter

    Examples:
    >>> f_776('abracadabra')
    {'ab': 2, 'br': 2, 'ra': 2, 'ac': 1, 'ca': 1, 'ad': 1, 'da': 1}
    >>> f_776('hello')
    {'he': 1, 'el': 1, 'll': 1, 'lo': 1}
    """
    pairs = list(map(''.join, zip(word[:-1], word[1:])))
    pairs_count = dict(Counter(pairs))
    return pairs_count

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with the word 'abracadabra'
        result = f_776('abracadabra')
        expected = {'ab': 2, 'br': 2, 'ra': 2, 'ac': 1, 'ca': 1, 'ad': 1, 'da': 1}  # Corrected this line
        self.assertEqual(result, expected)
    def test_case_2(self):
        # Test with the word 'hello'
        result = f_776('hello')
        expected = {'he': 1, 'el': 1, 'll': 1, 'lo': 1}
        self.assertEqual(result, expected)
    def test_case_3(self):
        # Test with the word 'python'
        result = f_776('python')
        expected = {'py': 1, 'yt': 1, 'th': 1, 'ho': 1, 'on': 1}
        self.assertEqual(result, expected)
    def test_case_4(self):
        # Test with an empty string
        result = f_776('')
        expected = {}
        self.assertEqual(result, expected)
    def test_case_5(self):
        # Test with a single character string
        result = f_776('a')
        expected = {}
        self.assertEqual(result, expected)
