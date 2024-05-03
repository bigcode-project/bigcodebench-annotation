import bs4
import requests
import re
import csv

def f_996(url="http://example.com", csv_path="emails.csv", 
                   regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
                   headers={'User-Agent': 'Mozilla/5.0'}):
    """
Scrapes a web page to extract all email addresses and writes them to a specified CSV file.
    
Functionality:
- Extracts email addresses from the specified URL.
- Writes the extracted emails to a CSV file at the given path.
    
Input:
- url (str): The URL of the web page to scrape. Default is "http://example.com".
- csv_path (str): The path where the CSV file should be saved. Default is "emails.csv".
- regex (str): The regular expression pattern to extract emails. Default is a common email pattern.
- headers (dict): The headers to use for the request. Default is {'User-Agent': 'Mozilla/5.0'}.
    
Output:
- Returns the path of the CSV file where the emails are saved.
    
Requirements:
- bs4
- requests
- re
- csv
    
Example:
>>> f_996()
"emails.csv"
    
>>> f_996(url="http://another-example.com", csv_path="another_emails.csv")
"another_emails.csv"
    """
    response = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    emails = re.findall(regex, text)

    with open(csv_path, 'w') as f:
        write = csv.writer(f)
        write.writerow(['Emails'])
        for email in emails:
            write.writerow([email])
    
    return csv_path

import unittest
from unittest.mock import patch
import os
import csv

# Adding the modified function content to the test environment

import bs4
import requests
import re
import csv

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    # Mocked HTML content for testing
    mocked_html_content = """<html>
        <head><title>Test Page</title></head>
        <body>
            <p>Emails: test1@example.com, test2@domain.com, not-an-email</p>
        </body>
    </html>"""

    @patch('requests.get')
    def test_case_1(self, mock_get):
        # Mocking the response of requests.get
        mock_get.return_value.text = self.mocked_html_content
        # Testing with default values
        result = f_996()
        self.assertEqual(result, "emails.csv")
        # Asserting that emails.csv contains the correct emails
        with open(result, 'r') as f:
            reader = csv.reader(f)
            emails = list(reader)
        self.assertEqual(emails, [['Emails'], ['test1@example.com'], ['test2@domain.com']])
        
    @patch('requests.get')
    def test_case_2(self, mock_get):
        # Mocking the response of requests.get
        mock_get.return_value.text = self.mocked_html_content
        # Testing with custom URL and default CSV path
        result = f_996(url="http://mocked-url.com")
        self.assertEqual(result, "emails.csv")

    @patch('requests.get')
    def test_case_3(self, mock_get):
        # Mocking the response of requests.get
        mock_get.return_value.text = self.mocked_html_content
        # Testing with custom URL and custom CSV path
        result = f_996(url="http://mocked-url.com", csv_path="custom_emails.csv")
        self.assertEqual(result, "custom_emails.csv")

    @patch('requests.get')
    def test_case_4(self, mock_get):
        # Mocking the response of requests.get
        mock_get.return_value.text = self.mocked_html_content
        # Testing with custom regex pattern
        result = f_996(regex=r"\b[A-Za-z0-9._%+-]+@example.com\b")
        # Since we used a specific regex pattern, only test1@example.com should be extracted
        with open(result, 'r') as f:
            reader = csv.reader(f)
            emails = list(reader)
        self.assertEqual(emails, [['Emails'], ['test1@example.com']])
        
    @patch('requests.get')
    def test_case_5(self, mock_get):
        # Mocking the response of requests.get
        mock_get.return_value.text = self.mocked_html_content
        # Testing with custom headers
        result = f_996(headers={'User-Agent': 'Custom-Agent'})
        self.assertEqual(result, "emails.csv")

# Cleaning up created CSV files after tests
if os.path.exists("emails.csv"):
    os.remove("emails.csv")
if os.path.exists("custom_emails.csv"):
    os.remove("custom_emails.csv")
if __name__ == "__main__":
    run_tests()