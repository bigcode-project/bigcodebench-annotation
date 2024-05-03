from texttable import Texttable
import os
import psutil

def f_3115():
    """
    Generates a table displaying the system's CPU usage, memory usage, and disk usage.

    Returns:
        A string representation of a table with the columns of 'Item' and 'Value',
        and the following system information:
        - CPU Usage (%)
        - Memory Usage (%)
        - Disk Usage (%)

    Requirements:
    - texttable.Texttable
    - os
    - psutil

    Examples:
    >>> table_str = f_3115()
    >>> isinstance(table_str, str)
    True
    >>> 'CPU Usage (%)' in table_str and 'Memory Usage (%)' in table_str
    True
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage(os.sep)

    table = Texttable()
    table.add_rows([
        ['Item', 'Value'],
        ['CPU Usage (%)', cpu_usage],
        ['Memory Usage (%)', memory_info.percent],
        ['Disk Usage (%)', disk_usage.percent]
    ])
    return table.draw()

import unittest
import re  # Import the regular expressions library

class TestCases(unittest.TestCase):
    def setUp(self):
        self.result = f_3115()

    def test_return_type(self):
        """Test that the function returns a string."""
        self.assertIsInstance(self.result, str)

    def test_table_headers(self):
        """Test the presence of correct headers in the table."""
        for header in ['CPU Usage (%)', 'Memory Usage (%)', 'Disk Usage (%)']:
            with self.subTest(header=header):
                self.assertIn(header, self.result)

    def test_non_empty_values(self):
        """Test that the table's values are not empty or zero."""
        # Extract numeric values using a regular expression
        values = re.findall(r'\|\s*[\d.]+\s*\|', self.result)
        # Convert extracted strings to float and test they are greater than 0
        for value_str in values:
            value = float(value_str.strip('| ').strip())
            with self.subTest(value=value):
                self.assertTrue(value > 0)

    def test_value_ranges(self):
        """Test that CPU and memory usage percentages are within 0-100%."""
        values = re.findall(r'\|\s*[\d.]+\s*\|', self.result)
        for value_str in values:
            value = float(value_str.strip('| ').strip())
            with self.subTest(value=value):
                self.assertTrue(0 <= value <= 100)

    def test_table_structure(self):
        """Test that the table's structure is as expected."""
        # Split the table into rows based on the unique row separator pattern
        parts = self.result.split('+------------------+--------+')
        # Filter out empty parts that might occur due to the split operation
        non_empty_parts = [part for part in parts if part.strip()]
        # Expect 4 non-empty parts: 1 header row + 3 data rows
        self.assertEqual(len(non_empty_parts), 3)



def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
