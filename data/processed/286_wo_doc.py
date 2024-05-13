from collections import Counter
import os
import csv

# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    """
    Count the number of words in multiple dictionary files (.txt) in a specific directory,
    export the counts to a CSV file, and then return the total number of words.

    Parameters:
    filename (str): The name of the output CSV file.
    test_directory (str): The directory containing the dictionary files (.txt).

    Returns:
    int: total number of words in .txt files

    Note:
    - Header for the csv output file is "Word", "Count"
    - Return 0 if the input invalid or error raised

    Requirements:
    - collections.Counter
    - os
    - csv

    Example:
    >>> task_func('word_counts.csv')
    10
    """

    total_words = 0
    try:
        word_counts = Counter()
        for file_name in os.listdir(test_directory):
            if not file_name.endswith('.txt'):
                continue
            with open(os.path.join(test_directory, file_name), 'r') as file:
                words = file.read().split()
                word_counts.update(words)
        with open(output_file, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Count'])
            writer.writerows(word_counts.items())
        for word in word_counts:
            total_words += word_counts[word]
    except Exception as e:
        print(e)
    return total_words

import unittest
from unittest.mock import patch, MagicMock
from collections import Counter
from faker import Faker
import shutil
# Blackbox test cases
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_directory = './testdir_f270'
        os.makedirs(self.test_directory, exist_ok=True)
        
        self.output_file = 'test_output.csv'
        self.list_files = []
    # Function to create fake dictionary files
    def create_fake_dict_files(self, directory, num_files, num_words):
        fake = Faker()
        for _ in range(num_files):
            file_name = fake.file_name(extension='txt')
            self.list_files.append(os.path.join(directory, file_name))
            with open(os.path.join(directory, file_name), 'w') as file:
                words = [fake.word() for _ in range(num_words)]
                file.write(' '.join(words))
    
    #remove fake files
    def remove_files(self):
        for fn in self.list_files:
            if os.path.exists(fn):
               os.remove(fn)
        self.list_files = []
    def tearDown(self):
        # Remove the test_output.json file after each test
        if os.path.exists('test_output.csv'):
            os.remove('test_output.csv')
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)
    def test_no_files_in_directory(self):
        # Test case where there are no txt files in the directory
        self.create_fake_dict_files(self.test_directory, 0, 0)
        result = task_func(self.output_file, self.test_directory)
        self.assertEqual(result, 0)
        self.remove_files()
    
    def test_single_file_multiple_words(self):
        # Test case with a single file containing multiple words
        self.create_fake_dict_files(self.test_directory, 1, 50)
        result = task_func(self.output_file, self.test_directory)
        self.assertEqual(50,result)
        self.remove_files()
    def test_multiple_files_multiple_words(self):
        # Test case with multiple files each containing multiple words
        self.create_fake_dict_files(self.test_directory, 5, 20)
        result = task_func(self.output_file, self.test_directory)
        self.remove_files()
        self.assertEqual(100,result)
    def test_directory_does_not_exist(self):
        # Test case where the specified directory does not exist
        result = task_func(self.output_file, self.test_directory)
        self.assertEqual(0,result)
    def test_empty_files_in_directory(self):
        # Test case with empty txt files in the directory
        self.create_fake_dict_files(self.test_directory, 3, 0)
        result = task_func(self.output_file, self.test_directory)
        self.remove_files()
        self.assertEqual(0,result)
