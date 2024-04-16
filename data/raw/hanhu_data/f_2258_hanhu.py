import random
import builtins

def f_2260(animals):
    """
    Simulates sales in a pet shop based on user input for the number of customers.
    Each customer randomly buys one type of animal from the specified list of animals.
    The function displays and returns a summary of the sales.

    Parameters:
        animals (list of str): A list of animal types available for sale.

    Returns:
        dict: A dictionary with animal types as keys and the number of sales as values.

    Requirements:
    - random
    - builtins

    Examples:
    >>> ANIMALS = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']
    >>> sales = f_2260(ANIMALS)  # Requires user input during execution
    >>> isinstance(sales, dict)
    True
    >>> all(animal in ANIMALS for animal in sales)
    True
    """
    sales = {animal: 0 for animal in animals}
    num_customers = int(builtins.input("Enter the number of customers: "))

    for _ in range(num_customers):
        animal = random.choice(animals)
        sales[animal] += 1

    print(f"Sales of the day: {sales}")
    return sales

import unittest
from unittest.mock import patch

ANIMALS = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster']

class TestF2260(unittest.TestCase):
    @patch('builtins.input', return_value='10')
    @patch('random.choice', side_effect=['Dog', 'Cat', 'Bird', 'Fish', 'Hamster'] * 2)
    def test_return_type(self, mock_input, mock_random):
        """Test that the function returns a dictionary."""
        result = f_2260(ANIMALS)
        self.assertIsInstance(result, dict)

    @patch('builtins.input', return_value='5')
    @patch('random.choice', side_effect=['Dog', 'Cat', 'Bird', 'Fish', 'Hamster'])
    def test_sales_content(self, mock_input, mock_random):
        """Test the content of the sales dictionary."""
        result = f_2260(ANIMALS)
        self.assertEqual(result, {'Dog': 1, 'Cat': 1, 'Bird': 1, 'Fish': 1, 'Hamster': 1})

    @patch('builtins.input', return_value='0')
    def test_no_customer(self, mock_input):
        """Test the function with zero customers."""
        result = f_2260(ANIMALS)
        self.assertEqual(result, {animal: 0 for animal in ANIMALS})

    @patch('builtins.input', return_value='20')
    def test_all_animals_sold(self, mock_input):
        """Test that all animal types are considered in sales."""
        result = f_2260(ANIMALS)
        self.assertTrue(all(animal in result for animal in ANIMALS))

    @patch('builtins.print')
    @patch('builtins.input', return_value='3')
    @patch('random.choice', side_effect=['Dog', 'Dog', 'Cat'])
    def test_sales_summary_printed(self, mock_input, mock_random, mock_print):
        """Test that the sales summary is printed correctly."""
        f_2260(ANIMALS)
        actual_print_call_args = mock_print.call_args[0][0]
        expected_print_string = "Sales of the day: {'Dog': 2, 'Cat': 1, 'Bird': 0, 'Fish': 0, 'Hamster': 0}"
        self.assertEqual(actual_print_call_args, expected_print_string)


if __name__ == "__main__":
    unittest.main()
