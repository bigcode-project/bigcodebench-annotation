import re
import collections


def f_88(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    """
    Counts the occurrence of specific patterns in a string.
    
    Parameters:
    string (str): The input string.
    patterns (list[str], optional): List of patterns to search for. Defaults to ['nnn', 'aaa', 'sss', 'ddd', 'fff'].
    
    Returns:
    dict: A dictionary with patterns as keys and their counts as values.

    Raises:
    - TypeError: If string is not a str.
    - TypeError: If patterns is not a list of str.
    
    Requirements:
    - re
    - collections
    
    Example:
    >>> f_88("nnnaaaasssdddeeefffggg")
    {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
    >>> f_88('asdfasdfasdfasdaaaaf', patterns=['a', 'asdf'])
    {'a': 8, 'asdf': 3}
    >>> f_88('123kajhdlkfah12345k,jk123', patterns=['123', '1234'])
    {'123': 3, '1234': 1}
    """
    if not isinstance(string, str):
        raise TypeError("Input string should be of type string.")
    if not isinstance(patterns, list):
        raise TypeError("patterns should be a list of strings.")
    if not all(isinstance(s, str) for s in patterns):
        raise TypeError("patterns should be a list of strings.")
    pattern_counts = collections.defaultdict(int)
    for pattern in patterns:
        pattern_counts[pattern] = len(re.findall(pattern, string))
    return dict(pattern_counts)

import unittest
class TestCases(unittest.TestCase):
    def test_empty_pattern(self):
        'empty pattern'
        result = f_88('asdf', patterns=[])
        expected_result = {}
        self.assertEqual(result, expected_result)
    
    def test_wrong_type(self):
        'wrong input types'
        self.assertRaises(Exception, f_88, {'string': 123})
        self.assertRaises(Exception, f_88, {'string': ['asdf']})
        self.assertRaises(Exception, f_88, {'string': {'a': 3}})
        self.assertRaises(Exception, f_88, {'string': ['test'], 'patterns': 3})
        self.assertRaises(Exception, f_88, {'string': ['test'], 'patterns': ['3', 1]})
    def test_case_1(self):
        result = f_88("nnnaaaasssdddeeefffggg")
        expected_result = {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
        self.assertEqual(result, expected_result)
    
    def test_case_2(self):
        result = f_88("")
        expected_result = {'nnn': 0, 'aaa': 0, 'sss': 0, 'ddd': 0, 'fff': 0}
        self.assertEqual(result, expected_result)
    
    def test_case_3(self):
        result = f_88("xyz")
        expected_result = {'nnn': 0, 'aaa': 0, 'sss': 0, 'ddd': 0, 'fff': 0}
        self.assertEqual(result, expected_result)
    
    def test_case_4(self):
        result = f_88("nnnaaannnsssdddfffnnn")
        expected_result = {'nnn': 3, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
        self.assertEqual(result, expected_result)
    
    def test_case_5(self):
        result = f_88("xxxyyyzzz", patterns=['xxx', 'yyy', 'zzz', 'aaa'])
        expected_result = {'xxx': 1, 'yyy': 1, 'zzz': 1, 'aaa': 0}
        self.assertEqual(result, expected_result)
