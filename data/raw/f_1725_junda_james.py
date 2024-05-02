
from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd

def f_1725(data, column1, column2):
    """
    Perform a linear regression on two columns of a dataset and record the result.
    Additionally, generates a plot representing the original data and the fitted line.

    Parameters:
    data (DataFrame): The dataset.
    column1 (str): The name of the first column.
    column2 (str): The name of the second column.

    Returns:
    tuple: The slope, intercept, r-value, p-value, and standard error of the regression.
    Axes: The matplotlib Axes object containing the plot.

    Raises:
    ValueError: If the specified columns do not exist in the DataFrame.

    Requirements:
    - scipy.stats
    - matplotlib.pyplot
    - pandas

    Example:
    >>> data = pd.DataFrame([[14, 25], [1, 22], [7, 8]], columns=['Column1', 'Column2'])
    >>> result, ax = f_1725(data, 'Column1', 'Column2')
    """
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError("Specified columns must exist in the DataFrame")

    x = data[column1].values
    y = data[column2].values

    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'o', label='original data')
    ax.plot(x, intercept + slope*x, 'r', label='fitted line')
    ax.legend()

    return (slope, intercept, r_value, p_value, std_err), ax

import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'Column1': [14, 1, 7, 10, 5],
            'Column2': [25, 22, 8, 15, 11]
        })

    def test_regression_results(self):
        result, _ = f_1725(self.data, 'Column1', 'Column2')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 5)

    def test_invalid_columns(self):
        with self.assertRaises(ValueError):
            f_1725(self.data, 'Invalid1', 'Column2')

    def test_plot_axes(self):
        _, ax = f_1725(self.data, 'Column1', 'Column2')
        self.assertEqual(len(ax.lines), 2)  # Original data and fitted line

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1725(pd.DataFrame(), 'Column1', 'Column2')

    def test_single_point_regression(self):
        single_point_data = pd.DataFrame({'Column1': [1], 'Column2': [2]})
        result, ax = f_1725(single_point_data, 'Column1', 'Column2')
        # self.assertEqual(result[0], np.nan)
        self.assertEqual(result[2], 0)  # Slope should be 0 for single point
    
    def test_return_values(self):
        result, ax = f_1725(self.data, 'Column1', 'Column2')
        # print(result)
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(result))
        expect = (0.3456790123456789, 13.641975308641975, 0.23699046752221187, 0.7011032163730078, 0.8181438416490141)
        for res, exp in zip(result, expect):
            self.assertAlmostEqual(res, exp, places=7) 

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