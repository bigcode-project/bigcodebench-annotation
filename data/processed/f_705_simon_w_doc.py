import random
import string
from collections import defaultdict


def f_356(n, seed=None):
    """
    Generate a dictionary with lists of random lowercase english letters. 
    
    Each key in the dictionary  represents a unique letter from the alphabet,
    and the associated value is a list, containing randomly generated instances
    of that letter based on a seed.

    The function randomly selects 'n' letters from the alphabet (a-z) and places each 
    occurrence in the corresponding list within the dictionary. The randomness is based
    on the provided seed value; the same seed will produce the same distribution of letters.

    The dictionary has only those keys for which a letter was generated.

    Parameters:
    n (int): The number of random letters to generate.
    seed (int, optional): A seed value for the random number generator. If None, the randomness
                          is based on system time or the OS's randomness source.

    Returns:
    defaultdict: A dictionary where the keys are characters ('a' to 'z') and the values 
                 are lists of randomly generated letters. Each list may have 0 to 'n' occurrences of 
                 its associated letter, depending on the randomness and seed.

    Requirements:
    - collections.defaultdict
    - random
    - string

    Example:
    >>> f_356(5, seed=123)
    defaultdict(<class 'list'>, {'b': ['b'], 'i': ['i'], 'c': ['c'], 'y': ['y'], 'n': ['n']})

    >>> f_356(30, seed=1)
    defaultdict(<class 'list'>, {'e': ['e'], 's': ['s'], 'z': ['z', 'z', 'z'], 'y': ['y', 'y', 'y', 'y'], 'c': ['c'], 'i': ['i', 'i'], 'd': ['d', 'd'], 'p': ['p', 'p', 'p'], 'o': ['o', 'o'], 'u': ['u'], 'm': ['m', 'm'], 'g': ['g'], 'a': ['a', 'a'], 'n': ['n'], 't': ['t'], 'w': ['w'], 'x': ['x'], 'h': ['h']})
    """
    LETTERS = string.ascii_lowercase
    random.seed(seed)
    letter_dict = defaultdict(list)
    for _ in range(n):
        letter = random.choice(LETTERS)
        letter_dict[letter].append(letter)
    return letter_dict

import unittest
from collections import defaultdict
import string
import random
class TestCases(unittest.TestCase):
    def test_return_type(self):
        result = f_356(10, seed=1)
        self.assertIsInstance(result, defaultdict)
        for key, value in result.items():
            self.assertIsInstance(value, list)
    def test_dictionary_keys(self):
        result = f_356(100, seed=2)
        for key in result.keys():
            self.assertTrue('a' <= key <= 'z')
    def test_random_seed_effect(self):
        result1 = f_356(50, seed=3)
        result2 = f_356(50, seed=3)
        self.assertEqual(result1, result2)
    def test_letters_distribution(self):
        n = 60
        result = f_356(n, seed=4)
        total_letters = sum(len(lst) for lst in result.values())
        self.assertEqual(total_letters, n)
    def test_edge_cases(self):
        result = f_356(0, seed=5)
        for lst in result.values():
            self.assertEqual(len(lst), 0)
        large_n = 10000
        result = f_356(large_n, seed=6)
        total_letters = sum(len(lst) for lst in result.values())
        self.assertEqual(total_letters, large_n)
