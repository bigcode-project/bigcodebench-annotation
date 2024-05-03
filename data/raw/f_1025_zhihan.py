import base64
from cryptography.fernet import Fernet


def f_1025(message, encryption_key):
    """
    Encrypt a message with a symmetric encryption key and then encode the encrypted message using base64.

    Parameters:
    message (str): The message to be encrypted and encoded.
    encryption_key (str): The key used for symmetric encryption. It should be a string of 32 bytes.

    Returns:
    str: The base64 encoded encrypted message.

    Requirements:
    - base64
    - cryptography.fernet

    Example:
    >>> f_1025('Hello, World!', '01234567890123456789012345678901')
    'Z0FBQUFBQmw0TmM4dWVXanFSTEVhbXdRT3F2R3JGLUFPZV9FNkx0SFVBdGNHcC1UWEgyb3pSaG9qaEh6S2pzaXQydXkyOUg5VDRFcEdiTWgyZG5XM1VEeWtIc1BHaGpKbWc9PQ=='
    >>> f_1025('Python is a programing language', '01234567890123456789012345678901')
    'Z0FBQUFBQmw0TjVQMWFVUlhOSXZ5TzR2TWhpazRMalZMZ1RYc0RZVzM5QU1BeVJHb1czY3pjN0JOQXFjeFk4SWdRSktISmptQVRjZmxEY1J3Vm9mcG51VUEwRmVVTDgzVWpCTWx6RWFEQUdHYU1kMHJoRXJDWUU9'
    """
    fernet = Fernet(base64.urlsafe_b64encode(encryption_key.encode()))
    encrypted_message = fernet.encrypt(message.encode())
    return base64.b64encode(encrypted_message).decode()


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Test with a basic message and a valid encryption key.
        result = f_1025('Hello, World!', '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, 'Hello, World!')

    def test_case_2(self):
        # Test with an empty message and a valid encryption key.
        result = f_1025('', '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, '')

    def test_case_3(self):
        # Test with a numeric message and a valid encryption key.
        result = f_1025('1234567890', '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, '1234567890')

    def test_case_4(self):
        # Test with a long message and a valid encryption key.
        long_message = 'A' * 500
        result = f_1025(long_message, '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, long_message)

    def test_case_5(self):
        # Test with a basic message and a shorter encryption key (to test if the function handles key length issues).
        with self.assertRaises(Exception):
            f_1025('Hello, World!', '0123456789')

    def test_encryption_and_encoding(self):
        message = 'Hello, World!'
        encryption_key = '01234567890123456789012345678901'  # A valid 32-byte key for Fernet
        # Encrypt and encode the message
        encrypted_message_b64 = f_1025(message, encryption_key)

        # Ensure the result is a base64-encoded string
        self.assertIsInstance(encrypted_message_b64, str)
        try:
            # Decode the base64-encoded encrypted message
            encrypted_message = base64.b64decode(encrypted_message_b64)

            # Decrypt the message using the same encryption key
            fernet = Fernet(base64.urlsafe_b64encode(encryption_key.encode()))
            decrypted_message = fernet.decrypt(encrypted_message).decode()

            # Verify the decrypted message matches the original message
            self.assertEqual(decrypted_message, message)
        except Exception as e:
            self.fail(f"Decryption or decoding failed with an exception: {e}")


if __name__ == "__main__":
    run_tests()
