import pandas as pd
import matplotlib.pyplot as plt


def f_121(array, age, height):
    """
    Given a 2D input array containing where the first three rows correspond to 'Age', 'Height', 'Weight' and each column denotes an individual. Convert this array into a pandas dataframes with column names 'Age', 'Height', 'Weight' and name the remaining rows as 'Feature 1', 'Feature 2', ... 'Feature k'. Then select rows in Pandas DataFrame df, where the value in the "Age" column is greater than age and the value in the "Height" column is smaller than height.
    It then plots the selected data as a scatter plot with 'Age' on the x-axis and 'Height' on the y-axis.

    Parameters:
    array (np.array): The input array.
    age (int): The minimum age for selection.
    height (int): The maximum height for selection.

    Returns:
    pd.DataFrame: The selected DataFrame.
    matplotlib.axes._subplots.AxesSubplot: The scatter plot of selected data.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> import numpy as np
    >>> array = np.array([
    ...    [30, 45, 60, 75],
    ...    [160, 170, 180, 190],
    ...    [55, 65, 75, 85]
    ... ])
    >>> selected_df, ax = f_121(array, 50, 185)
    >>> print(selected_df)
       Age  Height  Weight
    2   60     180      75
    """
    columns = ["Age", "Height", "Weight"] + [
        f"Feature {i+1}" for i in range(array.shape[0] - 3)
    ]
    df = pd.DataFrame(array.T, columns=columns)
    selected_df = df[(df["Age"] > age) & (df["Height"] < height)]
    ax = selected_df.plot(kind="scatter", x="Age", y="Height", title=None)
    return selected_df, ax


import unittest
from faker import Faker


def generate_dataframe(num_records=100):
    fake = Faker()
    Faker.seed(0)
    data = [
        [fake.random_int(min=0, max=100) for _ in range(num_records)],
        [fake.random_int(min=150, max=200) for _ in range(num_records)],
        [fake.random_int(min=50, max=100) for _ in range(num_records)],
        [fake.name() for _ in range(num_records)],
        [fake.address() for _ in range(num_records)],
        [fake.email() for _ in range(num_records)],
    ]
    return pd.DataFrame(data)


class TestCases(unittest.TestCase):
    """Test cases for the f_121 function."""

    def test_case_1(self):
        df = generate_dataframe(1000)
        selected_df, ax = f_121(df, 50, 185)
        self.assertTrue(selected_df["Age"].gt(50).all())
        self.assertTrue(selected_df["Height"].lt(185).all())
        self.assertEqual(ax.get_xlabel(), "Age")
        self.assertEqual(ax.get_ylabel(), "Height")
        self.assertEqual(ax.get_title(), "")

    def test_case_2(self):
        df = generate_dataframe(10)
        selected_df, ax = f_121(df, 40, 190)
        self.assertTrue(selected_df["Age"].gt(40).all())
        self.assertTrue(selected_df["Height"].lt(190).all())
        self.assertEqual(ax.get_xlabel(), "Age")
        self.assertEqual(ax.get_ylabel(), "Height")
        self.assertEqual(ax.get_title(), "")

    def test_case_3(self):
        df = generate_dataframe(500)
        selected_df, ax = f_121(df, 10, 200)
        self.assertTrue(selected_df["Age"].gt(10).all())
        self.assertTrue(selected_df["Height"].lt(200).all())
        self.assertEqual(ax.get_xlabel(), "Age")
        self.assertEqual(ax.get_ylabel(), "Height")
        self.assertEqual(ax.get_title(), "")

    def test_case_4(self):
        df = generate_dataframe(50)
        selected_df, ax = f_121(df, 20, 195)
        self.assertTrue(selected_df["Age"].gt(20).all())
        self.assertTrue(selected_df["Height"].lt(195).all())
        self.assertEqual(ax.get_xlabel(), "Age")
        self.assertEqual(ax.get_ylabel(), "Height")
        self.assertEqual(ax.get_title(), "")

    def test_case_5(self):
        df = generate_dataframe(100)
        selected_df, ax = f_121(df, 80, 170)
        self.assertTrue(selected_df["Age"].gt(80).all())
        self.assertTrue(selected_df["Height"].lt(170).all())
        self.assertEqual(ax.get_xlabel(), "Age")
        self.assertEqual(ax.get_ylabel(), "Height")
        self.assertEqual(ax.get_title(), "")

    def test_case_6(self):
        df = pd.DataFrame(
            {
                "Age": [25, 30, 17, 63, 44, 19, 39, 11],
                "Height": [174, 180, 190, 166, 150, 178, 195, 202],
            }
        )
        selected_df, ax = f_121(df, 23, 180)
        self.assertTrue(selected_df["Age"].gt(23).all())
        self.assertTrue(selected_df["Height"].lt(180).all())
        self.assertEqual(ax.get_xlabel(), "Age")
        self.assertEqual(ax.get_ylabel(), "Height")
        self.assertEqual(ax.get_title(), "")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
