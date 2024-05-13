import random
import numpy as np

def task_func(LETTERS):
    """
    Create a dictionary where keys are specified letters and values are lists of random integers.
    Then calculate the mean of these integers for each key and return a dictionary of these means.

    Parameters:
        LETTERS (list of str): List of single-character strings to be used as keys in the output dictionary.
    
    Returns:
        dict: A dictionary where each key is a letter from the input list and the value is the mean of 
              a randomly generated list of integers (with each list having 1 to 10 integers ranging from 0 to 100).
    
    Requirements:
    - random
    - np (numpy)
    
    Example:
    >>> LETTERS = ['a', 'b', 'c']
    >>> mean_dict = task_func(LETTERS)
    >>> isinstance(mean_dict, dict)
    True
    >>> 'a' in mean_dict.keys() and 'b' in mean_dict.keys() and 'c' in mean_dict.keys()
    True
    >>> all(isinstance(v, float) for v in mean_dict.values())  # Check if all values are floats
    True
    """

    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    mean_dict = {k: np.mean(v) for k, v in random_dict.items()}
    return mean_dict

import unittest
    
class TestCases(unittest.TestCase):
    def setUp(self):
        # Common setup for all tests: explicitly define the list of letters
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def test_case_1(self):
        # Test if the function returns a dictionary
        mean_dict = task_func(self.letters)
        self.assertIsInstance(mean_dict, dict)
    def test_case_2(self):
        # Test if the dictionary contains all letters of the alphabet
        mean_dict = task_func(self.letters)
        self.assertTrue(all(letter in mean_dict for letter in self.letters))
        
    def test_case_3(self):
        # Test if the values in the dictionary are floats (means of lists of integers)
        mean_dict = task_func(self.letters)
        self.assertTrue(all(isinstance(val, float) for val in mean_dict.values()))
    def test_case_4(self):
        # Test if the mean values are reasonable given the range of random integers (0-100)
        mean_dict = task_func(self.letters)
        self.assertTrue(all(0 <= val <= 100 for val in mean_dict.values()))
    def test_case_5(self):
        # Test if the dictionary has 26 keys (one for each letter of the alphabet)
        mean_dict = task_func(self.letters)
        self.assertEqual(len(mean_dict), 26)
