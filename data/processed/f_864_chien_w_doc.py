import binascii
import hashlib


def f_864(input_string, verify_hash=None):
    """
    Compute the SHA256 hash of a given input string and return its hexadecimal representation.
    Optionally, verify the computed hash against a provided hash.

    Parameters:
    - input_string (str): The string to be hashed.
    - verify_hash (str, optional): A hexadecimal string to be compared with the computed hash.

    Returns:
    - str: A hexadecimal string representing the SHA256 hash of the input string.
    - bool: True if verify_hash is provided and matches the computed hash, otherwise None.

    Raises:
    - TypeError: If the input is not a string or verify_hash is not a string or None.

    Requirements:
    - hashlib
    - binascii

    Example:
    >>> f_864("Hello, World!")
    'dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f'
    >>> f_864("Hello, World!", "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f")
    True
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    if verify_hash is not None and not isinstance(verify_hash, str):
        raise TypeError("verify_hash must be a string or None")

    hashed_bytes = hashlib.sha256(input_string.encode()).digest()
    hex_encoded_hash = binascii.hexlify(hashed_bytes).decode()

    if verify_hash is not None:
        return hex_encoded_hash == verify_hash

    return hex_encoded_hash

import unittest
import binascii
import hashlib
class TestCases(unittest.TestCase):
    """Tests for f_864."""
    def test_string_with_numbers(self):
        """Test that the function returns the correct hash for a string with numbers."""
        self.assertEqual(
            f_864("4a4b4c"),
            "1a3db6ced8854274567d707b509f7486a9244be0cab89217713fce9bf09f522e",
        )
    def test_string_with_space(self):
        """Test that the function returns the correct hash for a string with space."""
        self.assertEqual(
            f_864("Open AI"),
            "dd7503942d7be003d6faaa93d9951126fde3bdd4f3484404927e79585682878a",
        )
    def test_empty_string(self):
        """Test that the function returns the correct hash for an empty string."""
        self.assertEqual(
            f_864(""),
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
    def test_string_numbers(self):
        """Test that the function returns the correct hash for a string numbers."""
        self.assertEqual(
            f_864("123456"),
            "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
        )
    def test_long_string(self):
        """Test that the function returns the correct hash for a long string."""
        self.assertEqual(
            f_864("abcdefghijklmnopqrstuvwxyz"),
            "71c480df93d6ae2f1efad1447c66c9525e316218cf51fc8d9ed832f2daf18b73",
        )
    def test_verify_hash_correct(self):
        """Test that the function returns True when verify_hash is correct."""
        self.assertTrue(
            f_864(
                "Hello, World!",
                "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f",
            )
        )
    def test_verify_hash_incorrect(self):
        """Test that the function returns False when verify_hash is incorrect."""
        self.assertFalse(f_864("Hello, World!", "incorrect_hash"))
    def test_verify_hash_none(self):
        """Test that the function returns None when verify_hash is None."""
        self.assertEqual(
            f_864("Hello, World!"),
            "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f",
        )
    def test_input_string_not_string(self):
        """Test that the function raises an error when the input is not a string."""
        with self.assertRaises(TypeError):
            f_864(123)
    def test_verify_hash_not_string_or_none(self):
        """Test that the function raises an error when verify_hash is not a string or None."""
        with self.assertRaises(TypeError):
            f_864("Hello, World!", 123)
