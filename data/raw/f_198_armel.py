import collections
import pandas as pd
import matplotlib.pyplot as plt
import re

EMAIL_PATTERN = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

def f_198(customer_data):
    '''
    Analyze a list of customer data, validate customer emails using a defined regular expression pattern 
    (EMAIL_PATTERN), and return a count of customers by country and a bar chart (matplotlib Axes object) 
    of customer numbers by country.

    Parameters:
    customer_data (list): A list of dictionaries where each dictionary represents data for a customer.
                          Each dictionary should contain the keys 'name', 'email', and 'country'.
                          e.g., [{'name' : 'John', 'email': 'john@domain.com', 'country': 'USA'}]

    Returns:
    - dict: A dictionary with the count of valid customers by country. A customer is considered valid if all its informations are available (name, email and country) and its email matches the regular expression pattern.
    - matplotlib.axes._subplots.AxesSubplot: A bar chart (matplotlib Axes object) of valid customer count by country. If there is not valid customer, return None.

    Requirements:
    - collections
    - pandas
    - matplotlib.pyplot
    - re

    Example:
    >>> customer_data = [{'name' : 'John', 'email': 'john@domain.com', 'country': 'USA'}]
    >>> country_counts, ax = f_198(customer_data)
    >>> print(country_counts)
    >>> plt.show()
    '''
    if not customer_data:
        return {}, None
    
    valid_customers = [
        customer for customer in customer_data 
        if all(k in customer for k in ['name', 'email', 'country']) 
        and re.match(EMAIL_PATTERN, customer['email'])
    ]
    
    country_counts = collections.Counter([customer['country'] for customer in valid_customers])

    if not valid_customers:
        return country_counts, None

    customer_df = pd.DataFrame(valid_customers)
    ax = customer_df['country'].value_counts().plot(kind='bar', figsize=(10,6))
    ax.set_ylabel('Number of Customers')
    ax.set_xlabel('Country')
    ax.set_title('Customer Counts by Country')
    plt.tight_layout()

    return dict(country_counts), ax
    

import unittest
import collections
import re
from faker import Faker
fake = Faker()
Faker.seed(0)
def generate_mock_data(num_entries=3):
    names = [fake.unique.first_name() for _ in range(num_entries)]
    countries = [fake.country() for _ in range(num_entries)]
    data = []
    for name, country in zip(names, countries):
        data.append(
            {
                "name" : name,
                "country" : country,
                "email" : f"{fake.unique.word()}@domain{fake.random_int(min=0, max=num_entries)}.com"
            }
        )
    return data

class TestCases(unittest.TestCase):
    """Test cases for the f_198 function."""
    def test_case_1(self):
        """Test with a list of customers generated using Faker"""
        mock_data = generate_mock_data(num_entries=5)
        expected_output = collections.Counter([customer['country'] for customer in mock_data if re.match(EMAIL_PATTERN, customer['email'])]) 
        country_counts, ax = f_198(mock_data)
        # Assert that the dictionary output matches the expected output
        self.assertEqual(country_counts, expected_output)
        # Correctly extracting text from x-tick labels for comparison
        xtick_labels = [label.get_text() for label in ax.get_xticklabels()]
        self.assertListEqual(xtick_labels, list(expected_output.keys()))

    def test_case_2(self):
        """ Test with an empty list"""
        input_data = []
        expected_output = {}
        country_counts, ax = f_198(input_data)
        # Assert that the dictionary output matches the expected output
        self.assertEqual(country_counts, expected_output)
        
        # If the input list is empty, ax should be None
        self.assertIsNone(ax)

    def test_case_3(self):
        """Test with some invalid emails in the list"""
        mock_data = generate_mock_data(num_entries=9)
        input_data = mock_data + [{'name': 'Invalid', 'email': 'invalid_email', 'country': 'InvalidCountry'}]
        expected_output = collections.Counter([customer['country'] for customer in input_data if re.match(EMAIL_PATTERN, customer['email'])])
        
        country_counts, ax = f_198(input_data)
        
        # Assert that the dictionary output matches the expected output
        self.assertEqual(country_counts, expected_output)

    def test_case_4(self):
        """Test with only invalid emails in the list"""
        input_data = [
            {'name': 'Invalid1', 'email': 'invalid_email1', 'country': 'InvalidCountry1'},
            {'name': 'Invalid2', 'email': 'invalid_email2', 'country': 'InvalidCountry2'}
        ]
        expected_output = {}
        country_counts, ax = f_198(input_data)
        # Assert that the dictionary output matches the expected output
        self.assertEqual(country_counts, expected_output)
        # Assert that the plot is None
        self.assertEqual(ax, None)

    def test_case_5(self):
        """Test with duplicate countries to check aggregation"""
        mock_data = generate_mock_data(num_entries=7)
        input_data = mock_data + mock_data
        expected_output = collections.Counter([customer['country'] for customer in input_data if re.match(EMAIL_PATTERN, customer['email'])])
        country_counts, ax = f_198(input_data)
        # Assert that the dictionary output matches the expected output
        self.assertEqual(country_counts, expected_output)
        xtick_labels = sorted([label.get_text() for label in ax.get_xticklabels()])
        self.assertListEqual(xtick_labels, sorted(list(expected_output.keys())))

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__" :
    run_tests()