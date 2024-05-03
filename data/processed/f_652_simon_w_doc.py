import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def f_652(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
           ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    """
    Generate a demographic dataset with information about people from different countries, their age, and gender. 
    Genders are encoded using sklearn LabelEncoder.
    Datapoints are sampled from the lists using a numpy.random.default_rng with seed: rng_seed.

    Parameters:
    num_samples (int): The number of samples to generate.
    countries (list of str): A list of country names to use in the dataset. Default is ['Russia', 'China', 'USA', 'India', 'Brazil'].
    ages (array of int): An array of ages to use in the dataset. Default is np.arange(18, 60).
    genders (list of str): A list of genders to use in the dataset. Default is ['Male', 'Female'].
    rng_seed: seed for the random number generator
    
    Returns:
    DataFrame: A pandas DataFrame with the demographics data.

    Raises:
    - ValueError: If num_samples is not an integer.

    Requirements:
    - pandas
    - numpy
    - sklearn.preprocessing.LabelEncoder

    Example:
    >>> demographics = f_652(5, rng_seed=31)
    >>> print(demographics)
      Country  Age  Gender
    0     USA   46       0
    1  Brazil   21       1
    2     USA   37       1
    3  Russia   32       1
    4     USA   46       0

    >>> demographics = f_652(5, countries=['Austria', 'Germany'], rng_seed=3)
    >>> print(demographics)
       Country  Age  Gender
    0  Germany   51       1
    1  Austria   54       1
    2  Austria   42       0
    3  Austria   19       1
    4  Austria   21       1
    """

    if not isinstance(num_samples, int):
        raise ValueError("num_samples should be an integer.")

    rng = np.random.default_rng(seed=rng_seed)
    countries = rng.choice(countries, num_samples)
    ages = rng.choice(ages, num_samples)
    genders = rng.choice(genders, num_samples)

    le = LabelEncoder()
    encoded_genders = le.fit_transform(genders)

    demographics = pd.DataFrame({
        'Country': countries,
        'Age': ages,
        'Gender': encoded_genders
    })

    return demographics

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_num_samples(self):
        'num_samples not an integer'
        self.assertRaises(Exception, f_652, 'test')
    
    # Test Case 1: Basic test with default parameters
    def test_case_1(self):
        demographics = f_652(10, rng_seed=1)
        self.assertEqual(len(demographics), 10)
        self.assertTrue(set(demographics['Country'].unique()).issubset(['Russia', 'China', 'USA', 'India', 'Brazil']))
        self.assertTrue(all(18 <= age <= 59 for age in demographics['Age']))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))
    # Test Case 2: Test with custom countries list
    def test_case_2(self):
        demographics = f_652(5, countries=['Canada', 'Australia'], rng_seed=1)
        self.assertEqual(len(demographics), 5)
        self.assertTrue(set(demographics['Country'].unique()).issubset(['Canada', 'Australia']))
        self.assertTrue(all(18 <= age <= 59 for age in demographics['Age']))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))
    # Test Case 3: Test with custom age range
    def test_case_3(self):
        demographics = f_652(5, ages=np.arange(25, 40), rng_seed=1)
        self.assertEqual(len(demographics), 5)
        self.assertTrue(all(25 <= age <= 40 for age in demographics['Age']))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))
    # Test Case 4: Test with custom gender list
    def test_case_4(self):
        demographics = f_652(5, genders=['Non-Binary'], rng_seed=1)
        self.assertEqual(len(demographics), 5)
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0]))
    # Test Case 5: Test with larger sample size
    def test_case_5(self):
        demographics = f_652(100, rng_seed=1)
        self.assertEqual(len(demographics), 100)
        self.assertTrue(set(demographics['Country'].unique()).issubset(['Russia', 'China', 'USA', 'India', 'Brazil']))
        self.assertTrue(all(18 <= age <= 59 for age in demographics['Age']))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))
    def test_case_6(self):
        'check for specific return value'
        demographics = f_652(5, rng_seed=3)
        expected_df = pd.DataFrame({
            'Country': ['Brazil', 'Russia', 'Russia', 'China', 'Russia'],
            'Age': [51, 54, 42, 19, 21],
            'Gender': [1, 1, 0, 1, 1]
        })
        pd.testing.assert_frame_equal(demographics, expected_df)
