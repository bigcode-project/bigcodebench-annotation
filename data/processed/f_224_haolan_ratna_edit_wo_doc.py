import re
import json
import requests

def f_507(data_url: str) -> list:
    """
    Fetch data from a specific URL and extract all names from the JSON-formatted data that are not enclosed by square brackets.
    
    Note:
    - The function uses regular expressions to search for names in the fetched data. Names that are inside square
    brackets are ignored.
    - The function will return "Invalid url input" if the names cannot be extracted from the url.

    Parameters:
    - data_url (str): The URL from which to fetch data.

    Returns:
    - list[str]: A list of extracted names.

    Requirements:
    - re
    - json
    - requests

    Example:
    >>> import json
    >>> from unittest.mock import MagicMock
    >>> from io import BytesIO
    >>> mock_response = MagicMock()
    >>> mock_response.json.return_value = {"names": ["John", "[Adam]", "Eve"]}
    >>> requests.get = MagicMock(return_value=mock_response)
    >>> f_507("https://api.example.com/other_data")
    ['John', 'Eve']
    """

    try:
        response = requests.get(data_url)
        data = response.json()
        data_string = json.dumps(data['names'])
        names = re.findall(r'(?<!\[)(\w+)(?![\w]*\])', data_string)
        return names
    except Exception as e:
        return "Invalid url input"

import unittest
from unittest.mock import patch
import json
import requests
class TestCases(unittest.TestCase):
    def mock_requests_get(url):
        # Sample mock response data with names
        if url == "https://api.example.com/data":
            response = requests.Response()
            response._content = json.dumps({"names": ["John", "Doe", "Alice"]}).encode('utf-8')
            return response
        elif url == "https://api.example.com/other_data":
            response = requests.Response()
            response._content = json.dumps({"names": ["Bob", "[Adam]", "Eve"]}).encode('utf-8')
            return response
        elif url == "https://api.example.com/data_1":
            response = requests.Response()
            response._content = json.dumps({"names": ["Billy"]}).encode('utf-8')
            return response
        else:
            return ""
        
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, mock_get):
        context = "https://api.example.com/data"
        result = f_507(context)
        self.assertListEqual(result, ["John", "Doe", "Alice"])
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self, mock_get):
        context = "https://api.example.com/other_data"
        result = f_507(context)
        self.assertListEqual(result, ['Bob', 'Eve'])
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, mock_get):
        context = ""
        result = f_507(context)
        self.assertEqual(result, "Invalid url input")
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_4(self, mock_get):
        context = "https://api.example.com/error_data"
        result = f_507(context)
        self.assertEqual(result, "Invalid url input")
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_5(self, mock_get):
        context = "https://api.example.com/data_1"
        result = f_507(context)
        self.assertListEqual(result, ['Billy'])
