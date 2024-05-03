import subprocess
import csv
import glob
import random
import os

def f_1018(file):
    """
    Divide a CSV file into several smaller files and shuffle the lines in each file.
    
    This function takes a CSV file path as input, divides it into smaller files using 
    the shell 'split' command, and then shuffles the rows in each of the resulting files.

    Parameters:
    file (str): The path to the CSV file.

    Returns:
    list: The paths to the split files. If the file does not exist, does not have csv extension or some an exception occurs, 
    then returns empty list.

    Requirements:
    - subprocess
    - csv
    - glob
    - random
    - os

    Example:
    >>> f_1018('/path/to/file.csv')
    ['/path/to/split_00', '/path/to/split_01', ...]
    """
    # Check if file exists
    if not os.path.exists(file):
        print("Provided file does not exist.")
        return []
    
    # Check for CSV file extension
    if not file.endswith('.csv'):
        print("Provided file is not a CSV.")
        return []

    try:
        subprocess.call(['split', '-n', '5', '-d', file, 'split_'])
        split_files = glob.glob('split_*')

        for split_file in split_files:
            with open(split_file, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)

            random.shuffle(rows)

            with open(split_file, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(rows)

        return split_files
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

import unittest
import csv
import os

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_small_csv(self):
        split_files = f_1018(csv_files[0])
        self.assertTrue(len(split_files) > 0, "No files were split.")
        with open(csv_files[0], "r") as f:
            original_rows = list(csv.reader(f))
        with open(split_files[0], "r") as f:
            split_rows = list(csv.reader(f))
        self.assertNotEqual(original_rows[1:], split_rows[1:], "Rows are not shuffled.")
    
    def test_case_medium_csv(self):
        split_files = f_1018(csv_files[1])
        self.assertTrue(len(split_files) > 0, "No files were split.")
        with open(csv_files[1], "r") as f:
            original_rows = list(csv.reader(f))
        with open(split_files[0], "r") as f:
            split_rows = list(csv.reader(f))
        self.assertNotEqual(original_rows[1:], split_rows[1:], "Rows are not shuffled.")
    
    def test_case_large_csv(self):
        split_files = f_1018(csv_files[2])
        self.assertTrue(len(split_files) > 0, "No files were split.")
        with open(csv_files[2], "r") as f:
            original_rows = list(csv.reader(f))
        with open(split_files[0], "r") as f:
            split_rows = list(csv.reader(f))
        self.assertNotEqual(original_rows[1:], split_rows[1:], "Rows are not shuffled.")
    
    def test_case_invalid_file(self):
        split_files = f_1018("/path/that/does/not/exist.csv")
        self.assertEqual(split_files, [], "Expected an empty list for an invalid file path.")
    
    def test_case_non_csv_file(self):
        with open(os.path.join(test_data_dir, "test.txt"), "w") as f:
            f.write("This is a test text file.")
        split_files = f_1018(os.path.join(test_data_dir, "test.txt"))
        self.assertEqual(split_files, [], "Expected an empty list for a non-CSV file.")

if __name__ == "__main__":
    run_tests()