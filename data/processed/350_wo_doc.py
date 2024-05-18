import subprocess
import os
import shutil
from glob import glob


def task_func(src_folder, dst_folder):
    """Compress all files in the specified source folder and move the compressed files to a destination folder.
    This operation is executed as a background process using the 'gzip' command.

    Parameters:
    src_folder (str): The path of the source folder containing the files to be compressed.
    dst_folder (str): The path of the destination folder where the compressed files will be moved.

    Returns:
    dict: A dictionary containing:
        - 'success': A boolean indicating if all files were compressed and moved successfully.
        - 'message': A descriptive message about the operation's result.
        - 'failed_files': A list of filenames that failed to compress or move.

    Requirements:
    - subprocess
    - os
    - shutil
    - glob
    - gzip

    Example:
    >>> import tempfile
    >>> import os
    >>> src_folder = tempfile.mkdtemp()
    >>> dst_folder = tempfile.mkdtemp()
    >>> for i in range(3):
    ...     with open(os.path.join(src_folder, f'file{i}.txt'), 'w') as f:
    ...         _ = f.write(f'This is file {i}.')
    >>> task_func(src_folder, dst_folder)
    {'success': True, 'message': 'All files compressed and moved successfully.', 'failed_files': []}
    """
    if not os.path.isdir(src_folder):
        raise ValueError(f"Source folder '{src_folder}' does not exist.")
    if not os.path.isdir(dst_folder):
        raise ValueError(f"Destination folder '{dst_folder}' does not exist.")
    processes = []
    failed_files = []
    for file in glob(os.path.join(src_folder, '*')):
        process = subprocess.Popen(['gzip', file])
        processes.append((process, file))
    for process, file in processes:
        retcode = process.wait()
        if retcode != 0:
            failed_files.append(os.path.basename(file))
    for file in glob(os.path.join(src_folder, '*.gz')):
        try:
            shutil.move(file, dst_folder)
        except Exception as e:
            failed_files.append(os.path.basename(file))
    if failed_files:
        return {'success': False, 'message': 'Some files failed to compress or move.', 'failed_files': failed_files}
    else:
        return {'success': True, 'message': 'All files compressed and moved successfully.', 'failed_files': []}

import unittest
import doctest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.base_tmp_dir = tempfile.mkdtemp()
        self.src_folder_path = f"{self.base_tmp_dir}/test/source_folder"
        self.dst_folder_path = f"{self.base_tmp_dir}/test/destination_folder"
        
        # Reset the test folders before each test
        os.makedirs(self.src_folder_path, exist_ok=True)
        os.makedirs(self.dst_folder_path, exist_ok=True)
        # Create source and destination folders if they don't exist
        os.makedirs(self.src_folder_path, exist_ok=True)
        os.makedirs(self.dst_folder_path, exist_ok=True)
        # Create some sample files in the source folder
        self.file_contents = ["This is file 1.", "This is file 2.", "This is file 3."]
        file_paths = []
        for idx, content in enumerate(self.file_contents, 1):
            file_path = os.path.join(self.src_folder_path, f"file{idx}.txt")
            with open(file_path, "w") as file:
                file.write(content)
            file_paths.append(file_path)
    def tearDown(self):
        # Reset the test folders after each test
        if os.path.exists(self.base_tmp_dir):
            shutil.rmtree(self.base_tmp_dir, ignore_errors=True)
    def test_case_1(self):
        """Test basic functionality."""
        # Create some sample files in the source folder
        for idx, content in enumerate(self.file_contents, 1):
            file_path = os.path.join(self.src_folder_path, f"file{idx}.txt")
            with open(file_path, "w") as file:
                file.write(content)
        
        result = task_func(self.src_folder_path, self.dst_folder_path)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'All files compressed and moved successfully.')
        self.assertEqual(result['failed_files'], [])
        for idx in range(1, 4):
            self.assertTrue(os.path.exists(os.path.join(self.dst_folder_path, f"file{idx}.txt.gz")))
    def test_case_2(self):
        """Test non-existent source folder."""
        with self.assertRaises(ValueError) as context:
            task_func("/non/existent/path", self.dst_folder_path)
        self.assertEqual(str(context.exception), "Source folder '/non/existent/path' does not exist.")
    def test_case_3(self):
        """Test non-existent destination folder."""
        with self.assertRaises(ValueError) as context:
            task_func(self.src_folder_path, "/non/existent/path")
        self.assertEqual(str(context.exception), "Destination folder '/non/existent/path' does not exist.")
    def test_case_4(self):
        """Test empty source folder."""
        result = task_func(self.src_folder_path, self.dst_folder_path)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'All files compressed and moved successfully.')
        self.assertEqual(result['failed_files'], [])
    
    def test_case_5(self):
        """Test with destination folder having some files."""
        # Create some files in the destination folder
        with open(os.path.join(self.dst_folder_path, "existing_file.txt"), "w") as file:
            file.write("This is an existing file.")
        with open(os.path.join(self.dst_folder_path, "existing_file.txt.gz"), "w") as file:
            file.write("This is an existing compressed file.")
        
        # Create some sample files in the source folder
        for idx, content in enumerate(self.file_contents, 1):
            file_path = os.path.join(self.src_folder_path, f"file{idx}.txt")
            with open(file_path, "w") as file:
                file.write(content)
        
        result = task_func(self.src_folder_path, self.dst_folder_path)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'All files compressed and moved successfully.')
        self.assertEqual(result['failed_files'], [])
        for idx in range(1, 4):
            self.assertTrue(os.path.exists(os.path.join(self.dst_folder_path, f"file{idx}.txt.gz")))
        self.assertTrue(os.path.exists(os.path.join(self.dst_folder_path, "existing_file.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.dst_folder_path, "existing_file.txt.gz")))
