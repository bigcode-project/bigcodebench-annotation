import os
from pathlib import Path
import shutil
import zipfile

# Constants
BASE_DIR = Path.cwd()

def f_976(source_dir, target_dir, archive_name):
    """
    Move all files from a source directory to a target directory and create a zip archive of the target directory.

    Parameters:
    - source_dir (str): The source directory path relative to the current working directory.
    - target_dir (str): The target directory path relative to the current working directory.
    - archive_name (str): The name of the zip archive without the file extension.

    Returns:
    - str: The absolute path to the created zip archive.

    Requirements:
    - os
    - pathlib.Path
    - shutil
    - zipfile

    Data Structures:
    - Directories and files are manipulated using the pathlib.Path library.

    Examples:
    >>> f_976('sample_source', 'sample_target', 'archive_name')
    'absolute/path/to/archive_name.zip'
    """
    source_dir = BASE_DIR / source_dir
    target_dir = BASE_DIR / target_dir
    archive_path = BASE_DIR / f"{archive_name}.zip"

    for file_name in os.listdir(str(source_dir)):
        shutil.move(str(source_dir / file_name), str(target_dir))

    with zipfile.ZipFile(str(archive_path), 'w') as zipf:
        for root, dirs, files in os.walk(str(target_dir)):
            for file in files:
                zipf.write(os.path.join(root, file))

    return str(archive_path)

import unittest
import tempfile
import os


temp_dir = tempfile.mkdtemp()


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create mock directories and files for testing
        cls.source_dir_path = os.path.join(temp_dir, "source_dir")
        cls.target_dir_path = os.path.join(temp_dir, "target_dir")
        os.makedirs(cls.source_dir_path, exist_ok=True)
        os.makedirs(cls.target_dir_path, exist_ok=True)
        for i in range(5):
            with open(os.path.join(cls.source_dir_path, f"file_{i}.txt"), "w") as f:
                f.write(f"Content of file_{i}.txt")

    def test_case_1(self):
        archive_name = "test_archive_1"
        archive_path = f_976(self.source_dir_path, self.target_dir_path, archive_name)
        self.assertTrue(os.path.exists(archive_path))
        self.assertTrue(archive_name in archive_path)

    def test_case_2(self):
        archive_name = "test_archive_2"
        archive_path = f_976(self.source_dir_path, self.target_dir_path, archive_name)
        self.assertTrue(os.path.exists(archive_path))
        self.assertTrue(archive_name in archive_path)

    def test_case_3(self):
        archive_name = "test_archive_3"
        archive_path = f_976(self.source_dir_path, self.target_dir_path, archive_name)
        self.assertTrue(os.path.exists(archive_path))
        self.assertTrue(archive_name in archive_path)

    def test_case_4(self):
        archive_name = "test_archive_4"
        archive_path = f_976(self.source_dir_path, self.target_dir_path, archive_name)
        self.assertTrue(os.path.exists(archive_path))
        self.assertTrue(archive_name in archive_path)

    def test_case_5(self):
        archive_name = "test_archive_5"
        archive_path = f_976(self.source_dir_path, self.target_dir_path, archive_name)
        self.assertTrue(os.path.exists(archive_path))
        self.assertTrue(archive_name in archive_path)
if __name__ == "__main__":
    run_tests()