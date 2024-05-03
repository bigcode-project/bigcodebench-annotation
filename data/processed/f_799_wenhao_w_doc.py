import re
import string
import random


def f_630(text: str, seed=None) -> str:
    """
    Transforms a given string by removing special characters, normalizing whitespace,
    and randomizing character casing.

    Parameters:
    - text (str): The text string to be preprocessed.
    - seed (int, optional): Random seed for reproducibility. Defaults to None (not set).

    Returns:
    - str: The preprocessed text string.

    Requirements:
    - re
    - string
    - random

    Note:
    - This function considers special characters to be string punctuations.
    - Spaces, tabs, and newlines are replaced with with '_', '__', and '___' respectively.
    - To randomize casing, this function converts characters to uppercase with a 50% probability.

    Example:
    >>> f_630('Hello   World!', 0)
    'HeLlo___WORlD'
    >>> f_630('attention is all you need', 42)
    'ATtENTIOn_IS_ALL_You_Need'
    """

    if seed is not None:
        random.seed(seed)

    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)

    REPLACEMENTS = {" ": "_", "\t": "__", "\n": "___"}
    for k, v in REPLACEMENTS.items():
        text = text.replace(k, v)

    text = "".join(random.choice([k.upper(), k]) for k in text)

    return text

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_630("Hello   World!", seed=1)
        self.assertNotIn(" ", result, "Spaces should be replaced.")
        self.assertNotIn("!", result, "Special characters should be removed.")
        self.assertEqual(
            len(result), len("Hello___World"), "Length should match processed input."
        )
    def test_case_2(self):
        result = f_630("Python!", seed=2)
        self.assertNotIn("!", result, "Special characters should be removed.")
        self.assertEqual(
            len(result), len("Python"), "Length should match processed input."
        )
    def test_case_3(self):
        result = f_630("  ", seed=3)
        self.assertEqual(result, "__", "Spaces should be replaced with underscores.")
    def test_case_4(self):
        result = f_630("\t\n", seed=4)
        self.assertEqual(
            result, "_____", "Tab and newline should be replaced with underscores."
        )
    def test_case_5(self):
        result = f_630("a!b@c#", seed=5)
        self.assertTrue(result.isalpha(), "Output should only contain alphabets.")
        self.assertEqual(
            len(result), len("abc"), "Length should match processed input."
        )
    def test_case_6(self):
        # Test with all types of whitespace characters
        result = f_630("a b\tc\nd", seed=6)
        self.assertEqual(
            result.lower(),
            "a_b__c___d",
            "Should replace all types of whitespaces correctly.",
        )
    def test_case_7(self):
        # Test with a mix of alphanumeric and special characters
        result = f_630("a1! b2@ c3#", seed=7)
        self.assertTrue(
            all(char.isalnum() or char == "_" for char in result),
            "Should only contain alphanumeric characters and underscores.",
        )
    def test_case_8(self):
        # Test with an empty string
        result = f_630("", seed=8)
        self.assertEqual(result, "", "Should handle empty string correctly.")
    def test_case_9(self):
        # Test with a string that contains no special characters or whitespaces
        result = f_630("abcdefg", seed=9)
        self.assertTrue(result.isalpha(), "Should contain only letters.")
        self.assertEqual(len(result), 7, "Length should match the input.")
    def test_case_10(self):
        # Test with a long string of repeated characters
        result = f_630("a" * 50, seed=10)
        self.assertTrue(
            all(char.lower() == "a" for char in result),
            "All characters should be 'a' or 'A'.",
        )
        self.assertEqual(len(result), 50, "Length should match the input.")
    def test_case_11(self):
        # Test with only special characters
        result = f_630("!@#$%^&*", seed=11)
        self.assertEqual(
            result, "", "Should return an empty string for only special characters."
        )
    def test_case_12(self):
        # Test with numeric characters
        result = f_630("12345", seed=13)
        self.assertTrue(result.isdigit(), "Should contain only digits.")
        self.assertEqual(len(result), 5, "Length should match the input.")
    def test_case_13(self):
        # Test with a string containing only whitespace characters
        result = f_630(" \t\n", seed=14)
        self.assertEqual(
            result,
            "______",
            "Should replace all types of whitespaces correctly, with two underscores for tab and three for newline.",
        )
    def test_case_14(self):
        # Test the randomness of uppercase conversion with a long string
        result = f_630("a" * 100, seed=15)
        self.assertTrue(
            all(char.lower() == "a" for char in result),
            "All characters should be 'a' or 'A'.",
        )
        self.assertNotEqual(
            result, "a" * 100, "Should have some uppercase transformations."
        )
        self.assertNotEqual(
            result, "A" * 100, "Should have some lowercase transformations."
        )
    def test_case_15(self):
        # Test random seed impact
        result1 = f_630("test seed impact", seed=42)
        result2 = f_630("test seed impact", seed=42)
        self.assertEqual(
            result1, result2, "Results with the same seed should be identical."
        )
