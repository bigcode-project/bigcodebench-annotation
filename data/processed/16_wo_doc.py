import os
import glob
import subprocess

def task_func(directory, backup_dir='/path/to/backup'):
    """
    Backup all '.log' files in a specified directory to a tar.gz file and delete the original files after backup.
    The backup file is named 'logs_backup.tar.gz' and placed in the specified backup directory.
    
    Parameters:
    - directory (str): The directory that contains the log files to be backed up.
    - backup_dir (str, optional): The directory where the backup file will be saved.
                                  Default is '/path/to/backup'.
    
    Returns:
    - str: The path to the backup file if logs are found, otherwise returns a message 'No logs found to backup'.
    
    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    
    Requirements:
    - subprocess
    - glob
    - os
    
    Example:
    >>> task_func('/path/to/logs')
    '/path/to/backup/logs_backup.tar.gz'
    >>> task_func('/path/to/logs', '/alternative/backup/dir')
    '/alternative/backup/dir/logs_backup.tar.gz'
    """

    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' not found.")
    log_files = glob.glob(os.path.join(directory, '*.log'))
    if not log_files:
        return "No logs found to backup."
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    backup_file = os.path.join(backup_dir, 'logs_backup.tar.gz')
    subprocess.call(['tar', '-czvf', backup_file] + log_files)
    for file in log_files:
        os.remove(file)
    return backup_file

import unittest
import tempfile
import os
import subprocess
import glob
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.temp_backup_dir = tempfile.mkdtemp()
        
        # Create some log files and some non-log files
        for i in range(5):
            with open(os.path.join(self.temp_dir, f"file_{i}.log"), "w") as f:
                f.write(f"Mock log content for file_{i}")
            with open(os.path.join(self.temp_dir, f"file_{i}.txt"), "w") as f:
                f.write(f"Mock content for file_{i}.txt")
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
        shutil.rmtree(self.temp_backup_dir)
    def test_backup_creation_and_log_file_deletion(self):
        # Test the creation of the backup file and deletion of original log files.
        backup_path = task_func(self.temp_dir, self.temp_backup_dir)
        self.assertTrue(os.path.exists(backup_path))
        self.assertEqual(backup_path, os.path.join(self.temp_backup_dir, 'logs_backup.tar.gz'))
        self.assertFalse(any(file.endswith('.log') for file in os.listdir(self.temp_dir)))
    def test_no_log_files_to_backup(self):
        # Test behavior when no log files are present in the directory.
        empty_dir = tempfile.mkdtemp()
        result = task_func(empty_dir, self.temp_backup_dir)
        self.assertEqual(result, "No logs found to backup.")
        shutil.rmtree(empty_dir)
    def test_non_log_files_remain(self):
        # Ensure that non-log files are not deleted or included in the backup.
        backup_path = task_func(self.temp_dir, self.temp_backup_dir)
        self.assertEqual(len(glob.glob(os.path.join(self.temp_dir, '*.txt'))), 5)  # Check only non-log files remain
    def test_handle_non_existing_directory(self):
        # Verify that a FileNotFoundError is raised for a non-existing source directory.
        with self.assertRaises(FileNotFoundError):
            task_func('/non/existing/directory', self.temp_backup_dir)
