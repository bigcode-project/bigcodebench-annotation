import string
import matplotlib.pyplot as plt


def f_625(s):
    """
    Calculate the frequency of each letter in a string and return a bar chart of frequencies.
    Results are case-insensitive. If non-string input is provided, function will throw an error.

    Parameters:
    s (str): The string to calculate letter frequencies.

    Returns:
    tuple: A tuple containing:
        - dict: A dictionary with the frequency of each letter.
        - Axes: The bar subplot of 'Letter Frequencies' with 'Letters' on the x-axis and 'Frequency'
                on the y-axis.

    Requirements:
    - string
    - matplotlib.pyplot

    Example:
    >>> s = 'This is a test string.'
    >>> freqs, ax = f_625(s)
    >>> freqs
    {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 1, 'h': 1, 'i': 3, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 0, 'p': 0, 'q': 0, 'r': 1, 's': 4, 't': 4, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    if not isinstance(s, str):
        raise TypeError("Expected string input")
    LETTERS = string.ascii_lowercase
    s = s.lower()
    letter_counts = {letter: s.count(letter) for letter in LETTERS}
    fig, ax = plt.subplots()
    ax.bar(letter_counts.keys(), letter_counts.values())
    ax.set_xlabel("Letters")
    ax.set_ylabel("Frequency")
    ax.set_title("Letter Frequencies")
    return letter_counts, ax

import unittest
import string
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a simple sentence
        s = "This is a test string."
        expected_output = {
            letter: s.lower().count(letter) for letter in string.ascii_lowercase
        }
        result, ax = f_625(s)
        self.assertEqual(result, expected_output)
        self.assertEqual(ax.get_title(), "Letter Frequencies")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
    def test_case_2(self):
        # Test with a string having all alphabets
        s = "abcdefghijklmnopqrstuvwxyz"
        expected_output = {letter: 1 for letter in string.ascii_lowercase}
        result, ax = f_625(s)
        self.assertEqual(result, expected_output)
        self.assertEqual(ax.get_title(), "Letter Frequencies")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
    def test_case_3(self):
        # Test with a string having no alphabets
        s = "1234567890!@#$%^&*()"
        expected_output = {letter: 0 for letter in string.ascii_lowercase}
        result, ax = f_625(s)
        self.assertEqual(result, expected_output)
        self.assertEqual(ax.get_title(), "Letter Frequencies")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
    def test_case_4(self):
        # Test with an empty string
        s = ""
        expected_output = {letter: 0 for letter in string.ascii_lowercase}
        result, ax = f_625(s)
        self.assertEqual(result, expected_output)
        self.assertEqual(ax.get_title(), "Letter Frequencies")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
    def test_case_5(self):
        # Test error handling
        for invalid in [123, []]:
            with self.assertRaises(Exception):
                f_625(invalid)
    def tearDown(self):
        plt.close("all")
