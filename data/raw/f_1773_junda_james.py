import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def f_1773(df):
    """
    Normalize the last column of the DataFrame using MinMaxScaler from sklearn and plot the normalized data.

    Parameters:
    - df (DataFrame): The input DataFrame.
    - bins (int, optional): Number of bins for the histogram. Defaults to 20.

    Returns:
    - DataFrame: A pandas DataFrame where the last column has been normalized.
    - Axes: A Matplotlib Axes object representing the plot of the normalized last column. The plot includes:
      - Title: 'Normalized Data of <column_name>'
      - X-axis label: 'Index'
      - Y-axis label: 'Normalized Value'

    Raises:
    - ValueError: If the input is not a DataFrame or if the DataFrame is empty.

    Requirements:
    - numpy
    - pandas
    - matplotlib.pyplot
    - sklearn

    Example:
    >>> df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    >>> normalized_df, ax = f_1773(df)
    >>> plt.show()
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    last_col_name = df.columns[-1]
    scaler = MinMaxScaler()
    normalized_values = scaler.fit_transform(df[[last_col_name]])
    normalized_df = df.copy()
    normalized_df[last_col_name] = normalized_values.flatten()
    
    fig, ax = plt.subplots()
    ax.plot(normalized_df.index, normalized_df[last_col_name])
    ax.set_title(f'Normalized Data of {last_col_name}')
    ax.set_xlabel("Index")
    ax.set_ylabel("Normalized Value")

    return normalized_df, ax

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)

    def test_return_type(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        _, ax = f_1773(df)
        self.assertIsInstance(ax, plt.Axes)
        
    
    def test_normalized_dataframe_structure(self):
        np.random.seed(42)
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        normalized_df, _ = f_1773(df)
        self.assertTrue('D' in normalized_df.columns)
        df_list = normalized_df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        with open('df_contents.txt', 'w') as file:
            file.write(str(df_list))
        expect = ['51.0,92.0,14.0,0.7142857142857142', '60.0,20.0,82.0,0.8673469387755102', '74.0,74.0,87.0,0.9999999999999999', '23.0,2.0,21.0,0.520408163265306', '1.0,87.0,29.0,0.36734693877551017', '1.0,63.0,59.0,0.19387755102040813', '32.0,75.0,57.0,0.2040816326530612', '88.0,48.0,90.0,0.5816326530612245', '41.0,91.0,59.0,0.7959183673469387', '14.0,61.0,61.0,0.4591836734693877', '61.0,50.0,54.0,0.6326530612244897', '2.0,50.0,6.0,0.19387755102040813', '72.0,38.0,17.0,0.020408163265306124', '88.0,59.0,13.0,0.07142857142857142', '89.0,52.0,1.0,0.836734693877551', '91.0,59.0,70.0,0.42857142857142855', '7.0,46.0,34.0,0.7755102040816326', '80.0,35.0,49.0,0.020408163265306124', '1.0,5.0,53.0,0.020408163265306124', '53.0,92.0,62.0,0.16326530612244897', '89.0,43.0,33.0,0.7346938775510203', '61.0,99.0,13.0,0.9489795918367346', '47.0,14.0,71.0,0.7755102040816326', '86.0,61.0,39.0,0.846938775510204', '79.0,81.0,52.0,0.22448979591836732', '25.0,88.0,59.0,0.39795918367346933', '28.0,14.0,44.0,0.6428571428571428', '88.0,70.0,8.0,0.8775510204081631', '0.0,7.0,87.0,0.6224489795918366', '10.0,80.0,7.0,0.336734693877551', '34.0,32.0,4.0,0.39795918367346933', '27.0,6.0,72.0,0.7142857142857142', '11.0,33.0,32.0,0.4693877551020408', '22.0,61.0,87.0,0.3571428571428571', '98.0,43.0,85.0,0.9081632653061223', '34.0,64.0,98.0,0.4591836734693877', '77.0,2.0,0.0,0.030612244897959183', '89.0,13.0,26.0,0.07142857142857142', '78.0,14.0,89.0,0.4081632653061224', '76.0,50.0,62.0,0.9591836734693877', '51.0,95.0,3.0,0.9387755102040816', '22.0,14.0,42.0,0.2755102040816326', '35.0,12.0,31.0,0.7040816326530611', '58.0,85.0,27.0,0.6530612244897959', '41.0,44.0,61.0,0.5612244897959183', '5.0,27.0,27.0,0.42857142857142855', '83.0,29.0,61.0,0.7448979591836734', '91.0,88.0,61.0,0.9693877551020408', '0.0,26.0,61.0,0.7653061224489796', '2.0,69.0,71.0,0.2551020408163265', '8.0,61.0,36.0,0.9693877551020408', '50.0,43.0,23.0,0.7857142857142856', '58.0,31.0,95.0,0.8775510204081631', '51.0,61.0,57.0,0.510204081632653', '11.0,38.0,1.0,0.01020408163265306', '55.0,80.0,58.0,0.0', '1.0,91.0,53.0,0.8673469387755102', '95.0,96.0,0.0,0.173469387755102', '1.0,52.0,43.0,0.8979591836734693', '31.0,69.0,31.0,0.673469387755102', '54.0,74.0,55.0,0.1530612244897959', '37.0,23.0,68.0,0.9795918367346937', '69.0,85.0,10.0,0.14285714285714282', '96.0,72.0,58.0,0.693877551020408', '79.0,92.0,2.0,0.18367346938775508', '58.0,35.0,18.0,0.8979591836734693', '66.0,18.0,19.0,0.9591836734693877', '70.0,51.0,32.0,0.38775510204081626', '38.0,81.0,0.0,0.09183673469387754', '91.0,56.0,88.0,0.48979591836734687', '22.0,30.0,93.0,0.4081632653061224', '98.0,6.0,15.0,0.8979591836734693', '59.0,1.0,0.0,0.4693877551020408', '11.0,68.0,36.0,0.3061224489795918', '8.0,98.0,18.0,0.4693877551020408', '79.0,2.0,19.0,0.22448979591836732', '53.0,32.0,23.0,0.7448979591836734', '71.0,35.0,37.0,0.836734693877551', '98.0,88.0,98.0,0.2346938775510204', '92.0,17.0,81.0,0.6530612244897959', '53.0,34.0,79.0,0.6020408163265305', '40.0,99.0,32.0,0.673469387755102', '32.0,13.0,20.0,0.4693877551020408', '19.0,7.0,6.0,0.6632653061224489', '16.0,32.0,47.0,0.7551020408163265', '58.0,85.0,21.0,0.2857142857142857', '37.0,50.0,53.0,0.061224489795918366', '26.0,26.0,97.0,0.19387755102040813', '29.0,96.0,27.0,0.6326530612244897', '96.0,68.0,60.0,0.4693877551020408', '18.0,3.0,34.0,0.6326530612244897', '48.0,16.0,43.0,0.9183673469387754', '29.0,92.0,45.0,0.04081632653061224', '98.0,36.0,23.0,0.9285714285714285', '45.0,52.0,94.0,0.9897959183673468', '59.0,96.0,62.0,0.846938775510204', '31.0,86.0,32.0,0.6632653061224489', '17.0,24.0,94.0,0.5306122448979591', '57.0,66.0,45.0,0.22448979591836732', '31.0,46.0,85.0,0.21428571428571425']
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")

    def test_invalid_input_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1773(pd.DataFrame())

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            f_1773("not a dataframe")

    def test_plot_attributes(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        _, ax = f_1773(df)
        expected_title = f'Normalized Data of {df.columns[-1]}'
        self.assertEqual(ax.get_title(), expected_title)
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Normalized Value')
        
    def test_normalized_values_range(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        normalized_df, _ = f_1773(df)
        last_col_name = df.columns[-1]
        self.assertTrue(normalized_df[last_col_name].between(0, 1).all())

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