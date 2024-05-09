import unicodedata
import requests

URL = 'https://api.github.com/users/'

def f_4495(username):
    """
    Retrieves user information from the GitHub API for a given username, normalizes all string data to ASCII,
    and returns a dictionary of the normalized data. This function demonstrates data retrieval from a web API
    and handling of Unicode data normalization.

    Parameters:
    username (str): The GitHub username.

    Returns:
    dict: A dictionary with the user's data, where all string values are normalized to ASCII.

    Raises:
    requests.exceptions.HTTPError: For any HTTP response indicating an error.

    Requirements:
    - unicodedata
    - requests

    Examples:
    >>> result = f_4495('torvalds')
    >>> isinstance(result, dict)
    True
    >>> 'login' in result
    True
    """
    response = requests.get(URL + username)
    try:
        response.raise_for_status()  # This will raise an HTTPError if the response was an error
        user_data = response.json()
    except requests.exceptions.HTTPError as e:
        # Optionally, log the error or handle it according to your needs
        error_msg = f"Failed to fetch user data for '{username}'. HTTP status: {e.response.status_code} - {e.response.reason}."
        raise Exception(error_msg) from e

    normalized_user_data = {}
    for key, value in user_data.items():
        if isinstance(value, str):
            normalized_value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode()
            normalized_user_data[key] = normalized_value
        else:
            normalized_user_data[key] = value

    return normalized_user_data

import unittest
from unittest.mock import patch, Mock
import requests


class TestCases(unittest.TestCase):

    @patch('requests.get')
    def test_return_type(self, mock_get):
        mock_get.return_value.json.return_value = {'login': 'user', 'name': 'Test User'}
        result = f_4495('user')
        self.assertIsInstance(result, dict)

    @patch('requests.get')
    def test_normalized_string(self, mock_get):
        mock_get.return_value.json.return_value = {'login': 'user', 'name': 'Tést Üser'}
        result = f_4495('user')
        self.assertEqual(result['name'], 'Test User')

    @patch('requests.get')
    def test_non_string_values(self, mock_get):
        mock_get.return_value.json.return_value = {'login': 'user', 'id': 12345}
        result = f_4495('user')
        self.assertEqual(result['id'], 12345)

    @patch('requests.get')
    def test_empty_username(self, mock_get):
        mock_get.return_value.json.return_value = {}
        result = f_4495('')
        self.assertEqual(result, {})

    @patch('requests.get')
    def test_error_response(self, mock_get):
        mock_get.return_value.raise_for_status = Mock(side_effect=requests.exceptions.HTTPError("404 Not Found"))
        with self.assertRaises(Exception) as context:
            f_4495('nonexistentuser')



def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
