import heapq
import random

def task_func(k, list_length = 5, min_value = 0, max_value = 100):
    """
    Find the k smallest numbers in a randomly generated list using heapq.

    Parameters:
    k (int): The number of smallest elements to find.
    list_length (int): The length of the randomly generated list of integers.
    min_value (int): The minimum value for randomly generated integers.
    max_value (int): The maximum value for randomly generated integers.

    Returns:
    tuple: A tuple containing two lists: 
        - list[int]: The randomly generated list of integers with the specified length.
        - list[int]: The k smallest numbers found using heapq.

    Requirements:
    - heapq
    - random

    Example:
    >>> random.seed(0)
    >>> rand_list, least_k = task_func(3)
    >>> least_k[0] in rand_list
    True
    >>> rand_list, least_k = task_func(3,5,100,100)
    >>> print(least_k)
    [100, 100, 100]
    """
    numbers = [random.randint(min_value, max_value) for _ in range(list_length)]
    heapq.heapify(numbers)
    smallest_numbers = heapq.nsmallest(k, numbers)
    return numbers, smallest_numbers

import unittest
import random
class TestCases(unittest.TestCase):
    
    def test_empty_list(self):
        random.seed(0)
        rand_list, least_k = task_func(0, 0)
        self.assertEqual(rand_list, [])
        self.assertEqual(least_k, [])
    def test_k_larger_than_list_length(self):
        random.seed(0)
        rand_list, least_k = task_func(5, 10)
        self.assertEqual(len(rand_list), 10)
        self.assertEqual(len(least_k), 5)
    def test_sorted_list(self):
        random.seed(0)
        rand_list, least_k = task_func(100, 3)
        self.assertEqual(least_k, sorted(rand_list)[:3])
    def test_least_k_sorted(self):
        random.seed(0)
        rand_list, least_k = task_func(100, 5, 100, 100)
        self.assertEqual(least_k, sorted(least_k)[:5])
    
    def test_least_k_sorted_first(self):
        random.seed(0)
        rand_list, least_k = task_func(100, 5)
        self.assertEqual(least_k[0], sorted(least_k)[0])
