import sqlite3
import pandas as pd
import seaborn as sns


def f_641(db_name="test.db", table_name="People"):
    """
    Draw the age distribution of the persons in an SQLite3 table and returns the Axes object of the plot.
    Raises a ValueError if the loaded data contains negative age values.

    Parameters:
    db_name (str, optional): The full path to the SQLite3 database file. Defaults to 'test.db'.
    table_name (str, optional): The name of the table to plot from. Defaults to 'People'.

    Returns:
    matplotlib.axes._axes.Axes: Axes object representing the age distribution plot,
                                           with x-axis showing age and a default of bins=30, kde=True.

    Requirements:
    - sqlite3
    - pandas
    - seaborn

    Examples:
    >>> ax = f_641('path/to/test.db', 'People')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax = f_641()
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT age from {table_name}", conn)

    if (df["age"] < 0).any():
        raise ValueError("Data contains negative age values.")

    ax = sns.histplot(data=df, x="age", bins=30, kde=True)
    ax.set_xlabel("age")
    return ax

import unittest
import os
import sqlite3
import matplotlib.pyplot as plt
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        # Create test_alt.db with People table
        self.alt_db_path = os.path.join(self.test_dir.name, "test_alt.db")
        conn = sqlite3.connect(self.alt_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE People (name TEXT, age INT)")
        cursor.executemany(
            "INSERT INTO People VALUES (?, ?)", [("Alice", 25), ("Bob", 30)]
        )
        conn.commit()
        conn.close()
        # Create a standard test.db with Employees table
        self.default_db_path = os.path.join(self.test_dir.name, "test.db")
        conn = sqlite3.connect(self.default_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE Employees (name TEXT, age INT)")
        cursor.executemany(
            "INSERT INTO Employees VALUES (?, ?)", [("Charlie", 35), ("David", 40)]
        )
        conn.commit()
        conn.close()
        # Create standard db with more examples
        self.multiple_db_path = os.path.join(self.test_dir.name, "test_multiple.db")
        conn = sqlite3.connect(self.multiple_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE MultipleAge (name TEXT, age INT)")
        cursor.executemany(
            "INSERT INTO MultipleAge VALUES (?, ?)",
            [("Alice", 25), ("Bob", 30), ("Charlie", 35)],
        )
        conn.commit()
        conn.close()
        # Create a db for testing edge cases - negative age
        self.negative_age_db_path = os.path.join(
            self.test_dir.name, "test_negative_age.db"
        )
        conn = sqlite3.connect(self.negative_age_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE NegativeAge (name TEXT, age INT)")
        cursor.executemany(
            "INSERT INTO NegativeAge VALUES (?, ?)", [("Eve", -1), ("Frank", 20)]
        )
        conn.commit()
        conn.close()
        # Create a db for testing edge cases - empty
        self.empty_db_path = os.path.join(self.test_dir.name, "test_empty.db")
        conn = sqlite3.connect(self.empty_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE EmptyAge (name TEXT, age INT)")
        conn.commit()
        conn.close()
    def tearDown(self):
        self.test_dir.cleanup()
        plt.close("all")
    def _check_plot(self, ax, contains_data=True):
        self.assertTrue(isinstance(ax, plt.Axes), "The plot should be an Axes object.")
        self.assertEqual(ax.get_xlabel(), "age", "The x-axis label should be 'age'.")
        if contains_data:
            self.assertTrue(len(ax.lines) > 0, "The plot should contain a KDE line.")
    def test_case_1(self):
        ax = f_641(db_name=self.default_db_path, table_name="Employees")
        self._check_plot(ax)
    def test_case_2(self):
        ax = f_641(db_name=self.alt_db_path)
        self._check_plot(ax)
    def test_case_3(self):
        ax = f_641(db_name=self.default_db_path, table_name="Employees")
        self._check_plot(ax)
    def test_case_4(self):
        ax = f_641(db_name=self.multiple_db_path, table_name="MultipleAge")
        self._check_plot(ax)
    def test_case_5(self):
        ax = f_641(db_name=self.empty_db_path, table_name="EmptyAge")
        self._check_plot(ax, False)
    def test_case_6(self):
        # Test for non-existent table
        with self.assertRaises(Exception):
            f_641(db_name=self.default_db_path, table_name="Nonexistent")
    def test_case_7(self):
        # Test for negative age values
        with self.assertRaises(ValueError):
            f_641(db_name=self.negative_age_db_path, table_name="NegativeAge")
