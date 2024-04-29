import json
import requests

# Constants
PREFIX = 'ME'
API_URL = 'https://some-api-url.com/'

def f_993(endpoint: str) -> str:
    """Get JSON data from an API endpoint and write it to a file with a filename 
    that represents a concatenation of the "ME" prefix and the endpoint.
    
    Parameters:
    endpoint (str): The API endpoint.
    
    Returns:
    str: The filename that the JSON data was written to.
    
    Requirements:
    - json
    - requests
    
    Example:
    >>> filename = f_993('users')
    >>> print(filename)
    'MEusers.json'
    """
    try:
        response = requests.get(API_URL + endpoint)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching data from API: {e}")
    
    filename = PREFIX + endpoint + '.json'
    with open(filename, 'w') as f:
        json.dump(data, f)

    return filename

import unittest
from unittest.mock import patch, Mock
import json

# Assuming the function is imported from function.py

def mock_successful_request(*args, **kwargs):
    class MockResponse:
        @staticmethod
        def json():
            return {"key": "value"}
        @staticmethod
        def raise_for_status():
            pass
    return MockResponse()

def mock_failed_request(*args, **kwargs):
    class MockResponse:
        @staticmethod
    def test_successful_api_call(self, mock_get):
        filename = f_993('users')
        self.assertEqual(filename, 'MEusers.json')
        with open(filename, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, {"key": "value"})
    
    @patch('requests.get', side_effect=mock_failed_request)
    def test_failed_api_call(self, mock_get):
        with self.assertRaises(RuntimeError):
            f_993('invalid_endpoint')

    # Additional test cases can be added here...

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestF858Function))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# Uncomment the below line to run the tests
# run_tests()
if __name__ == "__main__":
    run_tests()