from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os

PUNCTUATION = set(punctuation)

def task_func(text, filename):
    """
    Save all words in a text beginning with the "$" character in a CSV file, excluding any words that are solely composed of punctuation characters.

    Parameters:
    text (str): The input text.
    filename (str): The name of the CSV file to save the '$' words.

    Returns:
    str: The absolute path of the saved CSV file.

    Note:
    - The header of the csv row is "Word"

    Requirements:
    - nltk.tokenize.RegexpTokenizer
    - string.punctuation
    - csv
    - os

    Example:
    >>> text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
    >>> task_func(text, 'dollar_words.csv')
    '/absolute/path/to/dollar_words.csv'
    """

    punctuation_set = set(punctuation)
    tokenizer = RegexpTokenizer(r'\$\w+')
    dollar_prefixed_words = tokenizer.tokenize(text)
    dollar_words = [word for word in dollar_prefixed_words if
                          not all(char in punctuation_set for char in word[1:])]
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Word"])
        for word in dollar_words:
            writer.writerow([word])
    return os.path.abspath(filename)

import unittest
import os
import csv
# Utility function to read the content of a CSV file
def read_csv_content(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)
class TestCases(unittest.TestCase):
    def setUp(self):
        self.filenames = []
        for i in range(1,7):
            self.filenames.append("task_func_test_output_"+str(i)+".csv")
    def tearDown(self):
        # Clean up the test file
        for filename in self.filenames:
            if os.path.exists(filename):
                os.remove(filename)
    def test_case_1(self):
        text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
        filename = self.filenames[0]
        result_path = task_func(text, filename)
        
        # Check if the returned path is correct
        self.assertTrue(os.path.exists(result_path))
        
        # Check the contents of the CSV file
        content = read_csv_content(result_path)
        expected_content = [["Word"], ["$abc"], ["$efg"], ["$hij"], ["$abc"], ["$abc"], ["$hij"], ["$hij"]]
        self.assertEqual(content, expected_content)
        
    def test_case_2(self):
        text = "$hello world $this is a $test"
        filename = self.filenames[1]
        result_path = task_func(text, filename)
        
        # Check if the returned path is correct
        self.assertTrue(os.path.exists(result_path))
        
        # Check the contents of the CSV file
        content = read_csv_content(result_path)
        expected_content = [["Word"], ["$hello"], ["$this"], ["$test"]]
        self.assertEqual(content, expected_content)
        
    def test_case_3(self):
        text = "There are no dollar words here"
        filename = self.filenames[2]
        result_path = task_func(text, filename)
        
        # Check if the returned path is correct
        self.assertTrue(os.path.exists(result_path))
        
        # Check the contents of the CSV file (it should only have the header)
        content = read_csv_content(result_path)
        expected_content = [["Word"]]
        self.assertEqual(content, expected_content)
    
    def test_case_4(self):
        text = "$word1 $word2 $word3 $word4 $word5"
        filename = self.filenames[3]
        result_path = task_func(text, filename)
        
        # Check if the returned path is correct
        self.assertTrue(os.path.exists(result_path))
        
        # Check the contents of the CSV file
        content = read_csv_content(result_path)
        expected_content = [["Word"], ["$word1"], ["$word2"], ["$word3"], ["$word4"], ["$word5"]]
        self.assertEqual(content, expected_content)
        
    def test_case_5(self):
        text = "No dollar words but containing special characters @ # % & *"
        filename = self.filenames[4]
        result_path = task_func(text, filename)
        
        # Check if the returned path is correct
        self.assertTrue(os.path.exists(result_path))
        
        # Check the contents of the CSV file (it should only have the header)
        content = read_csv_content(result_path)
        expected_content = [["Word"]]
        self.assertEqual(content, expected_content)
