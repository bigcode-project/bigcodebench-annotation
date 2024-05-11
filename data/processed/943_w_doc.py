import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    """
    Generate a sales time-series and decompose it into trend, seasonal, and residual components.
    
    Parameters:
    - start_date (str): The start date of the time-series in the format 'YYYY-MM-DD'. Default is '2016-01-01'.
    - periods (int): The number of periods to generate for the time-series. Default is 24.
    - freq (str): The frequency of the time-series data. Default is 'M' (Monthly End).
    - model (str): The type of seasonal decomposition ('additive' or 'multiplicative'). Default is 'additive'.

    Returns:
    - A dictionary containing 'trend', 'seasonal', and 'residual' components as Pandas Series.
    
    Requirements:
    - numpy
    - pandas
    - statsmodels
    
    Examples:
    >>> result = task_func('2016-01-01', 24, 'M')
    >>> all(key in result for key in ['trend', 'seasonal', 'residual'])
    True

    >>> result = task_func('2020-01-01', 24, 'M', 'multiplicative')
    >>> len(result['seasonal'])
    24
    """
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    sales_data = np.random.randint(low=100, high=500, size=periods)
    sales_series = pd.Series(sales_data, index=date_range)
    try:
        decomposition = seasonal_decompose(sales_series, model=model, period=12 if freq == 'M' else 4)
    except ValueError as e:
        return {'error': str(e)}
    return {
        'trend': decomposition.trend,
        'seasonal': decomposition.seasonal,
        'residual': decomposition.resid
    }

import unittest
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        np.random.seed(42)  # For reproducibility
        result = task_func(periods=24)  # Adjust to meet the minimum requirement for decomposition
        self.assertTrue(all(key in result for key in ['trend', 'seasonal', 'residual']))
    def test_multiplicative_model(self):
        np.random.seed(0)  # For reproducibility
        result = task_func('2020-01-01', 24, 'M', 'multiplicative')
        self.assertTrue(all(key in result for key in ['trend', 'seasonal', 'residual']))
    def test_custom_parameters(self):
        np.random.seed(55)  # For reproducibility
        result = task_func('2017-01-01', 36, 'M')
        self.assertEqual(len(result['trend']), 36)
    def test_weekly_frequency(self):
        np.random.seed(1)  # For reproducibility
        result = task_func('2022-01-01', 104, 'W', 'additive')
        self.assertTrue(all(key in result for key in ['trend', 'seasonal', 'residual']))
        self.assertEqual(len(result['seasonal']), 104)
        
    def test_insufficient_periods_error(self):
        np.random.seed(66)  # For reproducibility
        result = task_func('2022-01-01', 12, 'M')
        self.assertIn('error', result)
        
    def test_additive_decomposition_properties(self):
        np.random.seed(42)  # For reproducibility
        periods = 36
        result = task_func('2020-01-01', periods, 'M')
        reconstructed = result['trend'].fillna(0) + result['seasonal'].fillna(0) + result['residual'].fillna(0)
        self.assertTrue(np.allclose(reconstructed.head(12), reconstructed.head(12), atol=1))
