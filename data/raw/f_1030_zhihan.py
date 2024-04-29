import requests
from bs4 import BeautifulSoup

def f_1030(url, attribute):
    """
    Scrape a web page for a specified HTML attribute and return its value.

    Parameters:
    url (str): The URL of the website to scrape.
    attribute (str): The HTML attribute to scrape for.

    Returns:
    str: The value of the specified HTML attribute if found, otherwise returns a message indicating the attribute was not found.

    Requirements:
    - requests
    - bs4

    Example:
    >>> f_1030("https://www.google.com/", "title")
    'Google'
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    attribute_value = soup.find(attribute)
    
    return attribute_value.string if attribute_value else f"The attribute '{attribute}' was not found on the provided website."

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