import re
from nltk.corpus import words
from collections import Counter
from random import sample

# Ensure the words corpus is downloaded
import nltk
nltk.download('words')

# Constants
SAMPLE_ENGLISH_WORDS = set(words.words())  # Correct initialization

def f_628(s, n):
    """
    Extract up to n different English words from a string, ignoring case. 
    The string is split into words and only the English words are retained.
    If there are fewer than n different English words, all distinct ones are returned.
    
    Parameters:
    - s (str): The string to extract words from.
    - n (int): The maximum number of different English words to extract.
    
    Returns:
    - List[str]: A list of up to n different English words found in the string.
    
    Example:
    Given the nature of random sampling, the specific output can vary.
    >>> s = 'This is an example string with some random words: Apple, banana, Test, hello, world'
    >>> len(f_628(s, 5)) <= 5
    True
    >>> set(f_628("apple Apple APPle", 3)) == {"apple"}
    True
    """

    word_list = re.findall(r'\b\w+\b', s.lower())  # Convert to lowercase for comparison
    english_words = [word for word in word_list if word in SAMPLE_ENGLISH_WORDS]
    if len(english_words) < n:
        return english_words
    else:
        return sample(english_words, n)


import unittest


# Assuming ENGLISH_WORDS is defined for simplicity
SAMPLE_ENGLISH_WORDS = set(words.words())

class TestCases(unittest.TestCase):
    def test_extract_english_words(self):
        s = "This is a test string with some random words: apple, banana, test, hello, world"
        result = f_628(s, 5)
        self.assertTrue(all(word in SAMPLE_ENGLISH_WORDS for word in result))
        self.assertEqual(len(result), 5)
        self.assertEqual(len(set(result)), len(result), "All words should be unique")

    def test_fewer_than_n_words(self):
        s = "hello world"
        result = f_628(s, 5)
        self.assertTrue(len(result) <= 5)
        self.assertTrue(all(word in SAMPLE_ENGLISH_WORDS for word in result))

    def test_no_english_words(self):
        s = "xyz abcdef"
        result = f_628(s, 5)
        self.assertEqual(len(result), 0)

    def test_case_insensitivity(self):
        s = "Apple BANANA Test"
        result = f_628(s, 3)
        self.assertTrue(all(word.lower() in SAMPLE_ENGLISH_WORDS for word in result))
        self.assertEqual(len(result), 3)

    def test_duplicate_words(self):
        s = "apple banana apple banana"
        result = f_628(s, 5)
        self.assertTrue(all(word in SAMPLE_ENGLISH_WORDS for word in result))
        self.assertEqual(len(result), 2)
        self.assertEqual(set(result), {"apple", "banana"})

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()