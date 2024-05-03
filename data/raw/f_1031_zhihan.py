import numpy as np
from functools import reduce


def f_1031(list_of_pairs):
    """ 
    Calculate the product of the second elements in each tuple in a list and return the product as a single numeric value.

    Parameters:
    list_of_pairs (list of tuple): A list of tuples, where each tuple consists of a category (first element) and a numeric value (second element).

    Returns:
    int or float: The product of the second elements in the tuples.

    Requirements:
    - numpy
    - functools

    Example:
    >>> list_of_pairs = [('Fruits', 5), ('Vegetables', 9), ('Dairy', -1), ('Bakery', -2), ('Meat', 4)]
    >>> product = f_1031(list_of_pairs)
    >>> print(product)
    360
    """
    if len(list_of_pairs) == 0:
        return 0
    second_values = [pair[1] for pair in list_of_pairs]
    product = reduce(np.multiply, second_values)

    return product


import unittest
import numpy as np
from functools import reduce


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Basic test case with positive and negative numbers
        list_of_pairs = [('Fruits', 5), ('Vegetables', 9), ('Dairy', -1), ('Bakery', -2), ('Meat', 4)]
        expected_output = 360
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))

    def test_case_2(self):
        # Test case with all positive numbers
        list_of_pairs = [('A', 2), ('B', 3), ('C', 4)]
        expected_output = 24
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))

    def test_case_3(self):
        # Test case with all negative numbers
        list_of_pairs = [('A', -2), ('B', -3), ('C', -4)]
        expected_output = -24
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))

    def test_case_4(self):
        # Test case with a single tuple
        list_of_pairs = [('A', 10)]
        expected_output = 10
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))

    def test_case_5(self):
        # Test case with zeros
        list_of_pairs = [('A', 0), ('B', 5), ('C', 10)]
        expected_output = 0
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))

    def test_case_6(self):
        # Empty case
        list_of_pairs = []
        expected_output = 0
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))


if __name__ == "__main__":
    run_tests()
