import random
from datetime import datetime
import matplotlib.pyplot as plt

def f_388(epoch_milliseconds, seed=None):
    """
    Generate and draw a sales trend for different categories from a particular epoch milliseconds
    to the current time.

    The function selects category from ['Electronics', 'Clothing', 'Home', 'Books', 'Sports'].
    Each day's sales are randomly determined between 10 and 50 units for each category.
    The plot's x-axis represents 'Days since (the start date)', and the y-axis represents 'Sales' units.

    Parameters:
    - epoch_milliseconds (int): Start time. Must be positive and before current time.
    - seed (int, optional): Seed for random number generation. Default is None (no seed).

    Returns:
    - sales_data (dict): Sales data for different categories over days.
    - ax (plt.Axes): The plot depicting the sales trend.

    Raises:
    - ValueError: If the start time is negative or after the current time.
    
    Requirements:
    - random
    - datetime.datetime
    - matplotlib

    Example:
    >>> random.seed(42)
    >>> sales_data, ax = f_388(1236472051807, seed=42)
    >>> type(sales_data)
    <class 'dict'>
    >>> list(sales_data['Electronics'])[:3]
    [50, 24, 47]
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    CATEGORIES = ["Electronics", "Clothing", "Home", "Books", "Sports"]

    if seed is not None:
        random.seed(seed)

    if epoch_milliseconds < 0:
        raise ValueError("Start time cannot be negative.")

    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    current_time = datetime.now()
    days_diff = (current_time - start_time).days
    if days_diff <= 0:
        raise ValueError("Start date must be before current time.")

    sales_data = {category: [0] * days_diff for category in CATEGORIES}

    for i in range(days_diff):
        for category in CATEGORIES:
            sales = random.randint(10, 50)
            sales_data[category][i] += sales

    fig, ax = plt.subplots()
    for category, sales in sales_data.items():
        ax.plot(range(days_diff), sales, label=category)

    ax.set_xlabel("Days since " + start_time.strftime("%Y-%m-%d %H:%M:%S"))
    ax.set_ylabel("Sales")
    ax.legend()

    return sales_data, ax


import unittest
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta


class TestCases(unittest.TestCase):
    def _check_sales_data(self, sales_data, expected_days):
        """Utility function to validate sales data."""
        self.assertIsInstance(sales_data, dict)
        self.assertEqual(
            set(sales_data.keys()),
            set(["Electronics", "Clothing", "Home", "Books", "Sports"]),
        )
        for category, sales in sales_data.items():
            self.assertEqual(len(sales), expected_days)
            for sale in sales:
                self.assertGreaterEqual(sale, 10)
                self.assertLessEqual(sale, 50)

    def test_case_1(self):
        # Basic test on manual example - Jan 1 2021
        sales_data, ax = f_388(1609459200000, seed=1)
        self.assertIsInstance(sales_data, dict)
        self.assertIsInstance(ax, plt.Axes)
        self._check_sales_data(
            sales_data,
            (datetime.now() - datetime.fromtimestamp(1609459200000 / 1000.0)).days,
        )
        self.assertEqual(ax.get_ylabel(), "Sales")

    def test_case_2(self):
        # Basic test on current date - should raise error
        current_epoch = int(datetime.now().timestamp() * 1000)
        with self.assertRaises(ValueError):
            f_388(current_epoch, seed=2)

    def test_case_3(self):
        # Test random seed
        t = 1609459200000
        sales_data1, _ = f_388(t, seed=42)
        sales_data2, _ = f_388(t, seed=42)
        sales_data3, _ = f_388(t, seed=3)
        self.assertEqual(sales_data1, sales_data2)
        self.assertNotEqual(sales_data1, sales_data3)

    def test_case_4(self):
        # Test that future date raises ValueError
        future_epoch = int((datetime.now() + timedelta(days=1)).timestamp() * 1000)
        with self.assertRaises(ValueError):
            f_388(future_epoch, seed=4)

    def test_case_5(self):
        # Test that negative epoch milliseconds raise an error
        with self.assertRaises(ValueError):
            f_388(-1609459200000, seed=5)

    def test_case_6(self):
        # Test that non-integer types for epoch milliseconds raise a TypeError
        with self.assertRaises(TypeError):
            f_388("1609459200000", seed=6)

    def tearDown(self):
        plt.close("all")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
