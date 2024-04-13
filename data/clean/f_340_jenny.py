import pandas as pd
from random import randint


def f_340(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    """
    Generate a Pandas DataFrame of employees with their details based on the input provided.

    Parameters:
    - name (str): Name of the employee. This is case-sensitive. Must be one of the predefined
                  names: 'John', 'Alice', 'Bob', 'Charlie', 'David', otherwise the function raises
                  ValueError.
    - age (int): Age of the employee.
    - code (str): Code of the employee.
    - salary (float): Salary of the employee.
    - bio (str): Biography of the employee.

    Returns:
    data_df (pd.DataFrame): dataframe with columns: 'Name', 'Age', 'Code', 'Salary', 'Bio', 'Job Title'.
               The 'Job Title' is randomly assigned from the predefined job titles:
               'Engineer', 'Manager', 'Analyst', 'Developer', 'Tester'.

    Requirements:
    - pandas
    - random.randint

    Example:
    >>> df = f_340("John", 30, "A10B", 5000.0, "This is a bio with spaces")
    >>> print(df)
       Name  Age  Code  Salary                        Bio Job Title
    0  John   30  A10B  5000.0  This is a bio with spaces  Engineer
    """
    EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "David"]
    JOBS = ["Engineer", "Manager", "Analyst", "Developer", "Tester"]

    if name not in EMPLOYEES:
        raise ValueError(f"Invalid employee name. Must be one of {EMPLOYEES}")

    job = JOBS[randint(0, len(JOBS) - 1)]
    data_df = pd.DataFrame(
        [[name, age, code, salary, bio, job]],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    )
    return data_df


import unittest
import pandas as pd
import random


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test the DataFrame structure for a known input
        df = f_340("John", 30, "A10B", 5000.0, "Sample bio")
        expected_columns = ["Name", "Age", "Code", "Salary", "Bio", "Job Title"]
        self.assertListEqual(
            list(df.columns), expected_columns, "DataFrame columns mismatch"
        )
        for col, dtype in zip(
            df.columns, ["object", "int64", "object", "float64", "object", "object"]
        ):
            self.assertTrue(
                df[col].dtype == dtype,
                f"Column {col} has incorrect type {df[col].dtype}",
            )

    def test_case_2(self):
        # Test minimum and maximum valid ages and salary, including edge cases
        df_min_age = f_340("Alice", 18, "X10Y", 0.0, "Minimum age and salary")
        self.assertEqual(df_min_age["Age"][0], 18)
        self.assertEqual(df_min_age["Salary"][0], 0.0)

        df_max_age = f_340("Bob", 65, "Z99W", 1000000.0, "Maximum age and high salary")
        self.assertEqual(df_max_age["Age"][0], 65)
        self.assertEqual(df_max_age["Salary"][0], 1000000.0)

    def test_case_3(self):
        # Test bio with special characters, very long string, and empty string
        df_special_bio = f_340("Charlie", 30, "C30D", 5300.0, "!@#$%^&*()_+|")
        self.assertEqual(df_special_bio["Bio"][0], "!@#$%^&*()_+|")

        df_long_bio = f_340("David", 30, "D40E", 5400.5, "a" * 1000)
        self.assertEqual(len(df_long_bio["Bio"][0]), 1000)

        df_empty_bio = f_340("John", 30, "E50F", 5500.0, "")
        self.assertEqual(df_empty_bio["Bio"][0], "")

    def test_case_4(self):
        # Test code with different formats
        df_code_special_chars = f_340(
            "Alice", 25, "!@#$", 5500.5, "Bio with special char code"
        )
        self.assertEqual(df_code_special_chars["Code"][0], "!@#$")

    def test_case_5(self):
        # Test for case sensitivity
        with self.assertRaises(ValueError):
            f_340("john", 30, "J01K", 5000.0, "Case sensitive name test")

    def test_case_6(self):
        # Test each predefined name
        for name in ["John", "Alice", "Bob", "Charlie", "David"]:
            df = f_340(name, 30, "A10B", 5000.0, f"{name}'s bio")
            self.assertEqual(
                df["Name"][0], name, f"Valid name {name} failed to create a DataFrame"
            )

    def test_case_7(self):
        # Test randomness in job assignment
        job_titles_first_run = []
        job_titles_second_run = []
        job_titles_third_run = []

        n_iter = 15
        name, age, code, salary, bio = (
            "Bob",
            30,
            "B20C",
            5000.0,
            "Testing randomness in job titles",
        )
        random.seed(42)  # Set the seed for the first run
        for _ in range(n_iter):
            df = f_340(name, age, code, salary, bio)
            job_titles_first_run.append(df["Job Title"][0])

        random.seed(42)  # Reset the seed to ensure reproducibility for the second run
        for _ in range(n_iter):
            df = f_340(name, age, code, salary, bio)
            job_titles_second_run.append(df["Job Title"][0])

        random.seed(0)  # Repeat for third run with different seed
        for _ in range(n_iter):
            df = f_340(name, age, code, salary, bio)
            job_titles_third_run.append(df["Job Title"][0])

        self.assertEqual(job_titles_first_run, job_titles_second_run)
        self.assertNotEqual(job_titles_first_run, job_titles_third_run)

    def test_case_8(self):
        # Test invalid name
        with self.assertRaises(ValueError):
            f_340("InvalidName", 28, "C30D", 5300.0, "Bio of InvalidName")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
