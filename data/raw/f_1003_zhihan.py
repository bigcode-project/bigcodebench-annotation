import random
import numpy as np

def f_1003():
    """
    Create a dictionary in which keys are letters of the alphabet and values are lists of random integers.
    Then calculate the mean of the values for each key and return a dictionary with these means.
    
    Requirements:
    - random
    - numpy
    
    Returns:
    dict: A dictionary where keys are letters of the alphabet and values are their mean values from 
          a list of random integers associated with each letter.
          
    Example:
    >>> mean_dict = f_1003()
    >>> isinstance(mean_dict, dict)
    True
    >>> 'a' in mean_dict.keys()
    True
    """
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    mean_dict = {k: np.mean(v) for k, v in random_dict.items()}
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
        all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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