import requests
from bs4 import BeautifulSoup

def task_func(url, tag):
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
    >>> task_func("https://www.google.com/", "title")
    'Google'
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag_content = soup.find(tag)
    return tag_content.string if tag_content else None

import unittest
from unittest.mock import patch, Mock
import requests
from bs4 import BeautifulSoup
import os
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_title_tag_found(self, mock_get):
        """Test retrieving the title tag."""
        html_content = "<html><head><title>Test Page</title></head><body></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "title")
        self.assertEqual(result, "Test Page")
    @patch('requests.get')
    def test_h1_tag_found(self, mock_get):
        """Test retrieving the h1 tag."""
        html_content = "<html><body><h1>This is a test page</h1></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "h1")
        self.assertEqual(result, "This is a test page")
    @patch('requests.get')
    def test_nonexistent_tag(self, mock_get):
        """Test for a tag that doesn't exist."""
        html_content = "<html><body><h1>Existing Tag</h1></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "h2")
        self.assertIsNone(result)
    def test_invalid_url_handling(self):
        """Test how the function handles an invalid URL."""
        with self.assertRaises(requests.exceptions.RequestException):
            task_func("invalid_url", "title")
    @patch('requests.get')
    def test_malformed_html(self, mock_get):
        """Test the function with a malformed HTML input."""
        html_content = "<html><head><title>Test Page</title><head><body><h1>This is a test page<h1></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "title")
        self.assertEqual(result, "Test Page")
        result = task_func("http://test.com", "h1")
        self.assertIsNone(result)
    @patch('requests.get')
    def test_multiple_matching_tags(self, mock_get):
        """Test the function with multiple tags of the same type."""
        html_content = "<html><body><p>First Paragraph</p><p>Second Paragraph</p></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "p")
        self.assertEqual(result, "First Paragraph")
    @patch('requests.get')
    def test_empty_tag(self, mock_get):
        """Test the function with an empty tag content."""
        html_content = "<html><body><div></div><h1>Not empty</h1></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "div")
        self.assertIsNone(result)
        result = task_func("http://test.com", "h1")
        self.assertEqual(result, "Not empty")
