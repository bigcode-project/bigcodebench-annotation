import string
import wordninja

def f_775(word):
    """
    Converts a word into a list of tuples, with each tuple containing a lowercase English letter from the word and its position in the alphabet.
    Then, split the given word into a list of words.
    
    Requirements:
    - string
    - wordninja
    
    Parameters:
    - word (str): A string composed of lowercase letters.
    
    Returns:
    - list of tuples: Each tuple consists of a letter from the input string and its corresponding position in the alphabet.
    
    Examples:
    >>> f_775('abc')
    ([('a', 1), ('b', 2), ('c', 3)], ['abc'])
    >>> f_775('howistheweathertoday')
    ([('h', 8), ('o', 15), ('w', 23), ('i', 9), ('s', 19), ('t', 20), ('h', 8), ('e', 5), ('w', 23), ('e', 5), ('a', 1), ('t', 20), ('h', 8), ('e', 5), ('r', 18), ('t', 20), ('o', 15), ('d', 4), ('a', 1), ('y', 25)], ['how', 'is', 'the', 'weather', 'today'])
    """
    ALPHABET = list(string.ascii_lowercase)
    # Map each letter in the word to its corresponding alphabetical number
    word_numbers = [ALPHABET.index(letter) + 1 for letter in word]
    
    # Combine each letter with its alphabetical number in a tuple
    return [(word[i], word_numbers[i]) for i in range(len(word))],  wordninja.split(word)

import unittest
class TestCases(unittest.TestCase):
    
    def test_basic_word(self):
        self.assertEqual(f_775('abc'), ([('a', 1), ('b', 2), ('c', 3)], ['abc']))
        
    def test_non_consecutive_letters(self):
        self.assertEqual(f_775('ihatehim'), ([('i', 9), ('h', 8), ('a', 1), ('t', 20), ('e', 5), ('h', 8), ('i', 9), ('m', 13)], ['i', 'hate', 'him']))
    
    def test_single_letter(self):
        self.assertEqual(f_775('hellohello'), ([('h', 8), ('e', 5), ('l', 12), ('l', 12), ('o', 15), ('h', 8), ('e', 5), ('l', 12), ('l', 12), ('o', 15)], ['hello', 'hello']))
        
    def test_repeated_letters(self):
        self.assertEqual(f_775('aa'), ([('a', 1), ('a', 1)], ['a', 'a']))
        
    def test_empty_string(self):
        self.assertEqual(f_775(''), ([], []))
        
    def test_long_word(self):
        result = f_775('abcdefghijklmnopqrstuvwxyz')
        ALPHABET = list(string.ascii_lowercase)
        expected = [(letter, index + 1) for index, letter in enumerate(ALPHABET)]
        self.assertEqual(result, (expected, ['abcde', 'fg', 'hi', 'j', 'klm', 'no', 'p', 'qrs', 'tu', 'vw', 'xyz']))
        
    def test_word_with_uppercase_should_fail(self):
        with self.assertRaises(ValueError):
            f_775('aBc')
