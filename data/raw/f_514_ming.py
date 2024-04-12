import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def f_514(dataframe, target_value='332'):
    """
    Searches a given DataFrame for occurrences of a specified target value and visualizes these occurrences using a heatmap.

    Parameters:
    - dataframe (pd.DataFrame): The input DataFrame to search.
    - target_value (str, optional): The value to search for in the DataFrame. Defaults to '332'.

    Returns:
    - tuple: A tuple containing:
        - pd.DataFrame: A DataFrame with Boolean values indicating the presence of the target value in the input DataFrame.
        - matplotlib.axes._subplots.AxesSubplot: The Axes object of the heatmap.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - seaborn

    Example:
    >>> df = pd.DataFrame({
    ...     'Column1': ['0', 'a', '332', '33'],
    ...     'Column2': ['1', 'bb', '33', '22'],
    ...     'Column3': ['2', 'ccc', '2', '332']
    ... })
    >>> mask, ax = f_514(df, '332')
    """
    mask = dataframe.applymap(lambda x: x == target_value)

    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(mask, cmap='Blues', cbar=False)  # Adjusted to not display color bar for clarity in Boolean visualization
    plt.show()

    return mask, ax


import unittest
import pandas as pd

class TestF514(unittest.TestCase):
    def setUp(self):
        """Create a sample DataFrame for testing."""
        self.df = pd.DataFrame({
            'Column1': ['0', 'a', '332', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '332']
        })

    def test_target_value_occurrence(self):
        """Test if the function correctly identifies the target value."""
        mask, _ = f_514(self.df, '332')
        self.assertTrue(mask.iloc[2, 0], "Mask should be True where target value '332' exists.")

    def test_target_value_absence(self):
        """Test if the function correctly identifies absence of the target value."""
        mask, _ = f_514(self.df, '332')
        self.assertFalse(mask.iloc[0, 0], "Mask should be False where target value '332' does not exist.")

    def test_return_type(self):
        """Test the return type of the function."""
        mask, ax = f_514(self.df, '332')
        self.assertIsInstance(mask, pd.DataFrame, "First return value should be a DataFrame.")
        self.assertTrue(hasattr(ax, 'get_figure'), "Second return value should be an Axes object with a 'get_figure' method.")

    def test_default_target_value(self):
        """Test the function with the default target value."""
        mask, _ = f_514(self.df)
        self.assertEqual(mask.sum().sum(), 2, "There should be exactly 2 occurrences of the default target value '332'.")

    def test_custom_target_value(self):
        """Test the function with a custom target value."""
        mask, _ = f_514(self.df, 'a')
        self.assertEqual(mask.sum().sum(), 1, "There should be exactly 1 occurrence of the custom target value 'a'.")


if __name__ == '__main__':
    unittest.main()
