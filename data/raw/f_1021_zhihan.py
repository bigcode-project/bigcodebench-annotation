import collections
from itertools import zip_longest
from random import choices

# Constants
K = 10

def f_1021(l1, l2):
    """
    Combine two lists by alternating their elements, even if they are of different lengths. 
    Elements from the longer list without a counterpart in the shorter one will be included on their own.
    Then, create a random sample of size K from the combined list, and calculate the frequency of 
    each element in the sample.

    Parameters:
    l1 (list): The first list containing any hashable types.
    l2 (list): The second list containing any hashable types.

    Returns:
    collections.Counter: An object that counts the frequency of each element in the sample.

    Requirements:
    - collections
    - itertools.zip_longest
    - random.choices

    Example:
    >>> import random
    >>> random.seed(32)
    >>> l1 = list(range(10))
    >>> l2 = list(range(10, 20))
    >>> freq = f_1021(l1, l2)
    >>> print(freq)
    Counter({5: 2, 10: 1, 2: 1, 3: 1, 9: 1, 14: 1, 7: 1, 1: 1, 8: 1})
    """
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    sample = choices(combined, k=K)
    freq = collections.Counter(sample)
    return freq

import unittest
import collections

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        l1 = list(range(10))
        l2 = list(range(10, 20))
        freq = f_1021(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)

    def test_case_2(self):
        l1 = list(range(5))
        l2 = list(range(10, 15))
        freq = f_1021(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)

    def test_case_3(self):
        l1 = list(range(20, 30))
        l2 = list(range(30, 40))
        freq = f_1021(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)

    def test_case_4(self):
        l1 = list(range(50))
        l2 = list(range(50, 100))
        freq = f_1021(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)

    def test_case_5(self):
        l1 = []
        l2 = list(range(10, 20))
        freq = f_1021(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
if __name__ == "__main__":
    run_tests()