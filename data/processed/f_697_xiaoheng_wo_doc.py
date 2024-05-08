import re
import os
import string
import random

def f_573(input_string, directory='./text_files'):
    """
    Split a multi-line string into separate strings, remove special characters, and save each string as a separate text file.
    
    Parameters:
    - input_string (str): The multi-line string to be split and saved.
    - directory (str): The directory where the text files will be saved. Default is './text_files'.
    
    Returns:
    - file_paths (list): A list of file paths where the text is saved.
    
    Requirements:
    - re
    - os
    - string
    - random 
    
    Example:
    >>> f_573('line a\nfollows by line b\n...bye\n')
    ['./text_files/12345.txt', './text_files/67890.txt', './text_files/11223.txt']
    """
    lines = input_string.split('\n')
    file_paths = []
    for line in lines:
        line = re.sub('['+string.punctuation+']', '', line)
        filename = str(random.randint(10000, 99999)) + '.txt'
        filepath = os.path.join(directory, filename)
        file_paths.append(filepath)
        with open(filepath, 'w') as file:
            file.write(line)
    return file_paths

import unittest
import os
import random
import string
# Importing the refined function
class TestCases(unittest.TestCase):
    def setUp(self):
        # Set up the directory where test files will be saved
        self.test_dir = './test_text_files'
        os.makedirs(self.test_dir, exist_ok=True)
    def tearDown(self):
        # Remove all files in the test directory after each test
        for file_name in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file_name)
            os.remove(file_path)
    def test_single_line(self):
        # Test with a single line string
        input_string = "Hello, world!"
        output = f_573(input_string, self.test_dir)
        self.assertEqual(len(output), 1)
        with open(output[0], 'r') as file:
            self.assertEqual(file.read(), "Hello world")
    def test_multi_line(self):
        # Test with a multi-line string
        input_string = "Line A\nLine B\nLine C"
        output = f_573(input_string, self.test_dir)
        self.assertEqual(len(output), 3)
        expected_lines = ["Line A", "Line B", "Line C"]
        for i, file_path in enumerate(output):
            with open(file_path, 'r') as file:
                self.assertEqual(file.read(), expected_lines[i])
    def test_special_characters(self):
        # Test if special characters are removed
        input_string = "Hello!@$\nWorld!#"
        output = f_573(input_string, self.test_dir)
        self.assertEqual(len(output), 2)
        expected_lines = ["Hello", "World"]
        for i, file_path in enumerate(output):
            with open(file_path, 'r') as file:
                self.assertEqual(file.read(), expected_lines[i])
    def test_empty_string(self):
        # Test with an empty string
        input_string = ""
        output = f_573(input_string, self.test_dir)
        self.assertEqual(len(output), 1)
        with open(output[0], 'r') as file:
            self.assertEqual(file.read(), "")
    def test_random_filenames(self):
        # Test if filenames are random and unique
        input_string = "A\nB"
        output1 = f_573(input_string, self.test_dir)
        output2 = f_573(input_string, self.test_dir)
        self.assertNotEqual(output1, output2)
