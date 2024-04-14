import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def f_593(df, target_column):
    """
    Perform a logistic regression on a DataFrame to predict a specific target column.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - target_column (str): The target column name.

    Returns:
    - accuracy (float): The accuracy of the logistic regression model.

    Example:
    >>> np.random.seed(42)
    >>> data = np.random.randint(0, 100, size=(100, 4))  # Using np to generate random data
    >>> columns = ['A', 'B', 'C', 'target']
    >>> df = pd.DataFrame(data, columns=columns)  # Explicitly using pd to create DataFrame
    >>> f_593(df, 'target')
    0.0
    """
    if target_column not in df.columns:
        raise ValueError('Target column does not exist in DataFrame')

    X = df.drop(columns=target_column)  # Operate directly on the DataFrame
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [0, 1, 0]})
        self.assertEqual(f_593(df, 'C'), 0.0)
    def test_case_2(self):
        df = pd.DataFrame({'A': [1, 2, 3, -10], 'B': [4, 5, 6, -10], 'C': [1, 1, 1, 0]})
        self.assertEqual(f_593(df, 'C'), 1.0)
    def test_case_3(self):
        df = pd.DataFrame({'A': [1, 2, 3, -10], 'B': [4, 5, 6, -10], 'C': [0, 0, 0, 1]})
        self.assertEqual(f_593(df, 'C'), 1.0)
    def test_case_4(self):
        df = pd.DataFrame({'A': [-10, 2, 3, -10], 'B': [-10, 5, 6, -10], 'C': [1, 0, 0, 1]})
        self.assertEqual(f_593(df, 'C'), 1.0)
    def test_case_5(self):
        df = pd.DataFrame({'A': [-10, 2, 3, -10], 'B': [-10, 5, 6, -10], 'C': [0, 1, 1, 0]})
        self.assertEqual(f_593(df, 'C'), 1.0)
