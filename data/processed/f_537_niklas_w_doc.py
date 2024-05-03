import pandas as pd
import random

def f_376(df):
    """
    Generate a DataFrame that contains savegames for a number of games between different teams.
    Each row of the input DataFrame represents a match, and contains two teams and their respective scores.
    The function adds a 'winner' column to the DataFrame, which is the team with the highest score in each match.
    If the scores are equal, the winner is should be randomly decided.
    
    Parameters:
    - df (pandas.DataFrame): The input DataFrame with columns 'team1', 'team2', 'score1', 'score2'.

    Requirements:
    - pandas
    - random
    
    Returns:
    - df (pandas.DataFrame): The DataFrame with the added 'winner' column.
    
    Example:
    >>> import numpy as np
    >>> import pandas as pd
    >>> df = pd.DataFrame({'team1': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D', 'Team E'], 20),
    ...                    'team2': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D', 'Team E'], 20),
    ...                    'score1': np.random.randint(0, 10, 20),
    ...                    'score2': np.random.randint(0, 10, 20)})
    >>> df = f_376(df)
    >>> assert 'winner' in df.columns
    >>> assert df['winner'].dtype == object
    >>> assert all(winner in ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'] for winner in df['winner'])
    """

    def determine_winner(row):
        if row['score1'] > row['score2']:
            return row['team1']
        elif row['score1'] < row['score2']:
            return row['team2']
        else:
            return random.choice([row['team1'], row['team2']])
    
    # Using pd.Series to explicitly create a new Series for the 'winner' column
    winner_series = pd.Series([determine_winner(row) for index, row in df.iterrows()], index=df.index)
    df['winner'] = winner_series
    return df

import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(42)
    def test_case_1(self):
        df = pd.DataFrame({'team1': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                           'team2': ['Team B', 'Team C', 'Team D', 'Team E', 'Team A'],
                            'score1': [1, 2, 3, 4, 5],
                            'score2': [2, 3, 4, 5, 6]})
        df = f_376(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team B', 'Team C', 'Team D', 'Team E', 'Team A'])))
    def test_case_2(self):
        df = pd.DataFrame({'team1': ['Team C', 'Team D', 'Team E', 'Team A', 'Team B'],
                           'team2': ['Team D', 'Team E', 'Team A', 'Team B', 'Team C'],
                           'score1': [99, 99, 99, 99, 99],
                           'score2': [99, 99, 99, 99, 99]})
        df = f_376(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team C', 'Team D', 'Team A', 'Team A', 'Team B'])))
    def test_case_3(self):
        df = pd.DataFrame({'team1': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                            'team2': ['Team B', 'Team C', 'Team D', 'Team E', 'Team A'],
                             'score1': [0, 0, 0, 0, 0],
                             'score2': [0, 0, 0, 0, 0]})
        df = f_376(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team A', 'Team B', 'Team D', 'Team D', 'Team E'])))
    
    def test_case_4(self):
        df = pd.DataFrame({'team1': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                            'team2': ['Team B', 'Team C', 'Team D', 'Team E', 'Team A'],
                             'score1': [10, 9, 8, 7, 6],
                             'score2': [9, 8, 7, 6, 5]})
        df = f_376(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team A', 'Team B', 'Team C', 'Team D', 'Team E'])))
    
    def test_case_5(self):
        df = pd.DataFrame({'team1': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                            'team2': ['Team B', 'Team C', 'Team D', 'Team E', 'Team A'],
                             'score1': [10, 9, 8, 7, 6],
                             'score2': [11, 12, 13, 14, 15]})
        df = f_376(df)
        self.assertTrue('winner' in df.columns)
        self.assertTrue(df['winner'].equals(pd.Series(['Team B', 'Team C', 'Team D', 'Team E', 'Team A'])))
