import os
import shutil

# Constants
BACKUP_DIR = '/tmp/backup'

def task_func(directory):
    """
    Rollback the update of a directory by restoring it from a backup.
    
    Parameters:
    - directory (str): The directory path to rollback.
    
    Returns:
    - directory (str): The restored directory path if successful, otherwise an error message.
    
    Requirements:
    - os
    - shutil
    
    Constants:
    - BACKUP_DIR: The directory where backups are stored. Default is '/tmp/backup'.
    
    Examples:
    >>> task_func('/tmp/my_data')
    '/tmp/my_data'
    
    >>> task_func('/tmp/nonexistent')
    'Backup directory /tmp/backup does not exist. Cannot rollback update.'
    
    Note: 
    - This function will return the restored directory path on successful rollback, or an error message otherwise.
    """
    if not os.path.exists(BACKUP_DIR):
        return f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'
    backups = sorted(os.listdir(BACKUP_DIR))
    latest_backup = backups[-1] if backups else None
    if not latest_backup:
        return f'No backups found in {BACKUP_DIR}. Cannot rollback update.'
    if os.path.exists(directory):
        shutil.rmtree(directory)
    shutil.copytree(os.path.join(BACKUP_DIR, latest_backup), directory)
    return directory

import unittest
from unittest.mock import patch, MagicMock
import os
import shutil
class TestCases(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.rmtree')
    @patch('shutil.copytree')
    def test_successful_rollback(self, mock_copytree, mock_rmtree, mock_exists, mock_listdir):
        mock_exists.side_effect = lambda x: True if x == BACKUP_DIR else False
        mock_listdir.return_value = ['backup1']
        result = task_func('/tmp/my_data')
        self.assertEqual(result, '/tmp/my_data')
        mock_copytree.assert_called_once()
    @patch('os.listdir')
    @patch('os.path.exists')
    def test_no_backup_directory(self, mock_exists, mock_listdir):
        mock_exists.return_value = False
        result = task_func('/tmp/my_data')
        self.assertEqual(result, 'Backup directory /tmp/backup does not exist. Cannot rollback update.')
    @patch('os.listdir')
    @patch('os.path.exists')
    def test_no_backups_in_backup_directory(self, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = []
        result = task_func('/tmp/my_data')
        self.assertEqual(result, 'No backups found in /tmp/backup. Cannot rollback update.')
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.rmtree')
    @patch('shutil.copytree')
    def test_directory_does_not_exist(self, mock_copytree, mock_rmtree, mock_exists, mock_listdir):
        mock_exists.side_effect = lambda x: True if x == BACKUP_DIR else False
        mock_listdir.return_value = ['backup1']
        result = task_func('/tmp/nonexistent')
        self.assertEqual(result, '/tmp/nonexistent')
        mock_copytree.assert_called_once()
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.rmtree')
    @patch('shutil.copytree')
    def test_erroneous_backup_content(self, mock_copytree, mock_rmtree, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = ['corrupt_backup']
        mock_copytree.side_effect = Exception("Corruption detected")
        with self.assertRaises(Exception) as context:
            task_func('/tmp/my_data')
        self.assertTrue('Corruption detected' in str(context.exception))
