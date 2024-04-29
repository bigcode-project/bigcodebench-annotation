import configparser
import os
import sys
import shutil

# Constants
ARCHIVE_DIR = '/home/user/archive'

def f_1014(config_file_path):
    """
    Archive a specified project directory into a ZIP file.
    
    This function reads a configuration file to get the project directory and then archives this directory
    into a ZIP file. The name of the ZIP archive will be the same as the 
    project directory's basename, and it will be stored in a predefined archive directory.
    
    Configuration File Format:
    [Project]
    directory=path_to_project_directory
    
    Input:
    - config_file_path (str): Path to the configuration file.
    
    Output:
    - Returns True if the ZIP archive is successfully created, otherwise raises an exception.
    
    Requirements:
    - configparser
    - os
    - sys
    - shutil
    
    Constants:
    - ARCHIVE_DIR: Directory where the ZIP archive will be stored.
    
    Example:
    >>> f_1014("/path/to/config.ini")
    True
    """
    config = configparser.ConfigParser()
    config.read(config_file_path)

    project_dir = config.get('Project', 'directory')

    if not os.path.isdir(project_dir):
        raise Exception(f'Directory {project_dir} does not exist.')

    archive_file = f'{ARCHIVE_DIR}/{os.path.basename(project_dir)}.zip'
    
    # Using shutil to create the zip archive
    shutil.make_archive(base_name=os.path.splitext(archive_file)[0], format='zip', root_dir=project_dir)

    if not os.path.isfile(archive_file):
        raise Exception(f"Failed to create archive {archive_file}")

    return True

import unittest
import os
import sys

class TestF962Function(unittest.TestCase):

    def setUp(self):
        # Path to the test data directory
        self.test_data_dir = "/mnt/data/test_data"

    def test_valid_project_directory(self):
        # Set CONFIG_FILE to point to a valid config file
        refined_function.CONFIG_FILE = os.path.join(self.test_data_dir, "valid_config.ini")
        
        # Asserting that the function returns True (archive is successfully created)
        self.assertTrue(f_1014())

    def test_invalid_project_directory(self):
        # Set CONFIG_FILE to point to an invalid config file (non-existent project directory)
        refined_function.CONFIG_FILE = os.path.join(self.test_data_dir, "invalid_dir_config.ini")
        
        # Asserting that the function raises an exception due to the invalid directory
        with self.assertRaises(Exception) as context:
            f_1014()
        self.assertIn("Directory", str(context.exception))

    def test_empty_project_directory(self):
        # Set CONFIG_FILE to point to an empty config file (empty project directory path)
        refined_function.CONFIG_FILE = os.path.join(self.test_data_dir, "empty_config.ini")
        
        # Asserting that the function raises an exception due to the empty directory path
        with self.assertRaises(Exception) as context:
            f_1014()
        self.assertIn("Directory", str(context.exception))
        
    def test_archive_creation(self):
        # Set CONFIG_FILE to point to a valid config file
        refined_function.CONFIG_FILE = os.path.join(self.test_data_dir, "valid_config.ini")
        
        # Run the function to create the archive
        f_1014()
        
        # Asserting that the archive file is created
        archive_file = os.path.join(refined_function.ARCHIVE_DIR, "sample_project_1.zip")
        self.assertTrue(os.path.isfile(archive_file))

    def test_archive_content(self):
        # Set CONFIG_FILE to point to a valid config file
        refined_function.CONFIG_FILE = os.path.join(self.test_data_dir, "valid_config.ini")
        
        # Run the function to create the archive
        f_1014()
        
        # Asserting that the archive file contains the expected content
        archive_file = os.path.join(refined_function.ARCHIVE_DIR, "sample_project_1.zip")
        content = os.popen(f"unzip -l {archive_file}").read()
        self.assertIn("sample_file.txt", content)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestF962Function))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()