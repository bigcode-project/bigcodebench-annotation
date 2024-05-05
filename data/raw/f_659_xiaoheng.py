import os
import re
import shutil

# Constants
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def f_659():
    """
    Move all json files in a source directory to a target directory and rename them by splitting the filename the last time "-" occurs and keeping the prefix part of the filename.
    
    Parameters:
    - None

    Returns;
    - None

    Requirements:
    - os
    - re
    - shutil

    Example:
    >>> f_659()
    """
    SOURCE_DIR = '/source/dir'
    TARGET_DIR = '/target/dir'
    FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')
    for filename in os.listdir(SOURCE_DIR):
        match = FILE_PATTERN.match(filename)
        if match is not None:
            prefix = match.group(1)
            new_filename = f'{prefix}.json'
            shutil.move(os.path.join(SOURCE_DIR, filename), os.path.join(TARGET_DIR, new_filename))


import unittest
from unittest.mock import patch, MagicMock, call
import os
import shutil

source_dirs = ["/mnt/data/test_data/source_0", "/mnt/data/test_data/source_1", "/mnt/data/test_data/source_2", "/mnt/data/test_data/source_3", "/mnt/data/test_data/source_4"]
target_dirs = ["/mnt/data/test_data/target_0", "/mnt/data/test_data/target_1", "/mnt/data/test_data/target_2", "/mnt/data/test_data/target_3", "/mnt/data/test_data/target_4"]

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    @patch('os.listdir')
    @patch('shutil.move')
    @patch('os.path.join', side_effect=lambda *args: '/'.join(args))
    def test_move_json_files(self, mock_join, mock_move, mock_listdir):
        mock_listdir.return_value = ['data-1.json', 'info-2.json', 'report-3.json']
        f_659()
        expected_calls = [
            call('/source/dir/data-1.json', '/target/dir/data.json'),
            call('/source/dir/info-2.json', '/target/dir/info.json'),
            call('/source/dir/report-3.json', '/target/dir/report.json')
        ]
        mock_move.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir', MagicMock(return_value=[]))
    @patch('shutil.move')
    def test_no_files_to_move(self, mock_move):
        f_659()
        mock_move.assert_not_called()

    @patch('os.listdir', return_value=['wrongfile.txt', 'not-a-json-1.txt', 'badname.json'])
    @patch('shutil.move')
    def test_incorrect_file_patterns(self, mock_move, mock_listdir):
        f_659()
        mock_move.assert_not_called()

    @patch('os.listdir', return_value=['complex-pattern-123-1.json', 'simple-2.json'])
    @patch('shutil.move')
    @patch('os.path.join', side_effect=lambda *args: '/'.join(args))
    def test_renaming_accuracy(self, mock_join, mock_move, mock_listdir):
        f_659()
        expected_calls = [
            call('/source/dir/complex-pattern-123-1.json', '/target/dir/complex-pattern-123.json'),
            call('/source/dir/simple-2.json', '/target/dir/simple.json')
        ]
        mock_move.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir', return_value=['misleading-name-not-json-file-1', 'another-fake-2.json.data'])
    @patch('shutil.move')
    def test_special_cases_handling(self, mock_move, mock_listdir):
        f_659()
        mock_move.assert_not_called()


if __name__ == "__main__":
    run_tests()