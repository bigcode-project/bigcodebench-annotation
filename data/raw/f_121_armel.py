import pandas as pd
import matplotlib.pyplot as plt


def f_121(df, age, height):
    """
    Select rows in Pandas DataFrame df, where the value in the "Age" column is greater than age and the value in the "Height" column is smaller than height.
    It then plots the selected data as a scatter plot with 'Age' on the x-axis and 'Height' on the y-axis.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    age (int): The minimum age for selection.
    height (int): The maximum height for selection.

    Returns:
    pd.DataFrame: The selected DataFrame.
    matplotlib.axes._subplots.AxesSubplot: The scatter plot of selected data.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame({
    ...     'Age': [30, 45, 60, 75],
    ...     'Height': [160, 170, 180, 190],
    ...     'Weight': [55, 65, 75, 85]
    ... })
    >>> selected_df, ax = f_121(df, 50, 185)
    """
    selected_df = df[(df["Age"] > age) & (df["Height"] < height)]
    ax = selected_df.plot(kind="scatter", x="Age", y="Height", title=None)
    return selected_df, ax


import unittest
import pandas as pd
from faker import Faker


def generate_dataframe(num_records=100):
    fake = Faker()
    Faker.seed(0)
    data = {
        "Name": [fake.name() for _ in range(num_records)],
        "Age": [fake.random_int(min=0, max=100) for _ in range(num_records)],
        "Height": [fake.random_int(min=150, max=200) for _ in range(num_records)],
        "Weight": [fake.random_int(min=50, max=100) for _ in range(num_records)],
        "Address": [fake.address() for _ in range(num_records)],
        "Email": [fake.email() for _ in range(num_records)],
    }
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
