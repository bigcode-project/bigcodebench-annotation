import pandas as pd
import os

def task_func(filename):
    """
    Read a CSV file of pandas, reverse the order of the lines and write the inverted lines back into the file. Then move the cursor back to the beginning of the file. 
    The header should not be inverted and the file may be empty.

    Parameters:
    - filename (str): The name of the CSV file.

    Returns:
    - filename (str): The name of the CSV file.

    Requirements:
    - os
    - pandas

    Example:
    >>> task_func('file.csv')
    'file.csv'
    """
    if not os.path.exists(filename):
        return filename
    with open(filename, 'r') as file:
        if not file.read(1):
            return filename
    df = pd.read_csv(filename)
    df = df.iloc[::-1]
    df.to_csv(filename, index=False)
    with open(filename, 'r+') as file:
        file.seek(0)
    return filename

import unittest
class TestCases(unittest.TestCase):
    def base(self, filename, contents, expected):
        # Create file
        with open(filename, 'w') as f:
            f.write(contents)
        # Run function
        task_func(filename)
        # Check file
        with open(filename, 'r') as f:
            self.assertEqual(f.read().strip(), expected.strip())
        # Remove file
        os.remove(filename)
    def test_case_1(self):
        self.base('file.csv', 'a,b,c\n1,2,3\n4,5,6\n7,8,9', 'a,b,c\n7,8,9\n4,5,6\n1,2,3')
    def test_case_2(self):
        self.base('file.csv', 'a,b,c\n1,2,3\n4,5,6', 'a,b,c\n4,5,6\n1,2,3')
    def test_case_3(self):
        self.base('file.csv', 'a,b,c\n1,2,3', 'a,b,c\n1,2,3')
    def test_case_4(self):
        self.base('file.csv', 'a,b,c', 'a,b,c')
    def test_case_5(self):
        self.base('file.csv', '', '')
