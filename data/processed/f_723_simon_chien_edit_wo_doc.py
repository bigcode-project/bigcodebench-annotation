import pandas as pd

import pandas as pd
import random


def f_634(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    """ 
    Search for matches with a specified regex pattern in a given column of a CSV file and optionally return a random sample of these matches.
    
    The random sampling is implemented by generating a random list of integers which are used as indices.
    The number of generated indices is given by sample_size.
    

    Parameters:
    csv_file (str): Path to the CSV file.
    column_name (str, optional): The name of the column to search. Defaults to 'data'.
    pattern (str, optional): The regex pattern to search for. Defaults to '\d+[xX]'.
    sample_size (int, optional): Number of random samples to return from the matches. If None, all matches are returned. Defaults to None.
    seed (int, optional): Seed for the random number generator for reproducibility. Defaults to 42.
    
    Returns:
    DataFrame: A pandas DataFrame containing either all the rows with matches or a random sample of them.
    
    Requirements:
    - pandas
    - random: for generating the random list of indices
    
    Example:
    >>> result = f_634('sample.csv', column_name='data', pattern='\d+[xX]', sample_size=10, seed=42)
    >>> print(result)
            index                                               data
    210    211  Fund several agency oil. Evening plant thank t...
    45      46  Language interest four take old. Education if ...
    525    526  Action million cultural stand. Heart explain a...
    465    466  Security face clearly every could. Image beaut...
    430    431  Popular produce floor part soldier human. Youn...
    260    261  Customer game focus respond that central. Nigh...
    195    196  The writer parent. Life social house west ten ...
    165    166  Main hotel production nothing.\r\nCoach voice ...
    810    811  Early right nature technology. Conference mind...
    60      61  Interest require gas wall. Different it see fi...
    """
    df = pd.read_csv(csv_file)
    matches = df[df[column_name].str.contains(pattern, na=False)]

    if sample_size is not None:
        random.seed(seed)  # Set the seed for reproducibility
        sample_size = min(sample_size, len(matches))  # Ensure sample size is not greater than the number of matches
        sampled_indices = random.sample(range(len(matches)), sample_size)  # Randomly select indices
        matches = matches.iloc[sampled_indices]  # Select rows corresponding to sampled indices

    return matches

import unittest
import pandas as pd
import tempfile
import shutil
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store the test CSV files
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_data.csv")
        # Create a sample DataFrame
        data = {
            "data": ["123x good", "no match here", "456X bad", "789x good", "ABC"],
            "other_column": ["data1", "data2", "data3", "data4", "data5"]
        }
        self.df = pd.DataFrame(data)
        self.df.to_csv(self.test_file, index=False)
    def tearDown(self):
        # Remove temporary directory after the test
        shutil.rmtree(self.test_dir)
    def test_default_parameters(self):
        result = f_634(self.test_file)
        expected_data = {
            "data": ["123x good", "456X bad", "789x good"],
            "other_column": ["data1", "data3", "data4"]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)
    def test_custom_column(self):
        with self.assertRaises(KeyError):
            f_634(self.test_file, column_name="nonexistent_column")
    def test_custom_pattern(self):
        result = f_634(self.test_file, pattern='\d+X')
        expected_data = {
            "data": ["456X bad"],
            "other_column": ["data3"]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)
    def test_sample_size(self):
        result = f_634(self.test_file, sample_size=2, seed=42)
        self.assertEqual(len(result), 2)
    def test_no_matches(self):
        result = f_634(self.test_file, pattern="nope")
        self.assertTrue(result.empty)
    def test_sample_size_larger_than_matches(self):
        result = f_634(self.test_file, sample_size=10)
        self.assertEqual(len(result), 3)  # Only three matches exist
    def test_zero_sample_size(self):
        result = f_634(self.test_file, sample_size=0)
        self.assertTrue(result.empty)
