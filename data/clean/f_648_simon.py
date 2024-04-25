import numpy as np
import pandas as pd
import statsmodels.api as sm


def f_648(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    """
    Performs an OLS linear regression on a subset of the provided DataFrame. The subset is created by filtering rows 
    where the value in the second column of 'columns' is greater than 'height' and the value in the third column is 
    less than 'weight'. The first column in 'columns' is used as the dependent variable / target (y), and the rest as independent 
    variables (X) in the regression.

    If df is empty, or if no rows match the conditions None is returned.


    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.
    - height (int): The threshold to filter rows based on the second column in 'columns'.
    - weight (int): The threshold to filter rows based on the third column in 'columns'.
    - columns (list of str): A list of column names to use, where the first is the dependent variable.

    Returns:
    - sm.regression.linear_model.RegressionResultsWrapper: The result of the OLS regression, or None if no rows meet the criteria or DataFrame is empty.

    Requirements:
    - pandas
    - statsmodels

    Example:
    >>> df = pd.DataFrame({'Age': [30, 40], 'Height': [60, 70], 'Weight': [100, 150]})
    >>> model = f_648(df, 50, 120, ['Age', 'Height', 'Weight'])
    >>> print(model)
    <statsmodels.regression.linear_model.RegressionResultsWrapper object at 0x000001D32E5EAAD0>

    >>> df = pd.DataFrame(np.random.randint(10,98,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
    >>> model = f_648(df, 45, 72, columns=['Age', 'Height', 'Weight'])
    >>> print(model.params)
    const     36.613966
    Height     0.133301
    Weight     0.157604
    dtype: float64
    """
    # Check for empty DataFrame
    if df.empty:
        return None

    # Filter the DataFrame based on provided column names
    selected_df = df[(df[columns[1]] > height) & (df[columns[2]] < weight)]
    
    # If no rows match the condition, return None
    if selected_df.empty:
        return None
    
    X = selected_df[columns[1:]]
    y = selected_df[columns[0]]
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()

    return results
    

import unittest
import numpy as np
import pandas as pd

class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        np.random.seed(42)  # Set a seed for reproducibility

    def test_case_1(self):
        # Test with a DataFrame of random values
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = f_648(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper) 
        self.assertEqual(results.params.index.to_list(), ['const', 'Height', 'Weight']) # There should be 3 parameters: const, Height, Weight

    def test_case_2(self):
        # Test with a DataFrame where no rows match the condition
        df = pd.DataFrame(np.random.randint(30,40,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = f_648(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsNone(results) # There should be no regression result since no rows match the condition

    def test_case_3(self):
        # Test with a DataFrame where all rows match the condition
        df = pd.DataFrame(np.random.randint(60,80,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
        results = f_648(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper) 
        self.assertEqual(results.params.index.to_list(), ['const', 'Height', 'Weight']) # There should be 3 parameters: const, Height, Weight

    def test_case_4(self):
        # Test with a DataFrame with different column names
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 3)), columns=['Years', 'Size', 'Mass'])
        results = f_648(df, 50, 70, columns=['Years', 'Size', 'Mass'])
        self.assertIsInstance(results, sm.regression.linear_model.RegressionResultsWrapper) 
        self.assertEqual(results.params.index.to_list(), ['const', 'Size', 'Mass']) # There should be 3 parameters: const, Height, Weight

    def test_case_5(self):
        # Test with an empty DataFrame
        df = pd.DataFrame(columns=['Age', 'Height', 'Weight'])
        results = f_648(df, 50, 70, columns=['Age', 'Height', 'Weight'])
        self.assertIsNone(results) # There should be no regression result since DataFrame is empty


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()