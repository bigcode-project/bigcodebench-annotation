import pandas as pd
import numpy as np


def f_694(file_path, num_rows, data_dimensions=5, random_seed=None):
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
    >>> f_694('/tmp/data.csv', 100)
    '/tmp/data.csv'

    >>> f_694('test.csv'), 5, 2, random_seed=42)
    'test.csv'
    >>> pd.read_csv('test.csv)
        Feature_1	Feature_2
    0	0.154163	0.740050
    1	0.918747	0.900715
    2	0.283828	0.606083
    3	0.521226	0.552038
    4	0.764560	0.020810

    """
    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.rand(num_rows, data_dimensions), 
                      columns=[f'Feature_{i+1}' for i in range(data_dimensions)])

    df.to_csv(file_path, index=False)

    return file_path

import unittest
import os
import pandas as pd
import shutil


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    
    def setUp(self) -> None:
        os.makedirs('testing_694', exist_ok=True)

    def tearDown(self) -> None:
        shutil.rmtree('testing_694')

    def test_rng(self):
        path1 = f_694(os.path.join('testing_694', 'test_data_1.csv'), 10, random_seed=1)
        path2 = f_694(os.path.join('testing_694', 'test_data_2.csv'), 10, random_seed=1)

        df1 = pd.read_csv(path1)
        df2 = pd.read_csv(path2)
        pd.testing.assert_frame_equal(df1, df2)

    def test_case_1(self):
        # Test with default data dimensions and 400 rows
        file_path = f_694(os.path.join('testing_694', 'test_data_1.csv'), 400, random_seed=12)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        expected = pd.read_csv(os.path.join('f_694_data_simon', 'test_data_1.csv'))

        pd.testing.assert_frame_equal(df, expected)

    def test_case_2(self):
        # Test with custom data dimensions (7) and 100 rows
        file_path = f_694(os.path.join('testing_694', 'test_data_2.csv'), 100, 7, random_seed=21)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        expected = pd.read_csv(os.path.join('f_694_data_simon', 'test_data_2.csv'))
        pd.testing.assert_frame_equal(df, expected)
    
    def test_case_3(self):
        # Test with custom data dimensions (3) and 0 rows
        file_path = f_694(os.path.join('testing_694', 'test_data_3.csv'), 0, 3, random_seed=42)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        expected = pd.read_csv(os.path.join('f_694_data_simon', 'test_data_3.csv'))
        pd.testing.assert_frame_equal(df, expected)
    
    def test_case_4(self):
        # 0 rows
        file_path = f_694(os.path.join('testing_694', 'test_data_4.csv'), 1, 0)
        self.assertTrue(os.path.exists(file_path))
        csv = np.loadtxt(os.path.join('testing_694', 'test_data_4.csv'))        
        self.assertEqual(len(csv), 0)

if __name__ == "__main__":
    run_tests()