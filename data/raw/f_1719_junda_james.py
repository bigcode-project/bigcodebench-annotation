import numpy as np
import pandas as pd
from datetime import timedelta

def f_1719(start_date, end_date, random_seed=42):
    """
    Generate and plot weather data for a specified date range.
    
    This function creates a DataFrame containing simulated daily weather data 
    within the specified date range. It generates random values for temperature, 
    humidity, and wind speed for each day. The function also plots these parameters 
    over the date range and returns both the DataFrame and the plot object.
    
    Parameters:
    - start_date (datetime): The start date for the data generation.
    - end_date (datetime): The end date for the data generation.
    - random_seed (int, optional): Seed for the random number generator to ensure reproducibility. Defaults to 42.
    
    The generated weather data ranges are as follows:
    - Temperature: Between -10°C and 40°C.
    - Humidity: Between 20% and 100%.
    - Wind Speed: Between 0 and 20 meters per second.
    
    Returns:
    - DataFrame: A pandas DataFrame with columns ['Date', 'Temperature', 'Humidity', 'Wind Speed'], containing the generated weather data for each day within the specified range.
    - Axes: A matplotlib Axes object of the plot showing the generated weather data.
    
    Raises:
    - ValueError: If 'end_date' is before 'start_date', indicating an invalid date range.

    Requirements:
    - numpy
    - pandas
    - datetime

    Example:
    >>> start_date = datetime(2021, 1, 1)
    >>> end_date = datetime(2021, 12, 31)
    >>> data, plot = f_1719(start_date, end_date)
    >>> print(data.head())  # Display the first few rows of the DataFrame 
            Date  Temperature   Humidity  Wind Speed
    0 2021-01-01     8.727006  96.057145   14.639879
    1 2021-01-02    19.932924  32.481491    3.119890
    2 2021-01-03    -7.095819  89.294092   12.022300
    3 2021-01-04    25.403629  21.646760   19.398197
    4 2021-01-05    31.622132  36.987129    3.636499
    >>> plot.get_figure().savefig("weather_data_plot.png")  # Save the plot to a file
    """
    if end_date < start_date:
        raise ValueError("End date must be after start date")

    np.random.seed(random_seed)

    COLUMNS = ["Date", "Temperature", "Humidity", "Wind Speed"]
    data = []
    date = start_date

    while date <= end_date:
        temp = np.random.uniform(-10, 40)
        humidity = np.random.uniform(20, 100)
        wind_speed = np.random.uniform(0, 20)
        data.append([date, temp, humidity, wind_speed])
        date += timedelta(days=1)

    df = pd.DataFrame(data, columns=COLUMNS)
    ax = df.plot(x='Date', y=['Temperature', 'Humidity', 'Wind Speed'], title="Generated Weather Data")

    return df, ax


import unittest
from datetime import datetime

class TestCases(unittest.TestCase):

    def test_random_reproducibility(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 10)
        df1, _ = f_1719(start_date, end_date, random_seed=42)
        df2, _ = f_1719(start_date, end_date, random_seed=42)
        self.assertTrue(df1.equals(df2), "DataFrames should be equal for the same random seed")

    def test_date_range(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 10)
        df, _ = f_1719(start_date, end_date)
        expected_days = (end_date - start_date).days + 1
        self.assertEqual(len(df), expected_days, "DataFrame should have one row per day in the date range")

    def test_random_seed_effect(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 10)
        df1, _ = f_1719(start_date, end_date, random_seed=42)
        df2, _ = f_1719(start_date, end_date, random_seed=43)
        self.assertFalse(df1.equals(df2), "DataFrames should be different for different random seeds")

    def test_data_value_ranges(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 10)
        df, _ = f_1719(start_date, end_date)
        self.assertTrue(df['Temperature'].between(-10, 40).all(), "Temperature values should be within -10 to 40")
        self.assertTrue(df['Humidity'].between(20, 100).all(), "Humidity values should be within 20 to 100")
        self.assertTrue(df['Wind Speed'].between(0, 20).all(), "Wind Speed values should be within 0 to 20")

    def test_plot_attributes(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 10)
        _, ax = f_1719(start_date, end_date)
        lines = [line.get_label() for line in ax.get_lines()]
        self.assertIn('Temperature', lines, "Plot should contain a line for Temperature")
        self.assertIn('Humidity', lines, "Plot should contain a line for Humidity")
        self.assertIn('Wind Speed', lines, "Plot should contain a line for Wind Speed")
        self.assertEqual(ax.get_xlabel(), 'Date', "X-axis should be labeled 'Date'")
    
    def test_correct_column_names(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 5)
        df, _ = f_1719(start_date, end_date)
        expected_columns = ['Date', 'Temperature', 'Humidity', 'Wind Speed']
        self.assertListEqual(list(df.columns), expected_columns, "DataFrame should have the correct column names")

    def test_non_empty_dataframe(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 5)
        df, _ = f_1719(start_date, end_date)
        self.assertFalse(df.empty, "DataFrame should not be empty for a valid date range")

    def test_plot_object_type(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 5)
        _, ax = f_1719(start_date, end_date)
        self.assertTrue(str(type(ax)).endswith("matplotlib.axes._axes.Axes'>"), "The second return value should be a matplotlib Axes object")

    def test_negative_date_range(self):
        start_date = datetime(2021, 1, 10)
        end_date = datetime(2021, 1, 5)
        with self.assertRaises(ValueError):
            f_1719(start_date, end_date)


    def test_single_day_date_range(self):
        start_date = end_date = datetime(2021, 1, 1)
        df, _ = f_1719(start_date, end_date)
        self.assertEqual(len(df), 1, "DataFrame should contain exactly one row for a single day date range")

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