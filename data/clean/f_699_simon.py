import pandas as pd
import statistics
import random

def f_699(students, subjects, seed=None):
    """
    Create a grade report for a list of students across various subjects. Each student's grades are randomly generated, 
    and the report includes the average grade for each student. The randomness is seeded for reproducibility if a seed is provided.

    Parameters:
    students (list of str): The students for whom the report is being generated.
    subjects (list of str): The subjects included in the report.
    seed (int, optional): A seed for the random number generator to ensure reproducibility. If None, the randomness is seeded by the system.

    Returns:
    DataFrame: A pandas DataFrame containing each student's grades across the subjects and their average grade. 
               Columns are ['Student', 'Subject1', 'Subject2', ..., 'Average Grade'].

    Requirements:
    - pandas
    - statistics
    - random

    Example:
    >>> students = ['Alice', 'Bob', 'Charlie']
    >>> subjects = ['Math', 'Physics', 'English']
    >>> report = f_699(students, subjects, seed=123)
    >>> print(report)
    # This would print a DataFrame with students' names, their grades for each subject, and their average grade, 
    # with the randomness being reproducible due to the provided seed.
    """
    if seed is not None:
        random.seed(seed)

    report_data = []

    for student in students:
        grades = [random.randint(0, 100) for _ in subjects]
        avg_grade = statistics.mean(grades)
        report_data.append((student,) + tuple(grades) + (avg_grade,))

    report_df = pd.DataFrame(report_data, columns=['Student'] + subjects + ['Average Grade'])

    return report_df

import unittest
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_dataframe_structure(self):
        students = ['Alice', 'Bob']
        subjects = ['Math', 'Physics']
        report = f_699(students, subjects, seed=42)
        
        # Check if the output is a DataFrame
        self.assertIsInstance(report, pd.DataFrame)
        
        # Check the structure of the DataFrame
        expected_columns = ['Student'] + subjects + ['Average Grade']
        self.assertEqual(list(report.columns), expected_columns)

    def test_average_grade_calculation(self):
        students = ['Alice']
        subjects = ['Math', 'Physics']
        report = f_699(students, subjects, seed=42)

        # Since we know the seed, we know the grades. Let's check the average.
        alice_grades = report.iloc[0, 1:-1]
        self.assertEqual(report.at[0, 'Average Grade'], alice_grades.mean())

    def test_varying_input_sizes(self):
        # Testing with different numbers of students and subjects
        students = ['Alice', 'Bob', 'Charlie']
        subjects = ['Math', 'Physics', 'Biology', 'English']
        report = f_699(students, subjects, seed=42)

        # Check if the number of rows matches the number of students
        self.assertEqual(len(report), len(students))

    def test_random_seed_reproducibility(self):
        students = ['Alice', 'Bob']
        subjects = ['Math', 'Physics']
        
        # If we run the function with the same seed, we should get the same results.
        report1 = f_699(students, subjects, seed=42)
        report2 = f_699(students, subjects, seed=42)

        pd.testing.assert_frame_equal(report1, report2)

    def test_without_seed(self):
        students = ['Alice', 'Bob']
        subjects = ['Math', 'Physics']
        
        # When run without a seed, there should be variability in results.
        report1 = f_699(students, subjects)  # No seed here
        report2 = f_699(students, subjects)  # No seed here

        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(report1, report2)

# If the script is run directly, initiate the tests.
if __name__ == "__main__":
    run_tests()