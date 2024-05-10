from multiprocessing import Pool
import math

def calculate_factorial(number: int) -> tuple:
    return number, math.factorial(number)
    
def f_3049(numbers: list) -> dict:
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
    >>> factorials = f_3049([5, 6, 7, 8, 9])
    >>> factorials[5] == 120 and factorials[9] == 362880
    True
    """
    # Check input types
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
        result = f_3049([3, 4, 5])
        self.assertIsInstance(result, dict)

    def test_empty_list(self):
        """Test function with an empty list."""
        result = f_3049([])
        self.assertEqual(result, {})

    def test_single_element(self):
        """Test function with a single-element list."""
        result = f_3049([5])
        self.assertEqual(result, {5: 120})

    def test_non_integer_input(self):
        """Test function with non-integer input."""
        with self.assertRaises(ValueError):
            f_3049(["a"])

    def test_large_numbers(self):
        """Test function with large numbers."""
        result = f_3049([10])
        self.assertEqual(result[10], math.factorial(10))

    def test_negative_numbers(self):
        """Test function with a negative number."""
        with self.assertRaises(ValueError):
            f_3049([-1])  # Assuming we want to enforce non-negative integers only

    def test_very_large_number(self):
        """Test function with a very large number to check for performance or overflow issues."""
        number = 20  # A reasonable choice to avoid excessive computation time in tests
        result = f_3049([number])
        self.assertEqual(result[number], math.factorial(number))


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
