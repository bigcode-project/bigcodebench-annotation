import matplotlib.pyplot as plt

def f_172(df):
    """
    Create a histogram for values from column 'A' of the DataFrame df where column 'B' has values greater than 50 and column 'C' has values equal to 900.
    
    Parameters:
    - df (pd.DataFrame): A DataFrame with at least three columns 'A', 'B', and 'C'.
    
    Returns:
    - plt.Axes: Axes object with the histogram plotted.
        - Its title should be "Histogram of 'A' values"
        - x-label should be set to "'A' values"
        - y-label should be set to "Counts"
    
    Example:
    >>> df = pd.DataFrame({
    ...     'A': [10, 20, 30, 40, 50],
    ...     'B': [60, 45, 70, 55, 80],
    ...     'C': [900, 800, 900, 700, 900]
    ... })
    >>> ax = f_172(df)
    >>> ax.get_children()[0].get_height()  # First bar height
    2.0
    """
    # Selecting rows based on the given conditions
    selected_values = df['A'][(df['B'] > 50) & (df['C'] == 900)]
    # Plotting the histogram
    _, ax = plt.subplots()
    ax.hist(selected_values, bins=20, edgecolor='black', alpha=0.7)
    ax.set_title("Histogram of 'A' values")
    ax.set_xlabel("'A' values")
    ax.set_ylabel('Counts')
    return ax

import unittest
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):
    """Test cases for the f_172 function."""
    def test_case_1(self):
        df = pd.DataFrame(
            {
                'A': np.random.randint(0, 100, 100),
                'B': np.random.randint(0, 100, 100),
                'C': np.random.choice([900, 800, 700, 600], 100)}
            )
        result = f_172(df)
        self.assertTrue(isinstance(result, plt.Axes))
        self.assertEqual(ax.get_title(), "Histogram of 'A' values")
        self.assertEqual(ax.get_xlabel(), "'A' values")
        self.assertEqual(ax.get_ylabel(), "Counts")

    def test_case_2(self):
        df = pd.DataFrame(
            {
                'A': np.random.randint(0, 200, 200),
                'B': np.random.randint(50, 150, 200),
                'C': [900] * 200
            }
        )
        result = f_172(df)
        self.assertTrue(isinstance(result, plt.Axes))
    
    def test_case_3(self):
        df = pd.DataFrame(
            {
                'A': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                'B': [55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
                'C': [900, 900, 800, 700, 600, 500, 400, 300, 200, 100]
            }
        )
        result = f_172(df)
        self.assertTrue(isinstance(result, plt.Axes))

    def test_case_4(self):
        df = pd.DataFrame(
            {
                "A" : [10, 20, 30, 40, 50, 60, 70, 80, 90],
                "B" : [20, 70, 10, 80, 35, 95, 15, 100, 17],
                "C" : [900, 900, 100, 900, 300, 900, 400, 900, 1000]
            }
        )
        result = f_172(df)
        self.assertTrue(isinstance(result, plt.Axes))
        self.assertEqual(result.get_children()[0].get_height(), 1.0)
    
    def test_case_5(self):
        df = pd.DataFrame(
            {
                "A" : [10, 20, 10, 10],
                "B" : [60, 70, 80, 60],
                "C" : [900, 900, 900, 900]
            }
        )
        result = f_172(df)
        self.assertTrue(isinstance(result, plt.Axes))
        self.assertEqual(result.get_children()[0].get_height(), 3.0)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()