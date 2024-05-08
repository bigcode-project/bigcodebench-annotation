import configparser
import os
import shutil


def f_476(config_file_path, archieve_dir ='/home/user/archive'):
    """
    Archive a specified project directory into a ZIP file based on the configuration specified in a config file.
    
    This function reads a configuration file to determine the project directory and archives this directory into a ZIP file.
    The ZIP file's name will be the project directory's basename, stored in the specified archive directory.
    
    Configuration File Format:
    [Project]
    directory=path_to_project_directory
    
    Parameters:
    - config_file_path (str): Path to the configuration file. The file must exist and be readable.
    - archive_dir (str, optional): Path to the directory where the ZIP archive will be stored. Defaults to '/home/user/archive'.
    
    Returns:
    - bool: True if the ZIP archive is successfully created, otherwise an exception is raised.
    
    Requirements:
    - configparse
    - os
    - shutil

    Raises:
    - FileNotFoundError: If the `config_file_path` does not exist or the specified project directory does not exist.
    - Exception: If the ZIP archive cannot be created.
    
    Example:
    >>> f_476("/path/to/config.ini")
    True
    """
    config = configparser.ConfigParser()
    config.read(config_file_path)
    project_dir = config.get('Project', 'directory')
    if not os.path.isdir(project_dir):
        raise FileNotFoundError(f'Directory {project_dir} does not exist.')
    archive_file = f'{archieve_dir}/{os.path.basename(project_dir)}.zip'
    shutil.make_archive(base_name=os.path.splitext(archive_file)[0], format='zip', root_dir=project_dir)
    if not os.path.isfile(archive_file):
        raise Exception(f"Failed to create archive {archive_file}")
    return True

import unittest
import tempfile
import shutil
import os
import configparser
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory for the configuration files and another for the archive output
        self.test_data_dir = tempfile.mkdtemp()
        self.archive_dir = tempfile.mkdtemp()
        # Example valid configuration file setup
        self.valid_config_path = os.path.join(self.test_data_dir, "valid_config.ini")
        config = configparser.ConfigParser()
        config['Project'] = {'directory': self.test_data_dir}
        with open(self.valid_config_path, 'w') as configfile:
            config.write(configfile)
        # Invalid directory config
        self.invalid_config_path = os.path.join(self.test_data_dir, "invalid_config.ini")
        config['Project'] = {'directory': '/path/to/nonexistent/directory'}
        with open(self.invalid_config_path, 'w') as configfile:
            config.write(configfile)
    def tearDown(self):
        # Remove temporary directories after each test
        shutil.rmtree(self.test_data_dir)
        shutil.rmtree(self.archive_dir)
    def test_valid_project_directory(self):
        # Testing with a valid project directory
        result = f_476(self.valid_config_path, self.archive_dir)
        self.assertTrue(result)
    def test_invalid_project_directory(self):
        # Testing with a non-existent project directory
        with self.assertRaises(FileNotFoundError):
            f_476(self.invalid_config_path, self.archive_dir)
    def test_archive_creation(self):
        # Run the function to create the archive
        f_476(self.valid_config_path, self.archive_dir)
        archive_file = os.path.join(self.archive_dir, os.path.basename(self.test_data_dir) + '.zip')
        self.assertTrue(os.path.isfile(archive_file))
    def test_archive_content(self):
        # Adding a sample file to the project directory to check archive contents later
        sample_file_path = os.path.join(self.test_data_dir, "sample_file.txt")
        with open(sample_file_path, 'w') as f:
            f.write("Hello, world!")
        f_476(self.valid_config_path, self.archive_dir)
        archive_file = os.path.join(self.archive_dir, os.path.basename(self.test_data_dir) + '.zip')
        content = os.popen(f"unzip -l {archive_file}").read()
        self.assertIn("sample_file.txt", content)
