from collections import Counter
import itertools
import random


# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def task_func(list_of_lists, seed=0):
    """
    Count the frequency of each letter in a list of lists. If a list is empty, 
    fill it with a random sample from the alphabet, and then count the letters.
    
    Parameters:
    list_of_lists (list): The list of lists.
    seed (int): The seed for the random number generator. Defaults to 0.
    
    Returns:
    Counter: A Counter object with the frequency of each letter.
    
    Requirements:
    - collections.Counter
    - itertools
    - random.sample
    
    Example:
    >>> dict(task_func([['a', 'b', 'c'], [], ['d', 'e', 'f']]))
    {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'm': 1, 'y': 1, 'n': 1, 'i': 1, 'q': 1, 'p': 1, 'z': 1, 'j': 1, 't': 1}
    """

    random.seed(seed)
    flattened_list = list(itertools.chain(*list_of_lists))
    for list_item in list_of_lists:
        if list_item == []:
            flattened_list += random.sample(ALPHABET, 10)
    counter = Counter(flattened_list)
    return counter

import unittest
from collections import Counter
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func([['a', 'b', 'c'], ['d', 'e', 'f']])
        expected = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1})
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = task_func([['a', 'b', 'c'], [], ['d', 'e', 'f']])
        # Since the function can add random letters, we'll ensure that the known letters are counted correctly
        self.assertEqual(sum(result.values()), 16)  # 6 known letters + 10 random letters
    def test_case_3(self):
        result = task_func([[], [], []])
        # Here, the function should add 30 random letters (10 for each empty list)
        self.assertEqual(sum(result.values()), 30)
    def test_case_4(self):
        result = task_func([])
        # For an entirely empty input list, the result should also be an empty Counter
        self.assertEqual(result, Counter())
    def test_case_5(self):
        result = task_func([['x', 'y', 'z'], ['a', 'b', 'c']])
        expected = Counter({'x': 1, 'y': 1, 'z': 1, 'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(result, expected)
