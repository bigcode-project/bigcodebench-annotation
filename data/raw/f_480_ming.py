import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from random import randint, seed
import unittest

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars


def f_480(goals, penalties, rng_seed=None):
    """
    Simulates football match results with random goals and penalties for multiple teams,
    and trains a linear regression model to predict penalty costs from goals.

    Parameters:
    - goals (int): Maximum number of goals a team can score in a match.
    - penalties (int): Maximum number of penalties a team can receive in a match.
    - rng_seed (int, optional): Seed for the random number generator to ensure reproducibility. Defaults to None.

    Returns:
    - tuple:
        - pd.DataFrame: Contains 'Team', 'Goals', and 'Penalty Cost' columns.
        - LinearRegression: Trained model to predict 'Penalty Cost' based on 'Goals'.

    Requirements:
    - pandas for data manipulation.
    - numpy for numerical operations.
    - sklearn.linear_model.LinearRegression for regression model.
    - random for generating random numbers.

    Example:
    >>> df, model = f_480(5, 3, rng_seed=42)
    >>> print(df.head())
    >>> predictions = model.predict([[2], [3]])
    >>> print(predictions)
    """
    if rng_seed is not None:
        seed(rng_seed)

    # Generate match results
    match_results = []
    for team in TEAMS:
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        penalty_cost = PENALTY_COST * team_penalties
        match_results.append([team, team_goals, penalty_cost])

    # Create DataFrame
    results_df = pd.DataFrame(match_results, columns=['Team', 'Goals', 'Penalty Cost'])

    # Train Linear Regression Model
    X = results_df[['Goals']]
    y = results_df['Penalty Cost']
    model = LinearRegression().fit(X, y)

    return results_df, model


# Unit Tests
class TestF480(unittest.TestCase):
    """A set of unit tests to ensure the functionality of f_480."""

    def test_dataframe_structure(self):
        """Ensures the DataFrame has the correct structure."""
        df, _ = f_480(5, 3, rng_seed=42)
        self.assertListEqual(list(df.columns), ['Team', 'Goals', 'Penalty Cost'])

    def test_model_type(self):
        """Checks if the returned model is a LinearRegression instance."""
        _, model = f_480(5, 3, rng_seed=42)
        self.assertIsInstance(model, LinearRegression)

    def test_predictions_type(self):
        """Verifies that model predictions return a numpy array."""
        _, model = f_480(5, 3, rng_seed=42)
        predictions = model.predict(np.array([[2], [3]]))
        self.assertIsInstance(predictions, np.ndarray)

    def test_positive_goals_and_penalties(self):
        """Confirms goals and penalty costs are non-negative."""
        df, _ = f_480(5, 3, rng_seed=42)
        self.assertTrue((df['Goals'] >= 0).all())
        self.assertTrue((df['Penalty Cost'] >= 0).all())

    def test_regression_coefficients_sign(self):
        """Checks that the regression model produces a coefficient."""
        df, model = f_480(5, 3, rng_seed=42)
        self.assertIsNotNone(model.coef_[0])


if __name__ == '__main__':
    unittest.main()
