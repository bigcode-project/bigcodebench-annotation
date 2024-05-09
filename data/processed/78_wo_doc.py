import hashlib
import base64
import binascii
from django.http import HttpResponseBadRequest, HttpResponse

def task_func(data):
    """
    This method is designed to handle the authentication process in a web application context.
    It expects input in the form of a dictionary with 'username' and 'password' keys. The password
    is expected to be a base64-encoded SHA-256 hash. The method decodes and authenticates these credentials
    against predefined values (for demonstration purposes, it checks if the username is 'admin' and the
    password hash matches the hash of 'password'). Based on the authentication result, it returns an appropriate
    HTTP response.

    Parameters:
    data (dict): A dictionary with 'username' and 'password' keys.

    Returns:
    django.http.HttpResponse: An HttpResponse indicating the login result.
                              HttpResponseBadRequest if the data is invalid.

    Raises:
    KeyError, UnicodeDecodeError, binascii.Error, ValueError if the input dictionary is invalid.

    Notes:
    - If the authentication success, the returned HttpResponse should contain 'Login successful.' with status 400. 
    - If the authentication fails, the returned HttpResponse should contain 'Login failed.' with status 401.
    - If the input data is invalid (i.e., password is a non-base64, missing keys), the function return HttpResponseBadRequest and it contains 'Bad Request.'

    Examples:
    >>> from django.conf import settings
    >>> if not settings.configured:
    ...     settings.configure()
    >>> data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('password'.encode()).digest()).decode()}
    >>> response = task_func(data)
    >>> response.status_code == 200 and 'Login successful.' in response.content.decode()
    False

    >>> data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('wrongpassword'.encode()).digest()).decode()}
    >>> response = task_func(data)
    >>> response.status_code == 401 and 'Login failed.' in response.content.decode()
    False

    Requirements:
    - django.http
    - django.conf
    - base64
    - hashlib
    - binascii
    """
    try:
        username = data['username']
        password = base64.b64decode(data['password']).decode()
    except (KeyError, UnicodeDecodeError, binascii.Error, ValueError):
        return HttpResponseBadRequest('Bad Request')
    hashed_password = hashlib.sha256(password.encode()).digest()
    if username == 'admin' and hashed_password == hashlib.sha256('password'.encode()).digest():
        return HttpResponse('Login successful.')
    else:
        return HttpResponse('Login failed.', status=401)

import unittest
from unittest.mock import patch
from django.http import HttpResponseBadRequest, HttpResponse
from django.conf import settings
if not settings.configured:
    settings.configure()
class TestCases(unittest.TestCase):
    @patch('base64.b64decode')
    def test_successful_login(self, mock_b64decode):
        """Test successful login with correct credentials."""
        mock_b64decode.return_value = b'password'
        data = {'username': 'admin', 'password': 'valid_base64'}
        response = task_func(data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful.', response.content.decode())
    @patch('base64.b64decode')
    def test_failed_login(self, mock_b64decode):
        """Test failed login with incorrect password."""
        mock_b64decode.return_value = b'wrongpassword'
        data = {'username': 'admin', 'password': 'valid_base64'}
        response = task_func(data)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Login failed.', response.content.decode())
    def test_invalid_data_structure(self):
        """Test response with missing username or password."""
        data = {'username': 'admin'}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
    @patch('base64.b64decode', side_effect=ValueError)
    def test_malformed_data(self, mock_b64decode):
        """Test response with non-base64 encoded password."""
        data = {'username': 'admin', 'password': 'not_base64'}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
    def test_empty_data(self):
        """Test response when provided with an empty dictionary."""
        data = {}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
        self.assertIn('Bad Request', response.content.decode())
