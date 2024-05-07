import numpy as np
import pandas as pd


def f_659(num_teams=5, num_games=100):
    """
    Create a Pandas DataFrame that displays the random scores of different teams in multiple games.
    The function generates random scores for each game played by each team and populates them in
    a DataFrame with index=teams, columns=games.

    Parameters:
    - num_teams (int, optional): The number of teams participating. Default is 5.
    - num_games (int, optional): The number of games played. Default is 100.

    Returns:
    DataFrame: The generated DataFrame containing random scores for each team in each game.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> df = f_659(num_teams=3, num_games=10)
    >>> type(df)
    <class 'pandas.core.frame.DataFrame'>
    """
    scores = np.random.randint(0, 101, size=(num_teams, num_games))
    teams = ['Team' + str(i) for i in range(1, num_teams + 1)]
    games = ['Game' + str(i) for i in range(1, num_games + 1)]
    df = pd.DataFrame(scores, index=teams, columns=games)
    return df

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = f_659()
        self.assertEqual(df.shape, (5, 100))
    def test_case_2(self):
        df = f_659(num_teams=3, num_games=10)
        self.assertEqual(df.shape, (3, 10))
        
    def test_case_3(self):
        df = f_659(num_teams=4, num_games=20)
        self.assertListEqual(list(df.index), ['Team1', 'Team2', 'Team3', 'Team4'])
        
    def test_case_4(self):
        df = f_659(num_teams=2, num_games=5)
        self.assertListEqual(list(df.columns), ['Game1', 'Game2', 'Game3', 'Game4', 'Game5'])
        
    def test_case_5(self):
        df = f_659(num_teams=2, num_games=5)
        self.assertTrue((df.dtypes == 'int64').all())
