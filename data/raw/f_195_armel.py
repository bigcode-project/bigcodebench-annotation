import pandas as pd
import matplotlib.pyplot as plt
import collections
import re

# Constants
ID_PATTERN = r'\d{3}-\d{2}-\d{4}'

def f_195(employee_data):
    """Analyze a list of employee data, validate employee ID cards using a regular expression, and return the number of employees by work role and a bar chart of the number of employees by work role.

    Parameters:
    employee_data (list): A list of dictionaries where each dictionary represents data for an employee,
                          e.g., [{'name' : 'John', 'id': '123-45-6789', 'role': 'engineer'}]

    Returns:
    - dict: A dictionary with the count of valid employees by job role. An employee is considered valid if its id follows the regular expression ID_PATTERN.
    - matplotlib.figure.Figure: A bar chart of employee count by job role. If there is not valid employee, return an empty figure.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - collections
    - re

    Example:
    >>> employee_data = [{'name' : 'John', 'id': '123-45-6789', 'role': 'engineer'}]
    >>> role_counts, fig = f_195(employee_data)
    >>> print(role_counts)
    >>> fig.show()
    """
    valid_employees = [employee for employee in employee_data if re.match(ID_PATTERN, employee['id'])]
    role_counts = collections.Counter([employee['role'] for employee in valid_employees])
    # Check if valid_employees is empty
    if not valid_employees:
        fig = plt.figure()
        plt.close(fig)  # Close the plot to avoid displaying it
        return dict(role_counts), fig
    employee_df = pd.DataFrame(valid_employees)
    ax = employee_df['role'].value_counts().plot(kind='bar')
    fig = ax.get_figure()
    return dict(role_counts), fig

import unittest
import matplotlib.pyplot as plt
from faker import Faker

fake = Faker()
Faker.seed(0)

def generate_employee_data(num_employees=1):
    """Generate random employee data for testing."""
    employee_data = []
    for _ in range(num_employees):
        employee = {
            'name': fake.name(),
            'id': fake.ssn(taxpayer_identification_number_type="SSN"),
            'role': fake.job()
        }
        employee_data.append(employee)
    return employee_data

class TestCases(unittest.TestCase):
    """Test cases for the f_195 function."""   
    def test_case_1(self):
        """Testing with a single employee with a valid ID"""
        employee_data = generate_employee_data(1)
        role_counts, fig = f_195(employee_data)
        self.assertIsInstance(role_counts, dict, "Expected role_counts to be a dictionary.")
        self.assertIsInstance(fig, plt.Figure, "Expected fig to be a matplotlib.figure.Figure instance.")

    def test_case_2(self):
        """Testing with multiple employees"""
        employee_data = generate_employee_data(10)
        role_counts, fig = f_195(employee_data)
        self.assertIsInstance(role_counts, dict, "Expected role_counts to be a dictionary.")
        self.assertIsInstance(fig, plt.Figure, "Expected fig to be a matplotlib.figure.Figure instance.")

    def test_case_3(self):
        """Testing with no employees"""
        employee_data = []
        role_counts, fig = f_195(employee_data)
        self.assertEqual(role_counts, {}, "Expected role_counts to be an empty dictionary.")
        self.assertIsInstance(fig, plt.Figure, "Expected fig to be a matplotlib.figure.Figure instance.")
    
    def test_case_4(self):
        """Testing with multiple employees"""
        employee_data = [
            {"name" : "John", "id" : "123-45-6789", "role" : "engineer"},
            {"name" : "Mark", "id" : "234-56-7891", "role" : "manager"},
            {"name" : "Lee", "id" : "3456-78-912", "role" : "engineer"},
            {"name" : "Ngo", "id" : "456-78-8123", "role" : "manager"},
            {"name" : "Mona", "id" : "567-89-1234", "role" : "engineer"},
            {"name" : "Konstantin", "id" : "678-91-2345", "role" : "manager"},
            {"name" : "Lucy", "id" : "7891-23-456", "role" : "engineer"},
            {"name" : "Antoine", "id" : "891-23-4567", "role" : "manager"},
            {"name" : "Sara", "id" : "912-34-5678", "role" : "engineer"},
            {"name" : "Pablo", "id" : "213-45-6789", "role" : "manager"},
        ]
        role_counts, fig = f_195(employee_data)
        self.assertEqual(role_counts["engineer"], 3)
        self.assertEqual(role_counts["manager"], 5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
if __name__ == "__main__" :
    run_tests()