import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.parser import parse

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def f_510(dates_str_list):
    """
    Analyze the weekday distribution in a list of date strings.

    This function takes a list of date strings in "yyyy-mm-dd" format, calculates 
    the weekday for each date, and returns a distribution of the weekdays.

    Parameters:
    - dates_str_list (list): The list of date strings in "yyyy-mm-dd" format.

    Returns:
    - Series: A pandas Series of the weekday distribution, where the index represents 
              the weekdays (from Monday to Sunday) and the values represent the counts 
              of each weekday in the provided list.

    Requirements:
    - Libraries/modules to be used: datetime, dateutil.parser, numpy, and pandas.

    Example:
    >>> f_510(['2022-10-22', '2022-10-23', '2022-10-24', '2022-10-25'])
    Monday       1
    Tuesday      1
    Wednesday    0
    Thursday     0
    Friday       0
    Saturday     1
    Sunday       1
    dtype: int64
    """
    weekdays = [parse(date_str).weekday() for date_str in dates_str_list]
    weekday_counts = np.bincount(weekdays, minlength=7)
    
    distribution = pd.Series(weekday_counts, index=DAYS_OF_WEEK)

    return distribution

import unittest
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.parser import parse
DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def run_tests():
    import numpy as np
    import pandas as pd
    from datetime import datetime
    from dateutil.parser import parse
    
    # Constants for the test cases
    DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: Testing with a sample date list
        input_dates = ['2022-10-22', '2022-10-23', '2022-10-24', '2022-10-25']
        expected_output = pd.Series([1, 1, 0, 0, 0, 1, 1], index=DAYS_OF_WEEK)
        result = f_510(input_dates)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_2(self):
        # Input 2: Testing with a list where all dates fall on a single weekday
        input_dates = ['2022-10-24', '2022-10-31', '2022-11-07']
        expected_output = pd.Series([3, 0, 0, 0, 0, 0, 0], index=DAYS_OF_WEEK)
        result = f_510(input_dates)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_3(self):
        # Input 3: Testing with an empty list
        input_dates = []
        expected_output = pd.Series([0, 0, 0, 0, 0, 0, 0], index=DAYS_OF_WEEK)
        result = f_510(input_dates)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_4(self):
        # Input 4: Testing with a mixed list of dates
        input_dates = ['2022-01-01', '2022-02-14', '2022-03-17', '2022-12-31']
        expected_output = pd.Series([1, 0, 0, 1, 0, 2, 0], index=DAYS_OF_WEEK)
        result = f_510(input_dates)
        pd.testing.assert_series_equal(result, expected_output)

    def test_case_5(self):
        # Input 5: Testing with dates spanning multiple weeks
        input_dates = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07']
        expected_output = pd.Series([1, 1, 1, 1, 1, 1, 1], index=DAYS_OF_WEEK)
        result = f_510(input_dates)
        pd.testing.assert_series_equal(result, expected_output)


if __name__ == "__main__":
    run_tests()