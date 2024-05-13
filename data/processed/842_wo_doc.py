import sqlite3
import random


def task_func(db_path,
          num_entries,
          users=['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
          countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
          random_seed=None):
    """
    Generate an SQLite database to a given file path with random user data.

    The user data consists of a table named 'users' with columns:
        - id (integer): Used as Primary Key. numbering of entries starting at 0.
        - name (string): name of the user. sampled from 'users'
        - age (int): age of the user, where 20 <= age <= 60.
        - country (string): sampled from 'countries'

    The number of entries in the database is determined by num_entries.

    Parameters:
    db_path (str): The file path where the SQLite database should be created.
    num_entries (int): The number of entries of random data to generate.
    users (list of str, optional): List of user names to choose from. Defaults to ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'].
    countries (list of str, optional): List of countries to choose from. Defaults to ['USA', 'UK', 'Canada', 'Australia', 'India'].
    random_seed (int, optional): Seed used in rng. Defaults to Nonee.
    
    Returns:
    str: The file path of the generated SQLite database.

    Requirements:
    - sqlite3
    - random

    Example:
    >>> task_func('/tmp/users.db', 100)
    '/tmp/users.db'

    >>> path = task_func('test.db', num_entries=3, random_seed=2, users=['Simon', 'Albert'])
    >>> conn = sqlite3.connect('test.db')
    >>> c = conn.cursor()
    >>> c.execute("SELECT * FROM users")
    >>> c.fetchall()
    [(1, 'Simon', 25, 'USA'), (2, 'Viola', 30, 'Canada'), (3, 'Viola', 58, 'UK')]
    >>> c.execute("PRAGMA table_info(users)")
    >>> c.fetchall()
    [(0, 'id', 'INTEGER', 0, None, 1),
    (1, 'name', 'TEXT', 0, None, 0),
    (2, 'age', 'INTEGER', 0, None, 0),
    (3, 'country', 'TEXT', 0, None, 0)]
    """

    random.seed(random_seed)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE users
        (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, country TEXT)
    ''')
    for _ in range(num_entries):
        user = random.choice(users)
        age = random.randint(20, 60)
        country = random.choice(countries)
        c.execute('INSERT INTO users (name, age, country) VALUES (?, ?, ?)', (user, age, country))
    conn.commit()
    conn.close()
    return db_path

import unittest
import sqlite3
from faker import Faker
import os
import tempfile
import pandas as pd
class TestCases(unittest.TestCase):
    default_users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
    default_countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    def setUp(self):
        self.fake = Faker()
        self.temp_dir = tempfile.mkdtemp()  # Create a temporary directory for our databases
    def test_rng(self):
        db_path1 = os.path.join(self.temp_dir, self.fake.file_name(extension="db"))
        output_path1 = task_func(db_path1, 45, random_seed=12)
        db_path2 = os.path.join(self.temp_dir, self.fake.file_name(extension="db"))
        output_path2 = task_func(db_path2, 45, random_seed=12)
        df1 = self._load_table_as_df(db_path=output_path1)
        df2 = self._load_table_as_df(db_path=output_path2)
        pd.testing.assert_frame_equal(df1, df2, check_dtype=False)
    def test_case_1(self):
        # Test with default users and 5 entries
        db_path = os.path.join(self.temp_dir, self.fake.file_name(extension="db"))
        output_path = task_func(db_path, 5, random_seed=1)
        self.assertEqual(db_path, output_path)
        self.assertTrue(self._validate_db_structure(db_path))
        self.assertEqual(self._get_db_entries_count(db_path), 5)
        df = self._load_table_as_df(db_path=db_path)
        self.assertTrue(set(df['name'].to_list()).issubset(self.default_users))
        self.assertTrue(set(df['country'].to_list()).issubset(self.default_countries))
        expected = pd.DataFrame({
            'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
            'name': {0: 'Bob', 1: 'Charlie', 2: 'Dave', 3: 'Bob', 4: 'Alice'},
            'age': {0: 56, 1: 27, 2: 50, 3: 26, 4: 44},
            'country': {0: 'USA',
            1: 'Australia',
            2: 'Australia',
            3: 'Australia',
            4: 'Australia'}
        })
        pd.testing.assert_frame_equal(df, expected, check_dtype=False)
    def test_case_2(self):
        # Test with custom users and 10 entries
        db_path = os.path.join(self.temp_dir, self.fake.file_name(extension="db"))
        custom_users = ['Simon', 'Albert', 'Viola', 'Lisa', 'Monica']
        output_path = task_func(db_path, 10, custom_users, random_seed=2)
        self.assertEqual(db_path, output_path)
        self.assertTrue(self._validate_db_structure(db_path))
        self.assertEqual(self._get_db_entries_count(db_path), 10)
        df = self._load_table_as_df(db_path=db_path)
        self.assertTrue(set(df['name'].to_list()).issubset(custom_users))
        self.assertTrue(set(df['country'].to_list()).issubset(self.default_countries))
        expected = pd.DataFrame({
            'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10},
            'name': {0: 'Simon',
            1: 'Viola',
            2: 'Viola',
            3: 'Monica',
            4: 'Albert',
            5: 'Monica',
            6: 'Lisa',
            7: 'Simon',
            8: 'Lisa',
            9: 'Lisa'},
            'age': {0: 25, 1: 30, 2: 58, 3: 22, 4: 47, 5: 43, 6: 52, 7: 21, 8: 40, 9: 53},
            'country': {0: 'USA',
            1: 'Canada',
            2: 'UK',
            3: 'India',
            4: 'Australia',
            5: 'India',
            6: 'Canada',
            7: 'Canada',
            8: 'Australia',
            9: 'UK'}
        })
        pd.testing.assert_frame_equal(df, expected, check_dtype=False)
    def test_case_3(self):
        # Test with 0 entries
        db_path = os.path.join(self.temp_dir, self.fake.file_name(extension="db"))
        output_path = task_func(db_path, 0, random_seed=3)
        self.assertEqual(db_path, output_path)
        self.assertTrue(self._validate_db_structure(db_path))
        self.assertEqual(self._get_db_entries_count(db_path), 0)
    def test_case_4(self):
        # Test with a large number of entries (1000 entries) and custom countries
        db_path = os.path.join(self.temp_dir, self.fake.file_name(extension="db"))
        custom_countries = ['test', 'hi', 'abc']
        output_path = task_func(db_path, 1000, countries=custom_countries, random_seed=4)
        self.assertEqual(db_path, output_path)
        self.assertTrue(self._validate_db_structure(db_path))
        self.assertEqual(self._get_db_entries_count(db_path), 1000)
        df = self._load_table_as_df(db_path=db_path)
        self.assertTrue(set(df['country'].to_list()).issubset(custom_countries))
        self.assertTrue(set(df['name'].to_list()).issubset(self.default_users))
    def test_case_5(self):
        # Test with special characters in file path and 15 entries
        db_path = os.path.join(self.temp_dir, self.fake.file_name(extension="db").replace("/", "//"))
        output_path = task_func(db_path, 15, random_seed=55)
        self.assertEqual(db_path, output_path)
        self.assertTrue(self._validate_db_structure(db_path))
        self.assertEqual(self._get_db_entries_count(db_path), 15)
        df = self._load_table_as_df(db_path=db_path)
        self.assertTrue(set(df['name'].to_list()).issubset(self.default_users))
    def _validate_db_structure(self, db_path):
        """Validate if the DB has the correct structure."""
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in c.fetchall()]
        conn.close()
        expected_columns = ['id', 'name', 'age', 'country']
        return set(columns) == set(expected_columns)
    def _get_db_entries_count(self, db_path):
        """Return the number of entries in the DB."""
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM users")
        count = c.fetchone()[0]
        conn.close()
        return count
    
    def _load_table_as_df(self, db_path):
        """return sql table as dataframe"""
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM users", conn)
        return df
