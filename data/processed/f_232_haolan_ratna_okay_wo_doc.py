import re
import requests

def f_470(input):
    """
    Extract an API endpoint from the input string, send a GET request to the endpoint, and return the response data in JSON format.

    Parameters:
    input (str): The input string containing an API endpoint.

    Returns:
    dict: The response data.

    Requirements:
    - re
    - json
    - requests

    Example:
    >>> f_470('Fetch data from https://api.example.com/data')
    {'key': 'value'}
    """
    endpoint = re.search(r'https?:\/\/[^ ]+', input).group()
    response = requests.get(endpoint)
    return response.json()

import unittest
from unittest.mock import patch, Mock
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_case_1(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response
        
        # Test
        result = f_470('Fetch data from https://api.example.com/data')
        self.assertEqual(result, {"key": "value"})
    @patch('requests.get')
    def test_case_2(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"data": [1, 2, 3]}
        mock_get.return_value = mock_response
        
        # Test
        result = f_470('Get numbers from https://api.example.com/numbers')
        self.assertEqual(result, {"data": [1, 2, 3]})
    @patch('requests.get')
    def test_case_3(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response
        
        # Test
        result = f_470('Fetch empty data from https://api.example.com/empty')
        self.assertEqual(result, {})
    @patch('requests.get')
    def test_case_4(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"status": "OK"}
        mock_get.return_value = mock_response
        
        # Test
        result = f_470('Check status from https://api.example.com/status')
        self.assertEqual(result, {"status": "OK"})
    @patch('requests.get')
    def test_case_5(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"users": ["Alice", "Bob", "Charlie"]}
        mock_get.return_value = mock_response
        
        # Test
        result = f_470('List users from https://api.example.com/users')
        self.assertEqual(result, {"users": ["Alice", "Bob", "Charlie"]})
