import numpy as np
import random

def f_497(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    """
    Generates a palindrome sentence using random words from a specified pool. The sentence's length is randomly
    chosen between a minimum (MIN_WORDS) and maximum (MAX_WORDS) number of words. The function ensures that the
    sentence reads the same forwards and backwards.

    Parameters:
    MIN_WORDS (int): Minimum number of words in the palindrome sentence.
    MAX_WORDS (int): Maximum number of words in the palindrome sentence.
    WORDS_POOL (list): List of words to choose from for generating the palindrome.

    Returns:
    str: The generated palindrome sentence.

    Requirements:
    - numpy
    - random

    Examples:
    Generate a palindrome sentence and check if it's indeed a palindrome.
    >>> MIN_WORDS, MAX_WORDS, WORDS_POOL = 3, 10, ['apple', 'banana', 'racecar', 'world', 'level', 'madam', 'radar', 'rotor']
    >>> sentence = f_497(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    >>> re_sentence = " ".join(sentence.split()[::-1])
    >>> sentence == re_sentence
    True

    Check if the generated sentence length is within the specified range.
    >>> sentence = f_497(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    >>> MIN_WORDS <= len(sentence.split()) <= MAX_WORDS
    True
    """
    sentence_length = np.random.randint(MIN_WORDS, MAX_WORDS + 1)
    first_half = [random.choice(WORDS_POOL) for _ in range(sentence_length // 2)]
    if sentence_length % 2 == 1:
        middle_word = [random.choice(WORDS_POOL)]
        second_half = first_half[::-1]
        sentence = first_half + middle_word + second_half
    else:
        second_half = first_half[::-1]
        sentence = first_half + second_half
    return ' '.join(sentence)

import unittest
# Constants for testing
MIN_WORDS = 3
MAX_WORDS = 10
WORDS_POOL = ['apple', 'banana', 'racecar', 'world', 'level', 'madam', 'radar', 'rotor']
class TestCases(unittest.TestCase):
    def test_is_palindrome(self):
        """Test that the sentence generated is a palindrome."""
        sentence = f_497(MIN_WORDS, MAX_WORDS, WORDS_POOL)
        processed_sentence = " ".join(sentence.split()[::-1])
        self.assertEqual(processed_sentence, sentence)
    def test_sentence_length_within_range(self):
        """Test that the sentence length is within the specified range."""
        sentence = f_497(MIN_WORDS, MAX_WORDS, WORDS_POOL)
        length = len(sentence.split())
        self.assertTrue(MIN_WORDS <= length <= MAX_WORDS)
    def test_multiple_sentences(self):
        """Test that multiple generated sentences are palindromes."""
        for _ in range(5):
            sentence = f_497(MIN_WORDS, MAX_WORDS, WORDS_POOL)
            processed_sentence = " ".join(sentence.split()[::-1])
            self.assertEqual(processed_sentence, sentence)
    def test_word_choice_from_pool(self):
        """Test that all words in the sentence are from the provided word pool."""
        sentence = f_497(MIN_WORDS, MAX_WORDS, WORDS_POOL)
        words = sentence.split()
        for word in words:
            self.assertIn(word, WORDS_POOL)
    def test_symmetry_of_sentence(self):
        """Test that the sentence is symmetric around its center."""
        sentence = f_497(MIN_WORDS, MAX_WORDS, WORDS_POOL)
        words = sentence.split()
        mid = len(words) // 2
        if len(words) % 2 == 0:
            self.assertEqual(words[:mid], words[:-mid-1:-1])
        else:
            self.assertEqual(words[:mid], words[-mid:][::-1])
