import requests
from bs4 import BeautifulSoup

def f_1030(url, tag):
    """
    Scrape a web page for the first occurrence of a specified HTML tag and return its text content.

    Parameters:
    url (str): The URL of the website to scrape.
    tag (str): The HTML tag to find and retrieve text from.

    Returns:
    str: The text content of the specified HTML tag if found, otherwise returns None.

    Requirements:
    - requests
    - bs4.BeautifulSoup

    Example:
    >>> f_1030("https://www.google.com/", "title")
    'Google'
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag_content = soup.find(tag)
    
    return tag_content.string if tag_content else None

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_1030("file:///mnt/data/test_page_1.html", "title")
        self.assertEqual(result, "Test Page 1")

    def test_case_2(self):
        result = f_1030("file:///mnt/data/test_page_1.html", "h2")
        self.assertEqual(result, "The attribute 'h2' was not found on the provided website.")

    def test_case_3(self):
        result = f_1030("file:///mnt/data/test_page_2.html", "title")
        self.assertEqual(result, "Test Page 2")

    def test_case_4(self):
        result = f_1030("file:///mnt/data/test_page_2.html", "h2")
        self.assertEqual(result, "The attribute 'h2' was not found on the provided website.")

    def test_case_5(self):
        with self.assertRaises(requests.exceptions.RequestException):
            f_1030("invalid_url", "title")
if __name__ == "__main__":
    run_tests()