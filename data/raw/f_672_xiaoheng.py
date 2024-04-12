import os
import shutil
import sys

# Constants
BACKUP_DIR = '/tmp/backup'

def f_672(directory):
    """
    Rollback the update of a directory by restoring it from a backup.
    
    Parameters:
    - directory (str): The directory path to rollback.
    
    Returns:
    - directory (str): The restored directory path if successful, otherwise an error message.
    
    Requirements:
    - os
    - shutil
    - sys
    
    Constants:
    - BACKUP_DIR: The directory where backups are stored. Default is '/tmp/backup'.
    
    Examples:
    >>> f_672('/tmp/my_data')
    '/tmp/my_data'
    
    >>> f_672('/tmp/nonexistent')
    'Backup directory /tmp/backup does not exist. Cannot rollback update.'
    
    Note: 
    - This function will return the restored directory path on successful rollback, or an error message otherwise.
    """
    # Check if the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        return f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'

    # Get the latest backup
    backups = sorted(os.listdir(BACKUP_DIR))
    latest_backup = backups[-1] if backups else None

    if not latest_backup:
        return f'No backups found in {BACKUP_DIR}. Cannot rollback update.'

    # Remove the current directory if it exists
    if os.path.exists(directory):
        shutil.rmtree(directory)

    # Restore the backup
    shutil.copytree(os.path.join(BACKUP_DIR, latest_backup), directory)

    return directory

import unittest
from helper import setup_test_directories, teardown_test_directories
import os

class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.base_dir = '/tmp/test_base'
        self.backup_dir = '/tmp/test_backup'
        self.backup_subdirs = ['backup1', 'backup2', 'backup3']
        setup_test_directories(self.base_dir, self.backup_dir, self.backup_subdirs)
    
    def tearDown(self):
        teardown_test_directories(self.base_dir, self.backup_dir)

    def test_successful_rollback(self):
        result = f_672(self.base_dir)
        self.assertEqual(result, self.base_dir)
        self.assertTrue(os.path.exists(self.base_dir))

    def test_no_backup_directory(self):
        teardown_test_directories(self.base_dir, self.backup_dir)  # Remove backup directory
        result = f_672(self.base_dir)
        self.assertEqual(result, f'Backup directory {self.backup_dir} does not exist. Cannot rollback update.')
        
    def test_no_backups_in_backup_directory(self):
        for subdir in self.backup_subdirs:
            shutil.rmtree(os.path.join(self.backup_dir, subdir))  # Remove all backups
        result = f_672(self.base_dir)
        self.assertEqual(result, f'No backups found in {self.backup_dir}. Cannot rollback update.')
        
    def test_directory_does_not_exist(self):
        non_existent_dir = '/tmp/nonexistent'
        result = f_672(non_existent_dir)
        self.assertEqual(result, non_existent_dir)
        
    def test_empty_input(self):
        result = f_672('')
        self.assertEqual(result, 'Backup directory /tmp/test_backup does not exist. Cannot rollback update.')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()