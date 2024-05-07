import re
from pathlib import Path
import tarfile

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def f_634(directory=DIRECTORY, file_pattern=PATTERN):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, archive these files in a tar file.

    Parameters:
    - directory: The directory to search for files matching a specified pattern. The function will iterate over all files within this directory, including subdirectories.
    - file_pattern: A regular expression pattern used to match filenames. Files whose names match this pattern will be added to an archive (tar file).

    Returns:
    - str: Path to the created tar file.

    Requirements:
    - re
    - pathlib
    - tarfile

    Example:
    >>> f_680('/path/to/source', '/path/to/target')
    """
    tar_path = Path(directory) / 'archive.tar'
    with tarfile.open(tar_path, 'w') as tar:
        for path in Path(directory).rglob('*'):
            if re.match(file_pattern, path.name):
                try:
                    tar.add(path, arcname=path.relative_to(directory))
                except PermissionError as e:
                    print(f"Skipping {path} due to permission error: {e}")
    return str(tar_path)

import unittest
import tempfile
import os
import tarfile
from pathlib import Path
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup directories and files for testing
        self.source_dir = tempfile.mkdtemp()
        self.valid_files = {
            'test1.txt': 'content',
            'test2.doc': 'content',
            'AcroTray.exe': 'content',
            'sample.exe': 'content'
        }
        for filename, content in self.valid_files.items():
            with open(os.path.join(self.source_dir, filename), 'w') as f:
                f.write(content)
        self.test_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.test_dir.cleanup) 
    def create_test_files(self, files):
        """
        Helper function to create test files in the temporary directory.
        """
        for file_name, content in files.items():
            with open(os.path.join(self.test_dir.name, file_name), 'w') as f:
                f.write(content)
    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.source_dir)
    def test_valid_files_archived(self):
        # Setup files that should be archived
        files = {'AcroTray.exe': 'content', 'Ignore.exe': 'ignore this'}
        self.create_test_files(files)
        pattern = r"AcroTray\.exe$"
        
        # Function to test
        tar_file_path = f_634(self.test_dir.name, pattern)
        
        # Verify correct files are archived
        with tarfile.open(tar_file_path, 'r') as tar:
            archived_files = [m.name for m in tar.getmembers()]
            self.assertIn('AcroTray.exe', archived_files)
    def test_no_matches(self):
        # When no files match, the archive should be empty
        tar_file_path = f_634(self.source_dir, r"non_matching_pattern")
        with tarfile.open(tar_file_path, 'r') as tar:
            self.assertEqual(len(tar.getmembers()), 0)
    def test_with_subdirectories(self):
        # Setup files in subdirectories
        sub_dir = Path(self.test_dir.name) / 'subdir'
        sub_dir.mkdir(parents=True, exist_ok=True)
        file_name = 'AcroTray.exe'
        file_path = sub_dir / file_name
        with open(file_path, 'w') as f:
            f.write('content')
        pattern = r"AcroTray\.exe$"
        
        # Function to test
        tar_file_path = f_634(self.test_dir.name, pattern)
        
        # Verify correct files are archived
        with tarfile.open(tar_file_path, 'r') as tar:
            archived_files = [m.name for m in tar.getmembers()]
            self.assertIn(os.path.join('subdir', 'AcroTray.exe'), archived_files)
    def test_empty_directory(self):
        # If the directory is empty, the tar file should also be empty
        empty_dir = tempfile.mkdtemp()
        tar_file_path = f_634(empty_dir, PATTERN)
        with tarfile.open(tar_file_path, 'r') as tar:
            self.assertEqual(len(tar.getmembers()), 0)
        shutil.rmtree(empty_dir)
    def test_file_permission_issues(self):
        # Setup a file with restricted permissions
        file_name = 'AcroTray.exe'
        file_path = os.path.join(self.test_dir.name, file_name)
        with open(file_path, 'w') as f:
            f.write('content')
        os.chmod(file_path, 0o000)  # Make it unreadable
        pattern = r"AcroTray\.exe$"
        
        # Function to test
        tar_file_path = f_634(self.test_dir.name, pattern)
        
        # Verify that files with permission issues are handled
        with tarfile.open(tar_file_path, 'r') as tar:
            archived_files = [m.name for m in tar.getmembers()]
            self.assertNotIn('AcroTray.exe', archived_files)
        os.chmod(file_path, 0o666)  # Restore permissions
