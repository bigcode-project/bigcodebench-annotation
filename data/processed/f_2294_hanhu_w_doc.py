import random
import bisect
import statistics
import matplotlib.pyplot as plt


def f_412(n, value):
    """
    Generates 'n' random numbers between 0 and 1, finds those greater than their average,
    and counts how many are greater than or equal to a specified value, then plots 
    the sorted numbers.

    Parameters:
        n (int): The number of random numbers to generate.
        value (float): The value to compare against the random numbers.

    Returns:
        list: Numbers greater than the average of all generated numbers.
        int: The count of numbers greater than or equal to the specified value.

    Requirements:
    - random
    - bisect
    - statistics
    - matplotlib.pyplot

    Examples:
    >>> greater_avg, count = f_412(10, 0.5)
    >>> isinstance(greater_avg, list) and isinstance(count, int)
    True
    >>> len(greater_avg) <= 10
    True
    """
    if n < 1:  # Handle case where n is 0 or less
        return [], 0
    numbers = [random.random() for _ in range(n)]
    avg = statistics.mean(numbers)
    greater_avg = [x for x in numbers if x > avg]
    numbers.sort()
    bpoint = bisect.bisect_right(numbers, value)
    num_greater_value = len(numbers) - bpoint
    plt.plot(numbers)
    plt.show()
    return greater_avg, num_greater_value

import unittest
from unittest.mock import MagicMock, patch
class TestCases(unittest.TestCase):
    def setUp(self):
        # Mock random.random to return a fixed sequence of numbers
        self.random_sequence = [0.6, 0.4, 0.8, 0.2, 0.5]
        self.random_mock = MagicMock(side_effect=self.random_sequence)
    @patch('matplotlib.pyplot.show')
    def test_plotting_mocked(self, mock_show):
        """ Test that the function calls plt.show(). """
        with patch('random.random', self.random_mock):
            _ = f_412(5, 0.5)
            mock_show.assert_called_once()
    def test_return_types(self):
        """ Test that the function returns a list and an int. """
        greater_avg, count = f_412(10, 0.5)
        self.assertIsInstance(greater_avg, list)
        self.assertIsInstance(count, int)
    def test_number_of_elements(self):
        """Check if the list contains only numbers greater than the average."""
        with patch('random.random', self.random_mock):
            greater_avg, _ = f_412(5, 0.5)
            self.assertEqual(len(greater_avg), 2)
    def test_count_greater_than_or_equal_value(self):
        """Verify the count includes numbers greater than or equal to the value."""
        with patch('random.random', self.random_mock):
            _, count = f_412(5, 0.5)
            self.assertEqual(count, 2)
    def test_empty_case(self):
        """Test the function's behavior with n=0."""
        greater_avg, count = f_412(0, 0.5)
        self.assertEqual((greater_avg, count), ([], 0))
