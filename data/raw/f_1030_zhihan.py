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
import os
import requests
from bs4 import BeautifulSoup

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a dummy HTML file
        self.filename = "test_page.html"
        self.filepath = os.path.join("/tmp", self.filename)
        with open(self.filepath, "w") as file:
            file.write("<html><head><title>Test Page</title></head>"
                       "<body><h1>This is a test page</h1><p>Sample paragraph.</p></body></html>")
        self.url = "file://" + self.filepath

    def tearDown(self):
        # Remove the dummy HTML file after the test is done
        os.remove(self.filepath)

    def test_title_tag_found(self):
        # Test retrieving the title tag
        result = f_1030(self.url, "title")
        self.assertEqual(result, "Test Page")

    def test_h1_tag_found(self):
        # Test retrieving the h1 tag
        result = f_1030(self.url, "h1")
        self.assertEqual(result, "This is a test page")

    def test_nonexistent_tag(self):
        # Test for a tag that doesn't exist
        result = f_1030(self.url, "h2")
        self.assertIsNone(result)

    def test_invalid_url_handling(self):
        # Test how the function handles an invalid URL
        with self.assertRaises(requests.exceptions.RequestException):
            f_1030("invalid_url", "title")

if __name__ == "__main__":
    run_tests()