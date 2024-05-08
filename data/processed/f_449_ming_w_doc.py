import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

# Constants
RANGE = 10000  # The range within which random numbers are generated
SIZE = 1000  # The number of random numbers to generate
BIN_WIDTH = 100  # The width of bins for the histogram


def f_258():
    """
    Generates a pandas DataFrame with two columns, "Random Numbers" and "Moving Average,"
    filled with random integers and their moving average, respectively.
    Additionally, this function plots a histogram of the "Random Numbers" column.

    No Parameters.

    Returns:
        pd.DataFrame: A DataFrame with two columns:
                      - "Random Numbers": Contains a list of randomly generated integers.
                      - "Moving Average": Contains the moving average of the random integers,
                                          calculated over a window that includes the current
                                          and previous 5 integers.

    Requirements:
        - pandas
        - random
        - statistics
        - matplotlib.pyplot
        - numpy

    Example:
        >>> df = f_258()
        >>> isinstance(df, pd.DataFrame)
        True
        >>> 'Random Numbers' in df.columns and 'Moving Average' in df.columns
        True
        >>> len(df)
        1000
        >>> all(df['Random Numbers'].between(0, RANGE))
        True
    """
    numbers = [random.randint(0, RANGE) for _ in range(SIZE)]
    moving_avg = [statistics.mean(numbers[max(0, i - 5):i + 1]) for i in range(SIZE)]
    df = pd.DataFrame({
        'Random Numbers': numbers,
        'Moving Average': moving_avg
    })
    plt.hist(df['Random Numbers'],
             bins=np.arange(min(df['Random Numbers']), max(df['Random Numbers']) + BIN_WIDTH, BIN_WIDTH))
    plt.title('Histogram of Random Numbers')
    plt.xlabel('Random Numbers')
    plt.ylabel('Frequency')
    plt.show()
    return df

import unittest
class TestCases(unittest.TestCase):
    def test_dataframe_shape(self):
        """Test that the DataFrame has the correct shape."""
        df = f_258()
        self.assertEqual(df.shape, (SIZE, 2))
    def test_random_numbers_range(self):
        """Test that the random numbers fall within the specified range."""
        df = f_258()
        self.assertTrue(df['Random Numbers'].between(0, RANGE).all())
    def test_moving_average_calculation(self):
        """Test that the moving average is correctly calculated."""
        df = f_258()
        # Assuming moving average calculation correctness check for the first few entries
        for i in range(6):  # Check the first 6 entries for a window of 6 elements
            expected_avg = statistics.mean(df['Random Numbers'].iloc[max(0, i - 5):i + 1])
            self.assertEqual(df['Moving Average'].iloc[i], expected_avg, "Moving average calculation mismatch.")
    def test_columns_existence(self):
        """Ensure both required columns exist in the DataFrame."""
        df = f_258()
        self.assertIn('Random Numbers', df.columns)
        self.assertIn('Moving Average', df.columns)
    def test_non_empty_dataframe(self):
        """Check that the DataFrame is not empty."""
        df = f_258()
        self.assertFalse(df.empty)
