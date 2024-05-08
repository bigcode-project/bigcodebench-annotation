import random
import matplotlib.pyplot as plt

# Constants
SALARY_RANGE = (20000, 100000)

def f_146(dict1):
    """
    Analyze the salary distribution within the department with code 'EMPXX'. Generate random salaries for each employee and create a histogram.
    - For the department of interest, randomly generate as many salaries as its number of employees.
    - Make sure that the salary is within SALARY_RANGE.
    - The histogram title should be 'Salary Distribution in EMPXX Department'
    - The x-label should be set to 'Salary'
    - The y-label should be set to 'Number of Employees'

    Parameters:
    - dict1 (dict): A dictionary with department codes as keys and number of employees as values.

    Returns:
    - matplotlib.axes._subplots.AxesSubplot: Axes object representing the histogram.

    Requirements:
    - random
    - matplotlib.pyplot

    Example:
    >>> d = {'EMPXX': 10, 'MANXX': 5, 'DEVXX': 8, 'HRXX': 7}
    >>> ax = f_146(d)
    >>> print(ax)
    Axes(0.125,0.11;0.775x0.77)
    """
    emp_salaries = []

    for prefix, num_employees in dict1.items():
        if not prefix.startswith('EMPXX'):
            continue

        for _ in range(num_employees):
            salary = random.randint(*SALARY_RANGE)
            emp_salaries.append(salary)

    plt.hist(emp_salaries, bins=10, alpha=0.5)
    plt.title('Salary Distribution in EMPXX Department')
    plt.xlabel('Salary')
    plt.ylabel('Number of Employees')
    return plt.gca()

import unittest

class TestCases(unittest.TestCase):
    def test_case_1(self):
        random.seed(42)
        d = {'EMPXX': 10, 'MANXX': 5, 'DEVXX': 8, 'HRXX': 7}
        ax = f_146(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')
        self.assertEqual(len(ax.patches), 20)

    def test_case_2(self):
        random.seed(42)
        d = {'EMPXX': 5, 'MANXX': 2, 'DEVXX': 3, 'HRXX': 4}
        ax = f_146(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')

    def test_case_3(self):
        random.seed(42)
        d = {'EMPXX': 3, 'MANXX': 1, 'DEVXX': 1, 'HRXX': 7}
        ax = f_146(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')

    def test_case_4(self):
        random.seed(42)
        d = {'EMPXX': 6, 'MANXX': 7, 'DEVXX': 2, 'HRXX': 1}
        ax = f_146(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')

    def test_case_5(self):
        random.seed(42)
        d = {'EMPXX': 1, 'MANXX': 1, 'DEVXX': 1, 'HRXX': 1}
        ax = f_146(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
