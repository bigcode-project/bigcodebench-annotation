import numpy as np
import datetime

def task_func(arr):
    """
    Reverse the order of words separated by. "" in all strings of a numpy array.

    Parameters:
    - arr (numpy array): The numpy array.

    Returns:
    - numpy.ndarray: The numpy array with the strings reversed.

    Requirements:
    - numpy
    - datetime

    Example:
    >>> arr = np.array(['apple.orange', 'red.green.yellow'])
    >>> reversed_arr = task_func(arr)
    >>> print(reversed_arr)
    ['orange.apple' 'yellow.green.red']
    """

    vectorized_reverse = np.vectorize(lambda s: '.'.join(s.split('.')[::-1]))
    now = datetime.datetime.now()
    return vectorized_reverse(arr)

import numpy as np
import unittest
import re
class TestCases(unittest.TestCase):
    """
    Define test cases for the task_func function.
    """
    
    def test_case_1(self):
        # Test description: 
        # Test reversing of words separated by '.' for a typical input.
        arr = np.array(['apple.orange', 'red.green.yellow'])
        result = task_func(arr)
        expected = np.array(['orange.apple', 'yellow.green.red'])
        np.testing.assert_array_equal(result, expected)
    def test_case_2(self):
        # Test description: 
        # Test reversing of words separated by '.' for another typical input.
        arr = np.array(['hello.world', 'this.is.a.test'])
        result = task_func(arr)
        expected = np.array(['world.hello', 'test.a.is.this'])
        np.testing.assert_array_equal(result, expected)
    def test_case_3(self):
        # Test description: 
        # Test input where words are not separated by '.', so they should remain unchanged.
        arr = np.array(['hello', 'world'])
        result = task_func(arr)
        expected = np.array(['hello', 'world'])
        np.testing.assert_array_equal(result, expected)
    def test_case_4(self):
        # Test description: 
        # Test input with empty strings. The result should also be empty strings.
        arr = np.array(['', ''])
        result = task_func(arr)
        expected = np.array(['', ''])
        np.testing.assert_array_equal(result, expected)
    def test_case_5(self):
        # Test description: 
        # Test reversing of words with a mix of uppercase and lowercase letters.
        arr = np.array(['OpenAI.GPT', 'GPT-4.is.amazing'])
        result = task_func(arr)
        expected = np.array(['GPT.OpenAI', 'amazing.is.GPT-4'])
        np.testing.assert_array_equal(result, expected)
