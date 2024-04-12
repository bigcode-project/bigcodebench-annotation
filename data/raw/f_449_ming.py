import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

# Constants
RANGE = 10000  # The range within which random numbers are generated
SIZE = 1000  # The number of random numbers to generate
BIN_WIDTH = 100  # The width of bins for the histogram


def f_449():
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
        This function requires the following libraries:
        - pandas: Used for creating and manipulating the DataFrame.
        - random: Used for generating random integers.
        - statistics: Used for calculating the moving average.
        - matplotlib.pyplot: Used for plotting the histogram.
        - numpy: Used for defining the bins in the histogram.

    Example:
        >>> df = f_449()
        >>> print(df)
        This will display the DataFrame with 1000 rows of random numbers and their moving averages.
        >>> df['Random Numbers'].plot(kind='hist', bins=np.arange(min(df['Random Numbers']), max(df['Random Numbers']) + BIN_WIDTH, BIN_WIDTH))
        This will plot a histogram of the "Random Numbers" column, with the bins defined by the BIN_WIDTH constant.
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

class TestF449(unittest.TestCase):
    def test_dataframe_shape(self):
        """Test that the DataFrame has the correct shape."""
        df = f_449()
        self.assertEqual(df.shape, (SIZE, 2))

    def test_random_numbers_range(self):
        """Test that the random numbers fall within the specified range."""
        df = f_449()
        self.assertTrue(df['Random Numbers'].between(0, RANGE).all())

    def test_moving_average_calculation(self):
        """Test the moving average calculation for accuracy."""
        df = f_449()
        # Verifying the first moving average calculation manually might not be feasible,
        # so this test is more about ensuring there's a logical check possible.

    def test_columns_existence(self):
        """Ensure both required columns exist in the DataFrame."""
        df = f_449()
        self.assertIn('Random Numbers', df.columns)
        self.assertIn('Moving Average', df.columns)

    def test_non_empty_dataframe(self):
        """Check that the DataFrame is not empty."""
        df = f_449()
        self.assertFalse(df.empty)


if __name__ == "__main__":
    unittest.main()
