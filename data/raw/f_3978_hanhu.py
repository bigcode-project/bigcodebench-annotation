import hashlib
import hmac

def f_3980(secret, message):
    """
    Generates an HMAC (Hash-based Message Authentication Code) signature for a given message using a secret key.
    The function uses SHA-256 as the hash function to create the HMAC signature.

    Parameters:
    secret (str): The secret key used for HMAC generation.
    message (str): The message for which the HMAC signature is to be generated.

    Returns:
    str: The HMAC signature of the message, returned as a hexadecimal string.

    Requirements:
    - hashlib
    - hmac

    Examples:
    Generate an HMAC signature for a message.
    >>> len(f_3980('mysecretkey', 'Hello, world!')) == 64
    True

    Generate an HMAC for a different message with the same key.
    >>> len(f_3980('mysecretkey', 'Goodbye, world!')) == 64
    True
    """
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()


import unittest

class TestCases(unittest.TestCase):
    def test_hmac_signature_length(self):
        signature = f_3980('secretkey', 'Hello, world!')
        self.assertEqual(len(signature), 64)

    def test_hmac_signature_different_messages(self):
        sig1 = f_3980('secretkey', 'Hello, world!')
        sig2 = f_3980('secretkey', 'Goodbye, world!')
        self.assertNotEqual(sig1, sig2)

    def test_hmac_signature_same_message_different_keys(self):
        sig1 = f_3980('key1', 'Hello, world!')
        sig2 = f_3980('key2', 'Hello, world!')
        self.assertNotEqual(sig1, sig2)

    def test_hmac_signature_empty_message(self):
        signature = f_3980('secretkey', '')
        self.assertEqual(len(signature), 64)

    def test_hmac_signature_empty_key(self):
        signature = f_3980('', 'Hello, world!')
        self.assertEqual(len(signature), 64)


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
