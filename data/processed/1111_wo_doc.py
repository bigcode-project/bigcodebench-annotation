import os
from nltk import word_tokenize

def task_func(file_path='File.txt'):
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
    >>> task_func('sample.txt')
    ['Hello', ',', 'world', '!']
    >>> task_func('data.txt')
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
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_task_func'
        os.makedirs(self.test_dir, exist_ok=True)
        
        f = open(self.test_dir+"/sample1.txt","w")
        f.write("Hello, world!")
        f.close()
        f = open(self.test_dir+"/sample2.txt","w")
        f.write("The quick brown fox jumps over the lazy dog .")
        f.close()
        f = open(self.test_dir+"/sample3.txt","w")
        f.write("NLTK is a leading platform for building Python programs to work with human language data.")
        f.close()
        f = open(self.test_dir+"/sample4.txt","w")
        f.write("OpenAI is an organization focused on    ensuring that artificial general intelligence benefits all   of humanity    .")
        f.close()
        
        
        f = open(self.test_dir+"/sample5.txt","w")
        f.write("Python is an interpreted, high-level , general-purpose programming language.")
        f.close()
        
    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)
    def test_case_1(self):
        tokens = task_func(self.test_dir+'/sample1.txt')
        self.assertEqual(tokens, ['Hello', ',', 'world', '!'])
    def test_case_2(self):
        tokens = task_func(self.test_dir+'/sample2.txt')
        self.assertEqual(tokens, ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '.'])
    def test_case_3(self):
        tokens = task_func(self.test_dir+'/sample3.txt')
        self.assertEqual(tokens, ['NLTK', 'is', 'a', 'leading', 'platform', 'for', 'building', 'Python', 'programs', 'to', 'work', 'with', 'human', 'language', 'data', '.'])
    def test_case_4(self):
        tokens = task_func(self.test_dir+'/sample4.txt')
        self.assertEqual(tokens, ['OpenAI', 'is', 'an', 'organization', 'focused', 'on', 'ensuring', 'that', 'artificial', 'general', 'intelligence', 'benefits', 'all', 'of', 'humanity', '.'])
    def test_case_5(self):
        tokens = task_func(self.test_dir+'/sample5.txt')
        self.assertEqual(tokens, ['Python', 'is', 'an', 'interpreted', ',', 'high-level', ',', 'general-purpose', 'programming', 'language', '.'])
