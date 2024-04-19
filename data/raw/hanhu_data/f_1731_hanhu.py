import random
import string
from collections import Counter

def f_1732(num_strings, string_length):
    """
    Creates a list of random strings, each of a specified length, and counts the frequency
    of each character across all strings. The function then returns the characters
    and their frequencies sorted by frequency in descending order.
    The random strings are composed of ASCII lowercase characters.

    Args:
        num_strings (int): The number of random strings to generate.
        string_length (int): The length of each random string.

    Requirements:
    - random
    - string
    - collections.Counter

    Returns:
        list of tuple: A list of tuples where each tuple contains a character and its count,
                       sorted by count in descending order.

    Examples:
    >>> type(f_1732(1000, 5)) == list
    True
    >>> all(isinstance(pair, tuple) and len(pair) == 2 for pair in f_1732(1000, 5))
    True
    """
    strings = [''.join(random.choices(string.ascii_lowercase, k=string_length)) for _ in range(num_strings)]
    characters = ''.join(strings)
    character_counter = Counter(characters)
    most_common_characters = character_counter.most_common()

    return most_common_characters

import unittest
import random

class TestCases(unittest.TestCase):
    def setUp(self):
        # This method will be run before each test.
        random.seed(0)  # Set a seed for reproducibility in all tests

    def test_return_type(self):
        """ Test that the function returns a list. """
        result = f_1732(100, 5)
        self.assertIsInstance(result, list)

    def test_list_length(self):
        """ Test that the length of the list is not greater than the number of unique characters. """
        result = f_1732(100, 5)
        self.assertLessEqual(len(result), 26)  # 26 letters in the ASCII lowercase alphabet

    def test_tuple_structure(self):
        """ Test that each element in the list is a tuple with two elements. """
        result = f_1732(100, 5)
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)

    def test_deterministic_output(self):
        """ Test the function with a predefined seed for reproducibility. """
        result = f_1732(100, 5)
        self.assertTrue(all(isinstance(pair, tuple) and len(pair) == 2 for pair in result))
        self.assertGreater(len(result), 0)  # Ensure the result is not empty

    def test_specific_character_count(self):
        """ Test if a specific character count is as expected based on the seed. """
        result = f_1732(100, 5)
        specific_char = 'a'  # Example character to check
        specific_count = next((count for char, count in result if char == specific_char), 0)
        self.assertGreater(specific_count, 0)  # Check if the count for the specific character is greater than 0

    def test_zero_strings(self):
        """ Test the function returns an empty list when no strings are generated. """
        result = f_1732(0, 5)
        self.assertEqual(result, [])

    def test_zero_length(self):
        """ Test the function with string_length of zero returns empty strings but counts them. """
        result = f_1732(100, 0)
        self.assertEqual(result, [])


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
