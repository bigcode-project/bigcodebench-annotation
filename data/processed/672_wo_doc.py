import csv
import sys

def task_func(filename):
    """
    Read a CSV file, inverse the order of the lines and write the inverted lines back into the file. Then reset the cursor to the beginning of the file.

    Parameters:
    - filename (str): The name of the CSV file.

    Returns:
    - filename (str): The name of the CSV file.

    Requirements:
    - csv
    - sys

    Example:
    >>> task_func('file.csv')
    'file.csv'
    """
    try:
        with open(filename, 'r+') as file:
            reader = csv.reader(file)
            rows = list(reader)
            file.seek(0)
            file.truncate()
            writer = csv.writer(file)
            writer.writerows(reversed(rows))
            file.seek(0)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
    return filename

import unittest
import os
class TestCases(unittest.TestCase):
    def base(self, filename, contents, expected):
        # Create file
        with open(filename, 'w') as file:
            file.write(contents)
        # Run function
        task_func(filename)
        # Check file
        with open(filename, 'r') as file:
            txt = file.read()
            self.assertEqual(txt, expected)
        # Remove file
        os.remove(filename)
    def test_case_1(self):
        self.base('file.csv', "a,b\nc,d\ne,f\ng,h\n", "g,h\ne,f\nc,d\na,b\n")
    
    def test_case_2(self):
        self.base('file.csv', "a,b,c\nd,e,f\ng,h,i\n", "g,h,i\nd,e,f\na,b,c\n")
    def test_case_3(self):
        self.base('file.csv', "a,b,c,d\ne,f,g,h\ni,j,k,l\n", "i,j,k,l\ne,f,g,h\na,b,c,d\n")
    
    def test_case_4(self):
        self.base('file.csv', "a,b,c,d,e\nf,g,h,i,j\nk,l,m,n,o\n", "k,l,m,n,o\nf,g,h,i,j\na,b,c,d,e\n")
    def test_case_5(self):
        self.base('file.csv', "a,b,c,d,e,f\ng,h,i,j,k,l\nm,n,o,p,q,r\n", "m,n,o,p,q,r\ng,h,i,j,k,l\na,b,c,d,e,f\n")
