import pandas as pd
from datetime import datetime
import holidays

def f_2150(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    """
    Create a list of business days between two dates, excluding weekends and specified country's public holidays.

    Parameters:
    start_date (datetime): The start date. Default is January 1, 2023.
    end_date (datetime): The end date. Default is December 31, 2023. 
    country (str): ISO country code to determine public holidays. Default is 'US'.

    Returns:
    list[datetime]: A list of business days (as datetime objects). The start date and end date is included to process. 

    Raises:
    ValueError: If start_date is not a datetime object or is after end_date.
    ValueError: If end_date is not a datetime object or is before start_date.

    Requirements:
    - pandas
    - datetime
    - holidays

    Note:
    - The function depends on the 'holidays' package for fetching public holidays.
    - Ensure 'pandas' and 'holidays' packages are installed.

    Example:
    >>> business_days = f_2150()
    >>> print(business_days[0])
    2023-01-03 00:00:00
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime objects.")
    if start_date > end_date:
        raise ValueError("start_date must not be after end_date.")

    country_holidays = holidays.CountryHoliday(country)
    dates = pd.date_range(start_date, end_date)
    business_days = [date for date in dates if date.weekday() < 5 and date not in country_holidays]

    return business_days

import unittest
from datetime import datetime

class TestCases(unittest.TestCase):
    def test_default_dates(self):
        result = f_2150()
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(d, datetime) for d in result))
        self.assertNotIn(datetime(2023, 1, 1), result)  # New Year's Day, a holiday
    
    def test_custom_dates(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 3)
        result = f_2150(start_date, end_date)
        self.assertEqual([datetime(2023, 1, 3)], result)  # A business day

    def test_invalid_dates(self):
        with self.assertRaises(ValueError):
            f_2150(end_date=datetime(2022, 12, 31))  # end_date before default start_date

    def test_invalid_date_types(self):
        with self.assertRaises(ValueError):
            f_2150(start_date="2023-01-01", end_date="2023-12-31")  # String dates

    def test_non_default_country(self):
        # Testing with a different country's holidays (e.g., UK)
        result = f_2150(country='GB')
        self.assertNotIn(datetime(2023, 4, 7), result)  # Good Friday in UK
    def test_range_including_weekend(self):
        start_date = datetime(2023, 1, 6)  # Friday
        end_date = datetime(2023, 1, 9)    # Monday
        result = f_2150(start_date, end_date)
        self.assertEqual([datetime(2023, 1, 6), datetime(2023, 1, 9)], result)

    def test_range_including_public_holiday(self):
        start_date = datetime(2023, 7, 3)  # Day before Independence Day
        end_date = datetime(2023, 7, 5)    # Day after Independence Day
        result = f_2150(start_date, end_date)
        # print(result)
        self.assertEqual([datetime(2023, 7, 3), datetime(2023, 7, 5)], result)  # July 4th is excluded

    def test_short_business_week(self):
        start_date = datetime(2023, 11, 20)  # Week of Thanksgiving
        end_date = datetime(2023, 11, 24)
        result = f_2150(start_date, end_date)
        # print(result)
        self.assertEqual([datetime(2023, 11, 20), datetime(2023, 11, 21), datetime(2023, 11, 22),datetime(2023, 11, 24)], result)

    def test_single_day_range_business_day(self):
        start_date = end_date = datetime(2023, 1, 3)  # A Tuesday
        result = f_2150(start_date, end_date)
        self.assertEqual([datetime(2023, 1, 3)], result)

    def test_single_day_range_non_business_day(self):
        start_date = end_date = datetime(2023, 1, 1)  # A Sunday
        result = f_2150(start_date, end_date)
        self.assertEqual([], result)

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