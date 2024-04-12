import pandas as pd
import numpy as np


def f_499(num_teams=5, num_games=100):
    """
    Create a Pandas DataFrame that displays the random scores of different teams in multiple games.
    The function generates random scores for each game played by each team and populates them in a DataFrame.

    Parameters:
    - num_teams (int, optional): The number of teams participating. Default is 5.
    - num_games (int, optional): The number of games played. Default is 100.

    Returns:
    DataFrame: The generated DataFrame containing random scores for each team in each game.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> df = f_499(num_teams=3, num_games=10)
    >>> print(df)
           Game1  Game2  Game3  Game4  Game5  Game6  Game7  Game8  Game9  Game10
    Team1     23     56     12     78     45     67     89     10     34      60
    Team2     67     12     45     32     90     76     34     56     12      80
    Team3     12     45     78     90     67     45     23     12     34      67
    """
    scores = np.random.randint(0, 101, size=(num_teams, num_games))
    teams = ['Team' + str(i) for i in range(1, num_teams + 1)]
    games = ['Game' + str(i) for i in range(1, num_games + 1)]
    df = pd.DataFrame(scores, index=teams, columns=games)
    return df

import unittest

class TestGenerateGameScores(unittest.TestCase):
    def test_case_1(self):
        df = f_499()
        self.assertEqual(df.shape, (5, 100))

    def test_case_2(self):
        df = f_499(num_teams=3, num_games=10)
        self.assertEqual(df.shape, (3, 10))
        
    def test_case_3(self):
        df = f_499(num_teams=4, num_games=20)
        self.assertListEqual(list(df.index), ['Team1', 'Team2', 'Team3', 'Team4'])
        
    def test_case_4(self):
        df = f_499(num_teams=2, num_games=5)
        self.assertListEqual(list(df.columns), ['Game1', 'Game2', 'Game3', 'Game4', 'Game5'])
        
    def test_case_5(self):
        df = f_499(num_teams=2, num_games=5)
        self.assertTrue((df.dtypes == 'int64').all())

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGenerateGameScores))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()