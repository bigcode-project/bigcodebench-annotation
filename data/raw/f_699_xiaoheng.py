import textwrap

def f_699(input_string, width):
    """
    Divide a multi-line string into separate strings and wrap each line to a certain width.
    
    Parameters:
    - input_string (str): The multi-line string that needs to be wrapped.
    - width (int): The width to wrap each line to.
    
    Returns:
    - str: The wrapped string where each line is wrapped to the specified width.
    
    Requirements:
    - textwrap
    
    Example:
    >>> f_699('Hello world\\nThis is an example', 10)
    'Hello\\nworld This\\nis an\\nexample'
    >>> f_699('Another line\\nWith wrapping', 8)
    'Another\\nline\\nWith\\nwrapping'
    """
    lines = input_string.split('\\n')
    wrapped_lines = [textwrap.fill(line, width, break_long_words=False) for line in lines]
    return '\\n'.join(wrapped_lines)

import unittest
import textwrap

# Import the function for testing
import textwrap


class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test with multiple lines and specific width
        input_str = "Hello world\nThis is a test string\nHappy coding!"
        width = 10
        expected_output = "Hello\nworld\nThis is a\ntest\nstring\nHappy\ncoding!"
        self.assertEqual(f_699(input_str, width), expected_output)
        
    def test_case_2(self):
        # Test with single line and specific width
        input_str = "Hello world"
        width = 5
        expected_output = "Hello\nworld"
        self.assertEqual(f_699(input_str, width), expected_output)
    
    def test_case_3(self):
        # Test with empty string and specific width
        input_str = ""
        width = 10
        expected_output = ""
        self.assertEqual(f_699(input_str, width), expected_output)
    
    def test_case_4(self):
        # Test with multiple lines and extremely large width
        input_str = "Hello world\nThis is a test string\nHappy coding!"
        width = 1000
        expected_output = input_str  # Should remain unchanged
        self.assertEqual(f_699(input_str, width), expected_output)
    
    def test_case_5(self):
        # Test with special characters and specific width
        input_str = "Hello, @world!\n#This$is^a&test*string"
        width = 10
        expected_output = "Hello,\n@world!\n#This$is^a&test*string"
        self.assertEqual(f_699(input_str, width), expected_output)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()