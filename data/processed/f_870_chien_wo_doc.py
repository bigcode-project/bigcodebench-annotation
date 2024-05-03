import binascii
import urllib.parse


def f_252(url):
    """
    Decode a hexadecimal string from the 'q' query parameter of a URL.

    This function extracts the 'q' query parameter from the given URL,
    assumes it is a hexadecimal string, and decodes it into a UTF-8 string.
    If the hexadecimal string is invalid or cannot be decoded into a valid UTF-8 string, None is returned.

    Parameters:
    url (str): The URL to extract the query parameter from.

    Returns:
    str or None: The decoded string if the 'q' parameter exists and is a valid hexadecimal, otherwise None.

    Requirements:
    - binascii
    - urllib.parse
    
    Example:
    >>> f_252('https://www.example.com?q=4a4b4c')
    'JKL'
    """
    try:
        parsed_url = urllib.parse.urlparse(url)
        query = urllib.parse.parse_qs(parsed_url.query).get("q", [None])[0]
        return binascii.unhexlify(query).decode("utf-8") if query else None
    except (binascii.Error, UnicodeDecodeError):
        return None

import unittest
import binascii
import urllib.parse
class TestCases(unittest.TestCase):
    """Test cases for f_252."""
    def test_valid_hex_string(self):
        """Test with a valid hex string in query parameter."""
        url = "https://www.example.com?q=4a4b4c"
        self.assertEqual(f_252(url), "JKL")
    def test_no_query_parameter(self):
        """Test with no query parameter."""
        url = "https://www.example.com"
        self.assertIsNone(f_252(url))
    def test_invalid_hex_string(self):
        """Test with an invalid hex string in query parameter."""
        url = "https://www.example.com?q=4a4b4c4d4"
        self.assertIsNone(
            f_252(url)
        )  # Updated to assertIsNone as the function now handles the exception
    def test_valid_hex_non_utf8(self):
        """Test with a valid hex string that is not valid UTF-8."""
        url = "https://www.example.com?q=80"
        self.assertIsNone(
            f_252(url)
        )  # Updated to assertIsNone due to the handling of UnicodeDecodeError
    def test_multiple_query_parameters(self):
        """Test with multiple query parameters."""
        url = "https://www.example.com?a=123&q=4a4b4c&b=456"
        self.assertEqual(f_252(url), "JKL")
