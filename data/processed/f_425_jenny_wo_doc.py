import sqlite3
from random import choice, seed
import os


def f_55(db_name, table_name, num_entries, random_seed=None):
    """
    Create an SQLite3 table and fill it with random data using the provided database and table names.

    The function populates the table with columns 'name', 'age', 'height' using random data from the
    following constants:
    - NAMES: List of names ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    - AGES: Range of ages from 18 to 65.
    - HEIGHTS: Range of heights from 150cm to 200cm.

    Parameters:
    db_name (str): The name of the SQLite3 database.
    table_name (str): The name of the table to create and populate.
    num_entries (int): The number of entries to insert. Must not be negative.
    random_seed (int, optional): The seed for generating random values. Default is None.

    Returns:
    str: The absolute path of the SQLite3 database file.

    Raises:
    ValueError: If num_entries is negative.
    
    Requirements:
    - sqlite3
    - random.choice
    - random.seed
    - os

    Example:
    >>> db_path = f_55('test.db', 'People', 100, random_seed=42)
    >>> print(db_path)
    '/absolute/path/to/test.db'
    """
    NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    AGES = range(18, 65)
    HEIGHTS = range(150, 200)
    if random_seed:
        seed(random_seed)
    if num_entries < 0:
        raise ValueError("num_entries must not be negative")
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE {table_name} (name TEXT, age INTEGER, height INTEGER)")
    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        cur.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", (name, age, height))
    conn.commit()
    return os.path.abspath(db_name)

import unittest
import sqlite3
import os
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_dir_path = self.temp_dir.name
        self.db_name = "test_function.db"
        self.db_path = os.path.join(self.temp_dir_path, self.db_name)
        self.table_name = "TestTable"
        self.random_seed = 42
    def tearDown(self):
        self.temp_dir.cleanup()
    def test_case_1(self):
        # Test basic case
        num_entries = 5
        db_path = f_55(
            self.db_path, self.table_name, num_entries, random_seed=self.random_seed
        )
        self.assertTrue(os.path.exists(db_path))
        self.verify_db_content(num_entries)
    def test_case_2(self):
        # Test handling 0 entries
        num_entries = 0
        db_path = f_55(
            self.db_path, self.table_name, num_entries, random_seed=self.random_seed
        )
        self.assertTrue(os.path.exists(db_path))
        self.verify_db_content(num_entries)
    def test_case_3(self):
        # Test handling 1 entry
        num_entries = 1
        db_path = f_55(
            self.db_path, self.table_name, num_entries, random_seed=self.random_seed
        )
        self.assertTrue(os.path.exists(db_path))
        self.verify_db_content(num_entries)
    def test_case_4(self):
        # Test handling invalid num_entries
        with self.assertRaises(Exception):
            f_55(self.db_path, self.table_name, -1, random_seed=self.random_seed)
        with self.assertRaises(Exception):
            f_55(self.db_path, self.table_name, "1", random_seed=self.random_seed)
    def test_case_5(self):
        # Test invalid table names (SQL keywords)
        with self.assertRaises(sqlite3.OperationalError):
            f_55(self.db_path, "Select", 10)
    def test_case_6(self):
        # Test against SQL injection in table_name parameter
        malicious_name = "Test; DROP TABLE IntegrityCheck;"
        with self.assertRaises(sqlite3.OperationalError):
            f_55(self.db_path, malicious_name, 1)
    def verify_db_content(self, num_entries):
        # Connect to the database and check if the table has correct number of entries
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        count = cur.fetchone()[0]
        self.assertEqual(count, num_entries)
        # Verify data integrity
        cur.execute(f"SELECT name, age, height FROM {self.table_name}")
        rows = cur.fetchall()
        for row in rows:
            self.assertIn(row[0], ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"])
            self.assertIn(row[1], list(range(18, 65)))
            self.assertIn(row[2], list(range(150, 200)))
