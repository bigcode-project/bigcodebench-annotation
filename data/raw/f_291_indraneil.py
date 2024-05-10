# Importing the necessary libraries
import re
import os
import glob
import pandas as pd


LOG_PATTERN = r'ERROR (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}): (.*?)$'
# Redefining the function with the refined docstring and input parameters
def f_291(file_dir: str, file_pattern: str = '*.log') -> pd.DataFrame:
    """
    Find all error logs in the log files in the specified directory and return them in a Pandas DataFrame. The log scan uses
    the pattern 'ERROR <timestamp>: <message>'. The function reads all files in the directory matching the specified pattern
    and extracts the timestamp and message for each ERROR log entry.
    
    Parameters:
    - file_dir (str): The directory path where the log files are located.
    - file_pattern (str, optional): The file pattern to search for within the directory. Defaults to '*.log'.
    
    Returns:
    pd.DataFrame: A DataFrame with columns 'Timestamp' and 'Message' containing the timestamp and error message of the ERROR logs.
    
    Requirements:
    - re
    - os
    - glob
    - pandas
    
    Example:
    >>> errors = f_291('/path/to/files', '*.txt') # Search in empty directory
    >>> print(len(errors))
    0
    """
    errors = []

    for file in glob.glob(os.path.join(file_dir, file_pattern)):
        with open(file, 'r') as f:
            for line in f:
                match = re.match(LOG_PATTERN, line)
                if match:
                    timestamp, message = match.groups()
                    errors.append([timestamp, message])

    errors_df = pd.DataFrame(errors, columns=['Timestamp', 'Message'])

    return errors_df


import unittest
import doctest
import shutil
import tempfile


class TestCases(unittest.TestCase):
    
    def setUp(self):
        # Sample log entries
        self.error_log_1 = "ERROR 2023-10-24 12:34:56,789: Sample error message 1."
        self.error_log_2 = "ERROR 2023-10-25 10:10:10,111: Sample error message 2."
        self.non_error_log = "INFO 2023-10-24 12:00:00,000: This is a non-error log message."

        # Directory to save log files
        self.base_tmp_dir = tempfile.mkdtemp()
        self.log_dir = f"{self.base_tmp_dir}/test/"
        os.makedirs(self.log_dir, exist_ok=True)

        # Creating sample log files
        with open(os.path.join(self.log_dir, "file1.log"), "w") as f:
            f.write(self.error_log_1 + "\n")
            f.write(self.non_error_log + "\n")

        with open(os.path.join(self.log_dir, "file2.log"), "w") as f:
            f.write(self.error_log_2 + "\n")
            f.write(self.non_error_log + "\n")
            f.write(self.non_error_log + "\n")

    def tearDown(self):
        # Remove the test directory and its contents
        shutil.rmtree(self.base_tmp_dir)

    def test_case_1(self):
        """Test if the function correctly extracts error logs from multiple files."""
        errors = f_291(self.log_dir)
        self.assertIsInstance(errors, pd.DataFrame)
        self.assertEqual(len(errors), 2)
        self.assertEqual(errors.iloc[0]['Timestamp'], "2023-10-24 12:34:56,789")
        self.assertEqual(errors.iloc[0]['Message'], "Sample error message 2.")
        
    def test_case_2(self):
        """Confirm that non-error logs are excluded."""
        errors = f_291(self.log_dir)
        self.assertNotIn("This is a non-error log message.", errors['Message'].values)
        
    def test_case_3(self):
        """Test the file_pattern parameter."""
        # Creating a sample txt log file
        with open(os.path.join(self.log_dir, "file3.txt"), "w") as f:
            f.write(self.error_log_1 + "\n")
            f.write(self.non_error_log + "\n")
            
        errors = f_291(self.log_dir, "*.txt")
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors.iloc[0]['Timestamp'], "2023-10-24 12:34:56,789")
        self.assertEqual(errors.iloc[0]['Message'], "Sample error message 1.")
        
    def test_case_4(self):
        """Ensure the correct columns are present in the DataFrame."""
        errors = f_291(self.log_dir)
        self.assertIn('Timestamp', errors.columns)
        self.assertIn('Message', errors.columns)
        
    def test_case_5(self):
        """Check edge case: Empty directory."""
        empty_dir = f"{self.base_tmp_dir}/test/empty"
        os.makedirs(empty_dir, exist_ok=True)
        errors = f_291(empty_dir)
        self.assertIsInstance(errors, pd.DataFrame)
        self.assertTrue(errors.empty)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
