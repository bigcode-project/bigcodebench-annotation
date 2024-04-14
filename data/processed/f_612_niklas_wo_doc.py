import os
import shutil
import glob

def f_612(source_dir, dest_dir, extension):
    """
    Move all files with a particular extension from one directory to another.
    
    Parameters:
    - source_dir (str): The source directory.
    - dest_dir (str): The destination directory.
    - extension (str): The file extension.

    Returns:
    - result (int): The count of files that were moved. 

    Requirements:
    - os
    - shutil
    - glob
        
    Example:
    >>> f_612('path_to_source_dir', 'path_to_dest_dir', '.txt')
    10
    """
    files = glob.glob(os.path.join(source_dir, f'*.{extension}'))
    
    for file in files:
        shutil.move(file, dest_dir)
        
    result = len(files)

    return result

import unittest
class TestCases(unittest.TestCase):
    def tearDown(self):
        for d in ['./source', './destination', './src', './dst', './s', './d']:
            if os.path.exists(d):
                shutil.rmtree(d)
    def test_case_1(self):
        # Create source directory
        if os.path.exists('./source'):
            shutil.rmtree('./source')
        os.mkdir('./source')
        # Create destination directory
        if os.path.exists('./destination'):
            shutil.rmtree('./destination')
        os.mkdir('./destination')
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./source', filename), 'w') as f:
                f.write('test')
        # Run function
        f_612('./source', './destination', 'txt')
        # Check files
        for d in ['./destination', './source']:
            if d == './source':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))  
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
        # Remove files
        shutil.rmtree('./source')
        shutil.rmtree('./destination')
    def test_case_2(self):
        # Create source directory
        if os.path.exists('./src'):
            shutil.rmtree('./src')
        os.mkdir('./src')
        # Create destination directory
        if os.path.exists('./dst'):
            shutil.rmtree('./dst')
        os.mkdir('./dst')
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./src', filename), 'w') as f:
                f.write('test')
        # Run function
        f_612('./src', './dst', 'txt')
        # Check files
        for d in ['./dst', './src']:
            if d == './src':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))  
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
        # Remove files
        shutil.rmtree('./src')
        shutil.rmtree('./dst')
    def test_case_3(self):
        # Create source directory
        if os.path.exists('./s'):
            shutil.rmtree('./s')
        os.mkdir('./s')
        # Create destination directory
        if os.path.exists('./d'):
            shutil.rmtree('./d')
        os.mkdir('./d')
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./s', filename), 'w') as f:
                f.write('test')
        # Run function
        f_612('./s', './d', 'txt')
        # Check files
        for d in ['./d', './s']:
            if d == './s':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))  
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
        # Remove files
        shutil.rmtree('./s')
        shutil.rmtree('./d')
    def test_case_4(self):
        # Create source directory
        if os.path.exists('./s'):
            shutil.rmtree('./s')
        os.mkdir('./s')
        # Create destination directory
        if os.path.exists('./destination'):
            shutil.rmtree('./destination')
        os.mkdir('./destination')
        # Create files
        for filename in ['bbb.txt', 'a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./s', filename), 'w') as f:
                f.write('test')
        # Run function
        f_612('./s', './destination', 'txt')
        # Check files
        for d in ['./destination', './s']:
            if d == './s':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))  
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
        # Remove files
        shutil.rmtree('./s')
        shutil.rmtree('./destination')
    def test_case_5(self):
        # Create source directory
        if os.path.exists('./source'):
            shutil.rmtree('./source')
        os.mkdir('./source')
        # Create destination directory
        if os.path.exists('./d'):
            shutil.rmtree('./d')
        os.mkdir('./d')
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./source', filename), 'w') as f:
                f.write('xxx')
        # Run function
        f_612('./source', './d', 'docx')
        # Check files
        for d in ['./d', './source']:
            if d == './source':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))
                self.assertFalse(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertFalse(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertFalse(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
