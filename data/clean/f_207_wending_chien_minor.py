import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


def f_207(data):
    """
    Normalizes a given dataset using MinMax scaling and calculates the average of each row. This average is then
    added as a new column 'Average' to the resulting DataFrame. The function also visualizes these averages in a plot.

    Parameters:
    data (numpy.array): A 2D array where each row represents a sample and each column a feature, with a
    shape of (n_samples, 8).

    Returns:
    DataFrame: A pandas DataFrame where data is normalized, with an additional column 'Average' representing the
    mean of each row.
    Axes: A matplotlib Axes object showing a plot of the average values across the dataset.

    Required Libraries:
    - pandas
    - sklearn
    - matplotlib

    Example:
    >>> import numpy as np
    >>> data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
    >>> df, ax = f_207(data)
    >>> print(df.round(2))
         A    B    C    D    E    F    G    H  Average
    0  0.0  0.0  0.0  0.0  1.0  0.0  1.0  0.0     0.25
    1  1.0  0.0  0.0  0.0  0.0  1.0  0.0  0.0     0.25
    """
    COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    df = pd.DataFrame(normalized_data, columns=COLUMN_NAMES)
    df['Average'] = df.mean(axis=1)

    fig, ax = plt.subplots()
    df['Average'].plot(ax=ax)

    return df, ax


import unittest
import numpy as np
import matplotlib

matplotlib.use('Agg')


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
        df, ax = f_207(data)

        self.assertEqual(df.shape, (2, 9))
        self.assertTrue('Average' in df.columns)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 1)
        self.assertListEqual(list(lines[0].get_ydata()), list(df['Average']))

    def test_case_2(self):
        data = np.array([[5, 5, 5, 5, 5, 5, 5, 5]])
        df, ax = f_207(data)

        self.assertEqual(df.shape, (1, 9))
        self.assertTrue('Average' in df.columns)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 1)
        self.assertListEqual(list(lines[0].get_ydata()), list(df['Average']))

    def test_case_3(self):
        data = np.array([[0, 0, 0, 0, 0, 0, 0, 0], [10, 10, 10, 10, 10, 10, 10, 10]])
        df, ax = f_207(data)

        self.assertEqual(df.shape, (2, 9))
        self.assertTrue('Average' in df.columns)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 1)
        self.assertListEqual(list(lines[0].get_ydata()), list(df['Average']))

    def test_case_4(self):
        data = np.array([[1, 2, 3, 4, 5, 6, 7, 8]])
        df, ax = f_207(data)

        self.assertEqual(df.shape, (1, 9))
        self.assertTrue('Average' in df.columns)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 1)
        self.assertListEqual(list(lines[0].get_ydata()), list(df['Average']))

    def test_case_5(self):
        data = np.array([[8, 7, 6, 5, 4, 3, 2, 1]])
        df, ax = f_207(data)

        self.assertEqual(df.shape, (1, 9))
        self.assertTrue('Average' in df.columns)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 1)
        self.assertListEqual(list(lines[0].get_ydata()), list(df['Average']))


if __name__ == "__main__":
    run_tests()
