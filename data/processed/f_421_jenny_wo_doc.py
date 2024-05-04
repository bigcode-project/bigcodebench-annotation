import sqlite3
import numpy as np
from random import choice, seed


def f_399(db_path, table_name, num_entries, random_seed=None):
    """
    Insert random data into an SQLite3 table that contains random names, ages, and heights.
    If the table does not exist, it will be created.
    This function uses the following constants:
    - NAMES: List of possible names ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia'].
    - AGES: Range of possible ages from 18 to 64.
    - HEIGHTS: Range of possible heights from 150cm to 199cm.

    Parameters:
    db_path (str): The path to the SQLite3 database file.
    table_name (str): The name of the table to insert data into.
    num_entries (int): The number of entries to insert. Must not be negative.
    random_seed (int, optional): Seed for random number generation. Defaults to None (no fixed seed).

    Returns:
    int: The number of rows inserted.

    Raises:
    ValueError: If num_entries is negative.
    
    Requirements:
    - sqlite3
    - numpy
    - random.choice
    - random.seed

    Example:
    >>> f_399('path_to_test.db', 'People', 100, random_seed=42)
    100
    """
    if random_seed is not None:
        seed(random_seed)
        np.random.seed(random_seed)
    if num_entries < 0:
        raise ValueError("num_entries cannot be negative.")
    NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    AGES = list(range(18, 65))
    HEIGHTS = list(range(150, 200))
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    table_creation_sql = (
        "CREATE TABLE IF NOT EXISTS {} (name TEXT, age INTEGER, height INTEGER)".format(
            table_name
        )
    )
    cur.execute(table_creation_sql)
    inserted_rows = 0
    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        insertion_sql = "INSERT INTO {} VALUES (?, ?, ?)".format(table_name)
        cur.execute(insertion_sql, (name, age, height))
        inserted_rows += cur.rowcount
    conn.commit()
    return inserted_rows

import unittest
import os
import sqlite3
import tempfile
class TestCases(unittest.TestCase):
    NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    AGES = range(18, 65)
    HEIGHTS = range(150, 200)
    def setUp(self):
        # Setup a temporary directory before each test
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test.db")
    def tearDown(self):
        # Clean up the temporary directory after each test
        self.temp_dir.cleanup()
    def test_case_1(self):
        # Test inserting 50 entries with a fixed seed
        result = f_399(self.db_path, "SamplePeople", 50, random_seed=42)
        self.assertEqual(result, 50)
    def test_case_2(self):
        # Test inserting 30 entries into a new table with a fixed seed
        result = f_399(self.db_path, "NewPeople", 30, random_seed=42)
        self.assertEqual(result, 30)
    def test_case_3(self):
        # Test inserting 20 entries, verifying smaller batch works as expected
        result = f_399(self.db_path, "SamplePeople", 20, random_seed=42)
        self.assertEqual(result, 20)
    def test_case_4(self):
        # Test inserting a large number of entries (200) with a fixed seed
        result = f_399(self.db_path, "SamplePeople", 200, random_seed=42)
        self.assertEqual(result, 200)
    def test_case_5(self):
        # Test inserting 0 entries to check handling of empty input
        result = f_399(self.db_path, "SamplePeople", 0, random_seed=42)
        self.assertEqual(result, 0)
    def test_case_6(self):
        # Test the content of the rows for correctness against expected values
        f_399(self.db_path, "ContentCheck", 10, random_seed=42)
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM ContentCheck")
        rows = cur.fetchall()
        for row in rows:
            self.assertIn(row[0], self.NAMES)
            self.assertIn(row[1], self.AGES)
            self.assertIn(row[2], self.HEIGHTS)
    def test_case_7(self):
        # Test invalid db path
        with self.assertRaises(sqlite3.OperationalError):
            f_399("/invalid/path.db", "TestTable", 10)
    def test_case_8(self):
        # Test invalid table names (SQL keywords)
        with self.assertRaises(sqlite3.OperationalError):
            f_399(self.db_path, "Select", 10)
    def test_case_9(self):
        # Test handling invalid num_entries
        with self.assertRaises(Exception):
            f_399(self.db_path, "TestTable", -1)
        with self.assertRaises(TypeError):
            f_399(self.db_path, "TestTable", "ten")
    def test_case_10(self):
        # Test handling invalid random seed
        with self.assertRaises(Exception):
            f_399(self.db_path, "TestTable", 10, random_seed="invalid")
    def test_case_11(self):
        # Test different schema in existing table
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE TestTable (id INTEGER)")
        conn.close()
        with self.assertRaises(sqlite3.OperationalError):
            f_399(self.db_path, "TestTable", 10)
    def test_case_12(self):
        # Insert a known set of data and verify its integrity
        f_399(self.db_path, "IntegrityCheck", 1, random_seed=42)
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM IntegrityCheck")
        row = cur.fetchone()
        self.assertIsNotNone(row)
    def test_case_13(self):
        # Test against SQL injection in table_name parameter
        malicious_name = "Test; DROP TABLE IntegrityCheck;"
        with self.assertRaises(sqlite3.OperationalError):
            f_399(self.db_path, malicious_name, 1)
