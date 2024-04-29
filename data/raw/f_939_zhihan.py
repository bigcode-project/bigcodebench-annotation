import nltk
from string import punctuation
import os

# Constants
PUNCTUATION = set(punctuation)

def f_939(text, filename):
    """
    Save all words in a text beginning with the "$" character to a text file, excluding words entirely composed of punctuation.
    
    Parameters:
    text (str): The input text.
    filename (str): The name of the text file to save the '$' words.
    
    Returns:
    str: The absolute path of the saved text file.
    
    Requirements:
    - nltk
    - string
    - os
    
    Example:
    >>> text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
    >>> f_939(text, 'dollar_words.txt')
    """
    words = nltk.word_tokenize(text)
    dollar_words = [word for word in words if word.startswith('$') and not all(c in PUNCTUATION for c in word)]
    with open(filename, 'w') as f:
        for word in dollar_words:
            f.write(word + '\n')
    return os.path.abspath(filename)

import unittest
import os

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1
        text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
        filename = 'test_1.txt'
        expected_words = ["$abc", "$efg", "$hij", "$abc", "$abc", "$hij", "$hij"]
        output_path = f_939(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))

    def test_case_2(self):
        # Input 2
        text = "There are no dollar words here."
        filename = 'test_2.txt'
        expected_words = []
        output_path = f_939(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))
        
    def test_case_3(self):
        # Input 3
        text = "$$$$ $$ $$$$ $abc$ $def"
        filename = 'test_3.txt'
        expected_words = ["$abc$", "$def"]
        output_path = f_939(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))
        
    def test_case_4(self):
        # Input 4
        text = "$hello $world! This is a $test."
        filename = 'test_4.txt'
        expected_words = ["$hello", "$world!", "$test."]
        output_path = f_939(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))

    def test_case_5(self):
        # Input 5
        text = "$"
        filename = 'test_5.txt'
        expected_words = []
        output_path = f_939(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))

if __name__ == "__main__":
    run_tests()