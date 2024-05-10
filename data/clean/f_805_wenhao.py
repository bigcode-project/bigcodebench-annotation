import os
from pathlib import Path
import glob
import shutil


def f_805(source_directory: str, target_directory: str):
    """
    Moves files with specific extensions from a source directory to a target directory,
    handling naming conflicts by renaming duplicates.

    Parameters:
    - source_directory (str): The absolute or relative path of the source directory.
    - target_directory (str): The absolute or relative path of the target directory.
                              This function will create it if it does not exist.

    Returns:
    - int: The number of files successfully moved.

    Raises:
    - FileNotFoundError: If source_directory does not exist.

    Requirements:
    - os
    - pathlib
    - glob
    - shutil

    Notes:
    - This function scans the source directory recursively to find files.
    - Files are filtered by the extensions: ".txt", ".docx", ".xlsx", ".csv".
    - Renaming of files due to naming conflicts follows the pattern '<original_name>-n.<extension>'.

    Examples:
    >>> f_805('./source_folder', './target_folder')
    3
    >>> f_805('./empty_folder', './target_folder')
    0
    """
    moved_files = 0

    if not os.path.exists(source_directory):
        raise FileNotFoundError("source_directory must exist.")

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for extension in [".txt", ".docx", ".xlsx", ".csv"]:
        filepaths = glob.glob(
            os.path.join(source_directory, "**", "*" + extension), recursive=True
        )
        for filepath in filepaths:
            filename = Path(filepath).name
            stem = Path(filepath).stem
            target_filepath = os.path.join(target_directory, filename)

            count = 1
            while os.path.exists(target_filepath):
                new_filename = f"{stem}-{count}{extension}"
                target_filepath = os.path.join(target_directory, new_filename)
                count += 1

            shutil.move(filepath, target_filepath)
            moved_files += 1

    return moved_files


import unittest
import tempfile
from pathlib import Path


class TestCases(unittest.TestCase):
    def setUp(self):
        self.valid_extensions = [".txt", ".docx", ".xlsx", ".csv"]

    def test_case_1(self):
        # Test with an empty source directory
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            result = f_805(source_dir, target_dir)
            self.assertEqual(
                result, 0, "Should return 0 for an empty source directory."
            )

    def test_case_2(self):
        # Test with a source directory containing only files with no extensions
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            for i in range(3):
                Path(f"{source_dir}/file_{i}").touch()
            result = f_805(source_dir, target_dir)
            self.assertEqual(
                result, 0, "Should return 0 for files with non-matching extensions."
            )

    def test_case_3(self):
        # Test with a source directory containing files with a mix of extensions
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            extensions = self.valid_extensions + [".pdf", ".jpg"]
            for i, ext in enumerate(extensions):
                Path(f"{source_dir}/file_{i}{ext}").touch()
            result = f_805(source_dir, target_dir)
            self.assertTrue(result == len(self.valid_extensions))

    def test_case_4(self):
        # Test with a source directory containing files with all matching extensions
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            for i, ext in enumerate(self.valid_extensions):
                Path(f"{source_dir}/file_{i}{ext}").touch()
            result = f_805(source_dir, target_dir)
            self.assertEqual(
                result, 4, "Should return 4 for all files with matching extensions."
            )

    def test_case_5(self):
        # Test with a source directory containing nested directories with files
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            extensions = [".txt", ".docx", ".xlsx", ".csv"]
            Path(f"{source_dir}/subdir1").mkdir()
            Path(f"{source_dir}/subdir1/subdir2").mkdir()
            for i, ext in enumerate(extensions):
                Path(f"{source_dir}/file_{i}{ext}").touch()
                Path(f"{source_dir}/subdir1/file_{i}{ext}").touch()
                Path(f"{source_dir}/subdir1/subdir2/file_{i}{ext}").touch()
            result = f_805(source_dir, target_dir)
            self.assertEqual(
                result,
                12,
                "Should return 12 for all files in nested directories with matching extensions.",
            )

    def test_case_6(self):
        # Test files with the same name in different subdirectories of the source directory
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            Path(f"{source_dir}/subdir1").mkdir()
            Path(f"{source_dir}/subdir2").mkdir()
            extensions = [".txt", ".docx", ".xlsx", ".csv"]
            # Create files with the same name in different subdirectories
            for ext in extensions:
                (Path(f"{source_dir}/subdir1") / f"file{ext}").touch()
                (Path(f"{source_dir}/subdir2") / f"file{ext}").touch()
            result = f_805(source_dir, target_dir)
            self.assertEqual(
                result,
                8,
                "Should correctly move files with the same name from different source directories.",
            )

    def test_case_7(self):
        # Test handling of invalid path inputs
        source_dir = "/path/does/not/exist"
        with tempfile.TemporaryDirectory() as target_dir:
            with self.assertRaises(FileNotFoundError):
                f_805(source_dir, target_dir)

    def test_case_8(self):
        # Test file renaming when handling duplicate files
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            extensions = self.valid_extensions
            for i, ext in enumerate(extensions):
                filename = f"file_{i}{ext}"
                # Create duplicate files in the source directory
                Path(os.path.join(source_dir, filename)).touch()
                # Create expected duplicate files in the target directory to force renaming
                Path(os.path.join(target_dir, filename)).touch()

            result = f_805(source_dir, target_dir)
            self.assertEqual(result, len(extensions), "Should have moved all files.")

            # Check if files were renamed correctly to avoid overwriting
            expected_files = [f"file_{i}-1{ext}" for i, ext in enumerate(extensions)]
            actual_files = [Path(f).name for f in glob.glob(f"{target_dir}/*")]

            for expected_file in expected_files:
                self.assertIn(
                    expected_file,
                    actual_files,
                    f"{expected_file} was not found in target directory.",
                )


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
