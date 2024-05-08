import mechanize
from bs4 import BeautifulSoup


def f_200(url, form_id, data):
    """
    Submits a form on a given webpage using mechanize and extracts the title of the response page.

    Parameters:
        url (str): The URL of the webpage containing the form.
        form_id (int): The index of the form to be submitted.
        data (dict): A dictionary containing form data keys and values.

    Returns:
        str: The title of the page resulting from the form submission.

    Notes:
        - If the page has no title, it returns 'No Title'.

    Requirements:
        - mechanize
        - bs4.BeautifulSoup

    Examples:
        >>> data = {'username': 'admin', 'password': 'password'}
        >>> title = f_200('https://www.example.com/login', 0, data)
        >>> isinstance(title, str)
        True
    """
    br = mechanize.Browser()
    br.open(url)
    br.select_form(nr=form_id)
    for key, value in data.items():
        br[key] = value
    response = br.submit()
    soup = BeautifulSoup(response.read(), 'html.parser')
    title = soup.title.string if soup.title else 'No Title'
    return title

import unittest
from unittest.mock import patch, MagicMock
class TestCases(unittest.TestCase):
    @patch('mechanize.Browser')
    def test_return_type(self, mock_browser):
        """ Test that the function returns a string. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.return_value = MagicMock()
        mock_browser.return_value.submit.return_value.read.return_value = "<html><head><title>Test Page</title></head></html>"
        result = f_200('https://www.example.com/login', 0, {'username': 'admin'})
        self.assertIsInstance(result, str)
    @patch('mechanize.Browser')
    def test_form_submission(self, mock_browser):
        """ Test form submission with mock data. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.return_value = MagicMock()
        mock_browser.return_value.submit.return_value.read.return_value = "<html><head><title>Successful Submission</title></head></html>"
        result = f_200('https://www.example.com/submit', 0, {'data': 'test'})
        self.assertEqual("Successful Submission", result)
    @patch('mechanize.Browser')
    def test_incorrect_form_id(self, mock_browser):
        """ Test handling of incorrect form ID. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.side_effect = mechanize.FormNotFoundError
        with self.assertRaises(mechanize.FormNotFoundError):
            f_200('https://www.example.com/login', 99, {'username': 'admin'})
    @patch('mechanize.Browser')
    def test_no_title_page(self, mock_browser):
        """ Test handling of pages with no title. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.return_value = MagicMock()
        mock_browser.return_value.submit.return_value.read.return_value = "<html><body><h1>No Title Page</h1></body></html>"
        result = f_200('https://www.example.com/no_title', 0, {})
        self.assertEqual("No Title", result)
    @patch('mechanize.Browser')
    def test_different_data_inputs(self, mock_browser):
        """ Test the function with different data inputs. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.return_value = MagicMock()
        mock_browser.return_value.submit.return_value.read.return_value = "<html><head><title>Different Input</title></head></html>"
        result = f_200('https://www.example.com/different', 0, {'new_field': 'new_value'})
        self.assertIn("Different Input", result)
    @patch('mechanize.Browser')
    def test_invalid_url(self, mock_browser):
        """ Test handling of invalid URL. """
        mock_browser.return_value.open.side_effect = mechanize.URLError(None)
        with self.assertRaises(mechanize.URLError):
            f_200('invalid_url', 0, {'username': 'admin'})
