import numpy as np
import random

def task_func(my_list):
    """
    Appends a randomly selected integer between 0 and 100 to the given list 'my_list' and 
    returns a numpy array of random floating-point numbers. The size of the returned array 
    is equal to the sum of the numbers in the modified list.

    Parameters:
        my_list (list): A list of integers to which a random number will be added.

    Returns:
        numpy.ndarray: An array of random floating-point numbers. The length of the array 
                       is equal to the sum of the integers in 'my_list' after a random 
                       number has been appended.

    Requirements:
    - numpy
    - random
                       
    Examples:
        >>> result = task_func([2, 3, 5])
        >>> 10 <= len(result) <= 110  # Expecting the length to be within the range after adding a random number between 0 and 100
        True
        >>> isinstance(result, np.ndarray)
        True
    """
    random_number = random.randint(0, 100)
    my_list.append(random_number)
    size = sum(my_list)
    random_array = np.random.rand(size)
    return random_array

import unittest
from unittest.mock import patch
import numpy as np
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """ Test that the function returns a numpy array. """
        result = task_func([1, 2, 3])
        self.assertIsInstance(result, np.ndarray)
    @patch('random.randint', return_value=50)
    def test_array_size(self, mock_randint):
        """ Test that the returned array has the correct size. """
        input_list = [1, 2, 3]
        expected_size = sum(input_list) + 50  # The function adds a mocked random number to the list
        result = task_func(input_list)
        self.assertEqual(len(result), expected_size)
    @patch('random.randint', return_value=50)
    def test_list_modification(self, mock_randint):
        """ Test that the input list is modified correctly with a mocked random value. """
        input_list = [1, 2, 3]
        task_func(input_list)
        self.assertIn(50, input_list)  # Asserting the list contains the mocked random value
    @patch('random.randint', return_value=50)
    def test_empty_list(self, mock_randint):
        """ Test the function with an empty list and a mocked random addition. """
        result = task_func([])
        self.assertEqual(len(result), 50)  # Expecting the array size to be equal to the mocked random number
    @patch('numpy.random.rand')
    @patch('random.randint', return_value=50)
    def test_mock_random_array(self, mock_randint, mock_rand):
        """ Test the function with mocks of randint and np.random.rand to control the randomness. """
        mock_rand.return_value = np.array([0.5] * 53)  # Setting the mock array size to 53
        input_list = [1, 2]
        result = task_func(input_list)
        mock_rand.assert_called_once_with(53)  # Assert that np.random.rand is called with the size after adding 50
        np.testing.assert_array_equal(result, np.array([0.5] * 53))
