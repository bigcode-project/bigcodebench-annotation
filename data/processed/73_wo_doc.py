import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast

def task_func(db_file):
    """
    Load e-mail data from an SQLite database and convert it into a Pandas DataFrame. 
    Calculate the sum, mean, and variance of the list associated with each e-mail and then record these values.

    - The function expects the SQLite database to have a table named "EmailData" with columns 'email' and 'list'.
    - The column 'list' contains a string representation of the list. It should be converted before usage.
    - The function will return a DataFrame with additional columns 'sum', 'mean', and 'var' representing the calculated sum, mean, and variance respectively for each e-mail.

    Parameters:
    - db_file (str): The path to the SQLite database file.

    Returns:
    - tuple: A tuple containing:
      - DataFrame: A pandas DataFrame with email data including the calculated sum, mean, and variance.
      - Axes: A matplotlib Axes object representing the plotted bar chart of sum, mean, and variance.

    Requirements:
    - pandas
    - sqlite3
    - numpy
    - matplotlib.pyplot
    - ast

    Example:
    >>> df, ax = task_func('data/task_func/db_1.db')
    >>> print(df)
    """
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("SELECT * FROM EmailData", conn)
    df["list"] = df["list"].map(ast.literal_eval)
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)
    ax = df[['sum', 'mean', 'var']].plot(kind='bar')
    plt.show()
    return df, ax

import os
import shutil
from pathlib import Path
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_dir = "data/task_func"
        os.makedirs(self.test_dir, exist_ok=True)
        self.db_1 = os.path.join(self.test_dir, "db_1.db")
        if not os.path.exists(self.db_1) :
            Path(self.db_1).touch()
            conn = sqlite3.connect(self.db_1)
            c = conn.cursor()
            c.execute('''CREATE TABLE EmailData (email text, list text)''')
            df = pd.DataFrame(
                {
                    "email" : ["first@example.com", "second@example.com", "third@example.com"],
                    "list" : ["[12, 17, 29, 45, 7, 3]", "[1, 1, 3, 73, 21, 19, 12]", "[91, 23, 7, 14, 66]"]
                }
            )
            df.to_sql('EmailData', conn, if_exists='append', index = False)
        self.db_2 = os.path.join(self.test_dir, "db_2.db")
        if not os.path.exists(self.db_2) :
            Path(self.db_2).touch()
            conn = sqlite3.connect(self.db_2)
            c = conn.cursor()
            c.execute('''CREATE TABLE EmailData (email text, list text)''')
            df = pd.DataFrame(
                {
                    "email" : ["fourth@example.com", "fifth@example.com", "seventh@example.com", "eight@example.com"],
                    "list" : ["[12, 21, 35, 2, 1]", "[13, 4, 10, 20]", "[82, 23, 7, 14, 66]", "[111, 23, 4]"]
                }
            )
            df.to_sql('EmailData', conn, if_exists='append', index = False)
    
        self.db_3 = os.path.join(self.test_dir, "db_3.db")
        if not os.path.exists(self.db_3) :
            Path(self.db_3).touch()
            conn = sqlite3.connect(self.db_3)
            c = conn.cursor()
            c.execute('''CREATE TABLE EmailData (email text, list text)''')
            df = pd.DataFrame(
                {
                    "email" : ["ninth@example.com", "tenth@example.com"],
                    "list" : ["[1, 2, 3, 4, 5]", "[6, 7, 8, 9, 10]"]
                }
            )
            df.to_sql('EmailData', conn, if_exists='append', index = False)
    
    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_case_1(self):
        df, ax = task_func(self.db_1)
        
        # Test the DataFrame's shape and columns
        self.assertEqual(df.shape, (3, 5))
        self.assertListEqual(list(df.columns), ['email', 'list', 'sum', 'mean', 'var'])
        
        # Test a few values
        self.assertEqual(df.loc[0, 'email'], 'first@example.com')
        self.assertEqual(df.loc[0, 'sum'], 113)
        self.assertAlmostEqual(df.loc[1, 'mean'], 18.571429, places=6)
        self.assertAlmostEqual(df.loc[2, 'var'], 1066.160000, places=6)
        
        # Test if the plot has the correct data
        extracted_values = [bar.get_height() for bar in ax.patches] # extract bar height
        self.assertEqual(len(extracted_values), 3*3)
    
    def test_case_2(self):
        df, ax = task_func(self.db_2)
        
        # Test the DataFrame's shape and columns
        self.assertEqual(df.shape, (4, 5))
        self.assertListEqual(list(df.columns), ['email', 'list', 'sum', 'mean', 'var'])
        
        # Test a few values
        self.assertEqual(df.loc[0, 'email'], 'fourth@example.com')
        self.assertEqual(df.loc[0, 'sum'], 71)
        self.assertAlmostEqual(df.loc[1, 'mean'], 11.75, places=6)
        self.assertAlmostEqual(df.loc[2, 'var'], 896.240000, places=6)
        self.assertEqual(df.loc[3, 'sum'], 138)
        # Test if the plot has the correct data
        extracted_values = [bar.get_height() for bar in ax.patches] # extract bar height
        self.assertEqual(len(extracted_values), 4*3)
    def test_case_3(self):
        df, ax = task_func(self.db_3)
        
        # Test the DataFrame's shape and columns
        self.assertEqual(df.shape, (2, 5))
        self.assertListEqual(list(df.columns), ['email', 'list', 'sum', 'mean', 'var'])
        
        # Test a few values
        self.assertEqual(df.loc[0, 'email'], 'ninth@example.com')
        self.assertEqual(df.loc[0, 'sum'], 15.0)
        self.assertAlmostEqual(df.loc[1, 'mean'], 8.0, places=6)
        self.assertAlmostEqual(df.loc[1, 'var'], 2.0, places=6)
        
        # Test if the plot has the correct data
        extracted_values = [bar.get_height() for bar in ax.patches] # extract bar height
        self.assertEqual(len(extracted_values), 2*3)
