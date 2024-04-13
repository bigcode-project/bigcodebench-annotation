import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

def f_660(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    '''
    Generate a dataset with five features sampled from the standard normal
    distribution and a target variable.
    The target value is created by computing the sum of the features and adding
    random numbers sampled from the standard normal distribution.
    Then cross-validate the dataset using a RandomForestRegressor model and
    return the mean cross-validation score.

    Parameters:
    - num_samples (int): Number of samples in the generated dataset. Default is 100.
    - n_estimators (int): Number of trees in RandomForestRegressor. Default is 100.
    - random_seed (int): Seed for random number generation. Default is None.
    - cv (int): Number of cross-validation folds. Default is 5.

    Returns:
    float: The mean cross-validation score.

    Raises:
    - ValueError: If num_samples / cv < 2

    Requirements:
    - numpy
    - pandas
    - sklearn.model_selection.cross_val_score
    - sklearn.ensemble.RandomForestRegressor

    Example:
    >>> cv_score = f_660(random_seed=21, cv=3, n_estimators=90, num_samples=28)
    >>> print(cv_score)
    -0.7631373607354236

    >>> cv_score = f_660()
    >>> print(cv_score)
    0.5932193408127572
    '''
    if num_samples / cv < 2:
        raise ValueError("num_samples / cv should be greater than or equal to 2.")

    np.random.seed(random_seed)
    X = np.random.randn(num_samples, 5)
    y = np.sum(X, axis=1) + np.random.randn(num_samples)
    
    model = RandomForestRegressor(n_estimators=n_estimators,
                                  random_state=random_seed
                                  )
    
    cv_scores = cross_val_score(model, X, y, cv=cv)
    
    return np.mean(cv_scores), model
    

import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RoundedDeterministicTestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class RoundedDeterministicTestCases(unittest.TestCase):

    def test_case_rng(self):
        'rng reproducability'
        result1, _ = f_660(random_seed=42)
        result2, _ = f_660(random_seed=42)

        self.assertAlmostEqual(result1, result2)

    def test_case_1(self):
        'default params'
        result, model = f_660(random_seed=1)
        self.assertAlmostEqual(result, 0.47332912782858)
        self.assertTrue(isinstance(model, RandomForestRegressor))

    def test_case_2(self):
        'random outcome with distinct seeds'
        result1, _ = f_660(random_seed=2)
        result2, _ = f_660(random_seed=3)

        self.assertFalse(result1 == result2)

    def test_case_3(self):
        result, model = f_660(random_seed=2, cv=2, n_estimators=2)
        self.assertAlmostEqual(result, 0.2316988319594362)
        self.assertTrue(isinstance(model, RandomForestRegressor))

    def test_case_4(self):
        'test exception'
        self.assertRaises(Exception,
                          f_660,
                          {'random_seed': 223, 'cv': 3,
                           'n_estimators': 100, 'num_samples': 4}
                          )


if __name__ == "__main__":
    run_tests()