import pandas as pd
import random
from sklearn.model_selection import train_test_split

def f_312(n_data_points=10000, min_value=0.0, max_value=10.0, test_size=0.2):
    '''
    Generate a random set of floating-point numbers within a specified range, truncate each value to 3 decimal places,
    and divide the data into train and test sets based on a given test size.

    Parameters:
    - n_data_points (int): Number of data points to generate. Default is 10000.
    - min_value (float): Minimum value of the generated data points. Default is 0.0.
    - max_value (float): Maximum value of the generated data points. Default is 10.0.
    - test_size (float): Proportion of the dataset to include in the test split. Default is 0.2.

    Returns:
    tuple: A tuple with two pandas DataFrames (train set, test set).

    Requirements:
    - pandas
    - random
    - sklearn.model_selection

    Note:
    - The function use "Value" for the column name in the DataFrames (train set, test set) that being returned.

    Example:
    >>> random.seed(0)
    >>> train_data, test_data = f_312()
    >>> print(train_data.shape[0])
    8000
    >>> print(test_data.shape[0])
    2000
    >>> random.seed(0)
    >>> train_data, test_data = f_312(n_data_points=500, min_value=1.0, max_value=1.0, test_size=0.3)
    >>> print(train_data.shape[0])
    350
    >>> print(test_data.shape[0])
    150
    >>> print(test_data.iloc[0]['Value'])
    1.0
    '''

    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    train_data, test_data = train_test_split(data_df, test_size=test_size)

    return train_data, test_data

import unittest
import random
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        random.seed(0)
        train_data, test_data = f_312()
        self.assertEqual(len(train_data), 8000)  # 80% of 10000
        self.assertEqual(len(test_data), 2000)  # 20% of 10000
    def test_custom_parameters(self):
        random.seed(0)
        train_data, test_data = f_312(n_data_points=500, min_value=1.0, max_value=5.0, test_size=0.3)
        self.assertEqual(len(train_data), 350)  # 70% of 500
        self.assertEqual(len(test_data), 150)  # 30% of 500
        self.assertTrue(train_data['Value'].between(1.0, 5.0).all())
        self.assertTrue(test_data['Value'].between(1.0, 5.0).all())
    def test_train_test_size_ratio(self):
        random.seed(0)
        n_data_points = 1000
        test_size = 0.25
        train_data, test_data = f_312(n_data_points=n_data_points, test_size=test_size)
        expected_train_size = int(n_data_points * (1 - test_size))
        expected_test_size = n_data_points - expected_train_size
        self.assertEqual(len(train_data), expected_train_size)
        self.assertEqual(len(test_data), expected_test_size)
    def test_value_range(self):
        random.seed(0)
        min_value = 2.0
        max_value = 3.0
        train_data, _ = f_312(min_value=min_value, max_value=max_value)
        self.assertTrue(train_data['Value'].between(min_value, max_value).all())
    def test_value_precision(self):
        random.seed(0)
        train_data, _ = f_312()
        all_three_decimal = all(train_data['Value'].apply(lambda x: len(str(x).split('.')[1]) == 3))
        self.assertFalse(all_three_decimal)
