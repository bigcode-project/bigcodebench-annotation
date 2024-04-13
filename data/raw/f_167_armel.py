import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Constants
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def f_167(myString):
    '''
    Extract the first URL from a string and scrape the web page under that URL for links. Here is a step by step guide.
    - Extract first URL from myString, use the headers provided in HEADERS.
    - If there is no URL, return an empty pandas DataFrame with only one column named 'Link'
    - Otherwise, scrap the web page under that URL and retrieve all the links inside.
    - Store each link as a row of a pandas DataFrame with only one column named 'Link'.
    - Return the DataFrame

    Parameters:
    myString (str): The string from which to extract the URL.

    Returns:
    DataFrame: A pandas DataFrame of the links found on the webpage.

    Requirements:
    - re
    - bs4.BeautifulSoup
    - requests
    - pandas

    Example:
    >>> f_167('Visit: https://www.example.com')
    DataFrame containing links found on the webpage.
    '''
    # Extract the URL from the input string
    match = re.search(r'(https?://\S+)', myString)
    if not match:
        return pd.DataFrame(columns=['Link'])  # Return empty DataFrame if no URL found
    
    url = match.group()
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)  # Added a timeout of 5 seconds
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException:
        return pd.DataFrame(columns=['Link'])  # Return empty DataFrame on request error
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    links_df = pd.DataFrame(links, columns=['Link'])

    return links_df

import unittest
from unittest.mock import patch
import pandas as pd
from requests.exceptions import HTTPError

def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text: str, status_code: int):
            self.text = text
            self.content = text.encode("utf-8")
            self.status_code = status_code

        def raise_for_status(self):
            if self.status_code != 200 :
                raise HTTPError("")
    
    if args[0] == "https://www.example1.com":
        content = """
        <html>
            <body>
                <h1>Hello, BeautifulSoup!</h1>
                <ul>
                    <li><a href="index1.html"><img alt="Soumission" class="thumbnail" src="image11.jpg"/></a></li>
                    <li><a href="index2.html"><img alt="Soumission" class="thumbnail" src="image12.jpg"/></a></li>
                </ul>
            </body>
        </html>
        """
        return MockResponse(
            content,
            200
        )
    elif args[0] == "http://www.example2.com":
        content = """
        <html>
            <body>
                <h1>Hello, BeautifulSoup!</h1>
                <ul>
                    <li><a href="index.html"><img alt="Soumission" class="thumbnail" src="image2.jpg"/></a></li>
                </ul>
            </body>
        </html>
        """
        return MockResponse(
            content,
            200
        )
    elif args[0] == "http://www.example3.com":
        content = """
        <html>
            <body>
                <h1>Hello, BeautifulSoup!</h1>
                <ul>
                    <li><a href="index.html"><img alt="Soumission" class="thumbnail" src="image3.jpg"/></a></li>
                </ul>
            </body>
        </html>
        """
        return MockResponse(
            content,
            200
        )
    elif args[0] == "http://www.example4.com":
        content = """
        <html>
            <body>
                <h1>Hello, BeautifulSoup!</h1>
                <ul>
                    <li><a href="index.html"><img alt="Soumission" class="thumbnail" src="image4.jpg"/></a></li>
                </ul>
            </body>
        </html>
        """
        return MockResponse(
            content,
            200
        )
    else:
        return MockResponse('', 404)

class TestCases(unittest.TestCase):
    """Test cases for the f_167 function."""
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, *args, **kwargs):
        # Test with a string containing a valid URL
        result = f_167('Visit: https://www.example1.com')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('Link', result.columns)
        # Ensure that the function returns links (example.com should have links)
        self.assertEqual(result.shape[0], 2)
 
    def test_case_2(self):
        # Test with a string that does not contain a URL
        result = f_167('This is just a simple string.')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('Link', result.columns)
        self.assertEqual(len(result), 0)  # Expecting an empty DataFrame

    @patch('requests.get', side_effect=mock_requests_get) 
    def test_case_3(self, *args, **kwargs):
        # Test with a URL that leads to an inaccessible webpage
        result = f_167('Visit: https://example5.com')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('Link', result.columns)
        self.assertEqual(len(result), 0)  # Expecting an empty DataFrame

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_4(self, *args, **kwargs):
        # Test with a URL that redirects (e.g., http -> https)
        result = f_167('Visit: http://www.example4.com')  # http version of example.com
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('Link', result.columns)
        self.assertGreater(len(result), 0)
        self.assertEqual(result.shape[0], 1)
        self.assertEqual(result.loc[0, "Link"], "index.html")

    def test_case_5(self, *args, **kwargs):
        # Test with a non-HTTP/HTTPS URL
        result = f_167('Check out this ftp link: ftp://files.example.com')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('Link', result.columns)
        self.assertEqual(len(result), 0)  # Expecting an empty DataFrame

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()