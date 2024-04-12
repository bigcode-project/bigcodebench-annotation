import pandas as pd
import matplotlib.pyplot as plt
from random import randint, seed
import unittest

# Constants (they can be overridden with default parameters)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars


def f_477(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    '''
    Generate and record a Pandas DataFrame of the results of football matches for multiple teams
    with random goals and penalties, and create a bar plot of the results. Penalties are converted into fines according to the penalty costs.

    Parameters:
    - goals (int): The maximum number of goals a team can score in a match.
    - penalties (int): The maximum number of penalties a team can receive in a match.
    - teams (list of str, optional): A list of team names. Default is ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'].
    - penalty_cost (int, optional): Cost of a penalty in dollars. Default is 1000.
    - rng_seed (int, optional): Random seed for reproducibility. Default is None.

    Returns:
    - DataFrame: A pandas DataFrame containing columns for teams, their goals, and penalty costs.
    - Axes: A matplotlib Axes object representing the bar plot of the results.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - random

    Example:
    >>> df, ax = f_477(5, 3)
    >>> print(df.head())
    >>> plt.show()  # This will display the bar plot
    '''
    if rng_seed is not None:
        seed(rng_seed)

    # Ensure goals and penalties are treated as positive
    goals = abs(goals)
    penalties = abs(penalties)

    match_results = []
    for team in teams:
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        team_penalty_cost = penalty_cost * team_penalties
        match_results.append([team, team_goals, team_penalty_cost])

    results_df = pd.DataFrame(match_results, columns=['Team', 'Goals', 'Penalty Cost'])
    ax = results_df.plot(kind='bar', x='Team', y=['Goals', 'Penalty Cost'], stacked=True)
    plt.ylabel('Results')

    return results_df, ax


# Unit Tests
class TestF477(unittest.TestCase):
    def test_positive_outcomes(self):
        """Test the function with positive goals and penalties."""
        df, _ = f_477(5, 3, rng_seed=42)
        # Check if the DataFrame is not empty and has the correct columns
        self.assertFalse(df.empty)
        self.assertListEqual(list(df.columns), ['Team', 'Goals', 'Penalty Cost'])

    def test_zero_goals_penalties(self):
        """Test the function with zero goals and penalties."""
        df, _ = f_477(0, 0, teams=['Team A'], rng_seed=42)
        # Check that goals and penalty costs are 0
        self.assertTrue((df['Goals'] == 0).all())
        self.assertTrue((df['Penalty Cost'] == 0).all())

    def test_negative_input(self):
        """Ensure negative inputs are treated as positive."""
        df, _ = f_477(-5, -3, rng_seed=42)
        # Check for absence of negative values in results
        self.assertFalse((df['Goals'] < 0).any())
        self.assertFalse((df['Penalty Cost'] < 0).any())

    def test_single_team(self):
        """Test with a single team to ensure correct results."""
        df, _ = f_477(10, 5, teams=['Solo Team'], rng_seed=42)
        # Ensure only one row exists and contains 'Solo Team'
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Team'], 'Solo Team')

    def test_custom_penalty_cost(self):
        """Test the function with a custom penalty cost."""
        custom_cost = 500
        df, _ = f_477(5, 3, penalty_cost=custom_cost, rng_seed=42)
        # Validate that the penalty cost calculation uses the custom cost
        self.assertTrue((df['Penalty Cost'] % custom_cost == 0).all() or (df['Penalty Cost'] == 0).all())


if __name__ == '__main__':
    unittest.main()
