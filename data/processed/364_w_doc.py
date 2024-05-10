from multiprocessing import Pool
import math

def calculate_factorial(number: int) -> tuple:
    return number, math.factorial(number)
    
def task_func(numbers: list) -> dict:
    """
    Calculate factorials for a list of numbers in parallel using multiprocessing.

    Parameters:
    numbers (list[int]): List of numbers to calculate factorials.

    Returns:
    dict[int, int]: A dictionary with numbers as keys and their factorial as values.

    Raises:
    ValueError: If any element in the input list is not an integer or is negative.

    Requirements:
    - multiprocessing.Pool
    - math.factorial

    Example:
    >>> factorials = task_func([5, 6, 7, 8, 9])
    >>> factorials[5] == 120 and factorials[9] == 362880
    True
    """
    if not all(isinstance(n, int) and n >= 0 for n in numbers):
        raise ValueError("All elements in the list must be integers")
    with Pool() as pool:
        factorial_dict = dict(pool.starmap(calculate_factorial, [(i,) for i in numbers]))
    return factorial_dict

import unittest
import math
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a dictionary."""
        result = task_func([3, 4, 5])
        self.assertIsInstance(result, dict)
    def test_empty_list(self):
        """Test function with an empty list."""
        result = task_func([])
        self.assertEqual(result, {})
    def test_single_element(self):
        """Test function with a single-element list."""
        result = task_func([5])
        self.assertEqual(result, {5: 120})
    def test_non_integer_input(self):
        """Test function with non-integer input."""
        with self.assertRaises(ValueError):
            task_func(["a"])
    def test_large_numbers(self):
        """Test function with large numbers."""
        result = task_func([10])
        self.assertEqual(result[10], math.factorial(10))
    def test_negative_numbers(self):
        """Test function with a negative number."""
        with self.assertRaises(ValueError):
            task_func([-1])  # Assuming we want to enforce non-negative integers only
    def test_very_large_number(self):
        """Test function with a very large number to check for performance or overflow issues."""
        number = 20  # A reasonable choice to avoid excessive computation time in tests
        result = task_func([number])
        self.assertEqual(result[number], math.factorial(number))
