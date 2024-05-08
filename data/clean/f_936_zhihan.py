import ast
import requests
from bs4 import BeautifulSoup


def f_936(url):
    """
    Fetches the content of a webpage specified by its URL, parses it to find <script> tags,
    and attempts to evaluate any string within these tags as a Python dictionary.

    Parameters:
    - url (str): The URL of the webpage to scrape.

    Returns:
    - list of dict: A list containing dictionaries that were successfully evaluated from string representations
      found within <script> tags on the webpage. 
    
    Note:
    - If an error occurs during the request or if no dictionaries are found/evaluable, an empty list is returned.

    Requirements:
    - ast
    - requests
    - bs4.BeautifulSoup

    Example:
    >>> f_936('https://example.com')
    [{'key': 'value'}, ...]
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return []
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for script in soup.find_all('script'):
        try:
            results.append(ast.literal_eval(script.string))
        except (ValueError, SyntaxError):
            continue

    return results


import unittest
from unittest.mock import patch, Mock


def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

        def raise_for_status(self):
            if self.status_code != 200:
                raise requests.RequestException("Mocked error")

    if args[0] == 'https://test1.com':
        return MockResponse('<script>{"key": "value"}</script>', 200)
    elif args[0] == 'https://test2.com':
        return MockResponse('<script>{"key1": "value1"}</script><script>{"key2": "value2"}</script>', 200)
    elif args[0] == 'https://test3.com':
        return MockResponse('<div>No script tags here</div>', 200)
    elif args[0] == 'https://test4.com':
        return MockResponse('<script>Not a dictionary</script>', 200)
    elif args[0] == 'https://error.com':
        return MockResponse('Error', 404)

    return MockResponse('', 404)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, mock_get):
        # Test with a single dictionary in the script tag
        result = f_936('https://test1.com')
        self.assertEqual(result, [{"key": "value"}])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self, mock_get):
        # Test with multiple dictionaries in separate script tags
        result = f_936('https://test2.com')
        self.assertEqual(result, [{"key1": "value1"}, {"key2": "value2"}])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, mock_get):
        # Test with no script tags
        result = f_936('https://test3.com')
        self.assertEqual(result, [])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_4(self, mock_get):
        # Test with a script tag that doesn't contain a dictionary
        result = f_936('https://test4.com')
        self.assertEqual(result, [])

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_5(self, mock_get):
        # Test with a URL that returns an error
        result = f_936('https://error.com')
        self.assertEqual(result, [])


if __name__ == "__main__":
    run_tests()
