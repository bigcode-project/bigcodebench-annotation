import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def f_1782(df, target, random_state=42):
    """
    Train a linear regression model on a dataframe with a specific target column, allowing for a reproducible split using a random state.

    Parameters:
    df (DataFrame): The dataframe.
    target (str): The target column.
    random_state (int, optional): Random state for train_test_split (default is None).

    Returns:
    LinearRegression: The trained Linear Regression model.

    Raises:
    ValueError: If 'df' is not a DataFrame, 'target' is not a string, or 'target' column doesn't exist in 'df'.

    Requirements:
    - pandas
    - numpy
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LinearRegression

    Example:
    >>> np.random.seed(0)
    >>> df = pd.DataFrame({'A': np.random.normal(0, 1, 1000), 'B': np.random.exponential(1, 1000), 'C': np.random.uniform(-1, 1, 1000)})
    >>> model = f_1782(df, 'C', random_state=42)
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df must be a pandas DataFrame.")
    if not isinstance(target, str) or target not in df.columns:
        raise ValueError("target must be a string and a column name in the dataframe.")

    X = df.drop(target, axis=1)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
    model = LinearRegression().fit(X_train, y_train)
    return model

import unittest
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression

class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.df = pd.DataFrame({
            'A': np.random.normal(0, 1, 1000),
            'B': np.random.exponential(1, 1000),
            'C': np.random.uniform(-1, 1, 1000)
        })
    def test_return_type(self):
        model = f_1782(self.df, 'C')
        self.assertIsInstance(model, LinearRegression)

    def test_invalid_input_dataframe(self):
        with self.assertRaises(ValueError):
            f_1782("not a dataframe", 'C')

    def test_invalid_input_target(self):
        with self.assertRaises(ValueError):
            f_1782(self.df, 'D')

    def test_invalid_input_type_target(self):
        with self.assertRaises(ValueError):
            f_1782(self.df, 123)

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1782(pd.DataFrame(), 'C')

    def test_reproducibility_with_random_state(self):
        model1 = f_1782(self.df, 'C', random_state=42)
        model2 = f_1782(self.df, 'C', random_state=42)
        # Check if the models are trained on the same data split
        np.testing.assert_array_equal(model1.coef_, model2.coef_)
    
    def test_value(self):
        model = f_1782(self.df, 'C', random_state=42)
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(model.coef_.tolist()))
        expect = [0.025091496683364953, -0.011253722500115923]
        np.testing.assert_almost_equal(model.coef_.tolist(), expect, decimal=5, err_msg="Model coefficients should match the expected values")


    # ... other test cases ...

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()