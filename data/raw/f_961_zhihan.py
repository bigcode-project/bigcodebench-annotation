import os
from nltk import word_tokenize

def f_961(file_path='File.txt'):
    """
    Tokenizes a text file using the NLTK library. This function reads each line from the file, 
    breaks it into words or punctuation, and stores the tokens in a list.
    
    Parameters:
    - file_path (str): The path to the text file. Defaults to 'File.txt'.
    
    Returns:
    - list: A list of tokens.
    
    Requirements:
    - os
    - nltk.word_tokenize
    
    Examples:
    >>> f_961('sample.txt')
    ['Hello', ',', 'world', '!']
    >>> f_961('data.txt')
    ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '.']
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    tokens = []

    with open(file_path, 'r') as file:
        for line in file:
            tokens.extend(word_tokenize(line))

    return tokens

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        tokens = f_961('sample1.txt')
        self.assertEqual(tokens, ['Hello', ',', 'world', '!'])

    def test_case_2(self):
        tokens = f_961('sample2.txt')
        self.assertEqual(tokens, ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '.'])

    def test_case_3(self):
        tokens = f_961('sample3.txt')
        self.assertEqual(tokens, ['NLTK', 'is', 'a', 'leading', 'platform', 'for', 'building', 'Python', 'programs', 'to', 'work', 'with', 'human', 'language', 'data', '.'])

    def test_case_4(self):
        tokens = f_961('sample4.txt')
        self.assertEqual(tokens, ['OpenAI', 'is', 'an', 'organization', 'focused', 'on', 'ensuring', 'that', 'artificial', 'general', 'intelligence', 'benefits', 'all', 'of', 'humanity', '.'])

    def test_case_5(self):
        tokens = f_961('sample5.txt')
        self.assertEqual(tokens, ['Python', 'is', 'an', 'interpreted', ',', 'high-level', ',', 'general-purpose', 'programming', 'language', '.'])
if __name__ == "__main__":
    run_tests()