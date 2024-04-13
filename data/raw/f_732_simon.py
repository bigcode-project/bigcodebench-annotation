import os
import random
import pandas as pd

def f_732(data_dir,
          csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
          seed=None):
    """
    Randomly select one of the provided csv_files and select a certain number 
    of records from the file at random.
    The selected records are returned in a DataFrame. 
    The name of the selected csv_file is also returned.

    If the csv_file is empty return an empty DataFrame.

    Parameters:
    data_dir (str): The directory where the CSV files are located.
    csv_files (list of str): The list of CSV files to choose from. Default is ['file1.csv', 'file2.csv', 'file3.csv'].
    seed (int, optional): Seed for random number generation and for sampling from the csv.
    
    Returns:
    tuple: A tuple containing two elements:
        - str: The name of the randomly selected file.
        - DataFrame: A pandas DataFrame with the selected rows.

    Requirements:
    - os
    - random
    - pandas

    Example:
    >>> file_name, df = f_732('test_data')
    >>> print(file_name)
    'file2.csv'
    >>> print(df)
           Animal     Weight
     0        Cat          1
    21      Mouse         12
    15   Elephant       1000
     2      Tiger        500

    >>> file_name, df = f_732('data', csv_files=['test1.csv', 'test2.csv'], seed=42)
    >>> print(file_name)
    'test1.csv'
    >>> print(df)
                Name       House    Salary
     12        Simba     mansion     11111
    231      Dolores     mansion      2222
    135       Elaine        shed     93274
     21       Sophia      garden       111
    """

    random.seed(seed)

    file = csv_files[random.randint(0, len(csv_files)-1)]
    file_path = os.path.join(data_dir, file)

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return file, pd.DataFrame()

    selected_rows = df.sample(n=random.randint(1, len(df)), random_state=seed)

    return file, selected_rows

import unittest
import pandas as pd
import os

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    DATA_DIR = os.path.join('f_732_data_simon')

    def test_rng(self):
        file_name, df = f_732(data_dir=self.DATA_DIR, csv_files=['test_file1.csv', 'test_file2.csv'], seed=12)
        file_name2, df2 = f_732(data_dir=self.DATA_DIR, csv_files=['test_file1.csv', 'test_file2.csv'], seed=12)

        self.assertEqual(file_name, file_name2)
        pd.testing.assert_frame_equal(df, df2)

    def test_case_1(self):
        # Tests the function with only f_732_data_simon/test_file1.csv and checks if the returned file name matches 
        # and if the dataframe is not empty.
        file_name, df = f_732(data_dir=self.DATA_DIR, csv_files=['test_file1.csv'], seed=12)
        self.assertEqual(file_name, 'test_file1.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertNotEqual(len(df), 0)
        csv = pd.read_csv(os.path.join(self.DATA_DIR, 'test_file1.csv'))
        self.assertTrue(all(df.isin(csv)))

    def test_case_2(self):
        # Similar to test_case_1 but with f_732_data_simon/test_file2.csv.
        file_name, df = f_732(data_dir=self.DATA_DIR, csv_files=['test_file2.csv'], seed=1212)
        self.assertEqual(file_name, 'test_file2.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertNotEqual(len(df), 0)
        csv = pd.read_csv(os.path.join(self.DATA_DIR, 'test_file2.csv'))
        self.assertTrue(all(df.isin(csv)))


    def test_case_3(self):
        # Similar to test_case_1 but with f_732_data_simon/test_file3.csv.
        file_name, df = f_732(data_dir=self.DATA_DIR, csv_files=['test_file3.csv'], seed=127)
        self.assertEqual(file_name, 'test_file3.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertNotEqual(len(df), 0)
        csv = pd.read_csv(os.path.join(self.DATA_DIR, 'test_file3.csv'))
        self.assertTrue(all(df.isin(csv)))


    def test_case_4(self):
        # Tests the function with all CSV files and checks if the returned file name is one of the available files 
        # and if the dataframe is not empty.
        file_name, df = f_732(data_dir=self.DATA_DIR, csv_files=['test_file1.csv', 'test_file2.csv', 'test_file3.csv', 'test_file4.csv', 'test_file5.csv'], seed=152)
        self.assertIn(file_name, ['test_file1.csv', 'test_file2.csv', 'test_file3.csv', 'test_file4.csv', 'test_file5.csv'])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertNotEqual(len(df), 0)

    def test_case_5(self):
        # Tests the function with f_732_data_simon/test_file4.csv and f_732_data_simon/test_file5.csv and checks if the returned file name matches 
        # one of them and if the dataframe is not empty.
        file_name, df = f_732(data_dir=self.DATA_DIR, csv_files=['test_file4.csv', 'test_file5.csv'], seed=141)
        self.assertIn(file_name, ['test_file4.csv', 'test_file5.csv'])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertNotEqual(len(df), 0)

    def test_empty_csv(self):
        file_name, df = f_732(data_dir=self.DATA_DIR, csv_files=['empty.csv'], seed=42)
        self.assertEqual(file_name, 'empty.csv')
        self.assertTrue(df.empty)


if __name__ == "__main__":
    run_tests()