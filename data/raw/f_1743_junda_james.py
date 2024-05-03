import pandas as pd
import matplotlib.pyplot as plt

def f_1743(df, items=None, locations=None):
    """
    Generates a bar chart representing the distribution of specified items across given locations.
    
    The function takes a DataFrame with 'Item' and 'Location' columns and plots the count of each item
    per location. If lists of items and locations are provided, the chart will only include those specified,
    otherwise it defaults to a predefined list.

    Parameters:
    - df (pandas.DataFrame): DataFrame containing 'Item' and 'Location' columns.
    - items (list of str, optional): Specific items to include in the chart. Defaults to a predefined list
      ['apple', 'banana', 'grape', 'orange', 'pineapple'] if None.
    - locations (list of str, optional): Specific locations to include in the chart. Defaults to a predefined
      list ['store1', 'store2', 'store3', 'store4', 'store5'] if None.

    Returns:
    - matplotlib.axes.Axes: Axes object with the plotted bar chart.

    Raises:
    - ValueError: If 'df' is not a DataFrame, or if 'Item' or 'Location' columns are missing.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame({
    ...     'Item': ['apple', 'banana', 'apple', 'orange'],
    ...     'Location': ['store1', 'store2', 'store3', 'store1']
    ... })
    >>> ax = f_1743(df)
    >>> ax.get_title()
    'Item Distribution by Location'
    """
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['Item', 'Location']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns.")

    items = items or ['apple', 'banana', 'grape', 'orange', 'pineapple']
    locations = locations or ['store1', 'store2', 'store3', 'store4', 'store5']

    item_count_df = df.groupby(['Location', 'Item']).size().unstack().fillna(0)
    ax = item_count_df.plot(kind='bar', stacked=True)
    ax.set_title('Item Distribution by Location')
    ax.set_ylabel('Count')

    return ax

import unittest
import pandas as pd
import matplotlib.pyplot as plt

def get_bar_values(ax):
    """
    Extracts the heights of bars from a Matplotlib Axes object.

    Parameters:
    ax (Axes): A Matplotlib Axes object containing a bar chart.

    Returns:
    List[List[float]]: A list of lists containing the heights of the bars in each group.
    """
    values = []
    for container in ax.containers:
        values.append([bar.get_height() for bar in container])
    return values


class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Item': ['apple', 'banana', 'apple', 'orange', 'grape', 'pineapple', 'banana', 'orange'],
            'Location': ['store1', 'store2', 'store1', 'store3', 'store4', 'store5', 'store3', 'store2']
        })

    def test_value(self):
        ax = f_1743(self.df)
        self.assertIsInstance(ax, plt.Axes)
        bar_values = get_bar_values(ax)
            
        value = [[2.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0]]
        self.assertEqual(bar_values, value, "DataFrame contents should match the expected output")
        
    def test_return_type(self):
        ax = f_1743(self.df)
        self.assertIsInstance(ax, plt.Axes)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            f_1743(pd.DataFrame({'a': [1, 2], 'b': [3, 4]}))

    def test_custom_items_and_locations(self):
        custom_items = ['item1', 'item2']
        custom_locations = ['loc1', 'loc2']
        df = pd.DataFrame({'Item': custom_items * 2, 'Location': custom_locations * 2})
        ax = f_1743(df, items=custom_items, locations=custom_locations)
        self.assertIsInstance(ax, plt.Axes)

    def test_plot_title_and_labels(self):
        ax = f_1743(self.df)
        self.assertEqual(ax.get_title(), 'Item Distribution by Location')
        self.assertEqual(ax.get_ylabel(), 'Count')


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