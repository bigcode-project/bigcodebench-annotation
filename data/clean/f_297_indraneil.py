import os
import shutil


def f_297(src_folder, backup_dir):
    """
    Backs up a given source folder to the specified backup directory, then deletes the source folder.
    
    Parameters:
    src_folder (str): The path of the source folder to be backed up and deleted.
    backup_dir (str): The path of the directory where the source folder will be backed up.
    
    Returns:
    bool: True if the operation is successful, False otherwise.
    
    Requirements:
    - os
    - shutil
    
    Example:
    >>> import tempfile
    >>> src_folder = tempfile.mkdtemp()
    >>> backup_dir = tempfile.mkdtemp()
    >>> with open(os.path.join(src_folder, 'sample.txt'), 'w') as f:
    ...     _ = f.write('This is a sample file.')
    >>> f_297(src_folder, backup_dir)
    True
    """
    # Check if source folder exists
    if not os.path.isdir(src_folder):
        raise ValueError(f"Source folder '{src_folder}' does not exist.")
    
    # Backup folder
    backup_folder = os.path.join(backup_dir, os.path.basename(src_folder))
    shutil.copytree(src_folder, backup_folder)
    
    # Delete source folder
    try:
        shutil.rmtree(src_folder)
        return True
    except Exception as e:
        print(f"Error while deleting source folder: {e}")
        return False


import unittest
import tempfile
import doctest


class TestCases(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory for testing
        self.src_folder = tempfile.mkdtemp()
        self.backup_dir = tempfile.mkdtemp()
        
        # Create a sample file in the source folder
        with open(os.path.join(self.src_folder, "sample.txt"), "w") as f:
            f.write("This is a sample file.")
    
    def tearDown(self):
        # Cleanup
        if os.path.exists(self.src_folder):
            shutil.rmtree(self.src_folder)
        if os.path.exists(self.backup_dir):
            shutil.rmtree(self.backup_dir)
    
    def test_case_1(self):
        result = f_297(self.src_folder, self.backup_dir)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(self.src_folder))
        self.assertTrue(os.path.exists(os.path.join(self.backup_dir, os.path.basename(self.src_folder), "sample.txt")))
    
    def test_case_2(self):
        shutil.rmtree(self.src_folder)
        with self.assertRaises(ValueError):
            f_297(self.src_folder, self.backup_dir)
    
    def test_case_3(self):
        os.rmdir(self.backup_dir)
        result = f_297(self.src_folder, self.backup_dir)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(self.src_folder))
        self.assertTrue(os.path.exists(os.path.join(self.backup_dir, os.path.basename(self.src_folder), "sample.txt")))
    
    def test_case_4(self):
        self.assertTrue(f_297(self.src_folder, self.src_folder))
    
    def test_case_5(self):
        os.makedirs(os.path.join(self.backup_dir, os.path.basename(self.src_folder)))
        with self.assertRaises(FileExistsError):
            f_297(self.src_folder, self.backup_dir)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    doctest.testmod()
    run_tests()
