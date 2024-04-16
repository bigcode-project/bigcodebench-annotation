import re
import requests

def f_329(input):
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
    >>> f_232('Fetch data from https://api.example.com/data')
    {'key': 'value'}
    """

    endpoint = re.search(r'https?:\/\/[^ ]+', input).group()

    response = requests.get(endpoint)

    return response.json()

import unittest
from unittest.mock import patch, Mock

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_case_1(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response
        
        # Test
        result = f_329('Fetch data from https://api.example.com/data')
        self.assertEqual(result, {"key": "value"})

    @patch('requests.get')
    def test_case_2(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"data": [1, 2, 3]}
        mock_get.return_value = mock_response
        
        # Test
        result = f_329('Get numbers from https://api.example.com/numbers')
        self.assertEqual(result, {"data": [1, 2, 3]})

    @patch('requests.get')
    def test_case_3(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response
        
        # Test
        result = f_329('Fetch empty data from https://api.example.com/empty')
        self.assertEqual(result, {})

    @patch('requests.get')
    def test_case_4(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"status": "OK"}
        mock_get.return_value = mock_response
        
        # Test
        result = f_329('Check status from https://api.example.com/status')
        self.assertEqual(result, {"status": "OK"})

    @patch('requests.get')
    def test_case_5(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {"users": ["Alice", "Bob", "Charlie"]}
        mock_get.return_value = mock_response
        
        # Test
        result = f_329('List users from https://api.example.com/users')
        self.assertEqual(result, {"users": ["Alice", "Bob", "Charlie"]})

        
if __name__ == "__main__":
    run_tests()