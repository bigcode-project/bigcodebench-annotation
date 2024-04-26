import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def f_727(df, col_a='A', col_b='B', col_c='C', seed=None):
    """
    This function filters rows from the input DataFrame 'df' based on conditions in columns 'B' and 'C', 
    then uses linear regression to predict values in column 'B' using data from column 'A'. 
    Specifically, it selects rows where column 'B' values are greater than 50 and column 'C' values equal 900.
    
    A train test split of the remaining data is performed, where the test_size = 0.2
    and col_a is used as X value and col_b is used as Y values / target.

    This data is used to train a LinearRegression model. 

    The test split is used to generate predictions for col_b. These predictions
    are returned as well as the trained model.

    If df is empty or empty after the filtering, None is returned.
    If df does contain non numeric data None is returned.
    If the specified columns are not contained in df, None is returned.

    Parameters:
    df (DataFrame): The input pandas DataFrame with numeric data.
    col_a (str): The name of the first column to use for prediction (default is 'A').
    col_b (str): The name of the second column, the values of which are to be predicted (default is 'B').
    col_c (str): The name of the third column to use for row selection (default is 'C').
    seed (int, optional): random seed for the train test split. Default is None.

    Returns:
    ndarray: The predicted values for the filtered rows in column 'B', or None if input is invalid.
    LinearRegression: The trained linear regression model is returned, if 
    
    Requirements:
    - pandas
    - numpy
    - sklearn.model_selection
    - sklearn.linear_model

    Example:
    >>> df = pd.DataFrame({'A': np.random.randint(0, 100, 1000),
    ...                    'B': np.random.randint(0, 100, 1000),
    ...                    'C': np.random.choice([900, 800, 700, 600], 1000)})
    >>> predictions = f_727(df)
    >>> print(predictions)
    >>> print(model)
    [76.69220349 75.75947019 74.87337356 77.43839013 74.26709691 75.01328355
    76.08592685 76.45902017 76.69220349 74.5469169  75.05992022 74.96664689
    75.80610686 76.50565683 75.66619686 77.25184347 74.92001022 75.38637687
    72.8213603  72.96127029 73.94064026 73.24109028 76.59893016 76.03929018]
    LinearRegression()

    >>> df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
    ...                    'B': [10, 80, 80, 80, 80],
    ...                    'C': [900, 900, 900, 900, 900]})
    >>> predictions, model = f_727(df)
    >>> print(predictions) 
    >>> print(model)
    [80.]
    LinearRegression()
    """
    # Validating the input dataframe
    if df.empty or not all(col in df for col in [col_a, col_b, col_c]):
        return None  # Invalid input scenario
    
    try:
        # Ensuring the columns contain numeric data
        df[[col_a, col_b, col_c]] = df[[col_a, col_b, col_c]].apply(pd.to_numeric, errors='raise')
    except ValueError:
        return None  # Non-numeric data encountered

    # Filtering the data based on the conditions
    selected = df[(df[col_b] > 50) & (df[col_c] == 900)][[col_a, col_b]]

    if selected.empty:
        return None
    
    # Preparing the data for linear regression
    X_train, X_test, y_train, _ = train_test_split(selected[col_a].values.reshape(-1, 1),
                                                   selected[col_b].values,
                                                   test_size=0.2,
                                                   random_state=seed)

    # Applying linear regression
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    return predictions, model

import unittest
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression


class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        np.random.seed(0)  # Set a seed for reproducibility

    def test_normal_case(self):
        # Test with a normal DataFrame
        df = pd.DataFrame({'A': np.random.randint(0, 100, 100),
                           'B': np.random.randint(0, 100, 100),
                           'C': np.random.choice([900, 800], 100)})
        predictions, model = f_727(df, seed=12)
        self.assertIsInstance(model, LinearRegression)
        np.testing.assert_almost_equal(predictions, np.array([65.64, 67.24, 70.83, 64.04, 67.51, 66.44]), decimal=2)

    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        df = pd.DataFrame()
        predictions = f_727(df)
        self.assertIsNone(predictions)

    def test_missing_columns(self):
        # Test with a DataFrame missing one or more columns
        df = pd.DataFrame({'A': np.random.randint(0, 100, 100),
                           'C': np.random.choice([900, 800], 100)})
        predictions = f_727(df)
        self.assertIsNone(predictions)

    def test_non_numeric_data(self):
        # Test with non-numeric data
        df = pd.DataFrame({'A': ['a', 'b', 'c'],
                           'B': [1, 2, 3],
                           'C': [900, 900, 900]})
        predictions = f_727(df)
        self.assertIsNone(predictions)

    def test_no_rows_matching_criteria(self):
        # Test with no rows matching the criteria
        df = pd.DataFrame({'A': np.random.randint(0, 100, 100),
                           'B': np.random.randint(0, 50, 100),  # B values are always < 50
                           'C': np.random.choice([800, 700], 100)})  # C values are never 900
        predictions = f_727(df)
        self.assertIsNone(predictions)

    def test_large_dataset_performance(self):
        # Test with a very large DataFrame (performance test)
        df = pd.DataFrame({'test': np.random.randint(0, 100, 10000),
                           'hi': np.random.randint(0, 100, 10000),
                           'hello': np.random.choice([900, 800], 10000)})
        predictions, model = f_727(df, col_a='test', col_b='hi', col_c='hello')
        self.assertIsInstance(model, LinearRegression)
        self.assertIsNotNone(predictions)
        self.assertEqual(len(predictions), 500)

    def test_single_value_column(self):
        # Test with a DataFrame where one column has the same value
        df = pd.DataFrame({'A': [50] * 100,
                           'B': np.random.randint(50, 100, 100),
                           'C': [900] * 100})
        predictions, model = f_727(df, seed=1)
        self.assertIsInstance(model, LinearRegression)
        np.testing.assert_almost_equal(
            predictions,
            np.array([76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76., 76.]),
            decimal=2
            )

    def test_specific_return_values(self):
        # Test with known data to check specific return values
        df = pd.DataFrame({'A': [10, 20, 30, 40, 50],
                           'B': [60, 70, 80, 90, 100],
                           'C': [900, 900, 900, 900, 900]})
        predictions, model = f_727(df, seed=100)
        # Since the data is linear and simple, the model should predict close to the actual values
        expected_predictions = np.array([70])  # Assuming a perfect model
        np.testing.assert_almost_equal(predictions, expected_predictions)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()