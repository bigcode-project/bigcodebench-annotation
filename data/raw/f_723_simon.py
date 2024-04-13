import pandas as pd

import pandas as pd
import random

def f_723(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
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
    >>> result = f_723('sample.csv', column_name='data', pattern='\d+[xX]', sample_size=10, seed=42)
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

    >>> result = f_723('sample.csv', column_name='data', sample_size=2)
    >>> print(result)
        index                                               data
    125    126  Fund elephenat, the dinoasuar eat this language t...
    21      22  Such an important story banking at the house a da...



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
import os

class TestCases(unittest.TestCase):

    data_path = os.path.join('f_723_data_simon', 'complex_test_data.csv')

    def test_case_1(self):
        # Testing with default parameters
        result = f_723(self.data_path)
        expected = pd.read_csv(os.path.join('f_723_data_simon/test1.csv'), index_col=0)
        pd.testing.assert_frame_equal(result, expected)

    def test_case_2(self):
        # Testing with custom column name
        with self.assertRaises(KeyError):
            f_723(self.data_path, column_name='non_existent_column')

    def test_case_3(self):
        # Testing with custom pattern
        result = f_723(self.data_path, pattern='\d+X')
        expected = pd.read_csv(os.path.join('f_723_data_simon/test3.csv'), index_col=0)
        pd.testing.assert_frame_equal(result, expected)

    def test_case_4(self):
        # Testing with pattern that has no matches
        result = f_723(self.data_path, pattern='XYZ')
        self.assertEqual(len(result), 0)

    def test_case_5(self):
        # Testing with non-existent file
        with self.assertRaises(FileNotFoundError):
            f_723('non_existent_file.csv')

    def test_case_6(self):
        # Testing with random sampling
        sample_size = 10
        result = f_723(self.data_path, sample_size=sample_size)
        self.assertEqual(len(result), sample_size)

    def test_case_7(self):
        # Testing the reproducibility with seed
        sample_size = 10
        result1 = f_723(self.data_path, sample_size=sample_size, seed=42)
        result2 = f_723(self.data_path, sample_size=sample_size, seed=42)
        pd.testing.assert_frame_equal(result1, result2)

    def test_case_8(self):
        # Testing with a sample size larger than the dataset
        result = f_723(self.data_path, sample_size=1000)
        self.assertEqual(len(result), 133)  # Should return all available matches

    def test_case_9(self):
        # Testing with zero sample size
        result = f_723(self.data_path, sample_size=0)
        self.assertEqual(len(result), 0)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()