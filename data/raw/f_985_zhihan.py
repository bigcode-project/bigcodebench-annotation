import re
import json
import requests

def f_985(myString, token):
    """
Extract a URL from a string and send it to a REST API.

Parameters:
myString (str): The string from which to extract the URL.
token (str): The authorization token required for API access.

Returns:
dict: The response from the API.

Requirements:
- re
- json
- requests

Example:
>>> f_985('Please check: https://www.google.com', 'your_token_here')
{'message': 'URL received'}
    """
    url = re.search(r'(https?://\S+)', myString).group()
    headers = {'Authorization': 'Bearer ' + token}
    data = {'url': url}
    response = requests.post('https://api.example.com/urls', headers=headers, data=json.dumps(data))

    return response.json()

import unittest
from unittest.mock import patch

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

class TestCases(unittest.TestCase):
    def setUp(self):
        # Mocking the response from the API
        self.mock_response = MockResponse({'message': 'URL received'}, 200)

    @patch('requests.post')
    def test_case_1(self, mock_post):
        # Testing with a valid URL and token
        mock_post.return_value = self.mock_response
        result = f_985('Please check: https://www.google.com', 'test_token')
        self.assertEqual(result, {'message': 'URL received'})

    @patch('requests.post')
    def test_case_2(self, mock_post):
        # Testing with a different valid URL and token
        mock_post.return_value = self.mock_response
        result = f_985('Visit: https://www.example.com', 'test_token_2')
        self.assertEqual(result, {'message': 'URL received'})

    @patch('requests.post')
    def test_case_3(self, mock_post):
        # Testing with a string without a URL
        with self.assertRaises(AttributeError):
            f_985('This is just a string without a URL.', 'test_token_3')

    @patch('requests.post')
    def test_case_4(self, mock_post):
        # Testing with an empty string
        with self.assertRaises(AttributeError):
            f_985('', 'test_token_4')

    @patch('requests.post')
    def test_case_5(self, mock_post):
        # Testing with a string containing multiple URLs
        mock_post.return_value = self.mock_response
        result = f_985('Check these: https://www.google.com and https://www.example.com', 'test_token_5')
        self.assertEqual(result, {'message': 'URL received'})

if __name__ == "__main__":
    unittest.main()
if __name__ == "__main__":
    run_tests()