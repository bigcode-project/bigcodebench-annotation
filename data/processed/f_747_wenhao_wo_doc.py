import os
import glob
import csv

def f_464(directory_path, file_extension='.csv'):
    """
    Reads all files with a specified extension in a given directory and returns their data in a dictionary.
    - Reads all files with the specified extension in the given directory.
    - Uses the filename without the extension as a key in the output dictionary.
    - The value for each key is a list of rows from the file, where each row is represented as a list of values.

    Parameters:
    - directory_path (str): The path to the directory containing the files.
    - file_extension (str, optional): The file extension to look for. Default is '.csv'.

    Returns:
    - Returns a dictionary where each key is the filename (without extension) and the value is a list of rows from the file.

    Requirements:
    - os
    - glob
    - csv

    Example:
    >>> data = f_464('/home/user/data')
    >>> print(data['file1'])
    [['header1', 'header2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']]
    
    >>> data = f_464('/home/user/data', '.txt')
    >>> print(data)
    {}
    """
    data = {}
    for file in glob.glob(os.path.join(directory_path, '*' + file_extension)):
        filename = os.path.splitext(os.path.basename(file))[0]
        with open(file, 'r') as f:
            reader = csv.reader(f)
            data[filename] = list(reader)
    return data

import unittest
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # create a directory with test files
        os.mkdir('test_1')
        with open('test_1/file1.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([['header1', 'header2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']])
        os.mkdir('test_2')
        with open('test_2/file2.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([['name', 'age'], ['Alice', '30'], ['Bob', '40']])
        os.mkdir('test_5')
        with open('test_5/file3.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([['subject', 'marks'], ['Math', '90'], ['Science', '85']])
    def tearDown(self):
        # remove the test directories
        shutil.rmtree('test_1')
        shutil.rmtree('test_2')
        shutil.rmtree('test_5')
    
    def test_case_1(self):
        # This test assumes the existence of a directory named 'f_464_data' with a CSV file 'file1.csv'
        data = f_464('test_1')
        self.assertIsInstance(data, dict)
        self.assertIn('file1', data)
        self.assertEqual(data['file1'], [['header1', 'header2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']])
    def test_case_2(self):
        # This test checks explicit file_extension input
        data = f_464('test_2', '.csv')
        self.assertIsInstance(data, dict)
        self.assertIn('file2', data)
        self.assertEqual(data['file2'], [['name', 'age'], ['Alice', '30'], ['Bob', '40']])
    def test_case_3(self):
        # This test checks for a non-existent file extension, expecting an empty dictionary
        data = f_464('test_3', '.txt')
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 0)
    def test_case_4(self):
        # This test checks for a non-existent directory, expecting an empty dictionary
        data = f_464('/nonexistent/directory')
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 0)
    def test_case_5(self):
        # This test checks another file's presence and content in the dictionary
        data = f_464('test_5')
        self.assertIsInstance(data, dict)
        self.assertIn('file3', data)
        self.assertEqual(data['file3'], [['subject', 'marks'], ['Math', '90'], ['Science', '85']])
