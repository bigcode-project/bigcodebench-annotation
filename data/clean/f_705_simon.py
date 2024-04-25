import random
import string
from collections import defaultdict


def f_705(n, seed=None):
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
    >>> f_705(5, seed=123)
    defaultdict(list, {'b': ['b'], 'i': ['i'], 'c': ['c'], 'y': ['y'], 'n': ['n']})
    
    >>> f_705(30)
    defaultdict(list,
                {'i': ['i', 'i', 'i'],
                'm': ['m'],
                't': ['t', 't'],
                's': ['s'],
                'q': ['q', 'q'],
                'c': ['c', 'c', 'c'],
                'n': ['n'],
                'y': ['y'],
                'v': ['v'],
                'z': ['z', 'z', 'z', 'z'],
                'k': ['k'],
                'e': ['e', 'e'],
                'd': ['d'],
                'w': ['w', 'w'],
                'h': ['h'],
                'p': ['p'],
                'o': ['o', 'o'],
                'l': ['l']})
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

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_return_type(self):
        result = f_705(10, seed=1)
        self.assertIsInstance(result, defaultdict)
        for key, value in result.items():
            self.assertIsInstance(value, list)

    def test_dictionary_keys(self):
        result = f_705(100, seed=2)
        for key in result.keys():
            self.assertTrue('a' <= key <= 'z')

    def test_random_seed_effect(self):
        result1 = f_705(50, seed=3)
        result2 = f_705(50, seed=3)
        self.assertEqual(result1, result2)

    def test_letters_distribution(self):
        n = 60
        result = f_705(n, seed=4)
        total_letters = sum(len(lst) for lst in result.values())
        self.assertEqual(total_letters, n)

    def test_edge_cases(self):
        result = f_705(0, seed=5)
        for lst in result.values():
            self.assertEqual(len(lst), 0)

        large_n = 10000
        result = f_705(large_n, seed=6)
        total_letters = sum(len(lst) for lst in result.values())
        self.assertEqual(total_letters, large_n)

    def test_return_value(self):



if __name__ == "__main__":
    run_tests()