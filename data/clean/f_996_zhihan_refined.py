import bs4
import requests
import re
import csv

def f_996(url="http://example.com", csv_path="emails.csv", 
          regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
          headers={'User-Agent': 'Mozilla/5.0'}):
    """
    Scrapes a web page to extract all email addresses using a specified regular expression pattern and writes them to a CSV file. The csv file is
    always created eventhough no email is found in the url. The header of the csv should be "Emails".

    Parameters:
    - url (str): The URL of the web page to scrape. Default is "http://example.com".
    - csv_path (str): The filesystem path where the CSV file should be saved. Default is "emails.csv".
    - regex (str): The regular expression pattern used to identify email addresses. Default is a pattern that matches common email formats.
    - headers (dict): The HTTP headers to use for the request. Default includes a User-Agent header.

    Returns:
    - str: The path to the CSV file where the extracted email addresses have been saved.

    Requirements:
    - bs4
    - requests
    - re
    - csv
    
    Examples:
    >>> f_996()
    'emails.csv'
    >>> f_996(url="http://another-example.com", csv_path="another_emails.csv")
    'another_emails.csv'
    """
    response = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    emails = re.findall(regex, text)

    with open(csv_path, 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(['Emails'])
        for email in emails:
            write.writerow([email])
    
    return csv_path

import unittest
from unittest.mock import patch
import os
import csv
import tempfile

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to hold any output files
        self.test_dir = tempfile.mkdtemp()
        self.addCleanup(lambda: os.rmdir(self.test_dir))

    def tearDown(self):
        # Clean up all files created during the tests
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))

    @patch('requests.get')
    def test_extraction_and_saving_default(self, mock_get):
        """Test extracting emails using default parameters and saving to default path."""
        mocked_html_content = """<html><body>Emails: test1@example.com, test2@domain.com</body></html>"""
        mock_get.return_value.text = mocked_html_content
        
        csv_path = os.path.join(self.test_dir, "emails.csv")
        with patch('builtins.open', unittest.mock.mock_open()) as mocked_file:
            f_996(csv_path=csv_path)
            mocked_file.assert_called_once_with(csv_path, 'w', newline='')

    @patch('requests.get')
    def test_extraction_custom_url(self, mock_get):
        """Test the email extraction from a custom URL and ensure file creation even if no emails are found."""
        mock_get.return_value.text = "<html><body>No email here</body></html>"
        csv_path = os.path.join(self.test_dir, "output.csv")
        result = f_996(url="http://mocked-url.com", csv_path=csv_path)
        self.assertEqual(result, csv_path)
        self.assertTrue(os.path.exists(csv_path))  # Ensuring file is created
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.assertEqual(data, [['Emails']])

    @patch('requests.get')
    def test_extraction_custom_regex(self, mock_get):
        """Test extraction with a custom regex pattern."""
        mocked_html_content = "<html><body>Email: unique@example.com, other@sample.com</body></html>"
        mock_get.return_value.text = mocked_html_content
        csv_path = os.path.join(self.test_dir, "custom_regex.csv")
        f_996(csv_path=csv_path, regex=r"\b[A-Za-z0-9._%+-]+@example.com\b")
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            emails = [row for row in reader]
        self.assertEqual(emails, [['Emails'], ['unique@example.com']])  # Only matching specific domain

    @patch('requests.get')
    def test_with_headers_customization(self, mock_get):
        """Test extraction with customized headers."""
        mock_get.return_value.text = "<html><body>Email: info@test.com</body></html>"
        csv_path = os.path.join(self.test_dir, "headers.csv")
        f_996(csv_path=csv_path, headers={'User-Agent': 'Custom-Agent'})
        self.assertTrue(os.path.exists(csv_path))

if __name__ == "__main__":
    run_tests()