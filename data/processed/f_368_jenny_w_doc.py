import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def f_518(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    """
    Create a report on students' grades in a class, including a count of each grade out of all possible grades
    and a bar chart. Note: Grades are case-insensitive but whitespace-sensitive. Those not in possible grades
    are ignored.

    Parameters:
    student_grades (list): List of student grades. Must not be empty.
    possible_grades (list, optional): List of possible grade values. Defaults to ['A', 'B', 'C', 'D', 'F'].

    Returns:
    Tuple[DataFrame, Axes]:
        - A pandas DataFrame with 'Grade' as the named index and their 'Count' as values.
        - A bar chart plot (matplotlib's Axes object) visualizing 'Grade Distribution', with 'Grade' on the
          x-axis and 'Number of Students' on the y-axis.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - collections.Counter

    Example:
    >>> student_grades = ['A', 'B', 'B', 'C', 'A', 'D', 'F', 'B', 'A', 'C']
    >>> report_df, ax = f_518(student_grades)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> report_df
           Count
    Grade       
    A          3
    B          3
    C          2
    D          1
    F          1
    """
    if not student_grades:
        raise ValueError("student_grades cannot be empty")
    possible_grades = [*dict.fromkeys([g.upper() for g in possible_grades])]
    grade_counts = dict(Counter([g.upper() for g in student_grades]))
    report_data = {grade: grade_counts.get(grade, 0) for grade in possible_grades}
    report_df = pd.DataFrame.from_dict(report_data, orient="index", columns=["Count"])
    report_df.index.name = "Grade"

    ax = report_df.plot(kind="bar", legend=False, title="Grade Distribution")
    ax.set_ylabel("Number of Students")
    ax.set_xlabel("Grade")

    plt.tight_layout()

    return report_df, ax

import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def _validate_plot(self, ax):
        self.assertEqual(ax.get_title(), "Grade Distribution")
        self.assertEqual(ax.get_xlabel(), "Grade")
        self.assertEqual(ax.get_ylabel(), "Number of Students")
    def _test_helper(self, grades, expected_counts):
        expected_df = pd.DataFrame(
            {"Count": expected_counts}, index=["A", "B", "C", "D", "F"]
        )
        expected_df.index.name = "Grade"
        report_df, ax = f_518(grades)
        pd.testing.assert_frame_equal(report_df, expected_df)
        self._validate_plot(ax)
    def test_case_1(self):
        # Test with a mix of grades
        self._test_helper(
            ["A", "B", "B", "C", "A", "D", "F", "B", "A", "C"], [3, 3, 2, 1, 1]
        )
    def test_case_2(self):
        # Test with only one type of grade
        self._test_helper(["A", "A", "A", "A", "A"], [5, 0, 0, 0, 0])
    def test_case_3(self):
        # Test with an empty list of grades
        with self.assertRaises(Exception):
            f_518([], [0, 0, 0, 0, 0])
    def test_case_4(self):
        # Test correctly ignoring invalid grades
        self._test_helper(["A", "X", "Y", "Z"], [1, 0, 0, 0, 0])
    def test_case_5(self):
        # Test custom grades
        grades = ["A", "C", "G", "G"]
        expected_counts = [1, 0, 1, 0, 0, 2]
        possible_grades = ["A", "B", "C", "D", "F", "G"]
        expected_df = pd.DataFrame(
            {"Count": expected_counts},
            index=[*dict.fromkeys(g.upper() for g in possible_grades)],
        )
        expected_df.index.name = "Grade"
        report_df, ax = f_518(grades, possible_grades=possible_grades)
        pd.testing.assert_frame_equal(report_df, expected_df)
        self._validate_plot(ax)
    def test_case_6(self):
        # Test case insensitivity
        self._test_helper(["a", "b", "C"], [1, 1, 1, 0, 0])
    def test_case_7(self):
        # Test whitespace sensitivity
        self._test_helper(["A ", "b", " C"], [0, 1, 0, 0, 0])
    def tearDown(self):
        plt.close("all")
