import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def f_163(num_pairs=500, random_seed=42):
    """
    Generate a pair of normally distributed random variables, calculate the correlation coefficient, and draw a scatter plot with a regression line.
    Steps:
    0. Generate num_pairs normally distributed random variables.
    1. Generate num_pairs other normally distributed random variables by multiplying each variable above by 2.5 and adding a normally distributed random
    variable.
    2. Create a pandas DataFrame with columns 'X' and 'Y' representing the variables created at step 0 and step 1 respectively.
    3. Compute the correlation between both set of random variables.
    4. Create a regression line with seaborn where the x-axis represents the first set of normally distributed random variables and the y-axis the second.
    5. Set the plot title to 'Correlation: ' followed by the value correlation rounded to 2 decimals.


    Parameters:
    - num_pairs (int): The number of pairs of random variables to be generated. Default is 500. This determines the sample size for the generated data.
    - random_seed (int): The seed for the random number generator, ensuring reproducibility. Default is 42.

    Returns:
    - float: The correlation coefficient of the generated variables. This value ranges between -1 and 1.
    - Axes object: A scatter plot visualizing the relationship between the two variables with a regression line.

    Requirements:
    - numpy: For generating random numbers and setting the random seed.
    - pandas: For creating a DataFrame and calculating correlation.
    - matplotlib.pyplot: For plotting the relationship.
    - seaborn: For enhancing visualization with a regression line.

    Example:
    >>> correlation, plot = f_163(500, 42)
    >>> print(correlation)
    0.9253
    """
    np.random.seed(random_seed)
    X = np.random.randn(num_pairs)
    Y = 2.5*X + np.random.randn(num_pairs)
    df = pd.DataFrame({'X': X, 'Y': Y})

    correlation = df['X'].corr(df['Y'])

    _, ax = plt.subplots()
    sns.regplot(x='X', y='Y', data=df, line_kws={'color': 'red'}, ax=ax)
    ax.set_title(f'Correlation: {correlation:.2f}')
    
    return correlation, ax

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_163 function."""
    def test_case_1(self):
        correlation, plot = f_163()
        self.assertAlmostEqual(correlation, 0.9253, places=4)
        self.assertTrue(isinstance(plot, plt.Axes))
        self.assertEqual(plot.get_title(), 'Correlation: 0.93')
    
    def test_case_2(self):
        correlation, plot = f_163(num_pairs=1000, random_seed=100)
        self.assertTrue(isinstance(correlation, float))
        self.assertTrue(isinstance(plot, plt.Axes))
        self.assertTrue(0 <= abs(correlation) <= 1)
        
    def test_case_3(self):
        correlation, plot = f_163(random_seed=1)
        self.assertTrue(isinstance(correlation, float))
        self.assertTrue(isinstance(plot, plt.Axes))
        self.assertTrue(0 <= abs(correlation) <= 1)
    
    def test_case_4(self):
        num_pairs = 300
        random_seed = 122
        correlation, plot = f_163(num_pairs=num_pairs, random_seed=random_seed)
        self.assertTrue(isinstance(correlation, float))
        self.assertTrue(isinstance(plot, plt.Axes))
        self.assertTrue(0 <= abs(correlation) <= 1)
        
    def test_case_5(self):
        correlation, plot = f_163(num_pairs=2, random_seed=50)
        self.assertTrue(isinstance(correlation, float))
        self.assertTrue(isinstance(plot, plt.Axes))
        self.assertTrue(0 <= abs(correlation) <= 1)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()