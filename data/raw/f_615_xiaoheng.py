import os
import sys
import re

def f_615(log_file_path: str, keywords: list):
    '''
    Check a log file and format the lines that contain certain keywords. This code reads the log file specified by log_file_path; searches for lines containing any of the keywords provided in the list;
    and formats each line to display the keyword, the timestamp, and the message separated by 20 spaces.
    
    Parameters:
    - log_file_path (str): The path to the log file to be checked.
    - keywords (list): A list of keywords to be searched for in the log file.
    
    Returns:
    - formatted_lines (list): Returns a list of formatted strings containing the relevant information.
    
    Requirements:
    - os
    - re
    - sys
    
    Example:
    >>> f_615('/path/to/log_file.log', ['ERROR', 'WARNING'])
    ['    ERROR :    11:30:10 : This is an error message', '    WARNING :    11:35:10 : This is a warning message']
    '''
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"Log file {log_file_path} does not exist.")
    
    formatted_lines = []
    with open(log_file_path, 'r') as log:
        for line in log:
            for keyword in keywords:
                if keyword in line:
                    parts = re.split(r'\s+', line.strip(), maxsplit=2)
                    if len(parts) == 3:
                        formatted_line = f"{keyword:>{20}} : {parts[1]:>{20}} : {parts[2]:>{20}}"
                        formatted_lines.append(formatted_line)
                    else:
                        # Handle lines that do not conform to expected structure
                        formatted_lines.append(f"Line format unexpected: {line.strip()}")
    return formatted_lines
    

import unittest
import os

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup code to create a test log file
        cls.test_file_path = "test_log_file.log"
        with open(cls.test_file_path, 'w') as f:
            f.write("ERROR 11:30:10 This is an error message\n")
            f.write("WARNING 11:35:10 This is a warning message\n")

    @classmethod
    def tearDownClass(cls):
        # Cleanup the test log file
        os.remove(cls.test_file_path)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            f_615("/path/to/nonexistent/file.log", ['ERROR', 'WARNING'])

    def test_empty_keywords(self):
        self.assertEqual(f_615(self.test_file_path, []), [])

    def test_single_keyword(self):
        result = f_615(self.test_file_path, ['ERROR'])
        self.assertTrue(all('ERROR' in line for line in result))

    def test_multiple_keywords(self):
        result = f_615(self.test_file_path, ['ERROR', 'WARNING'])
        self.assertTrue(all(any(kw in line for kw in ['ERROR', 'WARNING']) for line in result))

    def test_all_keywords(self):
        result = f_615(self.test_file_path, ['ERROR', 'WARNING', 'INFO'])
        self.assertTrue(len(result) >= 2)

# Run the tests
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()