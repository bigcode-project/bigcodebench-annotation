import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def f_162(sample_size=1000, categories=['A', 'B', 'C', 'D', 'E'], random_seed=42):
    """
    Generate a random sample of categories, calculate the percentage of each category in the sample, and display the percentages in a bar chart.
    - Round each percentage to 1 decimal
    - The title of the barplot should be 'Category Percentages'
    - The xlabel of the barplot should be 'Category'
    - The ylabel of the barplot should be 'Percentage'

    Parameters:
    - random_seed (int, optional): The seed for the random generation. Defaults to 42.
    - sample_size (int, optional): The size of the sample to generate. Defaults to 1000.
    - categories (list, optional): A list of categories to sample from. Defaults to ['A', 'B', 'C', 'D', 'E'].

    Returns:
    - DataFrame: A pandas DataFrame with the sample data and their percentages. It should have only one column, and its name should be 'Category'.
    - Axes: A matplotlib Axes object displaying the bar chart.

    Requirements:
    - numpy
    - pandas
    - matplotlib.pyplot
    - seaborn

    Example:
    >>> sample_df, ax = f_162()
    >>> print(sample_df)
    """
    np.random.seed(random_seed)
    sample = np.random.choice(categories, sample_size)
    sample_df = pd.DataFrame(sample, columns=['Category'])
    sample_counts = sample_df['Category'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'

    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=sample_counts.index, y=sample_counts.str.rstrip('%').astype(float), palette='viridis', ax=ax)
    ax.set_xlabel('Category')
    ax.set_ylabel('Percentage')
    ax.set_title('Category Percentages')
    
    return sample_df, ax

import unittest
import numpy as np

class TestCases(unittest.TestCase):
    """Test cases for the f_162 function."""
    def test_case_1(self):
        # Test with default parameters
        df, ax = f_162()
        self.assertEqual(len(df), 1000)
        self.assertTrue(set(df['Category'].unique()).issubset(set(['A', 'B', 'C', 'D', 'E'])))
        self.assertEqual(ax.get_title(), 'Category Percentages')
    
    def test_case_2(self):
        # Test with custom parameters
        categories = ['X', 'Y', 'Z']
        sample_size = 500
        df, ax = f_162(sample_size=sample_size, categories=categories)
        self.assertEqual(len(df), sample_size)
        self.assertTrue(set(df['Category'].unique()).issubset(set(categories)))
        self.assertEqual(ax.get_title(), 'Category Percentages')
        self.assertEqual(ax.get_xlabel(), 'Category')
        self.assertEqual(ax.get_ylabel(), 'Percentage')
    
    def test_case_3(self):
        # Test with a large sample size
        df, ax = f_162(sample_size=10000)
        self.assertEqual(len(df), 10000)
        self.assertTrue(set(df['Category'].unique()).issubset(set(['A', 'B', 'C', 'D', 'E'])))
    
    def test_case_4(self):
        # Test with a single category
        df, ax = f_162(categories=['Z'])
        self.assertTrue(set(df['Category'].unique()).issubset(set(['Z'])))
    
    def test_case_5(self):
        # Test with an empty list of categories (should raise an exception)
        with self.assertRaises(ValueError):
            f_162(categories=[])

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()