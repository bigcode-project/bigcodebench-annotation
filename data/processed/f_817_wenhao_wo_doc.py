import shutil
import pathlib


def f_409(source_path, destination_path):
    """
    Lists files in the specified source directory without descending into subdirectories and copies them to a
    destination directory.

    Parameters:
    - source_path (str):      The source directory path to analyze. Must be an existing, accessible directory.
    - destination_path (str): The destination directory path where files will be copied.
                              If it does not exist, this function will create it.

    Returns:
    Tuple[str, List[str]]: A tuple containing the name of the source directory and a list of filenames (not
                           full paths) that were copied.

    Raises:
    - ValueError: If source_path does not exist or is not a directory.

    Requirements:
    - shutil
    - pathlib

    Example:
    >>> x = f_409('/Docs/src/Scripts')
    >>> type(x)
    <class 'tuple'>
    >>> x
    ('Scripts', ['file_1_in_scripts_dir.txt', 'file_2_in_scripts_dir.txt'])
    """
    source_path = pathlib.Path(source_path).resolve()
    destination_path = pathlib.Path(destination_path).resolve()
    if not (source_path.exists() and source_path.is_dir()):
        raise ValueError("source_path must be an existing directory.")
    destination_path.mkdir(parents=True, exist_ok=True)
    results = []
    for entry in source_path.iterdir():
        if entry.is_file():
            results.append(str(entry.name))
            shutil.copy(str(entry), str(destination_path))
    return (source_path.name, results)

import unittest
import tempfile
import pathlib
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_source_dir = pathlib.Path(self.temp_dir.name) / "testf817-source"
        self.test_target_dir = pathlib.Path(self.temp_dir.name) / "testf817-target"
        self.test_source_dir.mkdir(parents=True, exist_ok=True)
        self.test_target_dir.mkdir(parents=True, exist_ok=True)
    def tearDown(self):
        self.temp_dir.cleanup()
    def create_files(self, paths):
        for path in paths:
            full_path = self.test_source_dir / path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.touch()
    def test_case_1(self):
        # Test empty directory
        target_dir_before = list(self.test_target_dir.iterdir())
        result = f_409(str(self.test_source_dir), str(self.test_target_dir))
        target_dir_after = list(self.test_target_dir.iterdir())
        self.assertEqual(result, ("testf817-source", []))
        self.assertEqual(target_dir_before, target_dir_after)
    def test_case_2(self):
        # Test directory with one file
        self.create_files(["file1.txt"])
        result = f_409(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(result, ("testf817-source", ["file1.txt"]))
        # Check if files are copied correctly
        self.assertEqual(
            list(self.test_target_dir.iterdir()), [self.test_target_dir / "file1.txt"]
        )
    def test_case_3(self):
        # Test directory with multiple files
        self.create_files(["file1.txt", "file2.txt", "file3.txt"])
        result = f_409(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "testf817-source")
        self.assertEqual(
            sorted(result[1]), sorted(["file1.txt", "file2.txt", "file3.txt"])
        )
        self.assertEqual(
            sorted(self.test_target_dir.iterdir()),
            sorted(
                [
                    self.test_target_dir / "file1.txt",
                    self.test_target_dir / "file2.txt",
                    self.test_target_dir / "file3.txt",
                ]
            ),
        )
    def test_case_4(self):
        # Test directory with subdirectories
        self.test_source_dir.joinpath("subdir1").mkdir()
        self.create_files(["file1.txt", "file2.txt"])
        self.create_files(["subdir1/file3.txt"])  # File inside subdirectory
        result = f_409(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "testf817-source")
        self.assertEqual(sorted(result[1]), sorted(["file1.txt", "file2.txt"]))
        # Check if files in subdirectories are ignored and only files in the source directory are copied
        self.assertEqual(
            sorted(self.test_target_dir.iterdir()),
            sorted(
                [self.test_target_dir / "file1.txt", self.test_target_dir / "file2.txt"]
            ),
        )
    def test_case_5(self):
        # Test non-existent source directory
        with self.assertRaises(ValueError):
            f_409(str(self.test_source_dir / "nonexistent"), str(self.test_target_dir))
    def test_case_6(self):
        # Test non-existent destination directory
        shutil.rmtree(self.test_target_dir)
        result = f_409(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(result, ("testf817-source", []))
        # Check if destination directory is created
        self.assertTrue(self.test_target_dir.exists())
    def test_case_7(self):
        # Test copying files to existing destination directory
        self.create_files(["file1.txt", "file2.txt"])
        result = f_409(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(sorted(result[1]), sorted(["file1.txt", "file2.txt"]))
        # Call the function again
        self.create_files(["file3.txt", "file4.txt"])
        result = f_409(str(self.test_source_dir), str(self.test_target_dir))
        # There should now be 4 files in the directory
        self.assertEqual(
            sorted(self.test_source_dir.iterdir()),
            sorted(
                [
                    self.test_source_dir / "file1.txt",
                    self.test_source_dir / "file2.txt",
                    self.test_source_dir / "file3.txt",
                    self.test_source_dir / "file4.txt",
                ]
            ),
        )
        # which means 4 files should have been copied
        self.assertEqual(
            sorted(result[1]),
            sorted(["file1.txt", "file2.txt", "file3.txt", "file4.txt"]),
        )
        # and 4 files should be in the destination
        self.assertEqual(
            sorted(self.test_target_dir.iterdir()),
            sorted(
                [
                    self.test_target_dir / "file1.txt",
                    self.test_target_dir / "file2.txt",
                    self.test_target_dir / "file3.txt",
                    self.test_target_dir / "file4.txt",
                ]
            ),
        )
