from random import randint
import math

LETTERS = [chr(i) for i in range(97, 123)]

def f_1005():
    """
    Create a dictionary where:
    - Keys are letters from a predefined list LETTERS.
    - Values are lists of random integers.
    
    The function then calculates the standard deviation for each list of integers 
    and returns a dictionary with these standard deviations.

    Returns:
    dict: The dictionary with the standard deviations for each letter.
    
    Requirements:
    - random
    - math
    
    Example:
    >>> sd_dict = f_1005()
    >>> print(sd_dict)
    {'a': 29.546573405388315, 'b': 31.304951684997057, ...}
    """
    random_dict = {k: [randint(0, 100) for _ in range(randint(1, 10))] for k in LETTERS}
    sd_dict = {
        k: math.sqrt(sum((i - sum(v) / len(v)) ** 2 for i in v) / len(v))
        for k, v in random_dict.items()
    }
    return sd_dict

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        sd_dict = f_1005()
        self.assertEqual(set(LETTERS), set(sd_dict.keys()))
        for val in sd_dict.values():
            self.assertGreaterEqual(val, 0)
            
    def test_case_2(self):
        sd_dict = f_1005()
        self.assertEqual(set(LETTERS), set(sd_dict.keys()))
        for val in sd_dict.values():
            self.assertGreaterEqual(val, 0)
            
    def test_case_3(self):
        sd_dict = f_1005()
        self.assertEqual(set(LETTERS), set(sd_dict.keys()))
        for val in sd_dict.values():
            self.assertGreaterEqual(val, 0)
            
    def test_case_4(self):
        sd_dict = f_1005()
        self.assertEqual(set(LETTERS), set(sd_dict.keys()))
        for val in sd_dict.values():
            self.assertGreaterEqual(val, 0)
            
    def test_case_5(self):
        sd_dict = f_1005()
        self.assertEqual(set(LETTERS), set(sd_dict.keys()))
        for val in sd_dict.values():
            self.assertGreaterEqual(val, 0)
if __name__ == "__main__":
    run_tests()