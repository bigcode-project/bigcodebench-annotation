import numpy as np
import itertools

def f_666(dimension):
    """
    Create a 2D numeric array (matrix) of a given dimension with random integers between 1 and 100, 
    and a flat list of all elements in the matrix.

    Parameters:
    - dimension (int): The dimension of the square matrix to be created. It must be a positive integer.

    Returns:
    tuple: A tuple containing:
        - A 2D numpy array of the given dimension with random integers between 1 and 100.
        - A flat list of all elements in the matrix.

    Requirements:
    - numpy
    - itertools

    Example:
    >>> matrix, flat_list = f_666(3)
    Combinations of pairs of elements: [(52, 93), (52, 15), (52, 72), (52, 61), (52, 21), (52, 83), (52, 87), (52, 75), (93, 15), (93, 72), (93, 61), (93, 21), (93, 83), (93, 87), (93, 75), (15, 72), (15, 61), (15, 21), (15, 83), (15, 87), (15, 75), (72, 61), (72, 21), (72, 83), (72, 87), (72, 75), (61, 21), (61, 83), (61, 87), (61, 75), (21, 83), (21, 87), (21, 75), (83, 87), (83, 75), (87, 75)]
    >>> print(matrix)
    [[52 93 15]
     [72 61 21]
     [83 87 75]]
    >>> print(flat_list)
    [52, 93, 15, 72, 61, 21, 83, 87, 75]
    """
    if dimension <= 0:
        raise ValueError("The dimension must be a positive integer")
    np.random.seed(42)  # Ensure reproducible results
    matrix = np.random.randint(1, 101, size=(dimension, dimension))
    flat_list = matrix.flatten().tolist()
    combinations = list(itertools.combinations(flat_list, 2))
    print("Combinations of pairs of elements:", combinations)
    return matrix, flat_list

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_positive_dimension(self):
        """
        Test Case 1: Test with a positive dimension
        Input: 3 (a positive integer)
        Expected Output: A 3x3 matrix and a flat list of 9 elements, with all elements between 1 and 100.
        """
        dimension = 3
        matrix, flat_list = f_666(dimension)
        self.assertEqual(matrix.shape, (dimension, dimension))
        self.assertEqual(len(flat_list), dimension ** 2)
        self.assertTrue(all(1 <= x <= 100 for x in flat_list))
    def test_dimension_one(self):
        """
        Test Case 2: Test with the smallest positive dimension
        Input: 1 (smallest positive integer for dimension)
        Expected Output: A 1x1 matrix and a flat list of 1 element, with the element between 1 and 100.
        """
        dimension = 1
        matrix, flat_list = f_666(dimension)
        self.assertEqual(matrix.shape, (dimension, dimension))
        self.assertEqual(len(flat_list), dimension ** 2)
        self.assertTrue(all(1 <= x <= 100 for x in flat_list))
    def test_large_dimension(self):
        """
        Test Case 3: Test with a large dimension
        Input: 100 (a large positive integer)
        Expected Output: A 100x100 matrix and a flat list of 10000 elements, with all elements between 1 and 100.
        """
        dimension = 100
        matrix, flat_list = f_666(dimension)
        self.assertEqual(matrix.shape, (dimension, dimension))
        self.assertEqual(len(flat_list), dimension ** 2)
        self.assertTrue(all(1 <= x <= 100 for x in flat_list))
    def test_zero_dimension(self):
        """
        Test Case 4: Test with a dimension of zero (invalid input)
        Input: 0 (zero is an invalid input for dimension)
        Expected Output: ValueError
        """
        dimension = 0
        with self.assertRaises(ValueError):
            f_666(dimension)
    def test_negative_dimension(self):
        """
        Test Case 5: Test with a negative dimension (invalid input)
        Input: -3 (a negative integer, invalid input for dimension)
        Expected Output: ValueError
        """
        dimension = -3
        with self.assertRaises(ValueError):
            f_666(dimension)
