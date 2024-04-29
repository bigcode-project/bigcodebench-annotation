import re
from gensim.summarization import summarize

def f_943(text):
    """
    Create a summary of a text after you have removed URLs.

    Parameters:
    text (str): The text to summarize.

    Returns:
    str: The summary of the text.

    Requirements:
    - re
    - gensim.summarization.summarize

    Example:
    >>> f_943('Visit https://www.python.org for more info. Python is great. I love Python.')
    'Python is great. I love Python.'
    """
    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)

    return summarize(text)

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a URL
        input_text = 'Visit https://www.python.org for more info. Python is great.'
        expected_output = 'Python is great.'
        self.assertEqual(f_943(input_text), expected_output)

    def test_case_2(self):
        # Test without a URL
        input_text = 'Python is an amazing programming language.'
        expected_output = 'Python is an amazing programming language.'
        self.assertEqual(f_943(input_text), expected_output)

    def test_case_3(self):
        # Test with long text
        input_text = "Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
        expected_output = 'Python is an interpreted, high-level and general-purpose programming language.'
        self.assertEqual(f_943(input_text), expected_output)

    def test_case_4(self):
        # Test with multiple URLs
        input_text = 'Check out https://www.python.org and https://www.djangoproject.com. Both are amazing.'
        expected_output = 'Both are amazing.'
        self.assertEqual(f_943(input_text), expected_output)

    def test_case_5(self):
        # Test with short text
        input_text = 'I love Python.'
        expected_output = 'I love Python.'
        self.assertEqual(f_943(input_text), expected_output)

if __name__ == '__main__':
    run_tests()
if __name__ == "__main__":
    run_tests()