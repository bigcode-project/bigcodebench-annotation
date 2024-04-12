import re

import pandas as pd
import numpy as np
import unittest
from unittest.mock import patch

def f_465(matrix1, matrix2):
    """
    Connects two 2D numeric arrays (matrices) along the second axis (columns),
    converts them into a Pandas DataFrame, and returns a string representation of the DataFrame.

    Parameters:
    - matrix1 (np.ndarray): The first 2D numpy array.
    - matrix2 (np.ndarray): The second 2D numpy array.

    Returns:
    - str: The string representation of the DataFrame without the index and header.

    Requirements:
    - pandas: For creating and manipulating the DataFrame.
    - numpy: For array manipulation and concatenation.

    Example:
    >>> matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    >>> matrix2 = np.array([[7, 8, 9], [10, 11, 12]])
    >>> print(f_465(matrix1, matrix2))
     1  2  3  7  8  9
     4  5  6 10 11 12
    """
    combined_matrix = np.concatenate((matrix1, matrix2), axis=1)
    df = pd.DataFrame(combined_matrix)
    return df.to_string(index=False, header=False)


import unittest

class TestF465(unittest.TestCase):

    def normalize_whitespace(self, string):
        """Normalize the whitespace in the string to a single space."""
        return re.sub(r'\s+', ' ', string).strip()


    def test_basic_concatenation(self):
        """Test basic functionality of concatenating two matrices."""
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[5, 6], [7, 8]])
        expected_output = " 1  2  5  6\n 3  4  7  8"
        result = f_465(matrix1, matrix2)
        self.assertEqual(self.normalize_whitespace(result), self.normalize_whitespace(expected_output))

    def test_different_length_matrices(self):
        """Test concatenation of matrices with different numbers of rows."""
        matrix1 = np.array([[1, 2], [3, 4], [5, 6]])
        matrix2 = np.array([[7, 8]])
        with self.assertRaises(ValueError):
            f_465(matrix1, matrix2)

    def test_mismatched_dimensions(self):
        """Test concatenation with mismatched dimensions."""
        matrix1 = np.array([[1, 2]])
        matrix2 = np.array([[3], [4]])
        with self.assertRaises(ValueError):
            f_465(matrix1, matrix2)

    def test_single_row_matrices(self):
        """Test concatenation of single-row matrices."""
        matrix1 = np.array([[1, 2, 3]])
        matrix2 = np.array([[4, 5, 6]])
        expected_output = " 1  2  3  4  5  6"
        result = f_465(matrix1, matrix2)
        self.assertEqual(self.normalize_whitespace(result), self.normalize_whitespace(expected_output))


    def test_non_numeric_matrices(self):
        """Ensure non-numeric matrices are handled."""
        matrix1 = np.array([['a', 'b']])
        matrix2 = np.array([['c', 'd']])
        expected_output = " a  b  c  d"
        result = f_465(matrix1, matrix2)
        self.assertEqual(self.normalize_whitespace(result), self.normalize_whitespace(expected_output))


if __name__ == '__main__':
    unittest.main()
