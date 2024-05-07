from collections import Counter
import hashlib

def f_345(word: str) -> dict:
    """
    Count the occurrence of each adjacent pair of letters from left to right in a word and encode the result as an MD5 hash.

    Parameters:
    - word (str): The word in which to count the adjacent letter pairs.

    Returns:
    - dict: A dictionary where keys are adjacent letter pairs and values are their counts.

    Requirements:
    - collections.Counter

    Examples:
    >>> f_345('abracadabra')
    'bc9af285d87b312e61ab3661e66b741b'
    >>> f_345('hello')
    'dd5dec1a853625e2dc48f3d42665c337'
    """
    pairs = list(map(''.join, zip(word[:-1], word[1:])))
    pairs_count = dict(Counter(pairs))
    return hashlib.md5(str(pairs_count).encode()).hexdigest()

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with the word 'abracadabra'
        result = f_345('abracadabra')
        expected = 'bc9af285d87b312e61ab3661e66b741b'
        self.assertEqual(result, expected)
    def test_case_2(self):
        # Test with the word 'hello'
        result = f_345('hello')
        expected = 'dd5dec1a853625e2dc48f3d42665c337'
        self.assertEqual(result, expected)
    def test_case_3(self):
        # Test with the word 'python'
        result = f_345('python')
        expected = '2ef1af06ae4aa496eaa8e963bde5514e'
        self.assertEqual(result, expected)
    def test_case_4(self):
        # Test with an empty string
        result = f_345('')
        expected = '99914b932bd37a50b983c5e7c90ae93b'
        self.assertEqual(result, expected)
    def test_case_5(self):
        # Test with a single character string
        result = f_345('a')
        expected = '99914b932bd37a50b983c5e7c90ae93b'
        self.assertEqual(result, expected)
