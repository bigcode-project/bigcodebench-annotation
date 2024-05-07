import pandas as pd
import numpy as np


def f_637(file_path, num_rows, data_dimensions=5, random_seed=None):
    """
    Creates a CSV file on a given file path with random numeric data. 
    The number of rows in the CSV file is determined by the 'num_rows' parameter, 
    and the number of columns (features) is determined by the 'data_dimensions' parameter.
    Columns are named following the convention: 'Feature_x', where x is the number of the 
    feature column starting at 1.

    Parameters:
    file_path (str): The file path where the CSV file should be created.
    num_rows (int): The number of rows of random data to generate.
    data_dimensions (int, optional): The number of columns (features) in the CSV file. Defaults to 5.
    random_seed (int, optional): Seed used in rng. Defaults to None.
    
    Returns:
    str: The file path of the generated CSV file.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> f_637('/tmp/data.csv', 100)
    '/tmp/data.csv'
    """
    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.rand(num_rows, data_dimensions),
                      columns=[f'Feature_{i + 1}' for i in range(data_dimensions)])
    df.to_csv(file_path, index=False)
    return file_path

import unittest
import os
import pandas as pd
import shutil
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for each test case
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Remove the temporary directory after each test
        shutil.rmtree(self.test_dir)
    def test_basic_functionality(self):
        # Test with default parameters
        file_path = f_637(os.path.join(self.test_dir, 'data.csv'), 100)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 100)
        self.assertEqual(len(df.columns), 5)
    def test_custom_dimensions(self):
        # Test with custom dimensions
        file_path = f_637(os.path.join(self.test_dir, 'data_custom.csv'), 50, 7)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 50)
        self.assertEqual(len(df.columns), 7)
    def test_empty_file(self):
        # Test generating an empty file
        file_path = f_637(os.path.join(self.test_dir, 'empty.csv'), 0, 5)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 0)
    def test_random_seed(self):
        # Test reproducibility with a random seed
        file_path1 = f_637(os.path.join(self.test_dir, 'data_seed.csv'), 20, 5, 42)
        file_path2 = f_637(os.path.join(self.test_dir, 'data_seed.csv'), 20, 5, 42)
        df1 = pd.read_csv(file_path1)
        df2 = pd.read_csv(file_path2)
        pd.testing.assert_frame_equal(df1, df2)
    def test_no_columns(self):
        # Test with zero columns
        file_path = f_637(os.path.join(self.test_dir, 'no_columns.csv'), 10, 0)
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            data = file.read()
        # Expect the file to contain only the headers or be empty
        self.assertTrue(data == '' or all([x.strip() == '' for x in data.split(',')]))
