import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
from random import choice

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COST = [100, 200, 300, 400, 500]


def f_473(goals: dict, penalties: dict) -> pd.DataFrame:
    """
    Create a match report for teams with goals scored and penalties conceded.

    Parameters:
    - goals (dict): Team names as keys, numbers of goals scored as values.
    - penalties (dict): Team names as keys, numbers of penalties incurred as values.

    Returns:
    - pd.DataFrame: DataFrame with Team, Goals, Penalties, Penalties Cost, Performance Score.

    Requirements:
    - pandas: For DataFrame creation and manipulation.
    - numpy: For numerical calculations.
    - random.choice: For selecting penalties cost randomly.

    Example:
    >>> goals = {'Team A': 3, 'Team B': 2}
    >>> penalties = {'Team A': 1, 'Team B': 0}
    >>> report = f_473(goals, penalties)
    >>> print(report)
    """
    report_data = []
    for team in TEAMS:
        team_goals = goals.get(team, 0)
        team_penalties = penalties.get(team, 0)
        penalties_cost = team_penalties * choice(PENALTIES_COST)
        performance_score = np.max([0, team_goals - team_penalties])
        report_data.append({
            'Team': team,
            'Goals': team_goals,
            'Penalties': team_penalties,
            'Penalties Cost': penalties_cost,
            'Performance Score': performance_score
        })

    report_df = pd.DataFrame(report_data)
    return report_df


class TestF473(unittest.TestCase):

    @patch('f_473_ming.choice', return_value=400)
    def test_goals_greater_than_penalties(self, mock_choice):
        goals = {'Team A': 4, 'Team B': 2, 'Team C': 0, 'Team D': 0, 'Team E': 0}
        penalties = {'Team A': 1, 'Team B': 1, 'Team C': 0, 'Team D': 0, 'Team E': 0}
        expected_data = {
            'Team': TEAMS,
            'Goals': [4, 2, 0, 0, 0],
            'Penalties': [1, 1, 0, 0, 0],
            'Penalties Cost': [400, 400, 0, 0, 0],  # Mocked value is reflected here
            'Performance Score': [3, 1, 0, 0, 0]  # Assuming Performance Score is Goals - Penalties
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))

    @patch('f_473_ming.choice', return_value=200)
    def test_some_teams_missing(self, mock_choice):
        goals = {'Team A': 2, 'Team E': 5}
        penalties = {'Team A': 0, 'Team E': 3}
        expected_data = {
            'Team': TEAMS,
            'Goals': [2, 0, 0, 0, 5],
            'Penalties': [0, 0, 0, 0, 3],
            'Penalties Cost': [0, 0, 0, 0, 600],
            'Performance Score': [2, 0, 0, 0, 2]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch('f_473_ming.choice', return_value=500)
    def test_penalties_greater_than_goals(self, mock_choice):
        goals = {'Team B': 1, 'Team D': 2}
        penalties = {'Team B': 3, 'Team D': 5}
        expected_data = {
            'Team': TEAMS,
            'Goals': [0, 1, 0, 2, 0],
            'Penalties': [0, 3, 0, 5, 0],
            'Penalties Cost': [0, 1500, 0, 2500, 0],
            'Performance Score': [0, 0, 0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch('f_473_ming.choice', return_value=300)
    def test_all_teams_penalty(self, mock_choice):
        goals = {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}
        penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 1, 'Team E': 4}
        expected_penalties_cost = [penalty * mock_choice.return_value for penalty in penalties.values()]
        expected_data = {
            'Team': list(goals.keys()),  # The list of teams from the goals dictionary keys
            'Goals': list(goals.values()),  # The list of goals from the goals dictionary values
            'Penalties': list(penalties.values()),  # The list of penalties from the penalties dictionary values
            'Penalties Cost': expected_penalties_cost,
            'Performance Score': [0] * len(TEAMS)  # A list of zeros for performance score
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))

    @patch('f_473_ming.choice', return_value=100)
    def test_empty_goals_and_penalties(self, mock_choice):
        goals = {}
        penalties = {}
        expected_data = {
            'Team': TEAMS,
            'Goals': [0, 0, 0, 0, 0],
            'Penalties': [0, 0, 0, 0, 0],
            'Penalties Cost': [0, 0, 0, 0, 0],
            'Performance Score': [0, 0, 0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)


    @patch('f_473_ming.choice', return_value=300)
    def test_no_penalties(self, mock_choice):
        goals = {'Team A': 3, 'Team B': 2}
        penalties = {'Team A': 0, 'Team B': 0}
        expected_data = {
            'Team': ['Team A', 'Team B'] + ['Team C', 'Team D', 'Team E'],
            'Goals': [3, 2] + [0, 0, 0],
            'Penalties': [0, 0] + [0, 0, 0],
            'Penalties Cost': [0, 0] + [0, 0, 0],
            'Performance Score': [3, 2] + [0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)


if __name__ == '__main__':
    unittest.main()