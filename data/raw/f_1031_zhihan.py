import numpy as np
from functools import reduce

def f_1031(list_of_pairs):
    """ 
    Calculate the product of the second values in each tuple in a list of tuples and return the product as a numeric array.
    
    Parameters:
    list_of_pairs (list): A list of tuples, where the first element is the category 
                          and the second element is the numeric value.
    
    Returns:
    numpy.ndarray: A numpy array with the product of the second values.
    
    Requirements:
    - numpy
    - functools
    
    Example:
    >>> list_of_pairs = [('Fruits', 5), ('Vegetables', 9), ('Dairy', -1), ('Bakery', -2), ('Meat', 4)]
    >>> product_array = f_1031(list_of_pairs)
    >>> print(product_array)
    """
    second_values = [pair[1] for pair in list_of_pairs]
    product = reduce(np.multiply, second_values)
    product_array = np.array(product)

    return product_array

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
        expected_output = np.array(360)
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))
    
    def test_case_2(self):
        # Test case with all positive numbers
        list_of_pairs = [('A', 2), ('B', 3), ('C', 4)]
        expected_output = np.array(24)
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))
    
    def test_case_3(self):
        # Test case with all negative numbers
        list_of_pairs = [('A', -2), ('B', -3), ('C', -4)]
        expected_output = np.array(-24)
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))
    
    def test_case_4(self):
        # Test case with a single tuple
        list_of_pairs = [('A', 10)]
        expected_output = np.array(10)
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))
    
    def test_case_5(self):
        # Test case with zeros
        list_of_pairs = [('A', 0), ('B', 5), ('C', 10)]
        expected_output = np.array(0)
        actual_output = f_1031(list_of_pairs)
        self.assertTrue(np.array_equal(actual_output, expected_output))
if __name__ == "__main__":
    run_tests()