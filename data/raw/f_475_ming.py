import pandas as pd
import seaborn as sns
import unittest
from unittest.mock import patch
import matplotlib.pyplot as plt


def f_475(goals, penalties):
    """
    Visualize the distribution of goals and penalties for a number of teams and return the data as a DataFrame.

    Parameters:
    - goals (dict): A dictionary where keys are team names and values are numbers of goals scored.
    - penalties (dict): A dictionary where keys are team names and values are numbers of penalties incurred.

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame with the goals and penalties for the teams.
        - Axes: A seaborn pairplot visualization of goals and penalties distribution for the teams.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - seaborn

    Example:
    >>> goals = {'Team A': 3, 'Team B': 2, 'Team C': 1, 'Team D': 0, 'Team E': 2}
    >>> penalties = {'Team A': 1, 'Team B': 0, 'Team C': 2, 'Team D': 3, 'Team E': 1}
    >>> df, plot = f_475(goals, penalties)
    >>> print(df)
    >>> plot.show()
    """
    # Constants
    TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']

    data = []
    for team in TEAMS:
        team_goals = goals.get(team, 0)
        team_penalties = penalties.get(team, 0)
        data.append([team, team_goals, team_penalties])

    df = pd.DataFrame(data, columns=['Team', 'Goals', 'Penalties'])

    plot = sns.pairplot(df, hue='Team')

    return df, plot


# Unit tests for the function f_475
class TestF475(unittest.TestCase):
    @patch('matplotlib.pyplot.show')
    def test_visualization_output(self, mock_show):
        goals = {'Team A': 3, 'Team B': 2, 'Team C': 0}
        penalties = {'Team A': 1, 'Team B': 0, 'Team C': 2}
        df, _ = f_475(goals, penalties)
        self.assertEqual(list(df.columns), ['Team', 'Goals', 'Penalties'])
        self.assertEqual(df['Goals'].sum(), 5)
        self.assertEqual(df['Penalties'].sum(), 3)

    def test_empty_input(self):
        goals = {}
        penalties = {}
        df, _ = f_475(goals, penalties)
        # The dataframe should have the teams but with 0 goals and penalties.
        expected_data = {
            'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
            'Goals': [0, 0, 0, 0, 0],
            'Penalties': [0, 0, 0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df, expected_df)


    def test_plot_type(self):
        goals = {'Team A': 1}
        penalties = {'Team A': 1}
        _, plot = f_475(goals, penalties)
        self.assertIsInstance(plot, sns.axisgrid.PairGrid)

    def test_invalid_keys(self):
        goals = {'Team Z': 1}
        penalties = {'Team Z': 1}
        df, _ = f_475(goals, penalties)
        self.assertFalse('Team Z' in df['Team'].values)

    @patch('matplotlib.pyplot.show')
    def test_data_integrity(self, mock_show):
        goals = {'Team A': 3, 'Team B': 2, 'Team C': 1}
        penalties = {'Team A': 1, 'Team B': 2, 'Team C': 3}
        df, _ = f_475(goals, penalties)
        expected_data = {
            'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
            'Goals': [3, 2, 1, 0, 0],
            'Penalties': [1, 2, 3, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df, expected_df, check_like=True)


if __name__ == "__main__":
    unittest.main()
