import textwrap
import re

def f_103(input_string, width):
    """
    Divide a multi-line string into separate strings and wrap each line to a certain width.
    
    Parameters:
    - input_string (str): The multi-line string that needs to be wrapped.
    - width (int): The width to wrap each line to.
    
    Returns:
    - str: The wrapped string where each line is wrapped to the specified width.
    
    Requirements:
    - textwrap
    - re
    
    Example:
    >>> f_103('Another line\\nWith wrapping', 8)
    'Another\\nline\\nWith\\nwrapping'
    """
    lines = input_string.split('\\n')
    wrapped_lines = [textwrap.fill(line, width, break_long_words=False) for line in lines]
    wrapped_string = '\\n'.join(wrapped_lines)
    wrapped_string = re.sub(r'\bis\b', 'was', wrapped_string)
    return wrapped_string

import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        input_str = "Hello world\nThis is a test string\nHappy coding!"
        width = 10
        expected_output = "Hello\nworld This\nwas a test\nstring\nHappy\ncoding!"
        self.assertEqual(f_103(input_str, width), expected_output)
        
        
    def test_case_2(self):
        # Test with single line and specific width
        input_str = "Hello world"
        width = 5
        expected_output = "Hello\nworld"
        self.assertEqual(f_103(input_str, width), expected_output)
    
    def test_case_3(self):
        # Test with empty string and specific width
        input_str = ""
        width = 10
        expected_output = ""
        self.assertEqual(f_103(input_str, width), expected_output)
    
    def test_case_4(self):
        input_str = "Hello world This is a test string Happy coding!"
        width = 1000
        expected_output = "Hello world This was a test string Happy coding!"  # Very wide width, should not wrap
        self.assertEqual(f_103(input_str, width), expected_output)
    
    def test_case_5(self):
        # Test with special characters and specific width
        input_str = "Hello, @world!\n#This$is^a&test*string"
        width = 10
        expected_output = "Hello,\n@world!\n#This$was^a&test*string"
        self.assertEqual(f_103(input_str, width), expected_output)
