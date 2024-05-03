from collections import defaultdict
from random import randint

def f_971(dict1):
    """
    Create a dictionary of employee data for departments starting with 'EMP$$'. 
    The keys are department codes and the values are lists of the salaries of employees in that department.
    
    Parameters:
    dict1 (dict): A dictionary with department codes as keys and number of employees as values.
    
    Returns:
    dict: A dictionary with department codes starting with 'EMP$$' as keys and lists of employee salaries as values.
    
    Requirements:
    - collections
    - random
    
    Example:
    >>> d = {'EMP$$1': 10, 'MAN$$1': 5, 'EMP$$2': 8, 'HR$$1': 7}
    >>> emp_data = f_971(d)
    >>> print(emp_data.keys())
    dict_keys(['EMP$$1', 'EMP$$2'])
    """
    employee_data = defaultdict(list)
    
    for prefix, num_employees in dict1.items():
        if not prefix.startswith('EMP$$'):
            continue

        salaries = [randint(1, 100) for _ in range(num_employees)]
        employee_data[prefix].extend(salaries)

    return dict(employee_data)

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        d = {'EMP$$1': 10, 'MAN$$1': 5, 'EMP$$2': 8, 'HR$$1': 7}
        emp_data = f_971(d)
        self.assertIn('EMP$$1', emp_data)
        self.assertIn('EMP$$2', emp_data)
        self.assertNotIn('MAN$$1', emp_data)
        self.assertNotIn('HR$$1', emp_data)
        self.assertEqual(len(emp_data['EMP$$1']), 10)
        self.assertEqual(len(emp_data['EMP$$2']), 8)

    def test_case_2(self):
        d = {'EMP$$A': 5, 'DEV$$A': 5}
        emp_data = f_971(d)
        self.assertIn('EMP$$A', emp_data)
        self.assertNotIn('DEV$$A', emp_data)
        self.assertEqual(len(emp_data['EMP$$A']), 5)

    def test_case_3(self):
        d = {'MAN$$1': 5, 'HR$$1': 7}
        emp_data = f_971(d)
        self.assertNotIn('MAN$$1', emp_data)
        self.assertNotIn('HR$$1', emp_data)

    def test_case_4(self):
        d = {'EMP$$X': 0, 'EMP$$Y': 10}
        emp_data = f_971(d)
        self.assertIn('EMP$$X', emp_data)
        self.assertIn('EMP$$Y', emp_data)
        self.assertEqual(len(emp_data['EMP$$X']), 0)
        self.assertEqual(len(emp_data['EMP$$Y']), 10)

    def test_case_5(self):
        d = {}
        emp_data = f_971(d)
        self.assertEqual(emp_data, {})
if __name__ == "__main__":
    run_tests()