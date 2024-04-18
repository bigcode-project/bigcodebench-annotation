import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def f_4215(num, from_base, to_base, private_key, alphabet):
    """
    Converts a number from one base to another, signs it with a private RSA key,
    and encodes the signed number in base64 using a custom alphabet.

    Parameters:
    - num (str): The number to be converted, represented as a string.
    - from_base (int): The base of the number to be converted.
    - to_base (int): The base to convert the number to.
    - private_key (Any): The private RSA key for signing. The type hint is `Any` due to the dynamic nature of key objects.
    - alphabet (str): A string representing the custom alphabet for base64 encoding.

    Returns:
    - str: The base64-encoded signed number.

    Example:
    >>> from cryptography.hazmat.backends import default_backend
    >>> from cryptography.hazmat.primitives.asymmetric import rsa
    >>> private_key = rsa.generate_private_key( \
            public_exponent=65537, \
            key_size=2048, \
            backend=default_backend() \
        )
    >>> alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    >>> encoded = f_4215('A1', 16, 8, private_key, alphabet)
    >>> print(encoded)
        XMBRyV7pyHXbaojpPuA3iv42nL5AVNukWQjfG48OnojFHtklqZuEgYoOwUZiQAj/dUxXANzzHuKjGRoPcuN5An7J7Gs8pEfEnOmnJfJgGLeiBgAXUeBl5aUTDoMIzBt5exSJWnNC1h5KXp+dDCpB4Hz3qIqdHyqHGNBExXZcEDOW6bEvF+rQOoQpxUJ6Xh3M/46i0g+vSDVyxLxurZpfVNQjEkrV8IlQXXdHoy4ciUC4YrwM0FrdM1BIWdzrhL9k6NfJeI96rabT8xHLrnZDH57mJqWBhpywVFtB7BEnqND70T0fpauFKtuaiA3jc+IydFC+lvodTWe3LiqI2WBsQw==
    >>> isinstance(encoded, str)
    True
    
    Requirements:
    - numpy
    - cryptography.hazmat.primitives.hashes
    - cryptography.hazmat.primitives.asymmetric.padding
    - base64

    Note:
    - The function assumes that the provided number can be successfully converted from the specified source base to the target base.
    - The RSA private key must be generated and provided to sign the converted number.
    - The custom alphabet for base64 encoding allows for flexibility in encoding schemes.
    """
    base64_table = np.array(list(alphabet))
    n = int(num, from_base)
    
    new_num = ''
    while n > 0:
        n, m = divmod(n, to_base)
        new_num += base64_table[m]

    num = new_num[::-1]
    data = bytes(num, 'utf-8')
    signed_num = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    base64_encoded = base64.b64encode(signed_num)

    return base64_encoded.decode()


import unittest
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import base64

class TestF4215(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Generate a test RSA private key
        cls.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        cls.alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

    def test_base_conversion_and_signing(self):
        """Test base conversion and signing output is a base64 string"""
        encoded = f_4215('A1', 16, 8, self.private_key, self.alphabet)
        self.assertIsInstance(encoded, str)

    def test_different_numbers_produce_different_output(self):
        """Test that different numbers produce different signed output"""
        encoded1 = f_4215('A1', 16, 8, self.private_key, self.alphabet)
        encoded2 = f_4215('FF', 16, 8, self.private_key, self.alphabet)
        self.assertNotEqual(encoded1, encoded2)

    def test_f_4215_return_type(self):
        """Ensure f_4215 returns a string."""
        result = f_4215('A1', 16, 8, self.private_key, self.alphabet)
        self.assertIsInstance(result, str, "f_4215 should return a string")

    def test_invalid_base_conversion_raises_value_error(self):
        """Test that invalid base conversion raises a ValueError"""
        with self.assertRaises(ValueError):
            f_4215('G', 16, 8, self.private_key, self.alphabet)

    def test_output_is_base64_encoded(self):
        """Test that the output is properly base64 encoded"""
        encoded = f_4215('1', 10, 2, self.private_key, self.alphabet)
        self.assertTrue(self.is_base64(encoded), "Output should be valid base64.")

    @staticmethod
    def is_base64(s):
        """Utility function to check if a string is base64 encoded."""
        try:
            base64.b64decode(s)
            return True
        except ValueError:
            return False



def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestF4215)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
