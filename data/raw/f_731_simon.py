import os
import pandas as pd
import numpy as np

def f_731(data_dir: str, csv_file: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame and replace the NaN values in
    numeric columns with the mean of the corresponding column.
    The resulting DataFrame is returned.

    If an empty csv is passed, an empty DataFrame is returned.

    Parameters:
    - data_dir (str): The path to the directory containing the CSV file.
    - csv_file (str): The name of the CSV file to be processed.

    Returns:
    pd.DataFrame: A pandas DataFrame with the processed data.

    Raises:
    FileNotFoundError: If csv_file does not exist.

    Requirements:
    - os
    - pandas
    - numpy
    
    Example:
    >>> df = f_731("/path/to/data/directory", "file.csv")
    >>> print(df)
         Fruit     Taste     Cost
    0    Apple      Good        1
    1   Orange       NaN        2
    2  Avocado       Bad        1.667
    3  Coconut     Tasty        2

    >>> df = f_731("/path/to/data/directory", "test.csv")
    >>> print(df)
         Name     Score     
    0    Alex         25.2   
    1   Tanja         31.5   
    2   Maine         99  
    3    Lisa        100
    4  Simone         63.925
    """
    file_path = os.path.join(data_dir, csv_file)
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()



    for column in df.columns:
        if np.issubdtype(df[column].dtype, np.number):  # checking for numeric columns
            df[column].fillna(df[column].mean(), inplace=True)

    return df

import os
import pandas as pd
import numpy as np
import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def setUp(self):
        self.folder_path = 'f_731_data_simon'

    def test_case_1(self):
        df_result = f_731(self.folder_path, "mock_data1.csv")
        self.assertEqual(df_result["Age"].isnull().sum(), 0)
        self.assertEqual(df_result["Salary"].isnull().sum(), 0)
        self.assertEqual(df_result["Age"][1], 27.333333333333332)
        self.assertEqual(df_result["Salary"][2], 55000)

    def test_case_2(self):
        df_result = f_731(self.folder_path, "mock_data2.csv")

        exp = pd.DataFrame(
            {'Animal': {0: 'Cat', 1: 'Dog', 2: np.nan, 3: 'Fly'},
            ' Size': {0: 1.0, 1: 4.0, 2: 12.0, 3: 0.1},
            ' Weight': {0: 10.0, 1: 40.0, 2: 21.0, 3: 23.666666666666668}}
        )

        pd.testing.assert_frame_equal(df_result, exp)

    def test_case_3(self):
        # empty csv
        res = f_731(self.folder_path, "empty.csv")
        self.assertTrue(res.empty)

    def test_case_4(self):
        # non existing csv
        self.assertRaises(Exception, f_731, self.folder_path, "non_existing.csv")

    def test_case_5(self):
        # only strings
        df_result = f_731(self.folder_path, "strings.csv")
        exp = pd.DataFrame(
            {'A': {0: 'Test', 1: 'Test2', 2: np.nan, 3: 'Test3'},
            ' B ': {0: ' Hi', 1: ' Hello', 2: ' Hola', 3: np.nan}}
        )
        pd.testing.assert_frame_equal(df_result, exp)

if __name__ == "__main__":
    run_tests()