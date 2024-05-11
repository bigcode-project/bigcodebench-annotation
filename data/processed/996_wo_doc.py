import requests
import json
from bs4 import BeautifulSoup


def task_func(url: str, file_name: str = "Output.txt") -> str:
    """
    Scrape the 'title' from a specified web page, save it in JSON format to a given file, 
    and append to the file if it exists.`

    Parameters:
    - url (str): The URL of the web page from which the title is to be scraped.
    - file_name (str, optional): The name of the file to save the scraped title. 
    If the file already exists, the new data is appended. Defaults to 'Output.txt'.

    Returns:
    - str: The file path where the scraped title is saved.

    Requirements:
    - requests
    - json
    - bs4

    Notes:
    - If the web page does not have a title, 'None' is saved as the title value in the JSON data.
    - Data is appended to the specified file in JSON format, with each title on a new line.

    Example:
    >>> task_func("http://example.com")
    'Output.txt'
    >>> task_func("http://another-example.com", "AnotherOutput.txt")
    'AnotherOutput.txt'
    """
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else None
    data = {"title": title}
    json_data = json.dumps(data)
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(json_data + "\n")
    return file_name

import unittest
from unittest.mock import patch, mock_open
import requests
import json
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_scrape_title_page_1(self, mock_file):
        """Test that the title is scraped from a web page and saved to a file"""
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"<title>Test Page 1</title>"
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com")
            self.assertEqual(file_path, "Output.txt")
            mock_file().write.assert_called_once_with(
                json.dumps({"title": "Test Page 1"}) + "\n"
            )
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_scrape_title_page_2(self, mock_file):
        """Test that the title is scraped from a web page and saved to a file"""
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"<title>Test Page 2</title>"
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com", "AnotherOutput.txt")
            self.assertEqual(file_path, "AnotherOutput.txt")
            mock_file().write.assert_called_once_with(
                json.dumps({"title": "Test Page 2"}) + "\n"
            )
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_invalid_url(self, mock_file):
        """Test that an exception is raised when the URL is invalid"""
        with self.assertRaises(requests.RequestException):
            task_func("http://invalid-url")
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_page_without_title(self, mock_file):
        """Test that 'None' is saved as the title when the web page does not have a title"""
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"<html><head></head><body></body></html>"
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com")
            self.assertEqual(file_path, "Output.txt")
            mock_file().write.assert_called_once_with(
                json.dumps({"title": None}) + "\n"
            )
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_very_long_title(self, mock_file):
        """Test that a very long title is saved correctly"""
        long_title = "A" * 1024  # A very long title of 1024 characters
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = f"<title>{long_title}</title>".encode()
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com")
            self.assertEqual(file_path, "Output.txt")
            mock_file().write.assert_called_once_with(
                json.dumps({"title": long_title}) + "\n"
            )
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps({"title": "Existing Title"}) + "\n",
    )
    def test_append_to_existing_file(self, mock_file):
        """Test that data is appended to an existing file"""
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"<title>New Title</title>"
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com")
            self.assertEqual(file_path, "Output.txt")
            mock_file().write.assert_called_with(
                json.dumps({"title": "New Title"}) + "\n"
            )
