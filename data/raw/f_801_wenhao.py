import random
import re


def f_801(text, seed=None):
    """
    Scramble the letters in each word of a given text, keeping the first and last letters of each word intact.

    Parameters:
    text (str): The text to be scrambled.
    seed (int, optional): A seed for the random number generator to ensure reproducible results.
                          Defaults to None (not set).

    Returns:
    str: The scrambled text.

    Requirements:
    - random
    - re

    Notes:
    - Words are determined by regex word boundaries.
    - The scrambling only affects words longer than three characters, leaving shorter words unchanged.

    Examples:
    >>> f_801('Hello, world!', 0)
    'Hello, wlrod!'
    >>> f_801("Programming is fun, isn't it?", 42)
    "Prmiangmrog is fun, isn't it?"
    """
    if seed is not None:
        random.seed(seed)

    def scramble_word(match):
        word = match.group(0)
        if len(word) > 3:
            middle = list(word[1:-1])
            random.shuffle(middle)
            return word[0] + "".join(middle) + word[-1]
        else:
            return word

    pattern = r"\b\w+\b"
    scrambled_text = re.sub(pattern, scramble_word, text)

    return scrambled_text


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a simple sentence
        input_text = "Hello world"
        output_text = f_801(input_text, seed=1)
        self.assertTrue(output_text.startswith("H"))
        self.assertTrue(output_text.endswith("d"))
        self.assertEqual(len(input_text.split()), len(output_text.split()))

    def test_case_2(self):
        # Test with single word
        input_text = "Programming"
        output_text = f_801(input_text, seed=2)
        self.assertTrue(output_text.startswith("P"))
        self.assertTrue(output_text.endswith("g"))
        self.assertEqual(len(input_text), len(output_text))

    def test_case_3(self):
        # Test with a sentence having punctuation
        input_text = "Hello, world!"
        output_text = f_801(input_text, seed=3)
        self.assertTrue(output_text.startswith("H"))
        self.assertTrue(output_text.endswith("!"))
        self.assertEqual(len(input_text.split()), len(output_text.split()))

    def test_case_4(self):
        # Test with a sentence having numbers
        input_text = "I have 2 cats"
        output_text = f_801(input_text, seed=4)
        self.assertTrue(output_text.startswith("I"))
        self.assertTrue(output_text.endswith("s"))
        self.assertTrue("2" in output_text)
        self.assertEqual(len(input_text.split()), len(output_text.split()))

    def test_case_5(self):
        # Test with empty string
        input_text = ""
        output_text = f_801(input_text, seed=5)
        self.assertEqual(output_text, "")

    def test_case_6(self):
        # Test with words containing digits and special characters
        input_text = "Python3 is fun!"
        output_text = f_801(input_text, seed=6)
        self.assertTrue(output_text.startswith("P") and output_text.endswith("!"))
        self.assertIn("3", output_text)

    def test_case_7(self):
        # Test words that are 3 characters long
        input_text = "Can you see the cat?"
        output_text = f_801(input_text, seed=8)
        self.assertIn("Can", output_text)
        self.assertIn("the", output_text)
        self.assertIn("cat", output_text)

    def test_case_8(self):
        # Test with a longer paragraph
        input_text = (
            "This is a longer text to see how the function handles more complex inputs."
        )
        output_text = f_801(input_text, seed=9)
        self.assertGreaterEqual(
            len(output_text.split()), 10
        )  # Ensure it's a long input

    def test_case_9(self):
        # Test with non-English characters
        input_text = "Привет, как дела?"
        output_text = f_801(input_text, seed=10)
        self.assertTrue(output_text.startswith("П") and output_text.endswith("?"))

    def test_case_10(self):
        # Test reproducibility with the same seed
        input_text = "Reproducibility test"
        output_text1 = f_801(input_text, seed=11)
        output_text2 = f_801(input_text, seed=11)
        self.assertEqual(output_text1, output_text2)


if __name__ == "__main__":
    run_tests()
