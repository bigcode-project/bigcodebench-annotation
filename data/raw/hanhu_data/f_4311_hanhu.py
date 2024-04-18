from collections import OrderedDict
from prettytable import PrettyTable


def f_4313(my_dict):
    """
    Sorts a given dictionary by its keys in ascending order and returns a PrettyTable object displaying the sorted items.

    Parameters:
    my_dict (dict): The dictionary to be sorted and displayed.

    Returns:
    PrettyTable: A PrettyTable object representing the sorted dictionary.

    Requirements:
    - collections.OrderedDict
    - prettytable.PrettyTable

    Examples:
    Display a simple dictionary in a sorted table format.
    >>> table = f_4313({3: 'apple', 1: 'banana', 2: 'cherry'})
    >>> str(table).startswith('+') and 'banana' in str(table)
    True

    Display an empty dictionary.
    >>> str(f_4313({})).startswith('+')
    True
    """
    ordered_dict = OrderedDict(sorted(my_dict.items(), key=lambda t: t[0]))
    table = PrettyTable(['Key', 'Value'])

    for key, value in ordered_dict.items():
        table.add_row([key, value])

    return table


import unittest

class TestF4313(unittest.TestCase):
    def test_sort_and_display_dict(self):
        my_dict = {3: 'apple', 1: 'banana', 2: 'cherry'}
        table = f_4313(my_dict)
        expected_header = '+-----+--------+'
        self.assertIn(expected_header, str(table))
        self.assertIn('banana', str(table))

    def test_empty_dict(self):
        table = f_4313({})
        expected_header = '+-----+-------+'
        self.assertIn(expected_header, str(table))

    def test_single_element_dict(self):
        my_dict = {1: 'single'}
        table = f_4313(my_dict)
        self.assertIn('single', str(table))

    def test_non_string_values(self):
        my_dict = {1: 100, 2: 200.5}
        table = f_4313(my_dict)
        self.assertIn('100', str(table))
        self.assertIn('200.5', str(table))

    def test_string_keys(self):
        my_dict = {'a': 'apple', 'b': 'banana'}
        table = f_4313(my_dict)
        self.assertIn('apple', str(table))
        self.assertIn('banana', str(table))

    def test_large_dict(self):
        my_dict = {i: str(i) for i in range(1000)}
        table = f_4313(my_dict)
        self.assertEqual(len(table._rows), 1000)


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestF4313)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
