import heapq
import random


def f_291(list_length:5, k:int):
    """
    Find the k largest numbers in a random-generated list using heapq.

    Parameters:
    list_length (int): The length of the randomly generated list of integers.
    k (int): The number of largest elements to find.

    Returns:
    tuple: A tuple containing two lists: 
        - list[int]: The randomly generated list of integers with the specified length.
        - list[int]: The k largest numbers found using heapq.

    Requirements:
    - heapq
    - random

    Example:
    >>> rand_list, top_k = f_291(5, 3)
    >>> top_k[0] in rand_list
    True
    """

    
    numbers = [random.randint(0, 100) for _ in range(list_length)]
    heapq.heapify(numbers)
    largest_numbers = heapq.nlargest(k, numbers)
   
    return numbers, largest_numbers


import unittest

class TestCases(unittest.TestCase):
    def test_empty_list(self):
        rand_list, top_k = f_291(0, 3)
        self.assertEqual(rand_list, [])
        self.assertEqual(top_k, [])

    def test_k_larger_than_list_length(self):
        rand_list, top_k = f_291(5, 10)
        self.assertEqual(len(rand_list), 5)
        self.assertEqual(len(top_k), 5)

    def test_sorted_list(self):
        rand_list, top_k = f_291(100, 3)
        self.assertEqual(top_k, sorted(rand_list, reverse=True)[:3])

    def test_top_k_sorted(self):
        rand_list, top_k = f_291(100, 5)
        self.assertEqual(top_k, sorted(top_k, reverse=True)[:5])
    
    def test_top_k_sorted_first(self):
        rand_list, top_k = f_291(100, 5)
        self.assertEqual(top_k[0], sorted(top_k, reverse=True)[0])


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()