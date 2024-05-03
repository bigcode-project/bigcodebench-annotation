import re
import string


def f_366(text1, text2):
    """
    This function takes two strings, removes any ASCII punctuation using regular expressions, 
    and returns the cleaned strings as a tuple. It targets punctuation characters defined in 
    `string.punctuation`, which includes the following characters:
    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    Note: This function may not remove non-ASCII or uncommon punctuation symbols.

    Parameters:
    text1, text2 (str): The original texts containing punctuation.

    Returns:
    tuple: A tuple containing the cleaned texts (text1, text2) with punctuation removed.

    Requirements:
    - re
    - string

    Example:
    >>> cleaned_text1, cleaned_text2 = f_366("Hello, world!", "How's it going?")
    >>> print(cleaned_text1, cleaned_text2)
    Hello world Hows it going

    >>> cleaned_text1, cleaned_text2 = f_366("test (with parenthesis []!!)", "And, other; stuff ^_`")
    >>> print(cleaned_text1, cleaned_text2)
    test with parenthesis  And other stuff 
    """
    # Constants
    PUNCTUATION = string.punctuation

    cleaned_texts = []

    # Remove punctuation from each text string
    for text in [text1, text2]:
        cleaned_text = re.sub('['+re.escape(PUNCTUATION)+']', '', text)
        cleaned_texts.append(cleaned_text)

    return tuple(cleaned_texts)

import unittest
class TestCases(unittest.TestCase):
    def test_with_common_punctuation(self):
        input_text1 = "Hello, world!"
        input_text2 = "How's it going?"
        expected_output = ("Hello world", "Hows it going")
        self.assertEqual(f_366(input_text1, input_text2), expected_output)
    def test_with_uncommon_punctuation(self):
        input_text1 = "Weird«text»with‰symbols"
        input_text2 = "More»symbols«here†too"
        expected_output = (input_text1, input_text2)  # Unchanged since uncommon punctuations are not removed
        self.assertEqual(f_366(input_text1, input_text2), expected_output)
    def test_with_numeric_characters(self):
        input_text1 = "Text with numbers 12345"
        input_text2 = "67890, numbers continue."
        expected_output = ("Text with numbers 12345", "67890 numbers continue")
        self.assertEqual(f_366(input_text1, input_text2), expected_output)
    def test_empty_strings(self):
        input_text1 = ""
        input_text2 = ""
        expected_output = ("", "")
        self.assertEqual(f_366(input_text1, input_text2), expected_output)
    def test_no_punctuation(self):
        input_text1 = "Just a normal sentence"
        input_text2 = "Another normal sentence"
        expected_output = ("Just a normal sentence", "Another normal sentence")
        self.assertEqual(f_366(input_text1, input_text2), expected_output)
    def test_all_symbols(self):
        input_text1 = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'"'''
        input_text2 = "test"
        expected_output = ("", "test")
        self.assertEqual(f_366(input_text1, input_text2), expected_output)
