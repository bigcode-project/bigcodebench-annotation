import random
import string
from django.http import HttpResponse


def task_func(request, session_expire_time):
    """
    This function creates a random session key comprising letters and digits with a specific length of 20,
    then sets this key in a cookie on an HttpResponse object with the specified expiration time.

    Parameters:
    request (django.http.HttpRequest): The incoming Django HttpRequest.
    session_expire_time (int): The expiration time for the session cookie in seconds.

    Returns:
    django.http.HttpResponse: A Django HttpResponse with the session key set in a cookie.

    Raises:
    ValueError: If the session key does not contain both letters and digits or
                the session key length is not equal to 20.

    Note:
    -   The function set the response content to "Session key generated successfully." if the session key
        is valid.

    Examples:
    >>> from django.conf import settings
    >>> from django.http import HttpRequest
    >>> if not settings.configured:
    ...     settings.configure()
    >>> request = HttpRequest()
    >>> response = task_func(request, 60)
    >>> 'session_key' in response.cookies
    True
    >>> len(response.cookies['session_key'].value) == 20
    True
    >>> response.cookies['session_key']['max-age'] == 60
    True

    Requirements:
    - django.http
    - django.conf
    - random
    - string
    """

    session_key = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    has_digit = any(char.isdigit() for char in session_key)
    has_letter = any(char.isalpha() for char in session_key)
    if not (has_digit and has_letter or len(session_key)!=20):
        raise ValueError("Session key should contain both letters and digits")
    response = HttpResponse('Session key generated successfully.')
    response.set_cookie('session_key', session_key, max_age=session_expire_time)
    return response

import unittest
from unittest.mock import patch
from django.http import HttpRequest
from django.conf import settings
# Configure Django settings if not already configured
if not settings.configured:
    settings.configure(
        DEFAULT_CHARSET='utf-8',
        SECRET_KEY='a-very-secret-key',
    )
class TestCases(unittest.TestCase):
    @patch('random.choices')
    def test_session_key_in_cookies(self, mock_random_choices):
        """Test if 'session_key' is set in the response cookies with the correct expiration."""
        mock_random_choices.return_value = ['1a'] * 10  # Mock session key as 'aaaaaaaaaaaaaaaaaaaa'
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertIn('session_key', response.cookies)
        self.assertEqual(response.cookies['session_key']['max-age'], 60)
    @patch('random.choices')
    def test_session_key_length(self, mock_random_choices):
        """Test if the length of 'session_key' is 20."""
        mock_random_choices.return_value = ['1a'] * 10
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertEqual(len(response.cookies['session_key'].value), 20)
    @patch('random.choices')
    def test_response_content(self, mock_random_choices):
        """Test if the response content includes the expected message."""
        mock_random_choices.return_value = ['1a'] * 10
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertIn('Session key generated successfully.', response.content.decode())
    @patch('random.choices')
    def test_response_type(self, mock_random_choices):
        """Test if the response object is of type HttpResponse."""
        mock_random_choices.return_value = ['1a'] * 10
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertIsInstance(response, HttpResponse)
    @patch('random.choices')
    def test_raise_error(self, mock_random_choices):
        """Test if the function raises ValueError when the session key does not contain both letters and digits."""
        mock_random_choices.return_value = ['a'] * 20  # Only letters, no digits
        request = HttpRequest()
        with self.assertRaises(ValueError):
            task_func(request, 60)  # pass the session_expire_time
    @patch('random.choices')
    def test_valid_session_key(self, mock_random_choices):
        """Test if the function completes without error when session key is valid."""
        # Ensure the mock session key always contains both letters and digits
        mock_random_choices.return_value = list('A1' * 10)  # This creates a string 'A1A1A1A1A1A1A1A1A1A1'
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertEqual(len(response.cookies['session_key'].value), 20)
        self.assertTrue(any(char.isalpha() for char in response.cookies['session_key'].value))
        self.assertTrue(any(char.isdigit() for char in response.cookies['session_key'].value))
