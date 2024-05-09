import sqlite3
import pandas as pd
import os


def f_422(db_name, table_name, csv_path="data.csv"):
    """
    Read SQLite3 table via pandas and export to a CSV file.

    Parameters:
    - db_name (str): The path to the SQLite3 database.
    - table_name (str): The name of the table to export.
    - csv_path (str, optional): The path where the CSV file will be saved. Defaults to 'data.csv'.

    Requirements:
    - sqlite3
    - pandas
    - os

    Returns:
    str: The absolute path of the exported CSV file.

    Example:
    >>> f_422('test.db', 'People')
    'data.csv'
    >>> f_422('/absolute/path/to/test.db', 'Orders', 'orders.csv')
    '/absolute/path/to/orders.csv'
    """
    try:
        conn = sqlite3.connect(db_name)
        df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
        df.to_csv(csv_path, index=False)
        return os.path.abspath(csv_path)
    finally:
        conn.close()


import unittest
import os
import tempfile
import shutil
import sqlite3
import pandas as pd


class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir_obj = tempfile.TemporaryDirectory()
        self.temp_dir = self.temp_dir_obj.name
        self.db_path = os.path.join(self.temp_dir, "test.db")

        # Setup the database and tables
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create tables and insert some data
        cursor.execute("CREATE TABLE People (Name TEXT, Age INTEGER)")
        cursor.execute(
            "INSERT INTO People VALUES ('Alice', 30), ('Bob', 25), ('Charlie', 35)"
        )

        cursor.execute("CREATE TABLE Orders (Product TEXT, Quantity INTEGER)")
        cursor.execute(
            "INSERT INTO Orders VALUES ('Widgets', 5), ('Gadgets', 10), ('Doodads', 15)"
        )

        conn.commit()
        conn.close()

    def tearDown(self):
        self.temp_dir_obj.cleanup()

    def test_case_1(self):
        # Test exporting the People table
        csv_path = os.path.join(self.temp_dir, "data.csv")
        output_path = f_422(self.db_path, "People", csv_path)
        self.assertTrue(os.path.exists(output_path), "CSV file not created.")

        df = pd.read_csv(output_path)
        self.assertEqual(len(df), 3, "CSV contains incorrect number of rows.")
        self.assertTrue("Alice" in df["Name"].values, "Expected data not found in CSV.")

    def test_case_2(self):
        # Test exporting the Orders table
        csv_path = os.path.join(self.temp_dir, "orders.csv")
        output_path = f_422(self.db_path, "Orders", csv_path)
        self.assertTrue(os.path.exists(output_path), "CSV file not created.")

        df = pd.read_csv(output_path)
        self.assertEqual(len(df), 3, "CSV contains incorrect number of rows.")
        self.assertTrue(5 in df["Quantity"].values, "Expected data not found in CSV.")

    def test_case_3(self):
        # Test exporting with a custom CSV path
        custom_path = os.path.join(self.temp_dir, "custom_data.csv")
        output_path = f_422(self.db_path, "People", custom_path)
        self.assertTrue(
            os.path.exists(output_path), "CSV file not created at custom path."
        )
        self.assertEqual(
            output_path,
            os.path.abspath(custom_path),
            "Returned path does not match expected path.",
        )

    def test_case_4(self):
        # Test with a non-existent database
        with self.assertRaises(Exception):
            f_422(os.path.join(self.temp_dir, "nonexistent.db"), "People")

    def test_case_5(self):
        # Test with a non-existent table
        with self.assertRaises(pd.io.sql.DatabaseError):
            f_422(self.db_path, "NonexistentTable")

    def test_case_6(self):
        # Test if the function overwrites an existing CSV file
        csv_path = os.path.join(self.temp_dir, "data.csv")
        with open(csv_path, "w") as file:
            file.write("Old Content")

        output_path = f_422(self.db_path, "People", csv_path)
        self.assertTrue(os.path.exists(output_path), "CSV file not created.")

        with open(output_path, "r") as file:
            content = file.read()
            self.assertNotEqual(
                "Old Content", content, "Old content found in CSV. Overwriting failed."
            )

    def test_case_7(self):
        # Test error handling with invalid CSV path
        with self.assertRaises(OSError):
            f_422(self.db_path, "People", "/nonexistent_path/data.csv")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
