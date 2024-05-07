import requests
import pandas as pd
from bs4 import BeautifulSoup


def f_837(url: str, csv_file_path: str) -> list:
    """
    Extracts title, date, and author information from a webpage and writes the data to a CSV file.

    The function iterates through each 'div' element with a class 'container', extracting the text of 'h1', and 'span' elements with classes 
    'date' and 'author', respectively. Default values ('No Title', 'No Date', or 'No Author') are used if an element is 
    not found. The extracted data is stored in a list of tuples.

    The list of tuples is then converted into a Pandas DataFrame and saved to a CSV file at the specified file path. 
    The DataFrame's columns are labeled as 'Title', 'Date', and 'Author'. The function returns the list of tuples.

    Raises:
    - RuntimeError: If the URL is incorrect or the server is down, the error message might be "Error fetching URL: HTTP Error 404: Not Found" 
    or "Error fetching URL: ConnectionError". The function begins by making an HTTP request to the specified URL. It sets a timeout of 5 seconds to avoid 
    prolonged waiting in case of unresponsive webpages. If the request encounters any exceptions such as connection errors, timeouts, or HTTP errors, a 'requests.RequestException' is raised. 
    The function raises a '' with a message that includes the details of the exception. For example,, depending on the specific issue encountered.
    Parameters:

    Parameters:
    - url (str): The URL of the webpage to be parsed.
    - csv_file_path (str): The path where the resulting CSV file will be saved.

    Returns:
    list: A list of tuples containing the (title, date, author) extracted from the webpage. Default placeholders 
          are used for missing information.

    Requirements:
    - requests
    - bs4
    - pandas

    Example:
    >>> data = f_837('https://example.com/articles', '/path/to/save/csv/file.csv')
    >>> type(data)
    <class 'list'>
    >>> len(data) > 0
    True
    """


    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching URL: {e}")

    soup = BeautifulSoup(response.text, "html.parser")
    data = []
    for div in soup.find_all("div", class_="container"):
        title = div.find("h1").text.strip() if div.find("h1") else "No Title"
        date = (
            div.find("span", class_="date").text.strip()
            if div.find("span", class_="date")
            else "No Date"
        )
        author = (
            div.find("span", class_="author").text.strip()
            if div.find("span", class_="author")
            else "No Author"
        )
        data.append((title, date, author))

    df = pd.DataFrame(data, columns=["Title", "Date", "Author"])
    df.to_csv(csv_file_path, index=False)

    return data


import unittest
from unittest.mock import patch
import os
import shutil

# Mock HTML content
test_data_1_html = """
<html>
    <div class="container">
        <h1>Title1</h1>
        <span class="date">Date1</span>
        <span class="author">Author1</span>
    </div>
    <div class="container">
        <h1>Title2</h1>
        <span class="date">Date2</span>
        <span class="author">Author2</span>
    </div>
</html>
"""

test_data_2_html = """
<html>
    <div class="container">
        <h1>TitleA</h1>
        <span class="date">DateA</span>
        <span class="author">AuthorA</span>
    </div>
</html>
"""


class MockResponse:
    """Mock class for requests.Response"""

    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code != 200:
            raise Exception("HTTP Error")


class TestCases(unittest.TestCase):
    """Tests for the f_837 function"""

    def setUp(self):
        """Set up any necessary resources before any tests are run."""
        os.makedirs("mnt/data", exist_ok=True)  # Create the directory for test files

    @patch("requests.get")
    def test_html_parsing_multiple_entries(self, mock_get):
        """Test parsing of HTML with multiple data entries."""
        mock_get.return_value = MockResponse(test_data_1_html, 200)
        url = "https://example.com/test_data_1.html"
        csv_file_path = "mnt/data/output_1.csv"
        expected_output = [
            ("Title1", "Date1", "Author1"),
            ("Title2", "Date2", "Author2"),
        ]
        self.assertEqual(f_837(url, csv_file_path), expected_output)

    @patch("requests.get")
    def test_html_parsing_single_entry(self, mock_get):
        """Test parsing of HTML with a single data entry."""
        mock_get.return_value = MockResponse(test_data_2_html, 200)
        url = "https://example.com/test_data_2.html"
        csv_file_path = "mnt/data/output_2.csv"
        expected_output = [("TitleA", "DateA", "AuthorA")]
        self.assertEqual(f_837(url, csv_file_path), expected_output)

    @patch("requests.get")
    def test_html_parsing_with_same_data_as_first(self, mock_get):
        """Test parsing of HTML similar to first test case."""
        mock_get.return_value = MockResponse(test_data_1_html, 200)
        url = "https://example.com/test_data_1.html"
        csv_file_path = "mnt/data/output_3.csv"
        expected_output = [
            ("Title1", "Date1", "Author1"),
            ("Title2", "Date2", "Author2"),
        ]
        self.assertEqual(f_837(url, csv_file_path), expected_output)

    @patch("requests.get")
    def test_html_parsing_with_same_data_as_second(self, mock_get):
        """Test parsing of HTML similar to second test case."""
        mock_get.return_value = MockResponse(test_data_2_html, 200)
        url = "https://example.com/test_data_2.html"
        csv_file_path = "mnt/data/output_4.csv"
        expected_output = [("TitleA", "DateA", "AuthorA")]
        self.assertEqual(f_837(url, csv_file_path), expected_output)

    @patch("requests.get")
    def test_html_parsing_with_nonexistent_url(self, mock_get):
        """Test handling of HTTP error when URL does not exist."""
        mock_get.return_value = MockResponse("", 404)  # Simulating a 404 error
        url = "https://example.com/non_existent.html"  # Non-existent URL
        csv_file_path = "mnt/data/output_5.csv"
        with self.assertRaises(Exception):
            f_837(url, csv_file_path)  # Should raise HTTP Error

    @patch("requests.get")
    def test_f_837_request_exception(self, mock_get):
        """Test f_837 raises an exception when there is a request error."""
        mock_get.side_effect = requests.RequestException("Error fetching URL")
        url = "https://example.com/non_existent.html"
        csv_file_path = "mnt/data/output_error.csv"

        with self.assertRaises(Exception) as context:
            f_837(url, csv_file_path)

        self.assertIn("Error fetching URL", str(context.exception))

    def tearDown(self):
        """Clean up shared resources after all tests in the class have completed."""
        # Cleanup the test directories
        dirs_to_remove = ["mnt/data", "mnt"]
        for dir_path in dirs_to_remove:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)


def run_tests():
    """Run all testscases"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    run_tests()
