import numpy as np
from collections import Counter


def f_933(list_of_tuples):
    """
    Computes the sum of numeric values and counts the occurrences of categories in a list of tuples.

    Each tuple in the input list contains a numeric value and a category. This function calculates
    the sum of all the numeric values and also counts how many times each category appears in the list.

    Parameters:
    - list_of_tuples (list of tuple): A list where each tuple contains a numeric value and a category.

    Returns:
    - tuple: A 2-element tuple where the first element is the sum of the numeric values, and the
             second element is a dictionary with categories as keys and their counts as values.

    Requirements:
    - numpy
    - collections.Counter

    Example:
    >>> list_of_tuples = [(5, 'Fruits'), (9, 'Vegetables'), (-1, 'Dairy'), (-2, 'Bakery'), (4, 'Meat')]
    >>> sum_of_values, category_counts = f_933(list_of_tuples)
    >>> print(sum_of_values)
    15
    >>> print(category_counts)
    {'Fruits': 1, 'Vegetables': 1, 'Dairy': 1, 'Bakery': 1, 'Meat': 1}
    """

    numeric_values = [pair[0] for pair in list_of_tuples]
    categories = [pair[1] for pair in list_of_tuples]

    total_sum = np.sum(numeric_values)
    category_counts = Counter(categories)

    return total_sum, dict(category_counts)


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Regular list of tuples with different categories
        input_data = [(5, 'Fruits'), (9, 'Vegetables'), (-1, 'Dairy'), (-2, 'Bakery'), (4, 'Meat')]
        sum_values, count_values = f_933(input_data)
        self.assertEqual(sum_values, 15)
        self.assertEqual(count_values, {'Fruits': 1, 'Vegetables': 1, 'Dairy': 1, 'Bakery': 1, 'Meat': 1})

    def test_case_2(self):
        # List of tuples with all the same categories
        input_data = [(5, 'Fruits'), (9, 'Fruits'), (-1, 'Fruits'), (-2, 'Fruits')]
        sum_values, count_values = f_933(input_data)
        self.assertEqual(sum_values, 11)
        self.assertEqual(count_values, {'Fruits': 4})

    def test_case_3(self):
        # List of tuples with all negative numeric values
        input_data = [(-5, 'Fruits'), (-9, 'Vegetables'), (-1, 'Dairy')]
        sum_values, count_values = f_933(input_data)
        self.assertEqual(sum_values, -15)
        self.assertEqual(count_values, {'Fruits': 1, 'Vegetables': 1, 'Dairy': 1})

    def test_case_4(self):
        # Empty list
        input_data = []
        sum_values, count_values = f_933(input_data)
        self.assertEqual(sum_values, 0)
        self.assertEqual(count_values, {})

    def test_case_5(self):
        # List of tuples with mixed positive and negative numeric values for the same category
        input_data = [(5, 'Fruits'), (-5, 'Fruits'), (3, 'Fruits')]
        sum_values, count_values = f_933(input_data)
        self.assertEqual(sum_values, 3)
        self.assertEqual(count_values, {'Fruits': 3})

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(f_933([]), (0, {}))

    def test_all_negative_values(self):
        """Test with all negative numeric values."""
        list_of_tuples = [(-5, 'Fruits'), (-2, 'Vegetables')]
        self.assertEqual(f_933(list_of_tuples), (-7, {'Fruits': 1, 'Vegetables': 1}))

    def test_duplicate_categories(self):
        """Test with duplicate categories."""
        list_of_tuples = [(1, 'Fruits'), (2, 'Fruits'), (3, 'Vegetables')]
        self.assertEqual(f_933(list_of_tuples), (6, {'Fruits': 2, 'Vegetables': 1}))

    def test_single_tuple_in_list(self):
        """Test with a single tuple in the list."""
        list_of_tuples = [(10, 'Meat')]
        self.assertEqual(f_933(list_of_tuples), (10, {'Meat': 1}))

    def test_float_numeric_values(self):
        """Test with non-integer numeric values (floats)."""
        list_of_tuples = [(1.5, 'Fruits'), (2.5, 'Vegetables')]
        self.assertEqual(f_933(list_of_tuples), (4.0, {'Fruits': 1, 'Vegetables': 1}))


if __name__ == "__main__":
    run_tests()
