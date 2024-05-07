import pandas as pd
from datetime import datetime, timedelta
import locale
from random import choice, randint, seed
import matplotlib.axes

def f_3749(start_date, end_date, num_dates, seed_value=42, countries=None, country_codes=None):
    """
    Generate a reproducible random date distribution between two dates and record a histogram of this data for each country after converting the data to a specific territorial scale.

    Parameters:
    start_date (str): The start date string in "dd/mm/yyyy" format.
    end_date (str): The end date string in "dd/mm/yyyy" format.
    num_dates (int): The number of random dates to generate.
    seed_value (int): The seed value for random number generation.
    countries (list, optional): The list of countries. Default is ['Russia', 'Germany', 'France', 'Spain', 'Italy'].
    country_codes (dict, optional): A dictionary mapping country names to locale codes. Default is {'Russia': 'ru_RU', 'Germany': 'de_DE', 'France': 'fr_FR', 'Spain': 'es_ES', 'Italy': 'it_IT'}.

    Returns:
    dict: A dictionary where keys are country names and values are matplotlib.axes.Axes objects for the histograms.
    df: A dataframe that stores the randomly generated data with columns 'dates' and 'country'. 

    Raises:
    ValueError: If the input parameters are invalid.

    Requirements:
    - pandas
    - datetime
    - locale
    - random
    - matplotlib.axes

    Plot Title and Y-axis:
    - The title of each plot will be 'Date Distribution - [Country]'
    - The y-axis label will be 'Frequency'

    Example:
    >>> _, df = f_3749('01/01/2000', '01/01/2021', 1000, 42)
    >>> print(df.head())
           dates  country
    0 2014-05-05    Italy
    1 2002-07-01  Germany
    2 2000-07-23    Spain
    3 2016-08-18   France
    4 2006-03-03   France
    """
    seed(seed_value)  # Set the seed for random number generation

    default_countries = ['Russia', 'Germany', 'France', 'Spain', 'Italy']
    default_country_codes = {
        'Russia': 'ru_RU',
        'Germany': 'de_DE',
        'France': 'fr_FR',
        'Spain': 'es_ES',
        'Italy': 'it_IT'
    }

    countries = countries if countries is not None else default_countries
    country_codes = country_codes if country_codes is not None else default_country_codes

    try:
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'dd/mm/yyyy'.")

    if end_date < start_date:
        raise ValueError("End date must be after start date.")

    date_delta = end_date - start_date

    random_dates = [start_date + timedelta(days=randint(0, date_delta.days)) for _ in range(num_dates)]
    random_countries = [choice(countries) for _ in range(num_dates)]
    
    data = pd.DataFrame({'dates': random_dates, 'country': random_countries})

    axes = {}
    for country in countries:
        country_data = data[data['country'] == country]
        if not country_data.empty:
            locale.setlocale(locale.LC_TIME, country_codes[country])
            ax = country_data['dates'].hist()
            ax.set(title=f'Date Distribution - {country}', ylabel='Frequency')
            axes[country] = ax

    return axes, data

import unittest
import pandas as pd
import matplotlib.axes
from datetime import datetime

class TestCases(unittest.TestCase):
    def test_reproducibility_with_seed(self):
        axes1, data1 = f_3749('01/01/2000', '01/01/2021', 100, 42)
        axes2, data2 = f_3749('01/01/2000', '01/01/2021', 100, 42)

        # Test if the data generated with the same seed are identical
        pd.testing.assert_frame_equal(data1, data2)

    def test_random_date_generation(self):
        axes, data = f_3749('01/01/2000', '01/01/2021', 1000)
        self.assertIsInstance(axes, dict)
        for ax in axes.values():
            self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            f_3749('01-01-2000', '01/01/2021', 100)

    def test_end_date_before_start_date(self):
        with self.assertRaises(ValueError):
            f_3749('01/01/2021', '01/01/2000', 100)

    def test_histogram_frequencies(self):
        num_dates = 10
        axes, data = f_3749('01/01/2000', '01/01/2021', num_dates, seed_value=42)
        df_list = data.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(df_list))
        
        expect = ['2014-05-05 00:00:00,Italy', '2002-07-01 00:00:00,Russia', '2000-07-23 00:00:00,Italy', '2016-08-18 00:00:00,Spain', '2006-03-03 00:00:00,Russia', '2005-06-29 00:00:00,Russia', '2005-01-02 00:00:00,Russia', '2003-02-17 00:00:00,Germany', '2016-07-08 00:00:00,Germany', '2002-04-19 00:00:00,Italy']
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")

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