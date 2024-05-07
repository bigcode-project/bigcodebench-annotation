import hashlib
import binascii

def f_991(salt, cursor):
    """
    Updates the passwords in a user table of an SQLite database by hashing them with SHA256, 
    using a provided salt. The function directly modifies the database via the given cursor.

    Parameters:
    - salt (str): The salt value to be appended to each password before hashing.
    - cursor (sqlite3.Cursor): A cursor object through which SQL commands are executed.

    Returns:
    - int: The number of users whose passwords were successfully updated.

    Requirements:
    - hashlib
    - binascii

    Raises:
    TypeError if the salt is not a string
    
    Example:
    >>> conn = sqlite3.connect('sample.db')
    >>> cursor = conn.cursor()
    >>> num_updated = f_991('mysalt', cursor)
    >>> print(num_updated)
    5
    """
    if not isinstance(salt, str):
        raise TypeError
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
import hashlib
import binascii

def create_mock_db():
    """Helper function to create a mock SQLite database with a users table."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, password TEXT)")
    passwords = [("password1",), ("password2",), ("password3",), ("password4",), ("password5",)]
    cursor.executemany("INSERT INTO users (password) VALUES (?)", passwords)
    conn.commit()
    return conn

class TestCases(unittest.TestCase):
    def setUp(self):
        """Setup mock database for testing."""
        self.conn = create_mock_db()
        self.cursor = self.conn.cursor()

    def tearDown(self):
        """Tear down and close the mock database after testing."""
        self.conn.close()

    def test_updated_passwords(self):
        """Verify that the number of updated passwords matches the number of users."""
        salt = "testsalt"
        num_updated = f_991(salt, self.cursor)
        self.assertEqual(num_updated, 5, "Expected 5 users to be updated")

    def check_hash_correctness(self):
        """Verify that hash correctness."""
        salt = "testsalt1"
        _ = f_991(salt, self.cursor)
        self.cursor.execute("SELECT password FROM users")
        for row in self.cursor.fetchall():
            password = row[0]
            self.assertTrue(isinstance(password, str) and len(password) == 64,
                            "Expected hashed password to be 64 characters long")
            # Recreate hash to check if hashing was done correctly
            expected_hash = hashlib.sha256(("ME" + "password" + salt).encode()).hexdigest()
            self.assertNotEqual(password, expected_hash)  # Ensure the hash varies per user/password

    def test_empty_database(self):
        """Check behavior with an empty user table."""
        self.cursor.execute("DELETE FROM users")
        num_updated = f_991("testsalt", self.cursor)
        self.assertEqual(num_updated, 0, "Expected 0 users to be updated when the table is empty")

    def test_varied_salts(self):
        """Ensure different salts produce different hashes for the same password."""
        self.cursor.execute("UPDATE users SET password = 'constant'")
        salt1 = "salt1"
        salt2 = "salt2"
        f_991(salt1, self.cursor)
        hash1 = self.cursor.execute("SELECT password FROM users WHERE id = 1").fetchone()[0]
        
        self.cursor.execute("UPDATE users SET password = 'constant'")
        f_991(salt2, self.cursor)
        hash2 = self.cursor.execute("SELECT password FROM users WHERE id = 1").fetchone()[0]
        
        self.assertNotEqual(hash1, hash2, "Hashes should differ when different salts are used")

    def test_invalid_salt(self):
        with self.assertRaises(TypeError):
            f_991(1, self.cursor)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()