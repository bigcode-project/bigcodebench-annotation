import random
from scipy import stats

def f_2260(animals, mean):
    """
    Simulates sales in a pet shop based on a randomly determined number of customers.
    Each customer randomly buys one type of animal from the specified list of animals.
    The function displays and returns a summary of the sales, where the number of customers 
    follows a Poisson distribution with the specified mean (mu).

    Parameters:
        animals (list of str): A list of animal types available for sale.

    Returns:
        dict: A dictionary with animal types as keys and the number of sales as values.

    Requirements:
    - random
    - scipy.stats

    Examples:
    >>> ANIMALS = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
    >>> sales = f_2260(ANIMALS, 120)
    >>> isinstance(sales, dict)
    True
    >>> all(animal in ANIMALS for animal in sales.keys())
    True
    >>> sum(sales.values()) >= 0  # sum of sales should be non-negative
    True
    """
    if not animals:
        return {}

    sales = {animal: 0 for animal in animals}
    num_customers = stats.poisson(mu=mean).rvs()

    for _ in range(num_customers):
        animal = random.choice(animals)
        sales[animal] += 1
    return sales

import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def setUp(self):
        self.animals = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_typical_case(self, mock_poisson, mock_choice):
        """Test typical case with mock number of customers and sales."""
        mock_poisson.return_value.rvs.return_value = 100
        mock_choice.side_effect = lambda x: x[0]  # always choose the first animal
        expected = {'Dog': 100, 'Cat': 0, 'Bird': 0, 'Fish': 0, 'Hamster': 0}
        result = f_2260(self.animals, 100)
        self.assertEqual(result, expected)
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_zero_customers(self, mock_poisson, mock_choice):
        """Test the scenario where zero customers arrive."""
        mock_poisson.return_value.rvs.return_value = 0
        expected = {'Dog': 0, 'Cat': 0, 'Bird': 0, 'Fish': 0, 'Hamster': 0}
        result = f_2260(self.animals, 0)
        self.assertEqual(result, expected)
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_large_number_of_customers(self, mock_poisson, mock_choice):
        """Test the function with a very large number of customers."""
        mock_poisson.return_value.rvs.return_value = 1000
        mock_choice.side_effect = lambda x: 'Dog'  # simulate all choosing 'Dog'
        expected = {'Dog': 1000, 'Cat': 0, 'Bird': 0, 'Fish': 0, 'Hamster': 0}
        result = f_2260(self.animals, 500)
        self.assertEqual(result, expected)
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_random_animal_selection(self, mock_poisson, mock_choice):
        """Test random selection of animals."""
        mock_poisson.return_value.rvs.return_value = 5
        mock_choice.side_effect = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
        result = f_2260(self.animals, 5)
        expected = {'Dog': 1, 'Cat': 1, 'Bird': 1, 'Fish': 1, 'Hamster': 1}
        self.assertEqual(result, expected)
    def test_empty_animal_list(self):
        """Test with an empty list of animals."""
        result = f_2260([], 10)
        self.assertEqual(result, {})
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_return_type(self, mock_poisson, mock_random):
        """Test that the function returns a dictionary."""
        mock_poisson.return_value.rvs.return_value = 5
        mock_random.side_effect = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
        result = f_2260(self.animals, 120)
        self.assertIsInstance(result, dict)
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_sales_content(self, mock_poisson, mock_random):
        """Test the content of the sales dictionary matches the expected distribution of one each."""
        mock_poisson.return_value.rvs.return_value = 5
        mock_random.side_effect = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
        result = f_2260(self.animals, 120)
        self.assertEqual(result, {'Dog': 1, 'Cat': 1, 'Bird': 1, 'Fish': 1, 'Hamster': 1})
    @patch('scipy.stats.poisson')
    def test_no_customer(self, mock_poisson):
        """Test the function with zero customers."""
        mock_poisson.return_value.rvs.return_value = 0
        result = f_2260(self.animals, 120)
        self.assertEqual(result, {animal: 0 for animal in self.animals})
    @patch('random.choice')
    @patch('scipy.stats.poisson')
    def test_all_animals_sold(self, mock_poisson, mock_random):
        """Test that all animal types are considered in sales."""
        mock_poisson.return_value.rvs.return_value = 5
        mock_random.side_effect = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
        result = f_2260(self.animals, 120)
        self.assertTrue(all(animal in result for animal in self.animals))
