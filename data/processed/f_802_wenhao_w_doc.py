import string
import random


def f_446(text, seed=None):
    """
    Transforms the input text by replacing each alphabetic character with a random letter,
    while preserving the case and non-alphabetic characters of the original text.

    Parameters:
    - text (str): The input text to be transformed.
    - seed (int, optional): Random seed for reproducibility. Defaults to None (not set).

    Returns:
    - str: A transformed string with random letters replacing the alphabetic characters of the input text,
      preserving non-alphabetic characters and the original case.

    Requirements:
    - string
    - random

    Notes:
    - Alphabet replacements are chosen from ascii characters of the same case as the original.

    Example:
    >>> text = 'Hello, world!'
    >>> f_446(text, 0)
    'Mynbi, qpmzj!'
    """

    def replace_with_random_char(c):
        if c.isalpha():
            if c.islower():
                return random.choice(string.ascii_lowercase)
            else:
                return random.choice(string.ascii_uppercase)
        return c

    if seed is not None:
        random.seed(seed)
    return "".join(replace_with_random_char(c) for c in text)

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test single word
        input_text = "Hello"
        output_text = f_446(input_text, seed=1)
        self.assertTrue(
            all(oc.isalpha() == ic.isalpha() for oc, ic in zip(output_text, input_text))
        )
        self.assertEqual(len(output_text), len(input_text))
    def test_case_2(self):
        # Test multiple words and punctuation
        input_text = "Hello, World!"
        output_text = f_446(input_text, seed=2)
        self.assertTrue(
            all(oc.isalpha() == ic.isalpha() for oc, ic in zip(output_text, input_text))
        )
        self.assertEqual(len(output_text), len(input_text))
    def test_case_3(self):
        # Test empty string
        input_text = ""
        output_text = f_446(input_text, seed=3)
        self.assertEqual(output_text, "")
    def test_case_4(self):
        # Test case preservation
        input_text = "HeLlO"
        output_text = f_446(input_text, seed=4)
        self.assertTrue(
            all(
                oc.isupper() == ic.isupper() and oc.islower() == ic.islower()
                for oc, ic in zip(output_text, input_text)
            )
        )
    def test_case_5(self):
        # Test numbers, special characters
        input_text = "1234!@#$"
        output_text = f_446(input_text, seed=5)
        self.assertEqual(
            output_text, input_text
        )  # Numbers and special characters should remain unchanged
    def test_case_6(self):
        # Test random seed reproducibility
        input_text = "Colorless green ideas sleep furiously."
        output1 = f_446(input_text, seed=123)
        output2 = f_446(input_text, seed=123)
        self.assertEqual(output1, output2)
