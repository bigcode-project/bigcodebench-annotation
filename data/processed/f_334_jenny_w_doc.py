import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def f_334(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    """
    Perform linear regression analysis with specified characteristics and targets.
    The function should merge two dataframes based on the 'id' column, perform
    linear regression using columns specified in features to predict the target,
    and plot the residuals.

    Parameters:
    - df1 (DataFrame): The first dataframe containing columns 'id' and the features specified.
    - df2 (DataFrame): The second dataframe containing columns 'id' and target.
    - features (list of str, optional): List of feature column names. Default is ['feature1', 'feature2', 'feature3'].
    - target (str, optional): Name of the target column. Default is 'target'.

    Returns:
    dict: A dictionary containing:
        - 'coefficients': Regression coefficients (list).
        - 'intercept': Regression intercept (float).
        - 'residuals_plot': A matplotlib Axes object representing the residuals plot.

    Requirements:
    - pandas
    - sklearn.linear_model.LinearRegression
    - matplotlib.pyplot

    Example:
    >>> df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6], 'feature2': [2.3, 4.5, 6.7], 'feature3': [3.4, 5.6, 7.8]})
    >>> df2 = pd.DataFrame({'id': [1, 2, 3], 'target': [4.5, 6.7, 8.9]})
    >>> result = f_334(df1, df2)
    >>> result['coefficients']
    [0.3333333333333334, 0.33333333333333354, 0.3333333333333335]
    >>> type(result['residuals_plot'])
    <class 'matplotlib.axes._axes.Axes'>
    """
    df = pd.merge(df1, df2, on="id")
    X = df[features]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    residuals = y - y_pred
    fig, ax = plt.subplots()
    ax.scatter(y_pred, residuals)  # scatter plot of residuals
    ax.axhline(y=0, color="r", linestyle="-")  # horizontal line at y=0
    ax.set_xlabel("Predicted Values")
    ax.set_ylabel("Residuals")
    ax.set_title("Residuals Plot")
    return {
        "coefficients": list(model.coef_),
        "intercept": model.intercept_,
        "residuals_plot": ax,
    }

import unittest
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
class TestCases(unittest.TestCase):
    # Setting up sample data for some test cases
    def setUp(self):
        self.df1_sample = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [1, 2, 3],
                "feature2": [1, 2, 3],
                "feature3": [1, 2, 3],
            }
        )
        self.df2_sample = pd.DataFrame({"id": [1, 2, 3], "target": [6, 15, 24]})
    def tearDown(self):
        plt.close("all")
    # Test if the function returns the correct coefficients and intercept
    def test_case_1(self):
        result = f_334(self.df1_sample, self.df2_sample)
        for coef_actual, coef_expected in zip(result["coefficients"], [3.0, 3.0, 3.0]):
            self.assertAlmostEqual(coef_actual, coef_expected, places=7)
        self.assertAlmostEqual(result["intercept"], -3.0, places=7)
    # Test if the function returns the residuals plot
    def test_case_2(self):
        result = f_334(self.df1_sample, self.df2_sample)
        self.assertTrue(isinstance(result["residuals_plot"], plt.Axes))
    # Test if the residuals plot contains the right number of data points
    def test_case_3(self):
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [2, 4, 6],
                "feature2": [2, 4, 6],
                "feature3": [2, 4, 6],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [12, 30, 48]})
        result = f_334(df1, df2)
        self.assertEqual(len(result["residuals_plot"].collections), 1)
    # Test if the intercept of the model is correct
    def test_case_4(self):
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [1, 2, 3],
                "feature2": [4, 5, 6],
                "feature3": [7, 8, 9],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [10, 11, 12]})
        result = f_334(df1, df2)
        self.assertAlmostEqual(result["intercept"], 6.0, places=7)
    # Test the coefficients and intercept for a different set of data
    def test_case_5(self):
        result = f_334(self.df1_sample, self.df2_sample)
        for coef_actual, coef_expected in zip(result["coefficients"], [3.0, 3.0, 3.0]):
            self.assertAlmostEqual(coef_actual, coef_expected, places=7)
        self.assertAlmostEqual(result["intercept"], -3.0, places=7)
    # Test the coefficients and intercept against sklearn's LinearRegression for verification
    def test_case_6(self):
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "feature1": list(range(10)),
                "feature2": list(range(10, 20)),
                "feature3": list(range(20, 30)),
            }
        )
        df2 = pd.DataFrame(
            {"id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "target": list(range(30, 40))}
        )
        result = f_334(df1, df2)
        model = LinearRegression().fit(
            df1[["feature1", "feature2", "feature3"]], df2["target"]
        )
        expected_coefficients = model.coef_
        expected_intercept = model.intercept_
        self.assertListEqual(result["coefficients"], list(expected_coefficients))
        self.assertEqual(result["intercept"], expected_intercept)
    # Test the residuals plot's title and grid properties
    def test_case_7(self):
        df1 = pd.DataFrame(
            {
                "id": [1, 2, 3],
                "feature1": [1, 2, 3],
                "feature2": [4, 5, 6],
                "feature3": [7, 8, 9],
            }
        )
        df2 = pd.DataFrame({"id": [1, 2, 3], "target": [10, 11, 12]})
        result = f_334(df1, df2)
        self.assertEqual(result["residuals_plot"].get_title(), "Residuals Plot")
        self.assertTrue(result["residuals_plot"].grid)
        self.assertEqual(len(result["residuals_plot"].lines), 1)
