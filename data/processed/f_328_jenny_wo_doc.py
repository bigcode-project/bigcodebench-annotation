import sqlite3
import pandas as pd


def f_306(db_file: str, query: str) -> pd.DataFrame:
    """Query an SQLite database and return the results.

    This function connects to a given SQLite database, executes a given SQL query,
    and returns the results as a pandas DataFrame.

    Parameters:
    - db_file (str): Path to the SQLite database file.
    - query (str): SQL query to execute.

    Returns:
    - pd.DataFrame: A DataFrame containing the results of the executed query.

    Requirements:
    - sqlite3
    - pandas

    Example:
    >>> db_file = 'sample_database.db'
    >>> df = f_306(db_file, "SELECT * FROM users WHERE name = 'John Doe'")
    pd.DataFrame:
    id        name  age
    --  ----------  ---
    ..  John Doe   ..
    >>> df = f_306(db_file, "SELECT age, COUNT(*) AS count FROM users GROUP BY age")
    pd.DataFrame:
    age  count
    ---  -----
    25   3
    """
    with sqlite3.connect(db_file) as conn:
        return pd.read_sql_query(query, conn)

import unittest
import sqlite3
from faker import Faker
import os
class TestCases(unittest.TestCase):
    
    def setUp(self):
        """Set up test data before running tests."""
        self.fake = Faker()
        self.specific_names = [
            "John Doe",
            "Jane Smith",
            "Alice Brown",
            "Bob White",
            "Charlie Green",
        ]
        self.specific_ages = [25, 30, 35, 40, 45]
        self.db_file = self.generate_test_data_with_file()
    def generate_test_data_with_file(self) -> str:
        """Generate test data and save it to a temporary SQLite database file."""
        db_file = "./temp_test_db.sqlite3"
        if os.path.exists(db_file):
            os.remove(db_file)
        conn = sqlite3.connect(db_file)
        create_table_query = """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """
        conn.execute(create_table_query)
        for _ in range(100):
            name = self.fake.name()
            age = self.fake.random_int(min=20, max=70)
            conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        for name, age in zip(self.specific_names, self.specific_ages):
            conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        conn.close()
        return db_file
    def test_case_1(self):
        """Test fetching all users."""
        df = f_306(self.db_file, "SELECT * FROM users")
        self.assertEqual(len(df), 100 + len(self.specific_names))
        for name in self.specific_names:
            self.assertIn(name, df["name"].values)
    def test_case_2(self):
        """Test fetching specific users based on names."""
        names_as_strings = "', '".join(self.specific_names)
        df = f_306(
            self.db_file,
            f"SELECT name, age FROM users WHERE name IN ('{names_as_strings}')",
        )
        for name in self.specific_names:
            self.assertIn(name, df["name"].values)
        for age in self.specific_ages:
            self.assertIn(age, df["age"].values)
    def test_case_3(self):
        """Test fetching users based on age condition."""
        age_limit = self.fake.random_int(min=20, max=60)
        df = f_306(self.db_file, f"SELECT * FROM users WHERE age > {age_limit}")
        self.assertTrue(all(df["age"] > age_limit))
    def test_case_4(self):
        """Test fetching users and sorting by name."""
        df = f_306(self.db_file, "SELECT * FROM users ORDER BY name")
        sorted_names = sorted(df["name"].tolist())
        self.assertListEqual(df["name"].tolist(), sorted_names)
    def test_case_5(self):
        """Test fetching users based on age and sorting by age."""
        age_limit = self.fake.random_int(min=20, max=30)
        df = f_306(
            self.db_file,
            f"SELECT * FROM users WHERE age < {age_limit} ORDER BY age DESC",
        )
        self.assertTrue(all(df["age"] < age_limit))
        self.assertTrue(
            all(df["age"].iloc[i] >= df["age"].iloc[i + 1] for i in range(len(df) - 1))
        )
    def tearDown(self):
        """Clean up test data after running tests."""
        os.remove(self.db_file)
