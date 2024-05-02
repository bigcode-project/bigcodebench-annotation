import random


def f_1002(letters):
    """
    Generates a dictionary where each key is a letter from the input set and its value is a list of random integers.
    The size of each list and the integers within are randomly determined. The dictionary is then sorted
    by the sum of the integers in the lists, with the highest sums first.

    Parameters:
    letters (str): A string of characters to be used as keys in the generated dictionary.

    Returns:
    dict: A dictionary sorted by the sum of list values in descending order. Keys are characters from the input string, and values are lists of integers.

    Requirements:
    - random module for generating random integers.

    Example usage might produce output like this (note: output will vary due to randomness):
    >>> f_1002('ab')
    {'a': [30, 69, 83, 72, 0, 17, 26], 'b': [68, 35, 36]}
    >>> sorted_dict = f_1002('abcdef')
    >>> list(sorted_dict.keys())[0]  # Example: 'e' (the key with the highest sum of integers in its list, varies due to randomness)
    >>> type(sorted_dict['a'])  # Example: <class 'list'>
    """
    # Create a dictionary with each input letter as a key and a random list of integers as its value
    random_dict = {letter: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for letter in letters}

    # Sort the dictionary by the sum of integers in the lists associated with each letter, in descending order
    sorted_dict_by_sum = dict(sorted(random_dict.items(), key=lambda item: sum(item[1]), reverse=True))

    return sorted_dict_by_sum


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_with_empty_string(self):
        letters = ''
        result = f_1002(letters)
        # Check if the result is an empty dictionary
        self.assertEqual(result, {})

    def test_with_repeating_characters(self):
        letters = 'aaabbb'
        result = f_1002(letters)
        # Check if repeated characters are treated as unique keys
        self.assertTrue(len(result) <= len(set(letters)))
        # Check if the result contains only the characters present in the input
        self.assertTrue(all(letter in letters for letter in result))

    def test_with_english_alphabet(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        result_dict = f_1002(letters)
        self.assertEqual(len(result_dict), len(letters))
        for key in result_dict.keys():
            self.assertIn(key, letters)
            self.assertIsInstance(result_dict[key], list)

    def test_with_single_letter(self):
        letters = 'a'
        result_dict = f_1002(letters)
        self.assertEqual(len(result_dict), 1)
        self.assertIn('a', result_dict)
        self.assertIsInstance(result_dict['a'], list)

    def test_with_empty_string(self):
        letters = ''
        result_dict = f_1002(letters)
        self.assertEqual(len(result_dict), 0)

    def test_with_non_english_letters(self):
        letters = 'äöüß'
        result_dict = f_1002(letters)
        self.assertEqual(len(result_dict), len(letters))
        for key in result_dict.keys():
            self.assertIn(key, letters)
            self.assertIsInstance(result_dict[key], list)

    def test_with_duplicate_letters(self):
        letters = 'aaabbb'
        result_dict = f_1002(letters)
        # Expecting the function to handle duplicates by only using unique letters
        self.assertTrue(len(result_dict) <= len(set(letters)))
        for key in result_dict.keys():
            self.assertIn(key, letters)
            self.assertIsInstance(result_dict[key], list)


if __name__ == "__main__":
    run_tests()
