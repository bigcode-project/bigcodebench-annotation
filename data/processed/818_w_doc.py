import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    """
    Divide a string into words, remove punctuation marks and convert them to lowercase letters.

    Parameters:
    - text (str): The input string.

    Returns:
    - cleaned_words (list): A list of cleaned words.

    Requirements:
    - re
    - string

    Example:
    >>> task_func("Hello, world! This is a test.")
    ['hello', 'world', 'this', 'is', 'a', 'test']
    """
    words = re.split(r'\s+', text)
    cleaned_words = [re.sub(f'[{PUNCTUATION}]', '', word).lower() for word in words]
    return cleaned_words

import unittest
class TestCases(unittest.TestCase):
    def test_standard_input(self):
        """Test with standard input containing words, punctuation, and whitespaces"""
        input_text = "Hello, world! This is a test."
        expected_output = ['hello', 'world', 'this', 'is', 'a', 'test']
        self.assertEqual(task_func(input_text), expected_output)
    def test_empty_string(self):
        """Test with an empty string"""
        input_text = ""
        expected_output = ['']
        self.assertEqual(task_func(input_text), expected_output)
    def test_string_with_no_punctuation(self):
        """Test with a string that has no punctuation marks"""
        input_text = "Python is great"
        expected_output = ['python', 'is', 'great']
        self.assertEqual(task_func(input_text), expected_output)
    def test_string_with_numbers(self):
        """Test with a string that includes numbers and punctuation"""
        input_text = "1234! Test with numbers."
        expected_output = ['1234', 'test', 'with', 'numbers']
        self.assertEqual(task_func(input_text), expected_output)
    def test_string_with_special_characters(self):
        """Test with a string that includes special characters"""
        input_text = "Special chars @#$%^&*()"
        expected_output = ['special', 'chars', '']
        self.assertEqual(task_func(input_text), expected_output)
    def test_string_with_whitespaces(self):
        """Test with a string that includes extra whitespaces between words"""
        input_text = "   Extra   whitespaces   "
        expected_output = ['', 'extra', 'whitespaces', '']
        self.assertEqual(task_func(input_text), expected_output)
