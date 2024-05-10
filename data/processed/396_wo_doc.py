import re
import os
import glob
import natsort
import pandas as pd

def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    """
    Extract numeric data from all text files matching a given pattern in a directory and compile it into a Pandas DataFrame.

    Parameters:
    - directory (str): The directory to search for text files. Default is './'.
    - file_pattern (str): The glob pattern to match text files. Default is '*.txt'.
    - regex (str): The regular expression used to extract numeric data. Default is r'([0-9]+)'.

    Returns:
    - DataFrame: A pandas DataFrame with two columns: 'Filename' and 'Numeric Data'. Each row represents a file and its extracted numeric data.

    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    - ValueError: If no files matching the pattern are found.

    Requirements:
    - re
    - os
    - glob
    - natsort
    - pandas

    Example:
    >>> data_dir = './data/'
    >>> create_dummy_files(data_dir)
    >>> df = task_func('./data/', '*.txt', r'([0-9]+)')
    >>> tear_down_files(data_dir)
    >>> print(df)
              Filename Numeric Data
    0        empty.txt           []
    1        file1.txt   [123, 456]
    2        file2.txt        [789]
    3        mixed.txt   [123, 456]
    4  non_numeric.txt           []
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    files = natsort.natsorted(glob.glob(os.path.join(directory, file_pattern)))
    if not files:
        raise ValueError(f"No files found matching pattern '{file_pattern}' in directory '{directory}'.")
    data = []
    for filename in files:
        with open(filename, 'r') as file:
            content = file.read()
        numeric_data = re.findall(regex, content)
        data.append([os.path.basename(filename), numeric_data])
    df = pd.DataFrame(data, columns=['Filename', 'Numeric Data'])
    return df

import unittest
import pandas as pd
import os
def create_dummy_files(data_dir):
    os.makedirs(data_dir, exist_ok=True)
    # Creating test files
    test_files_data = {
        'file1.txt': '123 abc 456',
        'file2.txt': '789 xyz',
        'empty.txt': '',
        'non_numeric.txt': 'abc def',
        'mixed.txt': 'abc 123 def 456'
    }
    for filename, content in test_files_data.items():
        with open(data_dir + filename, 'w') as file:
            file.write(content)
def tear_down_files(data_dir):
    for filename in os.listdir(data_dir):
        os.remove(os.path.join(data_dir, filename))
    os.rmdir(data_dir)
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = './test_data/'
        os.makedirs(self.test_data_dir, exist_ok=True)
        # Creating test files
        test_files_data = {
            'file1.txt': '123 abc 456',
            'file2.txt': '789 xyz',
            'empty.txt': '',
            'non_numeric.txt': 'abc def',
            'mixed.txt': 'abc 123 def 456'
        }
        for filename, content in test_files_data.items():
            with open(self.test_data_dir + filename, 'w') as file:
                file.write(content)
    def tearDown(self):
        for filename in os.listdir(self.test_data_dir):
            os.remove(os.path.join(self.test_data_dir, filename))
        os.rmdir(self.test_data_dir)
    def test_normal_functionality(self):
        df = task_func(self.test_data_dir)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 5)  # Number of files
        self.assertIn('123', df.loc[df['Filename'] == 'file1.txt', 'Numeric Data'].values[0])
        df_list = df.apply(lambda row: ','.join(str(e) for e in row), axis=1).tolist()
        # Write the DataFrame to a file for inspection
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(df_list))
        expect = ['empty.txt,[]', "file1.txt,['123', '456']", "file2.txt,['789']", "mixed.txt,['123', '456']", 'non_numeric.txt,[]']
        self.assertEqual(df_list, expect)
    def test_directory_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            task_func('./nonexistent_directory/')
    def test_no_matching_files(self):
        with self.assertRaises(ValueError):
            task_func(self.test_data_dir, '*.csv')
    def test_empty_file(self):
        df = task_func(self.test_data_dir)
        self.assertEqual([], df.loc[df['Filename'] == 'empty.txt', 'Numeric Data'].values[0])
    def test_mixed_content_file(self):
        df = task_func(self.test_data_dir)
        self.assertIn('123', df.loc[df['Filename'] == 'mixed.txt', 'Numeric Data'].values[0])
        self.assertIn('456', df.loc[df['Filename'] == 'mixed.txt', 'Numeric Data'].values[0])
