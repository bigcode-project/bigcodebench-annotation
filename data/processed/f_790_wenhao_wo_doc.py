import numpy as np
import random
from datetime import datetime

def f_135(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    """
    Generates a matrix of given dimensions (rows x columns) containing unique dates between 
    a specified start date and end date.
    
    Parameters:
    - rows (int): The number of rows for the output matrix. Default is 3.
    - columns (int): The number of columns for the output matrix. Default is 2.
    - start_date (datetime): The start date for the range of unique dates. Default is datetime(2021, 1, 1).
    - end_date (datetime): The end date for the range of unique dates. Default is datetime(2021, 12, 31).
    
    Returns:
    - ndarray: A numpy ndarray with unique dates in the shape (rows, columns).
    
    Requirements:
    - numpy
    - itertools
    - datetime
    - random
    
    Example:
    >>> matrix = f_135(2, 2, datetime(2021, 1, 1), datetime(2021, 1, 10))
    >>> print(matrix)
    [['2021-01-03T00:00:00.000000000', '2021-01-07T00:00:00.000000000'],
     ['2021-01-09T00:00:00.000000000', '2021-01-04T00:00:00.000000000']]
    """
    if seed is not None:
        random.seed(seed)
    start_date_np = np.datetime64(start_date)
    end_date_np = np.datetime64(end_date)
    total_days = int((end_date_np - start_date_np).astype('timedelta64[D]').astype(int) + 1)
    selected_dates = sorted(random.sample(range(total_days), rows * columns))
    matrix = (start_date_np + np.array(selected_dates).astype('timedelta64[D]')).reshape(rows, columns)
    return matrix

# Unit testing
import unittest
import numpy.testing as npt
class TestCases(unittest.TestCase):
        
    def test_case_1(self):
        # Using default parameters
        matrix = f_135(seed=0)
        self.assertEqual(matrix.shape, (3, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) > 0))  # Dates should be unique
    def test_case_2(self):
        # Using custom rows and columns, and a small date range
        matrix = f_135(2, 2, datetime(2021, 1, 1), datetime(2021, 1, 10), seed=42)
        self.assertEqual(matrix.shape, (2, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))  # Dates should be unique
    def test_case_3(self):
        # Using custom rows and columns, and a large date range
        matrix = f_135(4, 4, datetime(2000, 1, 1), datetime(2021, 12, 31), seed=55)
        self.assertEqual(matrix.shape, (4, 4))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))  # Dates should be unique
    def test_case_4(self):
        # Using a date range of one day
        matrix = f_135(1, 1, datetime(2021, 1, 1), datetime(2021, 1, 1), seed=0)
        expected_date = np.array(['2021-01-01'], dtype='datetime64[us]').reshape(1, 1)
        npt.assert_array_equal(matrix, expected_date)  # Only one date in the range
    def test_case_5(self):
        # Using custom rows and columns, and a date range with only two days
        matrix = f_135(1, 2, datetime(2021, 1, 1), datetime(2021, 1, 2), seed=41)
        self.assertEqual(matrix.shape, (1, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))  # Dates should be unique
        expected_dates = np.array(['2021-01-01', '2021-01-02'], dtype='datetime64[us]').reshape(1, 2)
        for date in expected_dates.ravel():
            self.assertIn(date, matrix.ravel())
