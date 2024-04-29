import sqlite3
import hashlib
import binascii

def f_991(db_name: str, salt: str, cursor) -> int:
    """
    Hash all passwords in a user table of an SQLite database with SHA256.
    
    Parameters:
    db_name (str): The name of the SQLite database.
    salt (str): The salt value to combine with each password before hashing.
    cursor (Cursor): SQLite cursor object.
    
    Returns:
    int: The number of users whose passwords were updated.
    
    Requirements:
    - sqlite3
    - hashlib
    - binascii
    
    Example:
    >>> conn = sqlite3.connect('sample.db')
    >>> cursor = conn.cursor()
    >>> num_updated = f_991('sample.db', 'mysalt', cursor)
    >>> print(num_updated)
    5
    """
    cursor.execute("SELECT id, password FROM users")
    users = cursor.fetchall()
    count_updated = 0

    for user in users:
        password = user[1].encode('utf-8')
        salted_password = password + salt.encode('utf-8')
        hash_obj = hashlib.sha256(salted_password)
        hashed_password = binascii.hexlify(hash_obj.digest()).decode('utf-8')

        cursor.execute(f"UPDATE users SET password = '{hashed_password}' WHERE id = {user[0]}")
        count_updated += 1

    return count_updated

import unittest
import sqlite3

import sqlite3
import hashlib
import binascii

def create_mock_db(db_name: str):
    """Helper function to create a mock SQLite database with a users table."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create a users table and populate it with some sample data
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, password TEXT)")
    cursor.executemany("INSERT INTO users (password) VALUES (?)", [("password1",), ("password2",), ("password3",), ("password4",), ("password5",)])
    conn.commit()
    
    return conn, cursor

class TestCases(unittest.TestCase):
    def setUp(self):
        """Setup mock database for testing."""
        self.conn, self.cursor = create_mock_db(":memory:")

    def tearDown(self):
        """Tear down and close the mock database after testing."""
        self.conn.close()

    def test_case_1(self):
        num_updated = f_991(":memory:", "testsalt", self.cursor)
        self.assertEqual(num_updated, 5, "Expected 5 users to be updated")
        
        # Verify the passwords are hashed correctly
        self.cursor.execute("SELECT password FROM users WHERE id = 1")
        hashed_password = self.cursor.fetchone()[0]
        self.assertTrue(len(hashed_password) == 64, "Expected hashed password to be 64 characters long")

    def test_case_2(self):
        num_updated = f_991(":memory:", "diffsalt", self.cursor)
        self.assertEqual(num_updated, 5, "Expected 5 users to be updated")

    def test_case_3(self):
        num_updated = f_991(":memory:", "unique_salt", self.cursor)
        self.assertEqual(num_updated, 5, "Expected 5 users to be updated")

    def test_case_4(self):
        num_updated = f_991(":memory:", "salt123", self.cursor)
        self.assertEqual(num_updated, 5, "Expected 5 users to be updated")

    def test_case_5(self):
        num_updated = f_991(":memory:", "finalsalt", self.cursor)
        self.assertEqual(num_updated, 5, "Expected 5 users to be updated")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()