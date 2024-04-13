import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def f_733(csv_file_path, attribute, test_size=0.2, random_state=42):
    '''
    Train a linear regression model on a dataset and predict the value of a particular attribute.
    This function reads a CSV file to create a pandas DataFrame, separates the data into 
    training and testing sets, and performs linear regression. It returns the predicted 
    values for the testing set as well as the trained model.

    Parameters:
    csv_file_path (str): The path to the CSV file containing the data set.
    attribute (str): The attribute to predict.
    test_size (float, optional): Proportion of the dataset to include in the test split. Default is 0.2.
    random_state (int, optional): Seed used by the random number generator. Default is 42.

    Returns:
    tuple: A tuple containing:
        - model (LinearRegression): The trained linear regression model.
        - predictions (ndarray): An array of predicted values for the test set.

    Requirements:
    - pandas
    - sklearn.linear_model
    - sklearn.model_selection

    Example:
    >>> model, predictions = f_733("/path/to/data.csv", "target")
    >>> print(predictions)
    [123.45, ..., 126.78]

    >>> model, predictions = f_733("/path/to/test.csv", "target")
    >>> print(predictions)
    [1.2423, 4.2313, 28.2219, 10.3092]

    Note: The function assumes that the CSV file is correctly formatted and that the specified attribute exists.
    '''
    df = pd.read_csv(csv_file_path)
    X = df.drop(columns=[attribute])
    y = df[attribute]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    return model, predictions
    

import unittest
import numpy as np
import os
from sklearn.linear_model import LinearRegression

class TestCases(unittest.TestCase):
    def setUp(self):
        # Absolute path to the CSV file (modify this path to where you saved the f_733_data_simon/mock_data.csv file)
        self.csv_file_path = os.path.join("f_733_data_simon", "mock_data.csv")  # or provide the correct path

    def test_valid_data(self):
        # Test the function with valid data and default parameters
        model, predictions = f_733(csv_file_path=self.csv_file_path, attribute="target")
        self.assertIsInstance(model, LinearRegression)  # Check that a model is returned
        self.assertIsNotNone(predictions)  # Check that predictions are returned
        self.assertIsInstance(predictions, np.ndarray)  # Predictions should be a numpy array
        self.assertTrue(len(predictions) > 0)  # There should be at least one prediction

    def test_different_test_size(self):
        # Test the function with a different test size
        model, predictions = f_733(csv_file_path=self.csv_file_path, attribute="target", test_size=0.1)
        self.assertIsInstance(model, LinearRegression)  # Check that a model is returned
        self.assertIsNotNone(predictions)  # Check that predictions are returned
        self.assertIsInstance(predictions, np.ndarray)  # Predictions should be a numpy array
        self.assertTrue(len(predictions) > 0)  # There should be at least one prediction

    def test_different_test_size(self):
        # check actual prediction s
        model, predictions = f_733(csv_file_path=self.csv_file_path, attribute="target", test_size=0.05, random_state=12)
        self.assertIsInstance(model, LinearRegression)  # Check that a model is returned
        self.assertIsNotNone(predictions)  # Check that predictions are returned
        self.assertIsInstance(predictions, np.ndarray)  # Predictions should be a numpy array
        exp = [50.79382830317221, 55.43165477762747, 55.243834423268666, 49.64829868690964, 51.81468104159754]
        
        for i, expected in enumerate(exp):
            self.assertAlmostEqual(predictions[i], exp[i], places=2)

    def test_invalid_csv_path(self):
        # Test the function with an invalid CSV path
        with self.assertRaises(FileNotFoundError):
            f_733(csv_file_path="non_existent.csv", attribute="target")

    def test_invalid_attribute(self):
        # Test the function with an attribute not present in the CSV
        with self.assertRaises(KeyError):
            f_733(csv_file_path=self.csv_file_path, attribute="invalid_attribute")

    def test_predicting_non_numerical_data(self):
        # If the CSV contains non-numerical data for the target, the function should handle it gracefully
        # Note: This requires a separate CSV file with non-numerical target values.
        with self.assertRaises(ValueError):
            path = os.path.join("f_733_data_simon", "mock_data_with_non_numerical.csv")
            f_733(csv_file_path=path, attribute="target")

def run_tests():
    # Function to execute the test cases
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()