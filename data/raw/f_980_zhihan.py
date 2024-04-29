import re
import urllib.request
from bs4 import BeautifulSoup
import requests

# Constants
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

def f_980(myString):
    """
    Extract all URLs from a myString string, make a GET request to each URL, and return the title of each web page.
    
    Parameters:
    myString (str): The string to extract URLs from.
    
    Returns:
    dict: A dictionary with URLs as keys and webpage titles as values.

    Requirements:
    - re
    - urllib.request
    - bs4.BeautifulSoup
    - requests
    
    Example:
    >>> f_980("Check these links: http://www.google.com, https://www.python.org")
    {'http://www.google.com': 'Google', 'https://www.python.org': 'Welcome to Python.org'}
    """
    urls = re.findall('(https?://[^\\s]+)', myString)
    titles = {}

    for url in urls:
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': USER_AGENT
            }
        )

        with urllib.request.urlopen(req) as response:
            page_content = response.read()

        soup = BeautifulSoup(page_content, 'html.parser')
        titles[url] = soup.title.string

    return titles

import unittest

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with a string containing two valid URLs
        result = f_980("Check these links: http://www.google.com, https://www.python.org")
        self.assertTrue('http://www.google.com' in result)
        self.assertTrue('https://www.python.org' in result)

    def test_case_2(self):
        # Testing with a string containing no URLs
        result = f_980("No URLs in this string.")
        self.assertEqual(result, {})

    def test_case_3(self):
        # Testing with a string containing an invalid URL
        result = f_980("Check this invalid link: http://invalid.url")
        self.assertTrue('http://invalid.url' in result)

    def test_case_4(self):
        # Testing with a string containing multiple similar URLs
        result = f_980("Check these: http://www.example.com, http://www.example.com/path1, http://www.example.com/path2")
        self.assertTrue('http://www.example.com' in result)
        self.assertTrue('http://www.example.com/path1' in result)
        self.assertTrue('http://www.example.com/path2' in result)

    def test_case_5(self):
        # Testing with a string containing URLs with different protocols
        result = f_980("Links: http://protocol1.com, https://protocol2.com, ftp://protocol3.com")
        self.assertTrue('http://protocol1.com' in result)
        self.assertTrue('https://protocol2.com' in result)
        self.assertFalse('ftp://protocol3.com' in result)  # This protocol is not supported by the function

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()