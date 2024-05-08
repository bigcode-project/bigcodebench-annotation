import collections
from itertools import zip_longest
from random import choices

def f_21(l1, l2, K=10):
    """
    Combine two lists by alternating their elements, even if they are of different lengths. 
    Elements from the longer list without a counterpart in the shorter one will be included on their own.
    Then, create a random sample of size K from the combined list, and calculate the frequency of 
    each element in the sample.

    Parameters:
    l1 (list): The first list containing any hashable types.
    l2 (list): The second list containing any hashable types.
    K (int): the size of the random sample from the combined list. Default to 10.

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
    >>> freq = f_21(l1, l2)
    >>> print(freq)
    Counter({5: 2, 10: 1, 2: 1, 3: 1, 9: 1, 14: 1, 7: 1, 1: 1, 8: 1})
    """
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    sample = choices(combined, k=K)
    freq = collections.Counter(sample)
    return freq

import unittest
import collections
import random
class TestCases(unittest.TestCase):
    def setUp(self):
    # Set a consistent random seed for predictable outcomes in all tests.
        random.seed(42)
    def test_case_1(self):
        # Verify that combining two equal-length lists produces a correctly sized sample.
        l1 = list(range(10))
        l2 = list(range(10, 20))
        freq = f_21(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_2(self):
        # Test combining two short, equal-length lists to ensure correct sample size.
        l1 = list(range(5))
        l2 = list(range(10, 15))
        freq = f_21(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_3(self):
        # Check correct sampling from two equal-length lists starting from different ranges.
        l1 = list(range(20, 30))
        l2 = list(range(30, 40))
        freq = f_21(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_4(self):
        # Ensure that combining two long, equal-length lists correctly manages the sample size.
        l1 = list(range(50))
        l2 = list(range(50, 100))
        freq = f_21(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_5(self):
        # Confirm that an empty first list results in sampling exclusively from the second list.
        l1 = []
        l2 = list(range(10, 20))
        freq = f_21(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_with_non_integers(self):
        # Check sampling behavior with lists of non-integer floating-point numbers.
        l1 = [0.1, 0.2, 0.3]
        l2 = [0.4, 0.5, 0.6]
        freq = f_21(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
        most_common = freq.most_common(1)[0][0]
        self.assertIn(most_common, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    def test_imbalanced_lists(self):
        # Test sampling from two lists where one is significantly longer to ensure fair representation.
        l1 = [1, 2, 3]
        l2 = list(range(4, 104))
        freq = f_21(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
        self.assertTrue(any(item in freq for item in l1))
    def test_empty_first_list(self):
        # Verify behavior and sampling correctness when the first list is empty.
        l1 = []
        l2 = list(range(10, 20))
        freq = f_21(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
        self.assertTrue(all(item in l2 for item in freq.elements()))
