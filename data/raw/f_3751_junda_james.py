import pandas as pd
from datetime import datetime
import locale
import matplotlib.axes

def f_3751(data, date_column, country_column, date_format, countries=None, country_codes=None):
    """
    Processes a DataFrame to create histograms of date distributions for each specified country, 
    formatted according to the given locale. Raises a ValueError if a country does not have an 
    entry in the provided country_codes dictionary or if specified countries are not present in 
    the data.

    Parameters:
    - data (pd.DataFrame): The pandas DataFrame containing the data.
    - date_column (str): The column name in 'data' containing dates.
    - country_column (str): The column name in 'data' containing country names.
    - date_format (str): The date format string to parse dates in 'date_column'.
    - countries (list, optional): A list of country names to process. Defaults to 
      ['Russia', 'Germany', 'France', 'Spain', 'Italy']. If empty, no histograms will be generated.
    - country_codes (dict, optional): A dictionary mapping countries to locale codes 
      for date formatting. Defaults to a predefined mapping. All specified countries 
      must have corresponding entries in this dictionary. If a specified country is not 
      found in this mapping, a ValueError is raised.

    Returns:
    - list: A list of matplotlib.axes.Axes objects, each representing a histogram for 
      a country. Properties include a title ('Date Distribution - [Country Name]'), 
      X-axis label ('Date'), and Y-axis label ('Frequency'). If a country is specified but 
      does not exist in the data, no histogram will be generated for that country.

    Raises:
    - ValueError: If 'date_column' or 'country_column' doesn't exist in 'data', 
      if any specified country does not have a corresponding entry in the 
      country_codes dictionary, or if the parameters are otherwise invalid.
      Additionally, if a specified country is not present in the data.
    - TypeError: If `json_str` is not a string, bytes, or bytearray.
    - Exception: For other general errors related to file writing.

    Requirements:
    - pandas
    - datetime
    - locale
    - matplotlib.axes

    Example:
    >>> data = pd.DataFrame({'dates': ['01/01/2000', '01/02/2000', '02/03/2000', '04/05/2000', '06/07/2000'], 'country': ['Russia', 'Germany', 'France', 'Spain', 'Italy']})
    >>> plots = f_3751(data, 'dates', 'country', '%d/%m/%Y')
    >>> print(len(plots))
    5

    Note:
    - The function requires the 'locale' and 'matplotlib' libraries.
    - Ensure your Python environment supports the locales you intend to use, 
      as not all locales may be available on all systems. This affects date 
      formatting in the histograms.
    """

    
    if countries is None:
        countries = ['Russia', 'Germany', 'France', 'Spain', 'Italy']
    if country_codes is None:
        country_codes = {
            'Russia': 'ru_RU',
            'Germany': 'de_DE',
            'France': 'fr_FR',
            'Spain': 'es_ES',
            'Italy': 'it_IT'
        }

    if date_column not in data.columns or country_column not in data.columns:
        raise ValueError("Specified columns not found in DataFrame.")

    for country in countries:
        if country not in country_codes:
            raise ValueError(f"No locale code mapping found for '{country}'. Please provide a valid mapping in country_codes.")

    plots = []
    for country in countries:
        country_data = data[data[country_column] == country].copy()
        if not country_data.empty:
            try:
                locale.setlocale(locale.LC_TIME, country_codes[country])
            except Exception as e:
                raise Exception(f"Failed to set locale for '{country}': {e}")

            country_data.loc[:, 'parsed_dates'] = country_data[date_column].apply(
                lambda x: datetime.strptime(x, date_format).date())
            ax = country_data['parsed_dates'].hist()
            ax.set(title=f'Date Distribution - {country}', xlabel='Date', ylabel='Frequency')
            plots.append(ax)

    return plots

import unittest
import pandas as pd
import matplotlib.axes

class TestCases(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'dates': ['01/01/2000', '01/02/2000', '02/03/2000', '04/05/2000', '06/07/2000'],
            'country': ['Russia', 'Germany', 'France', 'Spain', 'Italy']
        })

    def test_valid_data(self):
        plots = f_3751(self.data, 'dates', 'country', '%d/%m/%Y')
            
        self.assertEqual(len(plots), 5)
        self.assertIsInstance(plots[0], matplotlib.axes.Axes)

    def test_invalid_date_column(self):
        with self.assertRaises(ValueError):
            f_3751(self.data, 'invalid_date', 'country', '%d/%m/%Y')

    def test_invalid_country_column(self):
        with self.assertRaises(ValueError):
            f_3751(self.data, 'dates', 'invalid_country', '%d/%m/%Y')

    def test_custom_countries(self):
        custom_countries = ['Russia', 'Germany']
        plots = f_3751(self.data, 'dates', 'country', '%d/%m/%Y', countries=custom_countries)
        self.assertEqual(len(plots), 2)
        
    def test_missing_country_code_mapping(self):
        custom_countries = ['Russia', 'Narnia']  # Assuming 'Narnia' does not exist in default country_codes
        with self.assertRaises(ValueError):
            f_3751(self.data, 'dates', 'country', '%d/%m/%Y', countries=custom_countries)

    def test_empty_dataframe(self):
        empty_data = pd.DataFrame({'dates': [], 'country': []})
        plots = f_3751(empty_data, 'dates', 'country', '%d/%m/%Y')
        self.assertEqual(len(plots), 0)  # Expecting no plots for an empty DataFrame

    def test_nonexistent_countries_in_data(self):
        custom_countries = ['Atlantis', 'El Dorado']  # Countries not present in the data
        custom_country_codes = {
            'Atlantis': 'en_US',  # Assuming these codes are for demonstrating they are handled
            'El Dorado': 'en_US'
            }
        plots = f_3751(self.data, 'dates', 'country', '%d/%m/%Y', countries=custom_countries, country_codes=custom_country_codes)
        self.assertEqual(len(plots), 0)  # Expecting no plots for non-existent countries
        
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