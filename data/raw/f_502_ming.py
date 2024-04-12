import re
import shutil

import pandas as pd
import csv
import os
# Set DATA_DIR to the 'data' subdirectory in the current script's directory
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def f_502(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    """
    Searches for files in the specified directory that match a given regex pattern.

    This function walks through the directory, matches filenames against the pattern,
    and saves the matched file paths to a CSV file. It returns a DataFrame of these paths.

    Parameters:
    - pattern (str): Regex pattern to match filenames.
    - directory (str): Directory to search for files.
    - output_csv (str): CSV file path to save matched file paths.

    Returns:
    - pd.DataFrame: DataFrame with a single column 'File Path' of matched paths.

    Requirements:
    - re for regex matching.
    - pandas for DataFrame operations.
    - csv for CSV file writing.
    - os for directory traversal and file operations.

    Example usage:
    >>> df = f_502(".*\.txt$", "/path/to/search", "matched_files.csv")
    DataFrame will contain file paths of all .txt files in the search path.
    """
    matched_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                matched_paths.append(os.path.join(root, file))

    df = pd.DataFrame(matched_paths, columns=['File Path'])
    df.to_csv(output_csv, index=False)

    return df

import unittest

class TestF502(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_dir = DATA_DIR
        if not os.path.exists(cls.test_dir):
            os.makedirs(cls.test_dir)

        # Create test files
        cls.test_file1 = os.path.join(cls.test_dir, "test1.txt")
        cls.test_file2 = os.path.join(cls.test_dir, "ignore.exe")
        with open(cls.test_file1, 'w') as f:
            f.write("This is a test file.")
        with open(cls.test_file2, 'w') as f:
            f.write("This file should be ignored.")

    @classmethod
    def tearDownClass(cls):
        # Remove the test directory and all its contents
        shutil.rmtree(cls.test_dir, ignore_errors=True)

    def test_file_matching(self):
        """Ensure function matches correct files."""
        output_csv = os.path.join(self.test_dir, "matched_files.csv")
        df = f_502(r".*\.txt$", self.test_dir, output_csv)
        self.assertTrue(os.path.exists(output_csv))
        self.assertIn(self.test_file1, df['File Path'].values)

    def test_no_files_matched(self):
        """Test when no files match the pattern."""
        output_csv = os.path.join(self.test_dir, "no_match.csv")
        df = f_502(r".*\.md$", self.test_dir, output_csv)
        self.assertTrue(df.empty)

    def test_output_file_creation(self):
        """Ensure the output file is created."""
        output_csv = os.path.join(self.test_dir, "output_creation.csv")
        _ = f_502(r".*\.txt$", self.test_dir, output_csv)
        self.assertTrue(os.path.exists(output_csv))

    def test_correct_number_of_matches(self):
        """Test the number of files matched is correct."""
        output_csv = os.path.join(self.test_dir, "correct_number.csv")
        df = f_502(r".*\.txt$", self.test_dir, output_csv)
        self.assertEqual(len(df), 1)

    def test_pattern_specificity(self):
        """Ensure the regex pattern correctly distinguishes file types."""
        output_csv = os.path.join(self.test_dir, "pattern_specificity.csv")
        df = f_502(r"test1\.txt$", self.test_dir, output_csv)
        self.assertEqual(len(df), 1)
        self.assertIn("test1.txt", df['File Path'].values[0])


if __name__ == '__main__':
    unittest.main()