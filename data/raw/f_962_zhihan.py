import os
import re
import csv

def f_962(file_path='File.txt', csv_path='File.csv'):
    """
    Converts a text file to a CSV file. The function fetches each line from the text file, splits it into words, and 
    saves the words in a list. The list is then written to a CSV file.
    
    Parameters:
    - file_path (str): The path to the text file. Defaults to 'File.txt'.
    - csv_path (str): The path to the CSV file where the words will be written. Defaults to 'File.csv'.
    
    Returns:
    str: The path to the created CSV file.
    
    Requirements:
    - os
    - re
    - csv
    
    Example:
    >>> f_962('sample.txt', 'sample.csv')
    'sample.csv'
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    lines = []

    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line)
            lines.append(words)

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(lines)
    
    return csv_path

import unittest
import os
import re
import csv

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConvertTxtToCsv))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestConvertTxtToCsv(unittest.TestCase):
    def test_basic_conversion(self):
        output_csv_path = f_962('sample.txt')
        self.assertTrue(os.path.isfile(output_csv_path), "CSV file not created.")

    def test_validate_csv_content(self):
        output_csv_path = f_962('sample.txt', 'test_output.csv')
        with open(output_csv_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            csv_content = list(reader)
        expected_content = [['Hello', 'world'], ['This', 'is', 'a', 'sample', 'text', 'file'], 
                            ['It', 'contains', 'multiple', 'words', 'and', 'lines'], 
                            ['We', 'will', 'convert', 'it', 'to', 'CSV']]
        self.assertEqual(csv_content, expected_content, "CSV content is not as expected.")

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            f_962('non_existent.txt')

    def test_custom_csv_path(self):
        custom_csv_path = 'custom_output.csv'
        output_csv_path = f_962('sample.txt', custom_csv_path)
        self.assertEqual(output_csv_path, custom_csv_path, "Custom CSV path not used.")

    def test_empty_file_path(self):
        with self.assertRaises(FileNotFoundError):
            f_962('')
if __name__ == "__main__":
    run_tests()