from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def f_564(l, x_data, plot=False):
    """
    Adjust a quadratic curve to the specified data and return the parameters and fitted values.
    
    Parameters:
    l (numpy array): The input y-values.
    x_data (numpy array): The x-values corresponding to l.
    plot (bool, optional): If True, a plot will be returned. Default is False.
    
    Returns:
    tuple: A tuple containing the following:
        - params (numpy array): Parameters of the fitted curve.
        - fitted_values (numpy array): Fitted y-values for the provided x_data.
        - ax (matplotlib.axes._axes.Axes, optional): Axes object of the plot if plot=True.

    Requirements:
    - scipy.optimize.curve_fit
    - matplotlib.pyplot

    Example:
    >>> import numpy as np
    >>> l = np.array([1, 4, 9, 16, 25])
    >>> x_data = np.array([1, 2, 3, 4, 5])
    >>> params, fitted_values = f_564(l, x_data)
    >>> print(fitted_values)
    [ 1.  4.  9. 16. 25.]
    """

    def func(x, a, b):
        return a * x**2 + b

    params, _ = curve_fit(func, x_data, l)
    fitted_values = func(x_data, *params)
    
    if plot:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(x_data, l, label='Data')
        ax.plot(x_data, fitted_values, label='Fitted function')
        ax.legend(loc='best')
        return params, fitted_values, ax

    return params, fitted_values

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        l = np.array([1, 4, 9, 16, 25])
        x_data = np.array([1, 2, 3, 4, 5])
        params, fitted_values = f_564(l, x_data)
        # Check the correctness of the fitted parameters
        self.assertAlmostEqual(params[0], 1.0, places=5)
        self.assertAlmostEqual(params[1], 0, places=5)
        # Check the correctness of the fitted values
        np.testing.assert_array_almost_equal(fitted_values, l, decimal=5)
    def test_case_2(self):
        l = np.array([2, 5, 10, 17, 26])
        x_data = np.array([1, 2, 3, 4, 5])
        params, fitted_values = f_564(l, x_data)
        # Check the correctness of the fitted values
        np.testing.assert_array_almost_equal(fitted_values, l, decimal=5)
    def test_case_3(self):
        l = np.array([0, 3, 8, 15, 24])
        x_data = np.array([1, 2, 3, 4, 5])
        params, fitted_values, ax = f_564(l, x_data, plot=True)
        # Ensure the fitted values are correct
        np.testing.assert_array_almost_equal(fitted_values, l, decimal=5)
        # Ensure a plot is returned by checking the type of ax
        self.assertIsInstance(ax, plt.Axes)
    def test_case_4(self):
        x_data = np.array([1, 2, 3, 4, 5])
        l = x_data ** 2
        params, fitted_values, ax = f_564(l, x_data, plot=True)
        line = ax.lines[0].get_xydata()
        self.assertTrue(np.allclose(line[:, 1], l))  # The plotted curve should match the fitted values
    def test_case_5(self):
        x_data = np.array([1, 2, 3, 4, 5])
        l = x_data ** 2
        
        self.assertEqual(len(f_564(l, x_data, plot=False)), 2)  # If plot=False, no Axes object should be returned
