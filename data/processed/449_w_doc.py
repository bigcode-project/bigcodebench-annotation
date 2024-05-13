import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    """
    This function takes a pandas DataFrame and standardizes its features using sklearn's StandardScaler,
    which standardizes features by removing the mean and scaling to unit variance.
    After standardization, it draws a histogram for each feature with 20 bins.

    Parameters:
    - data (pd.DataFrame): The input data to be standardized and plotted. It is expected to have
                           columns named 'Feature1', 'Feature2', 'Feature3', 'Feature4', and 'Feature5'.
                           If there are additional data columns, they are ignored.


    Returns:
    - standardized_data (pd.DataFrame): The standardized data.
    - axes_list (list): A list of matplotlib Axes objects representing the histograms for each feature.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - sklearn.preprocessing.StandardScaler
    
    Example:
    >>> data = pd.DataFrame({
    ...     'Feature1': [0.5, 0.6, 0.7, 0.8, 0.9],
    ...     'Feature2': [0.1, 0.2, 0.3, 0.4, 0.5],
    ...     'Feature3': [0.9, 0.8, 0.7, 0.6, 0.5],
    ...     'Feature4': [0.5, 0.4, 0.3, 0.2, 0.1],
    ...     'Feature5': [0.1, 0.3, 0.5, 0.7, 0.9]
    ... })
    >>> standardized_data, axes_list = task_func(data)
    >>> type(standardized_data)
    <class 'pandas.core.frame.DataFrame'>
    >>> axes_list
    [<Axes: title={'center': 'Histogram of Feature1'}>, <Axes: title={'center': 'Histogram of Feature2'}>, <Axes: title={'center': 'Histogram of Feature3'}>, <Axes: title={'center': 'Histogram of Feature4'}>, <Axes: title={'center': 'Histogram of Feature5'}>]
    >>> type(axes_list[0])
    <class 'matplotlib.axes._axes.Axes'>
    """
    FEATURES = ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]
    scaler = StandardScaler()
    data_standardized = pd.DataFrame(
        scaler.fit_transform(data[FEATURES]), columns=FEATURES
    )
    axes_list = []
    for feature in FEATURES:
        fig, ax = plt.subplots()
        ax.hist(data_standardized[feature], bins=20, alpha=0.5)
        ax.set_title("Histogram of {}".format(feature))
        axes_list.append(ax)
    return data_standardized, axes_list

import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.columns = ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]
        np.random.seed(0)
    def test_case_1(self):
        # Test basic case
        data = pd.DataFrame(
            np.random.rand(100, 5),
            columns=self.columns,
        )
        self.standardized_data_test(data)
    def test_case_2(self):
        # Test standardizing different distribution
        data = pd.DataFrame(
            np.random.exponential(scale=1.0, size=(100, 5)),
            columns=self.columns,
        )
        self.standardized_data_test(data)
    def test_case_3(self):
        # Test standardizing data combined from different distributions
        data_1 = np.random.rand(100, 3)
        data_2 = np.random.exponential(scale=1.0, size=(100, 2))
        data = pd.DataFrame(
            np.hstack((data_1, data_2)),
            columns=self.columns,
        )
        self.standardized_data_test(data)
    def test_case_4(self):
        # Test the function with highly skewed data
        data = pd.DataFrame(
            np.random.chisquare(df=1, size=(100, 5)),
            columns=self.columns,
        )
        standardized_data, _ = task_func(data)
        self.assertTrue(np.isclose(standardized_data.std().values, 1, atol=1e-1).all())
    def test_case_5(self):
        # Test function with a dataframe that has only one row
        data = pd.DataFrame(
            {
                "Feature1": [0.1],
                "Feature2": [0.2],
                "Feature3": [0.3],
                "Feature4": [0.4],
                "Feature5": [0.5],
            }
        )
        _, axes_list = task_func(data)
        self.assertEqual(len(axes_list), 5)
    def test_case_6(self):
        # Test with columns having identical values across all rows.
        data = pd.DataFrame(
            {
                "Feature1": [0.1] * 100,
                "Feature2": [0.2] * 100,
                "Feature3": [0.3] * 100,
                "Feature4": [0.4] * 100,
                "Feature5": [0.5] * 100,
            }
        )
        standardized_data, _ = task_func(data)
        # Identical values become NaN after standardization because variance is 0
        expected_zeros = pd.DataFrame(
            0,
            index=np.arange(100),
            columns=self.columns,
        )
        self.assertTrue(np.isclose(standardized_data, expected_zeros).all().all())
    def test_case_7(self):
        # Test with additional columns not in the expected FEATURES set
        data = pd.DataFrame(
            np.random.rand(100, 7),
            columns=self.columns
            + [
                "Extra1",
                "Extra2",
            ],
        )
        _, axes_list = task_func(data)
        self.assertEqual(len(axes_list), 5)
    def test_case_8(self):
        # Test with missing columns from the expected FEATURES set
        data = pd.DataFrame(
            np.random.rand(100, 3), columns=["Feature1", "Feature2", "Feature3"]
        )
        with self.assertRaises(KeyError):
            task_func(data)
    def test_case_9(self):
        # Test should fail when there is invalid input - empty dataframe
        data = pd.DataFrame()
        with self.assertRaises(KeyError):
            task_func(data)
    def test_case_10(self):
        # Test should fail when there is invalid input - NaN
        data = pd.DataFrame(
            {
                "Feature1": [np.nan, 0.2, 0.3],
                "Feature2": [0.1, np.nan, 0.3],
                "Feature3": [0.2, 0.2, np.nan],
                "Feature4": [np.nan, 0.4, 0.5],
                "Feature5": [0.5, 0.6, np.nan],
            }
        )
        standardized_data, _ = task_func(data)
        self.assertTrue(standardized_data.isnull().any().any())
    def test_case_11(self):
        # Test should fail when there is invalid input - inf
        data = pd.DataFrame(
            {
                "Feature1": [np.inf, 0.2, 0.3],
                "Feature2": [0.1, -np.inf, 0.3],
                "Feature3": [0.2, 0.2, np.inf],
                "Feature4": [-np.inf, 0.4, 0.5],
                "Feature5": [0.5, 0.6, -np.inf],
            }
        )
        with self.assertRaises(ValueError):
            task_func(data)
    def test_case_12(self):
        # Test the function with non-numeric columns.
        data = pd.DataFrame(
            {
                "Feature1": ["a", "b", "c"],
                "Feature2": ["d", "e", "f"],
                "Feature3": ["g", "h", "i"],
                "Feature4": ["j", "k", "l"],
                "Feature5": ["m", "n", "o"],
            }
        )
        with self.assertRaises(ValueError):
            task_func(data)
    def test_case_13(self):
        # Function should fail if more than expected number of features (5)
        data = pd.DataFrame(np.random.rand(100, 50))
        with self.assertRaises(KeyError):
            task_func(data)
    def standardized_data_test(self, data):
        np.random.seed(0)
        standardized_data, axes_list = task_func(data)
        # Check if the data is standardized (mean ~ 0 and standard deviation ~ 1)
        self.assertTrue(np.isclose(standardized_data.mean().values, 0, atol=1e-2).all())
        self.assertTrue(np.isclose(standardized_data.std().values, 1, atol=1e-1).all())
        # Check the number of returned histograms
        self.assertEqual(len(axes_list), 5)
        # Check if each histogram is correctly titled
        for ax, feature in zip(axes_list, self.columns):
            self.assertEqual(ax.get_title(), f"Histogram of {feature}")
        # Check if histograms have the right number of bins
        for ax in axes_list:
            self.assertEqual(len(ax.patches), 20)
    def tearDown(self):
        plt.close("all")
