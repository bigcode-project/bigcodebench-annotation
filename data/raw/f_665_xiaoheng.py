import subprocess
import os
import shutil
import glob

# Constants
ARCHIVE_DIR = '/tmp/archive'

def f_665(pattern):
    """
    Archive all files that match a particular pattern and then delete the original files.
    
    Parameters:
    - pattern (str): The pattern to match files.
    
    Returns:
    - archive_file (str): The archive file path.
    
    Requirements:
    - subprocess
    - os
    - shutil
    - glob
    
    Example:
    >>> f_665('*.txt')
    
    Note: This function will return the archive file path.
    """
    # Create archive directory if it does not exist
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Get the list of files matching the pattern
    file_list = glob.glob(pattern)
    
    if not file_list:
        return "No files found matching the pattern."

    # Create a unique archive file name
    archive_file_base = os.path.join(ARCHIVE_DIR, 'archive')
    archive_file = archive_file_base + '.tar.gz'
    counter = 1
    while os.path.exists(archive_file):
        archive_file = archive_file_base + f"_{counter}.tar.gz"
        counter += 1
    
    # Create an archive file
    subprocess.run(['tar', '-czf', archive_file] + file_list)
    
    # Delete the original files
    for file in file_list:
        os.remove(file)
    
    return archive_file

import unittest
import tarfile
import os
import glob

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create sample files for testing
        cls.files = ['f_665_data_xiaoheng/test1.txt', 'f_665_data_xiaoheng/test2.txt', 'f_665_data_xiaoheng/image1.jpg', 'f_665_data_xiaoheng/image2.jpg']
        for file in cls.files:
            with open(file, 'w') as f:
                f.write(f"Content of {file}")

    @classmethod
    def tearDownClass(cls):
        # Cleanup any generated files and archives
        for file in cls.files:
            if os.path.exists(file):
                os.remove(file)
        for archive in glob.glob('/tmp/archive/*.tar.gz'):
            os.remove(archive)
        if os.path.exists('/tmp/archive'):
            os.rmdir('/tmp/archive')

    def test_archive_txt_files(self):
        # Archive txt files and check results
        archive_path = f_665('*.txt')
        self.assertTrue(os.path.exists(archive_path), "Archive file not created.")
        with tarfile.open(archive_path, 'r:gz') as archive:
            archived_files = archive.getnames()
        self.assertIn('f_665_data_xiaoheng/test1.txt', archived_files, "f_665_data_xiaoheng/test1.txt not archived.")
        self.assertIn('f_665_data_xiaoheng/test2.txt', archived_files, "f_665_data_xiaoheng/test2.txt not archived.")
        self.assertFalse(os.path.exists('f_665_data_xiaoheng/test1.txt'), "f_665_data_xiaoheng/test1.txt not deleted.")
        self.assertFalse(os.path.exists('f_665_data_xiaoheng/test2.txt'), "f_665_data_xiaoheng/test2.txt not deleted.")

    def test_archive_jpg_files(self):
        # Archive jpg files and check results
        archive_path = f_665('*.jpg')
        self.assertTrue(os.path.exists(archive_path), "Archive file not created.")
        with tarfile.open(archive_path, 'r:gz') as archive:
            archived_files = archive.getnames()
        self.assertIn('f_665_data_xiaoheng/image1.jpg', archived_files, "f_665_data_xiaoheng/image1.jpg not archived.")
        self.assertIn('f_665_data_xiaoheng/image2.jpg', archived_files, "f_665_data_xiaoheng/image2.jpg not archived.")
        self.assertFalse(os.path.exists('f_665_data_xiaoheng/image1.jpg'), "f_665_data_xiaoheng/image1.jpg not deleted.")
        self.assertFalse(os.path.exists('f_665_data_xiaoheng/image2.jpg'), "f_665_data_xiaoheng/image2.jpg not deleted.")

    def test_no_matching_files(self):
        # Test with no matching files
        archive_path = f_665('*.pdf')
        self.assertEqual(archive_path, "No files found matching the pattern.", "Incorrect response for no matching files.")

    def test_multiple_archiving(self):
        # Test multiple archiving of the same pattern and ensure unique naming
        archive_path1 = f_665('*.txt')
        archive_path2 = f_665('*.txt')
        self.assertNotEqual(archive_path1, archive_path2, "Archive names are not unique.")

    def test_empty_pattern(self):
        # Test with an empty pattern
        archive_path = f_665('')
        self.assertEqual(archive_path, "No files found matching the pattern.", "Incorrect response for empty pattern.")
if __name__ == "__main__":
    run_tests()