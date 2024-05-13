import random
import math

def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    """
    Create a dictionary where keys are letters from a predefined list LETTERS and values are lists of random integers.
    Then, calculates the population standard deviation for each list of integers and returns a dictionary of these values.

    The random integers for each key are generated within the range 0 to 100, and each list contains between 1 to 10 integers.

    Parameters:
        LETTERS (list of str, optional): A list of single-character strings to be used as keys in the output dictionary.
                                         Defaults to the lowercase English alphabets ['a', 'b', ..., 'z'].

    Returns:
        dict: A dictionary where each key corresponds to a letter from the input list and each value is the 
              population standard deviation of a list of random integers associated with that key.

    Requirements:
    - random
    - math

    Example:
    >>> import random
    >>> random.seed(42)
    >>> sd_dict = task_func()
    >>> print(sd_dict)
    {'a': 45.5, 'b': 29.4659125092029, 'c': 25.575354649194974, 'd': 28.271717316074028, 'e': 29.118550788114437, 'f': 16.886056048968, 'g': 27.48108440364026, 'h': 32.67476090195611, 'i': 8.5, 'j': 17.5406234036238, 'k': 22.993205518152532, 'l': 2.0, 'm': 25.468935326524086, 'n': 10.23067283548187, 'o': 35.13922924736349, 'p': 26.649654437396617, 'q': 27.027763503479157, 'r': 20.316629447296748, 's': 24.997777679003566, 't': 0.0, 'u': 30.070288030250428, 'v': 21.82864622275892, 'w': 37.92308004368844, 'x': 29.899006961502092, 'y': 33.89321466016465, 'z': 21.0}
    """

    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    sd_dict = {
        k: math.sqrt(sum((i - sum(v) / len(v)) ** 2 for i in v) / len(v))
        for k, v in random_dict.items()
    }
    return sd_dict

import unittest
from unittest.mock import patch
import math
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        self.LETTERS = [chr(i) for i in range(97, 123)]
        random.seed(42)
    def test_default_letters(self):
        # Test the function with the default set of letters
        sd_dict = task_func()
        self.assertEqual(set(self.LETTERS), set(sd_dict.keys()))
        for val in sd_dict.values():
            self.assertGreaterEqual(val, 0)
    def test_custom_letters(self):
        # Test the function with a custom set of letters
        custom_letters = ['x', 'y', 'z']
        sd_dict = task_func(custom_letters)
        self.assertEqual(set(custom_letters), set(sd_dict.keys()))
        for val in sd_dict.values():
            self.assertGreaterEqual(val, 0)
    
    @patch('random.randint')
    def test_uniform_values(self, mocked_randint):
         # Test with uniform values to check standard deviation is zero
        mocked_randint.side_effect = [3, 50, 50, 50, 3, 50, 50, 50]  # Two iterations: size 3, values all 50
        letters = ['a', 'b']
        sd_dict = task_func(letters)
        self.assertTrue(all(math.isclose(val, 0, abs_tol=1e-5) for val in sd_dict.values()))
    
    def test_empty_letters(self):
        # Test with an empty list of letters
        sd_dict = task_func([])
        self.assertEqual(sd_dict, {})
    @patch('random.randint')
    def test_known_values(self, mocked_randint):
        # Test with known values to check correct standard deviation calculation
        mocked_randint.side_effect = [2, 10, 1]  # List size of 2, with values 10 and 1
        letters = ['a']
        sd_dict = task_func(letters)
        values = [10, 1]
        mean = sum(values) / len(values)
        sum_of_squares = sum((x - mean) ** 2 for x in values)
        expected_sd = math.sqrt(sum_of_squares / len(values))
        self.assertAlmostEqual(list(sd_dict.values())[0], expected_sd)
