import pandas as pd
import numpy as np
import statsmodels.api as sm


def f_404(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    """
    Generate a Pandas DataFrame from a 2D list and perform a multiple linear regression.

    The function first validates the input list, creates a DataFrame, separates independent and dependent variables,
    adds a constant to the model, and fits a linear regression using statsmodels.

    Parameters:
    - array (list of list of int): A 2D list where each sub-list represents a row of data.
                                   Each sub-list should have exactly 5 elements, where the first 4 elements are
                                   treated as independent variables ('A', 'B', 'C', 'D') and the last element is
                                   the dependent (Response) variable.

    - random_seed (int): A seed for reproducibility in numpy for statsmodels. Defaults to 0.

    Returns:
    - df (pd.DataFrame): DataFrame with columns 'A', 'B', 'C', 'D', 'Response'.
    - results (statsmodels.RegressionResults): Results of the linear regression.

    Requirements:
    - pandas
    - numpy
    - statsmodels.api.sm

    Example:
    >>> df, results = f_404([[1,2,3,4,5], [6,7,8,9,10]])
    >>> print(df)
       A  B  C  D  Response
    0  1  2  3  4         5
    1  6  7  8  9        10
    """
    COLUMNS = ["A", "B", "C", "D", "Response"]

    np.random.seed(random_seed)

    if not all(len(row) == len(COLUMNS) for row in array):
        raise ValueError(
            "Each sub-list in the input 2D list must have exactly 5 elements."
        )

    df = pd.DataFrame(array, columns=COLUMNS)
    X = df[COLUMNS[:-1]]
    y = df["Response"]
    X = sm.add_constant(X)

    model = sm.OLS(y, X)
    results = model.fit()

    return df, results


import unittest
import pandas as pd


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing dataframe creation, model accuracy, and parameters with various numeric data types
        test_data = [
            ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 42, 1.0),  # Positive values
            ([[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10]], 42, 1.0),  # Negative values
            (
                [[100, 200, 300, 400, 500], [600, 700, 800, 900, 1000]],
                42,
                1.0,
            ),  # Large values
        ]
        for array, random_seed, expected_r2 in test_data:
            with self.subTest(array=array):
                df, results = f_404(array, random_seed=random_seed)
                expected_df = pd.DataFrame(
                    array, columns=["A", "B", "C", "D", "Response"]
                )
                self.assertTrue(df.equals(expected_df))
                self.assertAlmostEqual(results.rsquared, expected_r2, places=2)
                for param in results.params:
                    self.assertNotEqual(param, 0)

    def test_case_2(self):
        # Testing with more rows in the 2D list to ensure model scalability and consistency
        random_seed = 42
        array = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ]
        df, results = f_404(array, random_seed=random_seed)
        expected_df = pd.DataFrame(array, columns=["A", "B", "C", "D", "Response"])
        self.assertTrue(df.equals(expected_df))
        self.assertAlmostEqual(results.rsquared, 1.0, places=2)
        for param in results.params:
            self.assertNotEqual(param, 0)

    def test_case_3(self):
        # Testing input validation for incorrect number of columns in a row
        array = [[1, 2, 3, 4], [5, 6, 7, 8]]  # Missing dependent variable
        with self.assertRaises(ValueError):
            f_404(array)

    def test_case_4(self):
        # Testing handling of non-numeric values to ensure type safety
        array = [["a", "b", "c", "d", "e"]]  # All elements as strings
        with self.assertRaises(ValueError):
            df, results = f_404(array)
            # This assumes the function is modified to catch and raise ValueError for non-numeric inputs

    def test_case_5(self):
        # Testing reproducibility by using the same random_seed
        array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        random_seed = 123
        df1, results1 = f_404(array, random_seed=random_seed)
        df2, results2 = f_404(array, random_seed=random_seed)
        self.assertTrue(df1.equals(df2))
        self.assertEqual(results1.params.tolist(), results2.params.tolist())

    def test_case_6(self):
        # Testing with an empty array to check function's handling of no input data
        array = []
        with self.assertRaises(ValueError):
            f_404(array)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
