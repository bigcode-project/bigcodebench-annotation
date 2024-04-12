import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler


def f_358(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    """
    Normalize the data and visualize it using a heatmap.

    This function takes a pandas DataFrame, normalizes the data to a range [0, 1], and then visualizes this
    normalized data using a seaborn heatmap.  The heatmap uses the "YlGnBu" colormap to represent normalized
    values and includes a color bar labeled "Normalized Value" to indicate the range of data values.
    It returns both the normalized data and the heatmap plot.

    Parameters:
    - data (pd.DataFrame): The input data with multiple features in columns.

    Returns:
    - pd.DataFrame: Normalized data.
    - plt.Axes: Heatmap plot of the normalized data.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    - seaborn
    
    Example:
    >>> df = pd.DataFrame([[1,1,1], [2,2,2], [3,3,3]], columns=['Feature1', 'Feature2', 'Feature3'])
    >>> normalized_df, _ = f_358(df)
    >>> type(normalized_df)
    <class 'pandas.core.frame.DataFrame'>
    >>> normalized_df['Feature1'].iloc[0]  # Returns a normalized value between 0 and 1
    0.0
    """
    # Normalizing the data
    scaler = MinMaxScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

    # Plotting heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        normalized_data, cmap="YlGnBu", cbar_kws={"label": "Normalized Value"}
    )

    return normalized_data, ax


import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        # default columns used for testing, but function is not limited to these options
        self.expected_columns = [
            "Feature1",
            "Feature2",
            "Feature3",
            "Feature4",
            "Feature5",
        ]

    def _check_data_structure(self, data, expected_columns):
        self.assertIsInstance(data, pd.DataFrame)
        for col in data.columns:
            self.assertIn(col, expected_columns)

    def _check_data_value(self, data):
        # Check if values in normalized data are between 0 and 1
        # (allowing a small margin for precision issues)
        self.assertTrue(((data.values >= -1e-10) & (data.values <= 1.00000001)).all())

    def _check_heatmap(self, ax):
        # Test visualization
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.collections), 1)  # 1 heatmap
        cbar = ax.collections[0].colorbar
        self.assertTrue(cbar is not None)
        self.assertTrue(cbar.ax.get_ylabel(), "Normalized Value")
        self.assertEqual(ax.collections[0].cmap.name, "YlGnBu")

    def test_case_1(self):
        # Test with random data
        data = pd.DataFrame(
            np.random.rand(100, 5),
            columns=self.expected_columns,
        )
        normalized_data, ax = f_358(data)
        self._check_data_structure(normalized_data, self.expected_columns)
        self._check_data_value(normalized_data)
        self._check_heatmap(ax)

    def test_case_2(self):
        # Test with data having all zeros
        data = pd.DataFrame(
            np.zeros((100, 5)),
            columns=self.expected_columns,
        )
        normalized_data, ax = f_358(data)
        self._check_data_structure(normalized_data, self.expected_columns)
        self._check_heatmap(ax)
        # Check if all values in normalized data are zero
        self.assertTrue((normalized_data.values == 0).all())

    def test_case_3(self):
        # Test with data having incremental values
        data = pd.DataFrame(
            np.arange(500).reshape(100, 5),
            columns=self.expected_columns,
        )
        normalized_data, ax = f_358(data)
        self._check_data_structure(normalized_data, self.expected_columns)
        self._check_data_value(normalized_data)
        self._check_heatmap(ax)

    def test_case_4(self):
        # Test with data having decremental values
        data = pd.DataFrame(
            np.arange(500, 0, -1).reshape(100, 5),
            columns=self.expected_columns,
        )
        normalized_data, ax = f_358(data)
        self._check_data_structure(normalized_data, self.expected_columns)
        self._check_data_value(normalized_data)
        self._check_heatmap(ax)

    def test_case_5(self):
        # Test single valid column
        data = pd.DataFrame(np.random.rand(100, 1), columns=["Feature1"])
        normalized_data, ax = f_358(data)
        self._check_data_structure(normalized_data, ["Feature1"])
        self._check_data_value(normalized_data)
        self._check_heatmap(ax)

    def test_case_6(self):
        # Test should fail when inputs are invalid - string column
        data = pd.DataFrame(
            {"Feature1": np.random.rand(100), "Feature2": ["string"] * 100}
        )
        with self.assertRaises(ValueError):
            f_358(data)

    def test_case_7(self):
        # Test should fail when inputs are invalid - empty dataframe
        data = pd.DataFrame()
        with self.assertRaises(ValueError):
            f_358(data)

    def tearDown(self):
        plt.close("all")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
