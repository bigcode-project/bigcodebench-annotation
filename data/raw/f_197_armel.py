import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f_197(inventory_data):
    """
    Analyze a list of inventory data, returning summary statistics and a line chart of inventory levels over time.

    Parameters:
    - inventory_data (list): A list of dictionaries where each dictionary represents inventory data for a product 
                             at a specific time. Each dictionary should contain the keys 'product', 'inventory', and 'time'.
                             e.g., [{'product': 'apple', 'inventory': 60, 'time': '2021-09-01'}, 
                                    {'product': 'orange', 'inventory': 65, 'time': '2021-09-01'}]

    Returns:
    - dict: Summary statistics (mean, median, mode) for the inventory data of each product. Each key of the dictionary represents a product and the associated value is a dictionary with the keys 'mean', 'median' and 'mode'.
    - matplotlib.axes._subplots.AxesSubplot: A line plot representing inventory levels over time for each product. If the list of inventory is empty, return None.

    Requirements:
    - collections: For efficient data structures (defaultdict) and counting occurrences (Counter).
    - numpy: For mathematical computations (mean, median).
    - pandas: For data manipulation and visualization.
    - matplotlib.pyplot: For plotting inventory levels over time.

    Example:
    >>> inventory_data = [{'product': 'apple', 'inventory': 60, 'time': '2021-09-01'}, 
                          {'product': 'orange', 'inventory': 65, 'time': '2021-09-01'}]
    >>> stats, ax = f_197(inventory_data)
    >>> print(stats)
    {'apple': {'mean': 60.0, 'median': 60.0, 'mode': 60}, 'orange': {'mean': 65.0, 'median': 65.0, 'mode': 65}}
    """
    if not inventory_data:
        return {}, None

    inventory = collections.defaultdict(list)
    for data in inventory_data:
        inventory[data['product']].append(data['inventory'])
    
    products = list(inventory.keys())
    summary_stats = {}
    for product in products:
        inventory_array = np.array(inventory[product])
        summary_stats[product] = {
            'mean': np.mean(inventory_array),
            'median': np.median(inventory_array),
            'mode': collections.Counter(inventory_array).most_common(1)[0][0]
        }

    inventory_df = pd.DataFrame(inventory_data)
    inventory_df['time'] = pd.to_datetime(inventory_df['time'])
    ax = inventory_df.pivot(index='time', columns='product', values='inventory').plot()
    ax.legend()
    return summary_stats, ax

import unittest
from faker import Faker
fake = Faker()
Faker.seed(0)

def generate_mock_data(num_entries=10, num_products=3):
    products = [fake.unique.first_name() for _ in range(num_products)]
    inventory_data = []
    
    # Ensure each product has at least one entry
    for product in products:
        inventory_data.append({
            'product': product,
            'inventory': fake.random_int(min=10, max=200),
            'time': fake.date_this_decade()
        })
    
    # Generate the remaining entries
    for _ in range(num_entries - num_products):
        product = fake.random_element(elements=products)
        inventory_data.append({
            'product': product,
            'inventory': fake.random_int(min=10, max=200),
            'time': fake.date_this_decade()
        })
    
    return inventory_data

class TestCases(unittest.TestCase):
    """Test cases for the f_197 function."""    
    def test_case_1(self):
        """Test normal operation with valid input"""
        inventory_data = [
            {'product': 'apple', 'inventory': 60, 'time': '2021-09-01'},
            {'product': 'orange', 'inventory': 65, 'time': '2021-09-01'}
        ]
        stats, ax = f_197(inventory_data)
        expected_stats = {
            'apple': {'mean': 60.0, 'median': 60.0, 'mode': 60},
            'orange': {'mean': 65.0, 'median': 65.0, 'mode': 65}
        }
        self.assertEqual(stats, expected_stats)
    
    def test_case_2(self):
        """Test normal operation with valid input"""
        inventory_data = [
            {'product': 'apple', 'inventory': 60, 'time': '2021-09-01'},
            {'product': 'orange', 'inventory': 65, 'time': '2021-09-01'},
            {'product': 'apple', 'inventory': 62, 'time': '2021-09-02'},
            {'product': 'orange', 'inventory': 67, 'time': '2021-09-02'}
        ]
        stats, ax = f_197(inventory_data)
        expected_stats = {
            'apple': {'mean': 61.0, 'median': 61.0, 'mode': 60},
            'orange': {'mean': 66.0, 'median': 66.0, 'mode': 65}
        }
        self.assertEqual(stats, expected_stats)
    
    def test_case_3(self):
        """Test with empty input"""
        inventory_data = []
        stats, ax = f_197(inventory_data)
        self.assertEqual(stats, {})
        self.assertIsNone(ax)
    
    def test_case_4(self):
        """Test normal operation with valid input"""
        inventory_data = generate_mock_data(num_entries=10, num_products=3)
        stats, ax = f_197(inventory_data)
        self.assertEqual(len(stats), 3)
        self.assertIsNotNone(ax)
    
    def test_case_5(self):
        """Test normal operation with valid input"""
        inventory_data = generate_mock_data(num_entries=20, num_products=5)
        stats, ax = f_197(inventory_data)
        self.assertEqual(len(stats), 5)
        self.assertIsNotNone(ax)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__" :
    run_tests()