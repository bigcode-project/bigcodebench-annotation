import random
import numpy as np


def f_1003():
    """
    Generates a dictionary with letters of the alphabet as keys and lists of random integers as values.
    Calculates the mean of these integers for each letter and returns a dictionary of these mean values.

    The random integers are generated within the range [0, 100], and each letter is associated with a
    list of 1 to 10 random integers.

    Returns:
    dict: A dictionary where keys are letters of the alphabet and values are the mean values of
          a list of random integers associated with each letter.

    Example:
    >>> mean_dict = f_1003()
    >>> isinstance(mean_dict, dict)
    True
    >>> 'a' in mean_dict.keys() and 'z' in mean_dict.keys()
    True
    >>> all(isinstance(value, float) for value in mean_dict.values())
    True
    """
    # Create a list of alphabet letters
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    # Generate a dictionary with letters as keys and lists of random integers as values
    random_dict = {letter: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for letter in letters}

    # Calculate the mean of the list of integers for each letter
    mean_dict = {letter: np.mean(values) for letter, values in random_dict.items()}

    return mean_dict


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test if the function returns a dictionary
        mean_dict = f_1003()
        self.assertIsInstance(mean_dict, dict)

    def test_case_2(self):
        # Test if the dictionary contains all letters of the alphabet
        mean_dict = f_1003()
        all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.assertTrue(all(letter in mean_dict.keys() for letter in all_letters))

    def test_case_3(self):
        # Test if the values in the dictionary are floats (means of lists of integers)
        mean_dict = f_1003()
        self.assertTrue(all(isinstance(val, float) for val in mean_dict.values()))

    def test_case_4(self):
        # Test if the values are between 0 and 100 (as random integers are between 0 and 100)
        mean_dict = f_1003()
        self.assertTrue(all(0 <= val <= 100 for val in mean_dict.values()))

    def test_case_5(self):
        # Test if the dictionary has 26 keys (for each letter of the alphabet)
        mean_dict = f_1003()
        self.assertEqual(len(mean_dict), 26)


if __name__ == "__main__":
    run_tests()
