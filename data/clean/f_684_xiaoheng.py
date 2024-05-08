import random
import string

# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def f_684(length, num_digits):
    """
    Generate a random password with a specified length and number of digits.

    The function creates a random password consisting of letters and digits. The total length of the password
    and the number of digits in it are specified by the user. The characters in the password are randomly
    shuffled to ensure variability.

    Parameters:
    - length (int): The total length of the password. Must be a positive integer.
    - num_digits (int): The number of digits to be included in the password. Must be a non-negative integer and
                      less than or equal to the total length of the password.

    Returns:
    - str: A string representing the randomly generated password.

    Requirements:
    - random
    - string

    Examples:
    >>> f_684(10, 3)
    'Vpbr812Ooh'
    >>> f_684(5, 2)
    '4Ob3h'
    """

    random.seed(42)
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    if not (0 <= num_digits <= length):
        raise ValueError("num_digits must be a non-negative integer and less than or equal to length.")

    password = []
    for _ in range(length - num_digits):
        password.append(random.choice(LETTERS))
    for _ in range(num_digits):
        password.append(random.choice(DIGITS))

    random.shuffle(password)

    return ''.join(password)

import unittest

class TestCases(unittest.TestCase):
    def test_valid_input(self):
        """
        Test Case 1: Valid Input
        - Verify that the function returns a password of the correct length.
        - Verify that the function returns a password with the correct number of digits.
        - Verify that the function returns a password with the correct number of letters.
        """
        password = f_684(10, 3)
        self.assertEqual(len(password), 10, "Password length should be 10")
        self.assertEqual(sum(c.isdigit() for c in password), 3, "Password should have 3 digits")
        self.assertEqual(sum(c.isalpha() for c in password), 7, "Password should have 7 letters")

    def test_length_zero(self):
        """
        Test Case 2: Length Zero
        - Verify that the function raises a ValueError when the length is zero.
        """
        with self.assertRaises(ValueError, msg="Should raise ValueError for length 0"):
            f_684(0, 3)

    def test_negative_length(self):
        """
        Test Case 3: Negative Length
        - Verify that the function raises a ValueError when the length is negative.
        """
        with self.assertRaises(ValueError, msg="Should raise ValueError for negative length"):
            f_684(-5, 3)

    def test_negative_num_digits(self):
        """
        Test Case 4: Negative Number of Digits
        - Verify that the function raises a ValueError when the number of digits is negative.
        """
        with self.assertRaises(ValueError, msg="Should raise ValueError for negative num_digits"):
            f_684(10, -3)

    def test_num_digits_greater_than_length(self):
        """
        Test Case 5: Number of Digits Greater than Length
        - Verify that the function raises a ValueError when the number of digits is greater than the length.
        """
        with self.assertRaises(ValueError, msg="Should raise ValueError when num_digits > length"):
            f_684(5, 10)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()