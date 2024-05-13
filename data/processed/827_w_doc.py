import math
from sympy import isprime


def task_func(input_list):
    """
    Filter the prime numbers from the specified list, sort the prime numbers 
    ascending based on their radian value converted to degrees, and return the sorted list.
    
    The function uses the isprime function from the sympy library to determine prime numbers 
    and the degrees function from the math library to sort the numbers based on their degree value.

    Parameters:
    input_list (list[int]): A list of integers to be filtered and sorted.

    Returns:
    list[int]: A sorted list of prime numbers based on their degree value.

    Requirements:
    - math
    - sympy

    Examples:
    >>> task_func([4, 5, 2, 7, 89, 90])
    [2, 5, 7, 89]
    
    >>> task_func([101, 102, 103, 104])
    [101, 103]
    """

    primes = [i for i in input_list if isprime(i)]
    sorted_primes = sorted(primes, key=lambda x: (math.degrees(x), x))
    return sorted_primes

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_data = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = [2, 3, 5, 7]
        self.assertEqual(task_func(input_data), expected_output)
    def test_case_2(self):
        input_data = [2, 3, 5, 7, 11, 13, 17, 19]
        expected_output = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(task_func(input_data), expected_output)
    def test_case_3(self):
        input_data = [4, 6, 8, 9, 10, 12, 14, 15, 16]
        expected_output = []
        self.assertEqual(task_func(input_data), expected_output)
    def test_case_4(self):
        input_data = []
        expected_output = []
        self.assertEqual(task_func(input_data), expected_output)
    def test_case_5(self):
        input_data = [89, 90, 91, 97, 98, 99, 100]
        expected_output = [89, 97]
        self.assertEqual(task_func(input_data), expected_output)
