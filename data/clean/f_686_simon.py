import numpy as np
from itertools import product
import string


def f_686(length, seed=None, alphabets=list(string.ascii_lowercase)):
    """
    Generate a list of 10 randomly picked strings from all possible strings of a given
    length from the provided series of characters, using a specific seed for
    reproducibility.

    Parameters:
    length (int): The length of the strings to generate.
    seed (int): The seed for the random number generator. Default is None.
    alphabets (list, optional): The series of characters to generate the strings from. 
                Default is lowercase English alphabets.

    Returns:
    list: A list of generated strings.

    Requirements:
    - numpy
    - itertools.product
    - string

    Example:
    >>> f_686(2, 123)
    ['tq', 'ob', 'os', 'mk', 'du', 'ar', 'wx', 'ec', 'et', 'vx']

    >>> f_686(2, 123, alphabets=['x', 'y', 'z'])
    ['xz', 'xz', 'zx', 'xy', 'yx', 'zx', 'xy', 'xx', 'xy', 'xx']
    """
    np.random.seed(seed)
    all_combinations = [''.join(p) for p in product(alphabets, repeat=length)]
    return np.random.choice(all_combinations, size=10).tolist()


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_rng(self):
        output1 = f_686(2, 123)
        output2 = f_686(2, 123)

        self.assertCountEqual(output1, output2)
    
    def test_case_1(self):
        output = f_686(2, 123)
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 2 for word in output))
        self.assertTrue(all(word.islower() for word in output))
        expected = ['tq', 'ob', 'os', 'mk', 'du', 'ar', 'wx', 'ec', 'et', 'vx']
        self.assertCountEqual(output, expected)
        
    def test_case_2(self):
        output = f_686(3, 456)
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 3 for word in output))
        self.assertTrue(all(word.islower() for word in output))
        expected = ['axp', 'xtb', 'pwx', 'rxv', 'soa', 'rkf', 'cdp', 'igv', 'ruh', 'vmz']
        self.assertCountEqual(output, expected)
        
    def test_case_3(self):
        output = f_686(2, 789, alphabets=['x', 'y', 'z'])
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 2 for word in output))
        self.assertTrue(all(letter in ['x', 'y', 'z'] for word in output for letter in word))
        expected = ['yx', 'xz', 'xy', 'yx', 'yy', 'zz', 'yy', 'xy', 'zz', 'xx']
        self.assertCountEqual(output, expected)

    def test_case_4(self):
        output = f_686(1, 100)
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 1 for word in output))
        self.assertTrue(all(word.islower() for word in output))
        expected = ['i', 'y', 'd', 'h', 'x', 'p', 'q', 'k', 'u', 'c']
        self.assertCountEqual(output, expected)
        
    def test_case_5(self):
        output = f_686(4, 200, alphabets=['a', 'b'])
        self.assertEqual(len(output), 10)
        self.assertTrue(all(len(word) == 4 for word in output))
        self.assertTrue(all(letter in ['a', 'b'] for word in output for letter in word))
        expected = ['baba', 'baab', 'aaaa', 'abaa', 'baba', 'abbb', 'bbaa', 'bbbb', 'baab', 'bbba']
        self.assertCountEqual(output, expected)


if __name__ == "__main__":
    run_tests()