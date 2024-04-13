import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def f_145(data='/path/to/data.csv', emp_prefix='EMP'):
    """
    Load a CSV file into a DataFrame, filter the lines in which the employee ID begins with a prefix, and draw a histogram of its age.
    
    Parameters:
    - data (str): The path to the data file. Default is '/path/to/data.csv'.
    - emp_prefix (str): The prefix of the employee IDs. Default is 'EMP$$'.
    
    Returns:
    - DataFrame: A pandas DataFrame with the filtered data.
    - AxesSubplot: A histogram plot of the 'Age' column of the filtered data.
    
    Requirements:
    - pandas
    - seaborn
    - matplotlib.pyplot
    
    Example:
    >>> df, ax = f_145()
    >>> print(df)
    """
    # Load data and filter
    df = pd.read_csv(data)
    df = df[df['Employee ID'].str.startswith(emp_prefix)]
    
    # Plot histogram
    ax = sns.histplot(data=df, x='Age', kde=True)
    
    return df, ax

import unittest
import pandas as pd
import shutil
import os

class TestCases(unittest.TestCase):
    """Test cases for the f_145 function."""
    def setUp(self):
        self.test_dir = "data/f_145"
        os.makedirs(self.test_dir, exist_ok=True)

        self.f_1 = os.path.join(self.test_dir, "csv_1.csv")
        df = pd.DataFrame(
            {
                "Employee ID" : ["EMP001", "EMP002", "EMP003", "ENG001", "ENG002"],
                "Age" : [23, 45, 27, 32, 33]
            }
        )
        df.to_csv(self.f_1, index = False)

        self.f_2 = os.path.join(self.test_dir, "csv_2.csv")
        df = pd.DataFrame(
            {
                "Employee ID" : ["CUSTOM001", "MAN001", "CUSTOM002", "HR001"],
                "Age" : [34, 56, 27, 29]
            }
        )
        df.to_csv(self.f_2, index = False)

        self.f_3 = os.path.join(self.test_dir, "csv_3.csv")
        df = pd.DataFrame(
            {
                "Employee ID" : ["CUSTOM003", "CUSTOM004", "CUSTOM005"],
                "Age" : [44, 45, 46]
            }
        )
        df.to_csv(self.f_3, index = False)

        self.f_4 = os.path.join(self.test_dir, "csv_4.csv")
        df = pd.DataFrame(
            {
                "Employee ID" : ["HR007", "HR008", "HR009", "DR001", "DR002"],
                "Age" : [57, 31, 28, 49, 51]
            }
        )
        df.to_csv(self.f_4, index = False)

        self.f_5 = os.path.join(self.test_dir, "csv_5.csv")
        df = pd.DataFrame(
            {
                "Employee ID" : ["RS001", "RS002"],
                "Age" : [29, 36]
            }
        )
        df.to_csv(self.f_5, index = False)
    
    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_case_1(self):
        # Test the function with default parameters
        df, ax = f_145(self.f_1)
        print(df.columns)
        expected_df = pd.DataFrame(
            {
                "Employee ID" : ["EMP001", "EMP002", "EMP003"],
                "Age" : [23, 45, 27]
            }
        )

        self.assertIsInstance(df, pd.DataFrame)
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df.reset_index(drop=True))
        self.assertIsNotNone(ax)

    def test_case_2(self):
        # Test the function with custom input data and prefix
        df, ax = f_145(self.f_2, 'CUSTOM')
        expected_df = pd.DataFrame(
            {
                "Employee ID" : ["CUSTOM001", "CUSTOM002"],
                "Age" : [34, 27]
            }
        )

        self.assertIsInstance(df, pd.DataFrame)
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df.reset_index(drop=True))
        self.assertIsNotNone(ax)

    def test_case_3(self):
        # Test the function with invalid prefix
        df, ax = f_145(self.f_3, 'INVALID')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.shape[0] == 0)
        self.assertTrue(all([col in df.columns for col in ["Employee ID", "Age"]]))
        self.assertIsNotNone(ax)
        
    def test_case_4(self):
        # Test the function with custom input data and prefix
        df, ax = f_145(self.f_4, 'DR')
        expected_df = pd.DataFrame(
            {
                "Employee ID" : ["DR001", "DR002"],
                "Age" : [49, 51]
            }
        )

        self.assertIsInstance(df, pd.DataFrame)
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df.reset_index(drop=True))
        self.assertIsNotNone(ax)
    
    def test_case_5(self):
        # Test the function with custom input data and prefix
        df, ax = f_145(self.f_5, 'RS')
        expected_df = pd.DataFrame(
            {
                "Employee ID" : ["RS001", "RS002"],
                "Age" : [29, 36]
            }
        )

        self.assertIsInstance(df, pd.DataFrame)
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df.reset_index(drop=True))
        self.assertIsNotNone(ax)
    
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests() 
