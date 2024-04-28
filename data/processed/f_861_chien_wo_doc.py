from bs4 import BeautifulSoup
import requests

# Constants
URL = "http://example.com"


def f_340(url=URL, from_encoding="cp1251", use_lxml=False):
    """
    Fetches a web page from a given URL, decodes its content from a specified encoding,
    and returns the parsed HTML using BeautifulSoup. If specified, 'lxml' is used as
    the parser for improved performance. In case of any failure (like network issues,
    invalid URL, or decoding errors), the function returns None.

    Parameters:
    - url (str): The URL of the webpage to fetch. Defaults to the constant URL.
    - from_encoding (str): The original encoding of the webpage content. Defaults to 'cp1251'.
    - use_lxml (bool): Flag to use 'lxml' as the parser for BeautifulSoup. If False, the default 'html.parser' is used. Defaults to False.

    Returns:
    - BeautifulSoup object if the fetch and parse are successful.
    - None if the URL is invalid, the request fails, or parsing fails.

    Requirements:
    - bs4
    - requests

    Example:
    >>> html = f_340('http://example.com', 'cp1251', True)
    >>> print(html.prettify()) if html else print("Error fetching or parsing the webpage.")

    Notes:
    - The function returns None if the URL is empty or None.
    - Network errors, HTTP errors, and decoding issues are caught and result in None being returned.
    - If the HTTP response status code is 200 (indicating success), the content is decoded using the specified encoding
    - If the response status code is not 200, it implies an unsuccessful HTTP request (e.g., 404 Not Found, 403 Forbidden).
      In such cases, the function returns None, indicating that the webpage could not be successfully retrieved or was not available.
      
    """
    if not url:
        return None
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        if response.status_code == 200:
            decoded_content = response.content.decode(from_encoding)
            parser = "lxml" if use_lxml else "html.parser"
            soup = BeautifulSoup(decoded_content, parser)
            return soup
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

from bs4 import BeautifulSoup
import unittest
from unittest.mock import patch, MagicMock
class TestCases(unittest.TestCase):
    """Test cases for f_340."""
    @patch("requests.get")
    def test_successful_fetch_and_parse_html_parser(self, mock_get):
        """Test if the function correctly fetches and parses a webpage with valid encoding using html.parser."""
        mock_get.return_value = MagicMock(
            status_code=200, content=b"Valid HTML content"
        )
        result = f_340("http://example.com", "utf8")
        self.assertIsInstance(result, BeautifulSoup)
    @patch("requests.get")
    def test_successful_fetch_and_parse_lxml_parser(self, mock_get):
        """Test if the function correctly fetches and parses a webpage with valid encoding using lxml."""
        mock_get.return_value = MagicMock(
            status_code=200, content=b"Valid HTML content"
        )
        result = f_340("http://example.com", "utf8", use_lxml=True)
        self.assertIsInstance(result, BeautifulSoup)
    @patch("requests.get")
    def test_connection_error_handling(self, mock_get):
        """Test how the function handles connection errors."""
        mock_get.side_effect = requests.exceptions.ConnectionError()
        result = f_340("http://example.com", "utf8")
        self.assertIsNone(result)
    @patch("requests.get")
    def test_incorrect_encoding_handling(self, mock_get):
        """Test how the function handles incorrect or unsupported encodings."""
        mock_get.return_value = MagicMock(
            status_code=200, content=b"Valid HTML content"
        )
        result = f_340("http://example.com", "invalid_encoding")
        self.assertIsNone(result)
    @patch("requests.get")
    def test_status_code_handling(self, mock_get):
        """Test if the function handles non-200 status code responses correctly."""
        mock_get.return_value = MagicMock(status_code=404)
        result = f_340("http://example.com", "utf8")
        self.assertIsNone(result)
    @patch("requests.get")
    def test_empty_url_handling(self, mock_get):
        """Test how the function handles an empty URL."""
        result = f_340("", "utf8")
        self.assertIsNone(result)
