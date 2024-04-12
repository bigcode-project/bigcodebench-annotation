import pandas as pd
from random import randint, seed
import unittest
from pandas.testing import assert_frame_equal

# Method
def f_476(goals, penalties, rng_seed=None):
    """
    Generate a Pandas DataFrame of the results of football matches for multiple teams, incorporating random goals and penalties. Penalties are converted into fines using a predefined cost.

    Parameters:
    - goals (int): The maximum number of goals a team can score in a match. Must be non-negative.
    - penalties (int): The maximum number of penalties a team can receive in a match. Must be non-negative.
    - rng_seed (int, optional): Seed for the random number generator to ensure reproducible results. Defaults to None.

    Returns:
    - pd.DataFrame: A pandas DataFrame with columns ['Team', 'Match Result'], detailing each team's goals and accumulated fines.

    Requirements:
    - pandas>=1.1.5
    - Python standard library: random

    Example:
    >>> seed(42)  # Setting seed for reproducibility in this example
    >>> results = f_476(5, 3, 42)
    >>> print(results)
         Team      Match Result
    0  Team A  (3 goals, $3000)
    1  Team B  (1 goals, $2000)
    ...
    """
    # Constants
    TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    PENALTY_COST = 1000  # in dollars

    if rng_seed is not None:
        seed(rng_seed)  # Set seed for reproducibility

    match_results = []
    for team in TEAMS:
        team_goals = randint(0, abs(goals))
        team_penalties = randint(0, abs(penalties))
        penalty_cost = PENALTY_COST * team_penalties
        result_string = f"({team_goals} goals, ${penalty_cost})"
        match_results.append([team, result_string])

    results_df = pd.DataFrame(match_results, columns=['Team', 'Match Result'])

    return results_df

# Test Suite
class TestF476(unittest.TestCase):
    def setUp(self):
        self.teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
        self.penalty_cost = 1000  # Match the PENALTY_COST used in f_476

    def test_goals_and_penalties_within_range(self):
        """Test that goals and penalties fall within specified ranges."""
        max_goals = 5
        max_penalties = 3
        df = f_476(max_goals, max_penalties)

        for _, row in df.iterrows():
            # Correctly extract goals and penalty cost from the 'Match Result' string
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])

            # Check if goals are within the expected range
            self.assertTrue(0 <= goals <= max_goals, f"Goals {goals} not within range 0 to {max_goals}")

            # Calculate the maximum possible penalty cost and check it
            max_penalty_cost = max_penalties * self.penalty_cost
            self.assertTrue(0 <= penalty_cost <= max_penalty_cost,
                            f"Penalty cost {penalty_cost} not within range 0 to {max_penalty_cost}")

    def test_negative_input_handling(self):
        """Test that negative inputs are handled correctly."""
        max_goals = -5
        max_penalties = -3
        df = f_476(max_goals, max_penalties)

        for _, row in df.iterrows():
            # Correctly extract and check values as before, ensuring no negative values are produced
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])

            self.assertTrue(0 <= goals, "Goals are negative which is not expected")
            self.assertTrue(0 <= penalty_cost, "Penalty cost is negative which is not expected")

    def test_zero_goals_and_penalties(self):
        """Test that the function handles 0 goals and 0 penalties correctly."""
        df = f_476(0, 0)
        for _, row in df.iterrows():
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])
            self.assertEqual(goals, 0, "Goals should be 0 when max_goals is set to 0")
            self.assertEqual(penalty_cost, 0, "Penalty cost should be 0 when max_penalties is set to 0")

    def test_extremely_high_values(self):
        """Test the function with extremely high values for goals and penalties."""
        max_goals = 1000
        max_penalties = 500
        df = f_476(max_goals, max_penalties)
        for _, row in df.iterrows():
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])
            self.assertTrue(0 <= goals <= max_goals, f"Goals {goals} not within range 0 to {max_goals}")
            max_penalty_cost = max_penalties * self.penalty_cost
            self.assertTrue(0 <= penalty_cost <= max_penalty_cost, f"Penalty cost {penalty_cost} not within range 0 to {max_penalty_cost}")

    def test_mixed_values(self):
        """Test the function with a mix of low and high values for goals and penalties."""
        max_goals = 10
        max_penalties = 1
        df = f_476(max_goals, max_penalties)
        for _, row in df.iterrows():
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])
            self.assertTrue(0 <= goals <= max_goals, f"Goals {goals} not within range 0 to {max_goals}")
            max_penalty_cost = max_penalties * self.penalty_cost
            self.assertTrue(0 <= penalty_cost <= max_penalty_cost, f"Penalty cost {penalty_cost} not within range 0 to {max_penalty_cost}")


if __name__ == '__main__':
    unittest.main()
