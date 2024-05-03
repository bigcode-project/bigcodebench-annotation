import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def f_720(data, target, test_size=0.2, random_state=None):
    """
    Trains a RandomForestRegressor model and returns the mean squared error 
    (MSE) of the predictions and the model.

    First the data is split into a train and test set. The fractional size of
    the test set is determined by 'test_size'. Then a RandomForestRegressor is
    trained on the data, using the in 'target' specified column as target.

    The MSE on the test set is calculated. 

    Parameters:
    data (pd.DataFrame): A DataFrame containing the dataset, including the target column.
    target (str): The name of the target column in the data DataFrame.
    test_size (float, optional): The proportion of the dataset to include in the test split. Default is 0.2.
    random_state (int, optional): Controls both the randomness of the bootstrapping of the samples used 
                                   when building trees and the sampling of the features to consider when 
                                   looking for the best split at each node. Default is None.

    Returns:
    float: The mean squared error of the model's predictions on the test set.

    Raises:
    ValueError: If the input DataFrame is empty or the target column name is not in the DataFrame.

    Requirements:
    - pandas
    - sklearn: sklearn.model_selection.train_test_split,
               sklearn.ensemble.RandomForestRegressor,
               sklearn.metrics.mean_squared_error

    Examples:
    >>> df = pd.DataFrame({'feature1': [1,2,3], 'feature2': [2,3,4], 'target': [5,6,7]})
    >>> f_720(df, 'target')
    (1.5625, RandomForestRegressor())

    >>> df = pd.DataFrame({'feature1': [1, 2, 3, 53], 'feature2': [2, 3, 4, 1], 'feature3': [-12, -2, 4.2, -2], 'trgt': [5, 6, 7, 1]})
    >>> f_720(df, 'trgt', random_state=12, test_size=0.4)
    (2.7250000000000005, RandomForestRegressor(random_state=12))
    """
    if data.empty or target not in data.columns:
        raise ValueError("Data must not be empty and target column must exist in the DataFrame.")

    # Splitting the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(columns=[target]), data[target], test_size=test_size, random_state=random_state
    )

    # Training the model
    model = RandomForestRegressor(random_state=random_state)
    model.fit(X_train, y_train)

    # Making predictions and returning the MSE
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse, model

import unittest
import pandas as pd
import numpy as np
from faker import Faker
from sklearn.ensemble import RandomForestRegressor
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.fake = Faker() 
    def test_case_1(self):
        # Simple test case
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'target': [10, 11, 12]})
        mse, model = f_720(data, 'target', random_state=2)
        self.assertAlmostEqual(mse, 1.537, delta=0.2)
        self.assertTrue(isinstance(model, RandomForestRegressor))
    def test_case_2(self):
        # Random test case with larger data
        np.random.seed(42)
        data = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        data['target'] = np.random.randint(0, 100, size=(100,))
        mse, model = f_720(data, 'target', random_state=12)
        self.assertAlmostEqual(mse, 1230, delta=20)
        self.assertTrue(isinstance(model, RandomForestRegressor))
    def test_case_3(self):
        # Random test case with different test_size
        np.random.seed(42)
        data = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        data['target'] = np.random.randint(0, 100, size=(100,))
        mse, model = f_720(data, 'target', test_size=0.3, random_state=12)
        self.assertAlmostEqual(mse, 1574, delta=20)
        self.assertTrue(isinstance(model, RandomForestRegressor))
    def test_case_4(self):
        # test working random state
        np.random.seed(42)
        data = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        data['target'] = np.random.randint(0, 100, size=(100,))
        mse1, model = f_720(data, 'target', test_size=0.3, random_state=12)
        mse2, model = f_720(data, 'target', test_size=0.3, random_state=12)
        self.assertAlmostEqual(mse1, mse2)
    def test_case_5(self):
        # Random test case with Faker-generated data
        self.fake.seed_instance(42)
        data = pd.DataFrame({'A': [self.fake.random_int(min=0, max=100) for _ in range(100)],
                             'B': [self.fake.random_int(min=0, max=100) for _ in range(100)],
                             'C': [self.fake.random_int(min=0, max=100) for _ in range(100)],
                             'D': [self.fake.random_int(min=0, max=100) for _ in range(100)],
                             'target': [self.fake.random_int(min=0, max=100) for _ in range(100)]})
        mse, model = f_720(data, 'target')
        self.assertAlmostEqual(mse, 1119, delta=20)
        self.assertTrue(isinstance(model, RandomForestRegressor))
    def test_edge_case_empty_dataset(self):
        # Edge case: Empty dataset
        data = pd.DataFrame(columns=['A', 'B', 'C', 'target'])
        with self.assertRaises(ValueError):
            f_720(data, 'target')
    def test_edge_case_very_small_dataset(self):
        # Edge case: Very small dataset
        data = pd.DataFrame({'A': [1], 'B': [2], 'C': [3], 'target': [4]})
        with self.assertRaises(ValueError):
            f_720(data, 'target')
    def test_edge_case_invalid_test_size(self):
        # Edge case: Invalid test size
        data = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        data['target'] = np.random.randint(0, 100, size=(100,))
        with self.assertRaises(ValueError):
            f_720(data, 'target', test_size=-0.1)
