import base64
import re
from html import unescape
import textwrap

def f_8(raw_string, line_length):
    """
    Decode a raw string from base64, decouple HTML entities, replace multiple spaces with a single space, strip leading and subsequent spaces, and wrap text to a certain line length.

    Parameters:
    - raw_string (str): The base64 encoded string.
    - line_length (int): The maximum length of a line.

    Returns:
    - wrapped_text (str): The cleaned and formatted string.

    Requirements:
    - base64
    - re
    - html
    - textwrap

    Example:
    >>> f_8('SGVsbG8sICBXb3JsZCEgICAg', 5)
    'Hello\\n, Wor\\nld!'
    """
    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    unescaped_string = unescape(decoded_string)
    cleaned_string = re.sub(' +', ' ', unescaped_string).strip()
    wrapped_text = textwrap.fill(cleaned_string, line_length)
    return wrapped_text

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(f_8('SGVsbG8sICBXb3JsZCEgICAg', 5), 'Hello\n, Wor\nld!')
    def test_case_2(self):
        self.assertEqual(f_8('SGVsbG8sICBXb3JsZCEgICAg', 10), 'Hello,\nWorld!')
    def test_case_3(self):
        self.assertEqual(f_8('SGVsbG8sICBXb3JsZCEgICAg', 20), 'Hello, World!')
    def test_case_4(self):
        self.assertEqual(f_8('SGVsbG8sICBXb3JsZCEgICAg', 1), 'H\ne\nl\nl\no\n,\nW\no\nr\nl\nd\n!')
    def test_case_5(self):
        self.assertEqual(f_8('SGVsbG8sICBXb3JsZCEgICAg', 2), 'He\nll\no,\nWo\nrl\nd!')
