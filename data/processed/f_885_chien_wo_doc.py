import re
import os


def f_905(request):
    """
    Handles an HTTP GET request to retrieve a static file from the server.

    This function processes an HTTP GET request, extracts the filename from it, checks the existence of the file
    in the server's directory, and returns an HTTP response. The response either contains the file content (if found) or an
    appropriate error message (if not found or if the request is invalid).

    Parameters:
    - request (str): An HTTP GET request in string format. The expected format is "GET /<filename> HTTP/1.1".

    Returns:
    - str: An HTTP response string, which includes the status code, content length (for 200 OK responses), and the file content
           or an error message.

    Requirements:
    - os
    - re

    Examples:
    >>> f_905("GET /test.txt HTTP/1.1")
    "HTTP/1.1 200 OK\r\nContent-Length: <size of test.txt>\r\n\r\n<contents of test.txt>"
    >>> f_905("GET /nonexistent.txt HTTP/1.1")
    "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
    >>> f_905("INVALID REQUEST")
    "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
    >>> f_905("GET /restricted.txt HTTP/1.1") # Assuming an I/O error occurs
    "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
    """
    match = re.match(r"^GET /([\w\.\-]+) HTTP/1\.1$", request)
    if match:
        file_name = match.group(1)
        if os.path.exists(file_name):
            try:
                with open(file_name, "rb") as file:
                    content = file.read()
                    response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(content)}\r\n\r\n{content.decode('utf-8')}"
            except Exception:
                response = (
                    "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
                )
        else:
            response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
    else:
        response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
    return response

import unittest
import re
import os
from unittest.mock import mock_open, patch
class TestCases(unittest.TestCase):
    """Test cases for the f_905 function."""
    def setUp(self):
        """Set up the environment for testing by creating test files."""
        with open("test.txt", "w", encoding="utf-8") as f:
            f.write("This is a test file.")
    def tearDown(self):
        """Clean up the environment by deleting the test files created."""
        os.remove("test.txt")
    def test_file_found(self):
        """Test the response when the requested file is found."""
        request = "GET /test.txt HTTP/1.1"
        expected_response = (
            "HTTP/1.1 200 OK\r\nContent-Length: 20\r\n\r\nThis is a test file."
        )
        self.assertEqual(f_905(request), expected_response)
    def test_file_not_found(self):
        """Test the response when the requested file is not found."""
        request = "GET /nonexistent.txt HTTP/1.1"
        expected_response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
        self.assertEqual(f_905(request), expected_response)
    def test_bad_request(self):
        """Test the response for a badly formatted request."""
        request = "BAD REQUEST"
        expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
        self.assertEqual(f_905(request), expected_response)
    def test_empty_request(self):
        """Test the response for an empty request."""
        request = ""
        expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
        self.assertEqual(f_905(request), expected_response)
    def test_invalid_method_request(self):
        """Test the response for a request with an invalid HTTP method."""
        request = "POST /test.txt HTTP/1.1"
        expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
        self.assertEqual(f_905(request), expected_response)
    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_internal_server_error(self, mock_file):
        """Test the response when there's an internal server error (e.g., file read error)."""
        mock_file.side_effect = Exception("Mocked exception")
        request = "GET /test.txt HTTP/1.1"
        expected_response = (
            "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
        )
        self.assertEqual(f_905(request), expected_response)
