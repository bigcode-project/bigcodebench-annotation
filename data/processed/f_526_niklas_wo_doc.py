import shutil
import os
import fnmatch
import itertools

def f_528(src_dir, dst_dir):
    """
    Copy all files from 'src_dir' to 'dst_dir' that match any pattern in ['*.txt', '*.docx'].

    Parameters:
    - src_dir (str): The source directory.
    - dst_dir (str): The destination directory.

    Returns:
    - str: The destination directory.
    
    Requirements:
    - shutil
    - os
    - fnmatch
    - itertools

    Example:
    >>> f_528('./source', './destination')
    >>> './destination'
    """
    FILE_PATTERNS = ['*.txt', '*.docx']
    matching_files = list(itertools.chain.from_iterable(
        fnmatch.filter(os.listdir(src_dir), pattern) for pattern in FILE_PATTERNS))
    for filename in matching_files:
        shutil.copy2(os.path.join(src_dir, filename), dst_dir)
    return dst_dir

import unittest
class TestCases(unittest.TestCase):
    def base(self, src_dir, dst_dir):
        if os.path.exists(src_dir):
            shutil.rmtree(src_dir)
        # Create source directory
        os.mkdir(src_dir)
        # Create destination directory
        os.mkdir(dst_dir)
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join(src_dir, filename), 'w') as f:
                f.write('test')
        # Run function
        f_528(src_dir, dst_dir)
        # Check files
        for d in [src_dir, dst_dir]:
            self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
            self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
            self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
            self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))
            self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
            self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
            if d == src_dir:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
            else:
                self.assertFalse(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertFalse(os.path.exists(os.path.join(d, 'a.doc')))
    
    def tearDown(self):
        for d in ['./source', './destination', './src', './dst', './s', './d']:
            if os.path.exists(d):
                shutil.rmtree(d)
    def test_case_1(self):
        self.base('./source', './destination')
    
    def test_case_2(self):
        self.base('./src', './dst')
    
    def test_case_3(self):
        self.base('./s', './d')
    
    def test_case_4(self):
        self.base('./s', './destination')
    def test_case_5(self):
        self.base('./source', './d')
