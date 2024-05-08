import random
from collections import Counter

def f_614(values, weights, n_samples):
    """
    Sample random numbers based on a given weighted distribution and return a histogram of the samples.

    Parameters:
    - values (list): List of values to be sampled from.
    - weights (list): List of weights corresponding to the values.
    - n_samples (int): Number of samples to be drawn.

    Returns:
    - histogram (dict): A histogram as a dictionary with the values as keys and counts as values.

    Requirements:
    - collections.Counter
    - random

    Example:
    >>> random.seed(42)
    >>> f_614([1, 2, 3], [3, 2, 1], 1000)
    {2: 342, 1: 480, 3: 178}
    """
    import random
    samples = random.choices(values, weights=weights, k=n_samples)
    histogram = dict(Counter(samples))
    return histogram

import unittest
class TestCases(unittest.TestCase):
    def test_1(self):
        result = f_614([1, 2, 3], [3, 2, 1], 1000)
        self.assertTrue(set(result.keys()) == {1, 2, 3})
    def test_2(self):
        result = f_614([1, 2], [1, 1], 500)
        self.assertTrue(set(result.keys()) == {1, 2})
    def test_3(self):
        result = f_614([1], [1], 300)
        self.assertTrue(result == {1: 300})
    def test_4(self):
        result = f_614(list(range(1, 11)), list(range(10, 0, -1)), 5000)
        self.assertTrue(set(result.keys()) == set(range(1, 11)))
    def test_5(self):
        result = f_614([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 2500)
        self.assertTrue(set(result.keys()) == {1, 2, 3, 4, 5})
