import pandas as pd
import random
import csv

def f_665(n, 
           categories=['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'],
           news_sites=['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'],
           likert_scale=['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'],
           file_path='news_survey_data.csv',
           random_seed=None):
    """
    Generate a DataFrame with random survey data based on given categories, 
    news sites, and Likert scale responses. The function writes the generated
    data to a CSV file and then reads it into a Pandas DataFrame.
    
    Parameters:
    n (int): The number of survey responses to generate.
    categories (list, optional): Categories of news to choose from. Defaults to ['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'].
    news_sites (list, optional): News sites to choose from. Defaults to ['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'].
    likert_scale (list, optional): Likert scale responses to choose from. Defaults to ['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'].
    file_path (str, optional): Path to save the generated CSV file. Defaults to 'news_survey_data.csv'.
    random_seed (int): Seed for rng. Used for generating datapoints. Defaults to None.

    Returns:
    DataFrame: A pandas DataFrame with columns ['Site', 'Category', 'Response', 'Value']. 
               The 'Value' column assigns a numerical value to the Likert scale response (starting from 1).
    
    Requirements:
    - pandas
    - random
    - csv
    
    Example:
    >>> df = f_665(5)
    >>> print(df)
            Site    Category           Response  Value
    0   USA Today      Sports     Strongly Agree      5
    1   USA Today      Sports  Strongly Disagree      1
    2         CNN  Technology           Disagree      2
    3  Apple News      Sports     Strongly Agree      5
    4         CNN    Business              Agree      4
    
    >>> df = f_665(8, ['test', 'fun'], likert_scale=['true', 'false'], news_sites=['cat', 'dog'])
    >>> print(df)
        Site Category  Response  Value
    0  dog     test      True      1
    1  cat      fun     False      2
    2  dog     test     False      2
    3  dog     test     False      2
    4  dog     test     False      2
    5  cat     test     False      2
    6  cat      fun     False      2
    7  cat      fun     False      2
    """
    survey_data = []

    random.seed(random_seed)
    
    for _ in range(n):
        site = random.choice(news_sites)
        category = random.choice(categories)
        response = random.choice(likert_scale)
        value = likert_scale.index(response) + 1  # Assign a numerical value to the response
        survey_data.append({'Site': site, 'Category': category, 'Response': response, 'Value': value})
    
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Site', 'Category', 'Response', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(survey_data)
        
    df = pd.read_csv(file_path)
    
    return df

import unittest
import os


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # Setting up a temporary directory to save CSV files during tests
        self.temp_dir = "temp_test_dir"
        os.makedirs(self.temp_dir, exist_ok=True)
        
    def test_rng(self):
        'test rng reproducability'
        df1 = f_665(300, file_path=os.path.join(self.temp_dir, "test1.csv"), random_seed=42)
        df1_from_csv = pd.read_csv(os.path.join(self.temp_dir, "test1.csv"))
        df2 = f_665(300, file_path=os.path.join(self.temp_dir, "test2.csv"), random_seed=42)
        df2_from_csv = pd.read_csv(os.path.join(self.temp_dir, "test2.csv"))

        self.assertTrue(pd.testing.assert_frame_equal(df1, df2) is None)
        self.assertTrue(pd.testing.assert_frame_equal(df1_from_csv, df1) is None)
        self.assertTrue(pd.testing.assert_frame_equal(df2_from_csv, df2) is None)


    def test_case_1(self):
        # Test with default values for categories, news_sites, and likert_scale
        n = 100
        df = f_665(n, file_path=os.path.join(self.temp_dir, "test1.csv"), random_seed=1)
        df_from_csv = pd.read_csv(os.path.join(self.temp_dir, "test1.csv"))
        self.assertTrue(pd.testing.assert_frame_equal(df_from_csv, df) is None)

        self.assertEqual(len(df), n)
        self.assertTrue(set(df['Site'].unique()).issubset(set(['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'])))
        self.assertTrue(set(df['Category'].unique()).issubset(set(['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'])))
        self.assertTrue(set(df['Response'].unique()).issubset(set(['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'])))
        self.assertTrue(set(df['Value'].unique()).issubset(set(range(1, 6))))

    def test_case_2(self):
        # Test with custom values for categories and default values for others
        n = 500
        categories = ['Science', 'Math']
        df = f_665(n, categories=categories, file_path=os.path.join(self.temp_dir, "test2.csv"), random_seed=12)
        df_from_csv = pd.read_csv(os.path.join(self.temp_dir, "test2.csv"))
        self.assertTrue(pd.testing.assert_frame_equal(df_from_csv, df) is None)

        self.assertEqual(len(df), n)
        self.assertTrue(set(df['Category'].unique()).issubset(set(categories)))

    def test_case_3(self):
        # Test with custom values for news_sites and default values for others
        n = 775
        news_sites = ['ABC', 'NBC']
        df = f_665(n, news_sites=news_sites, file_path=os.path.join(self.temp_dir, "test3.csv"), random_seed=11)
        df_from_csv = pd.read_csv(os.path.join(self.temp_dir, "test3.csv"))
        self.assertTrue(pd.testing.assert_frame_equal(df_from_csv, df) is None)

        self.assertEqual(len(df), n)
        self.assertTrue(set(df['Site'].unique()).issubset(set(news_sites)))

    def test_case_4(self):
        # Test with custom values for likert_scale and default values for others
        n = 20
        likert_scale = ['Yes', 'No']
        df = f_665(n, likert_scale=likert_scale, file_path=os.path.join(self.temp_dir, "test4.csv"), random_seed=18)
        df_from_csv = pd.read_csv(os.path.join(self.temp_dir, "test4.csv"))
        self.assertTrue(pd.testing.assert_frame_equal(df_from_csv, df) is None)

        self.assertEqual(len(df), n)
        self.assertTrue(set(df['Response'].unique()).issubset(set(likert_scale)))
        self.assertTrue(set(df['Value'].unique()).issubset(set(range(1, 3))))

    def test_case_5(self):
        # Test for empty df
        n = 0
        df = f_665(n, file_path=os.path.join(self.temp_dir, "test5.csv"))
        self.assertEqual(len(df), n)

    def tearDown(self):
        # Cleanup temporary directory after tests
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)
if __name__ == "__main__":
    run_tests()