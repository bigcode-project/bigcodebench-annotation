import unittest
import string

# Constants
ALPHABET = list(string.ascii_lowercase)

def f_779(word: str) -> str:
    """
    Sort the letters of a given word based on their position in the alphabet.
    
    Parameters:
    word (str): The input word consisting of lowercase alphabetic characters.
    
    Returns:
    str: The word with its letters sorted alphabetically.
    
    Requirements:
    - Utilizes the string library to define the alphabet.
    - Uses a constant ALPHABET list to represent the lowercase alphabet.
    
    Example:
    >>> f_779('cba')
    'abc'
    >>> f_779('zyx')
    'xyz'
    """
    return ''.join(sorted(word))

class TestF748(unittest.TestCase):

    def test_case_1(self):
        # Testing with a word that's already sorted
        self.assertEqual(f_779('abc'), 'abc')

    def test_case_2(self):
        # Testing with a word that's in reverse order
        self.assertEqual(f_779('zyx'), 'xyz')

    def test_case_3(self):
        # Testing with a word that has duplicate letters
        self.assertEqual(f_779('aabbcc'), 'aabbcc')

    def test_case_4(self):
        # Testing with a single-letter word
        self.assertEqual(f_779('a'), 'a')

    def test_case_5(self):
        # Testing with an empty string
        self.assertEqual(f_779(''), '')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestF748))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()