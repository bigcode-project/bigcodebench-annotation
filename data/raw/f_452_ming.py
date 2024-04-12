import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants defining the range of random integers and the size of the DataFrame
RANGE = 100
SIZE = 1000


def f_452():
    """
    Generates a DataFrame with two columns, 'X' and 'Y', each filled with random integers within a specified range,
    and plots these points using a scatter plot. The visualization is created using Seaborn on top of Matplotlib.

    The function is designed to be parameter-free for simplicity, utilizing constants for configuration.

    Returns:
        pd.DataFrame: A DataFrame with 'X' and 'Y' columns containing the generated random integers.

    Requirements:
        - numpy: Used for generating arrays of random integers.
        - pandas: Utilized for creating and handling the DataFrame.
        - seaborn: For plotting the scatter plot in a more aesthetically pleasing manner than Matplotlib's default.
        - matplotlib.pyplot: Provides the underlying plotting functions used by Seaborn and controls for displaying the plot.

    No Parameters.

    Example:
        >>> df = f_452()
        This will display a scatter plot of points corresponding to the 'X' and 'Y' columns in the DataFrame.
        The DataFrame itself is returned and can be inspected or used for further analysis.
    """
    # Generate the DataFrame with random integers within the specified range [0, RANGE)
    df = pd.DataFrame({
        'X': np.random.randint(0, RANGE, SIZE),
        'Y': np.random.randint(0, RANGE, SIZE)
    })

    # Draw a scatter plot using Seaborn for a more refined visual output
    sns.scatterplot(data=df, x='X', y='Y')
    plt.show()

    return df


import unittest

class TestF452(unittest.TestCase):
    def test_dataframe_shape(self):
        """Test that the DataFrame has the correct shape."""
        df = f_452()
        self.assertEqual(df.shape, (SIZE, 2))

    def test_random_range(self):
        """Test that the random numbers fall within the specified range."""
        df = f_452()
        self.assertTrue(df['X'].between(0, RANGE-1).all())
        self.assertTrue(df['Y'].between(0, RANGE-1).all())

    def test_columns_existence(self):
        """Ensure both 'X' and 'Y' columns exist."""
        df = f_452()
        self.assertIn('X', df.columns)
        self.assertIn('Y', df.columns)

    def test_non_empty_dataframe(self):
        """Check that the DataFrame is not empty."""
        df = f_452()
        self.assertFalse(df.empty)

    def test_columns_type(self):
        """Test that 'X' and 'Y' columns are of integer type."""
        df = f_452()
        self.assertTrue(np.issubdtype(df['X'].dtype, np.integer))
        self.assertTrue(np.issubdtype(df['Y'].dtype, np.integer))


if __name__ == "__main__":
    unittest.main()
