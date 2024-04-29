import collections
import random
import string

def f_1001(length=100):
    """
    Generate a random string of the specified length, and then count the occurrence of each character.
    
    Parameters:
    - length (int, optional): The length of the random string to be generated. Default is 100.
    
    Returns:
    dict: A dictionary where keys are characters and values are their counts.

    Requirements:
    - collections
    - random
    - string

    Example:
    >>> f_1001(10)
    # Returns a dictionary with counts of each character in the generated string. 
    # Since the output is random, the exact dictionary will vary.
    """
    random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))
    char_counts = collections.Counter(random_string)
    return dict(char_counts)

import unittest
import string

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        self.valid_chars = string.ascii_uppercase + string.ascii_lowercase

    def test_case_1(self):
        result = f_1001(10)
        self.assertTrue(len(result) <= 10)
        self.assertEqual(sum(result.values()), 10)
        for char in result:
            self.assertTrue(char in self.valid_chars)

    def test_case_2(self):
        result = f_1001(50)
        self.assertTrue(len(result) <= 50)
        self.assertEqual(sum(result.values()), 50)
        for char in result:
            self.assertTrue(char in self.valid_chars)

    def test_case_3(self):
        result = f_1001(100)
        self.assertTrue(len(result) <= 100)
        self.assertEqual(sum(result.values()), 100)
        for char in result:
            self.assertTrue(char in self.valid_chars)

    def test_case_4(self):
        result = f_1001(150)
        self.assertTrue(len(result) <= 150)
        self.assertEqual(sum(result.values()), 150)
        for char in result:
            self.assertTrue(char in self.valid_chars)

    def test_case_5(self):
        result = f_1001(5)
        self.assertTrue(len(result) <= 5)
        self.assertEqual(sum(result.values()), 5)
        for char in result:
            self.assertTrue(char in self.valid_chars)

if __name__ == "__main__":
    run_tests()