import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import random

def f_1736(temperatures):
    """
    Calculate and plot the daytime temperatures for New York over a given period. The plot uses Arial font for display.

    Parameters:
        temperatures (pandas.DataFrame): The temperatures data as a pandas DataFrame with a DateTimeIndex 
                                         in the 'America/New_York' timezone and a 'temperature' column.

    Returns:
        matplotlib.axes.Axes: The Axes object containing the temperature plot.
        
    for the returned plot,  set the xlabel as 'Date', ylabel as 'Temperature (°C)' and
    title as Daily Temperatures in New York

    Raises:
        ValueError: If the input DataFrame is not in the expected format or empty.

    Requirements:
        - matplotlib
        - pandas
        - random
        - datetime

    Example:
        >>> temperatures = pd.DataFrame({
        ...     'temperature': [random.randint(-10, 30) for _ in range(365)],
        ...     'date': pd.date_range(start='01-01-2023', periods=365, tz='America/New_York')
        ... }).set_index('date')
        >>> ax = f_1736(temperatures)
        >>> type(ax)
        <class 'matplotlib.axes._axes.Axes'>
    """
    try:
        if temperatures.empty or not isinstance(temperatures, pd.DataFrame):
            raise ValueError("Input temperatures must be a non-empty pandas DataFrame.")

        # Setting the font to Arial
        font = {'sans-serif': 'Arial', 'family': 'sans-serif'}
        plt.rc('font', **font)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(temperatures.index, temperatures['temperature'])
        ax.set_xlabel('Date')
        ax.set_ylabel('Temperature (°C)')
        ax.set_title('Daily Temperatures in New York')

        return ax

    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

import unittest
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import random

class TestCases(unittest.TestCase):

    def setUp(self):
        self.temperatures = pd.DataFrame({
            'temperature': [random.randint(-10, 30) for _ in range(365)],
            'date': pd.date_range(start='01-01-2023', periods=365, tz='America/New_York')
        }).set_index('date')

    def test_basic_functionality(self):
        ax = f_1736(self.temperatures)
        self.assertIsInstance(ax, plt.Axes)

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1736(pd.DataFrame())

    def test_incorrect_dataframe(self):
        incorrect_df = pd.DataFrame({'temp': [20, 21], 'time': [datetime.now(), datetime.now()]})
        with self.assertRaises(ValueError):
            f_1736(incorrect_df)

    def test_data_on_plot(self):
        ax = f_1736(self.temperatures)
        self.assertEqual(len(ax.get_lines()[0].get_xdata()), 365)
        self.assertEqual(len(ax.get_lines()[0].get_ydata()), 365)

    def test_plot_labels_and_title(self):
        ax = f_1736(self.temperatures)
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Temperature (°C)')
        self.assertEqual(ax.get_title(), 'Daily Temperatures in New York')
    
    def test_value_consistency(self):
        ax = f_1736(self.temperatures)
        line = ax.get_lines()[0]
        plot_dates = line.get_xdata()
        plot_temperatures = line.get_ydata()
        for date, temperature in zip(plot_dates, plot_temperatures):
            self.assertAlmostEqual(temperature, self.temperatures.at[pd.Timestamp(date), 'temperature'])

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