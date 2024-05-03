from random import randint
import math


def f_1005(letters):
    """
    Generates a dictionary mapping each given letter to a list of random integers.
    It then calculates the standard deviation of the integers in each list and returns a new dictionary
    with these standard deviations associated with each letter.

    Parameters:
    letters (list of str): A list of letters for which to generate random integer lists and calculate standard deviations.

    Returns:
    dict: A dictionary where each key is a letter from the input list and each value is the standard deviation
          of a list of random integers associated with that letter.

    Requirements:
    - The 'random' module for generating random integers.
    - The 'math' module for calculating the square root.

    Example:
    >>> letters = ['a', 'b', 'c', 'd', 'e']
    >>> f_1005(letters)
    {'a': 15.892136420255145,
     'b': 26.661138882849926,
     'c': 0.0,
     'd': 2.5,
     'e': 18.587630295441105}

    >>> letters = ['#']
    >>> f_1005(letters)
    {'#': 14.5}
    """
    # Generate a dictionary with input letters as keys and lists of random integers as values
    random_dict = {letter: [randint(0, 100) for _ in range(randint(1, 10))] for letter in letters}

    # Calculate the standard deviation for each list in the dictionary
    sd_dict = {}
    for letter, values in random_dict.items():
        mean = sum(values) / len(values)  # Calculate the mean of the list
        variance = sum((x - mean) ** 2 for x in values) / len(values)  # Calculate the variance
        standard_deviation = math.sqrt(variance)  # Calculate the standard deviation
        sd_dict[letter] = standard_deviation  # Store it in the new dictionary

    return sd_dict


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_empty_list_of_letters(self):
        letters = []
        result = f_1005(letters)
        # Expecting an empty dictionary since no letters were provided
        self.assertEqual(result, {}, "The result should be an empty dictionary for an empty list of letters.")

    def test_single_letter_list(self):
        letters = ['a']
        result = f_1005(letters)
        # Checking that the result is a dictionary with a single key and its value is a float (standard deviation)
        self.assertIsInstance(result, dict, "The result should be a dictionary.")
        self.assertTrue(len(result) == 1, "The result dictionary should contain a single element.")
        self.assertIn('a', result, "The letter 'a' should be a key in the result dictionary.")
        self.assertIsInstance(result['a'], float,
                              "The value for the letter should be a float representing the standard deviation.")

    def test_list_with_special_characters(self):
        letters = ['$', '#', '&']
        result = f_1005(letters)
        # Ensuring each special character has a corresponding float standard deviation
        for letter in letters:
            self.assertIn(letter, result)
            self.assertIsInstance(result[letter], float)

    def test_repeated_letters(self):
        letters = ['a', 'a', 'b', 'b']
        result = f_1005(letters)
        # Expecting results only for unique letters
        self.assertTrue(len(result) == 2 and all(letter in result for letter in set(letters)))

    def test_case_sensitivity(self):
        letters = ['a', 'A']
        result = f_1005(letters)
        # Expecting different entries for 'a' and 'A' if case sensitivity is preserved
        self.assertTrue('a' in result and 'A' in result,
                        "Both lowercase and uppercase letters should be treated as distinct keys.")


if __name__ == "__main__":
    run_tests()
