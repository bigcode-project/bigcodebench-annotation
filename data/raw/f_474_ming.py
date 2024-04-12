import pandas as pd
from matplotlib import pyplot as plt
import unittest

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)


def f_474_and_plot(goals, penalties):
    """
    Calculates the net score for each team, returns a scores distribution DataFrame, and plots the distribution.

    Parameters:
    - goals (dict): A dictionary where keys are team names and values are the number of goals scored.
    - penalties (dict): A dictionary where keys are team names and values are the number of penalties incurred.

    Returns:
    - DataFrame: A pandas DataFrame with columns 'Team' and 'Score', representing each team's net score.

    Additionally, this function plots the score distribution using matplotlib to provide a visual representation of the scores.
    """
    scores_data = []

    for team in TEAMS:
        team_goals = goals.get(team, 0)
        team_penalties = penalties.get(team, 0)
        score = team_goals - team_penalties
        scores_data.append([team, score])

    scores_df = pd.DataFrame(scores_data, columns=['Team', 'Score'])
    scores_df['Score'] = scores_df['Score'].clip(*GOALS_RANGE)

    #Plotting (commented out for testing)
    plt.figure(figsize=(10, 6))
    plt.bar(scores_df['Team'], scores_df['Score'], color='skyblue')
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.title('Team Scores Distribution')
    plt.ylim(GOALS_RANGE[0] - 1, GOALS_RANGE[1] + 1)
    plt.grid(axis='y', linestyle='--')
    plt.show()

    return scores_df


# Unit Tests
class TestF474AndPlot(unittest.TestCase):
    def test_no_goals_no_penalties(self):
        goals, penalties = {}, {}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [0] * 5})
        pd.testing.assert_frame_equal(f_474_and_plot(goals, penalties), expected)

    def test_goals_no_penalties(self):
        goals = {team: index for index, team in enumerate(TEAMS, start=1)}
        penalties = {}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [1, 2, 3, 4, 5]})
        pd.testing.assert_frame_equal(f_474_and_plot(goals, penalties), expected)

    def test_goals_with_penalties(self):
        goals = {team: 5 for team in TEAMS}
        penalties = {team: 2 for team in TEAMS}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [3] * 5})
        pd.testing.assert_frame_equal(f_474_and_plot(goals, penalties), expected)

    def test_clipping_negative_scores(self):
        goals = {team: -15 for team in TEAMS}
        penalties = {team: 0 for team in TEAMS}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [-10] * 5})
        pd.testing.assert_frame_equal(f_474_and_plot(goals, penalties), expected)

    def test_clipping_positive_scores(self):
        goals = {team: 20 for team in TEAMS}
        penalties = {team: 0 for team in TEAMS}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [10] * 5})
        pd.testing.assert_frame_equal(f_474_and_plot(goals, penalties), expected)


if __name__ == '__main__':
    unittest.main()
