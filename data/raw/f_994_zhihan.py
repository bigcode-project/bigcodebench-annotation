import os
import glob
import hashlib

def f_994(source_dir=SOURCE_DIR, target_dir=TARGET_DIR, prefix=PREFIX):
    """
    Compute the MD5 hash of each file's content in the provided `source_dir`, prepend the computed hash to the original content,
    and write the modified content to a new file in the provided `target_dir`. Existing files with the same name in the `target_dir` will be overwritten.
    
    Parameters:
    - source_dir (str): The source directory containing the files to be hashed. Default is 'source'.
    - target_dir (str): The target directory where the hashed files will be written. Default is 'target'.
    - prefix (str): The line to prepend before the hash in the new files. Default is '#Hash: '.
    
    Returns:
    - list: A list of paths to the newly created files in the `target_dir`.
    
    Requirements:
    - os
    - glob
    - hashlib
    
    Example:
    >>> f_868(source_dir='samples', target_dir='hashed_samples')
    ['hashed_samples/file1.txt', 'hashed_samples/file2.txt']
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    new_files = []
    for file in glob.glob(source_dir + '/*'):
        with open(file, 'r') as infile:
            content = infile.read()
        hash_object = hashlib.md5(content.encode())
        new_file_path = os.path.join(target_dir, os.path.basename(file))
        with open(new_file_path, 'w') as outfile:
            outfile.write(prefix + hash_object.hexdigest() + '\n' + content)
        new_files.append(new_file_path)
    return new_files

import unittest
import os
import hashlib

SOURCE_DIR = 'source'
TARGET_DIR = 'target'
PREFIX = '#Hash: '

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Using default directories and prefix
        result = f_868(source_dir='samples', target_dir='hashed_samples')
        expected_files = [os.path.join('hashed_samples', file_name) for file_name in ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']]
        self.assertListEqual(result, expected_files)
        for file in expected_files:
            with open(file, 'r') as f:
                lines = f.readlines()
                self.assertTrue(lines[0].startswith(PREFIX))
                self.assertEqual(''.join(lines[1:]), file_contents[os.path.basename(file)])
    
    def test_case_2(self):
        # Using custom prefix
        custom_prefix = "MD5Hash: "
        result = f_868(source_dir='samples', target_dir='hashed_samples', prefix=custom_prefix)
        for file in result:
            with open(file, 'r') as f:
                lines = f.readlines()
                self.assertTrue(lines[0].startswith(custom_prefix))
    
    def test_case_3(self):
        # Using empty directory
        empty_dir = "/mnt/data/empty_samples"
        os.makedirs(empty_dir, exist_ok=True)
        result = f_868(source_dir=empty_dir, target_dir='hashed_samples')
        self.assertEqual(result, [])
    
    def test_case_4(self):
        # Using non-existing source directory
        non_existing_dir = "/mnt/data/non_existing"
        with self.assertRaises(FileNotFoundError):
            f_868(source_dir=non_existing_dir, target_dir='hashed_samples')
    
    def test_case_5(self):
        # Overwriting existing files in target directory
        initial_content = "Initial content."
        with open(os.path.join('hashed_samples', "file1.txt"), 'w') as f:
            f.write(initial_content)
        result = f_868(source_dir='samples', target_dir='hashed_samples')
        with open(os.path.join('hashed_samples', "file1.txt"), 'r') as f:
            self.assertNotEqual(f.read(), initial_content)
if __name__ == "__main__":
    run_tests()