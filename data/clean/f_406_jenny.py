import pandas as pd
from scipy.spatial.distance import pdist, squareform


def f_406(array):
    """
    Generate a Pandas DataFrame from a 2D list and calculate a distance matrix.

    This function converts a 2D list into a DataFrame, with columns named alphabetically starting from 'A'.
    It uses the `chr()` function, which converts an integer to its corresponding Unicode character,
    to dynamically assign alphabetical labels to each column based on their index. The function then
    computes the Euclidean distance matrix between rows.

    Parameters:
    array (list of list of int): The 2D list representing the data.
                                 Each sublist must contain only integers or floats. If the input does not
                                 conform to this structure, a TypeError is raised.

    Returns:
    - df (pd.DataFrame): data converted from 2D list.
    - distance_matrix (pd.DataFrame): output distance matrix.

    Requirements:
    - pandas
    - scipy.spatial.distance.pdist
    - scipy.spatial.distance.squareform

    Example:
    >>> df, distance_matrix = f_406([[1,2,3,4,5], [6,7,8,9,10]])
    >>> print(df)
       A  B  C  D   E
    0  1  2  3  4   5
    1  6  7  8  9  10
    >>> print(distance_matrix)
          0          1
    0  0.0  11.180340
    1  11.180340  0.0
    """
    if not isinstance(array, list):
        raise TypeError("Input must be a list.")

    if not all(isinstance(sublist, list) for sublist in array):
        raise TypeError("Input must be a list of lists.")

    for sublist in array:
        if not all(isinstance(item, (int, float)) for item in sublist):
            raise TypeError("All elements in the sublists must be int or float.")

    columns = [chr(65 + i) for i in range(len(array[0]))]
    df = pd.DataFrame(array, columns=columns)

    distances = pdist(df.values, metric="euclidean")
    distance_matrix = pd.DataFrame(
        squareform(distances), index=df.index, columns=df.index
    )

    return df, distance_matrix


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Teset basic case
        input_data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        df, distance_matrix = f_406(input_data)
        self.assertEqual(df.shape, (2, 5))
        self.assertTrue((df.columns == ["A", "B", "C", "D", "E"]).all())
        self.assertEqual(distance_matrix.shape, (2, 2))
        self.assertAlmostEqual(distance_matrix.iloc[0, 1], 11.18034, places=5)
        self.assertAlmostEqual(distance_matrix.iloc[1, 0], 11.18034, places=5)

    def test_case_2(self):
        # Test negatives and zero
        input_data = [[-5, -4, -3, -2, -1], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5]]
        df, distance_matrix = f_406(input_data)
        self.assertEqual(df.shape, (3, 5))
        self.assertEqual(distance_matrix.shape, (3, 3))
        self.assertAlmostEqual(distance_matrix.iloc[0, 1], 7.41620, places=5)
        self.assertAlmostEqual(distance_matrix.iloc[1, 2], 7.41620, places=5)

    def test_case_3(self):
        # Test small lists
        input_data = [[1, 2], [3, 4]]
        df, distance_matrix = f_406(input_data)
        self.assertEqual(df.shape, (2, 2))
        self.assertEqual(distance_matrix.shape, (2, 2))
        self.assertAlmostEqual(distance_matrix.iloc[0, 1], 2.82843, places=5)

    def test_case_4(self):
        # Test repeated single element
        input_data = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        df, distance_matrix = f_406(input_data)
        self.assertEqual(df.shape, (3, 3))
        self.assertEqual(distance_matrix.shape, (3, 3))
        self.assertEqual(distance_matrix.iloc[0, 1], 0)
        self.assertEqual(distance_matrix.iloc[1, 2], 0)

    def test_case_5(self):
        # Test single list
        input_data = [[1, 2, 3, 4, 5]]
        df, distance_matrix = f_406(input_data)
        self.assertEqual(df.shape, (1, 5))
        self.assertEqual(distance_matrix.shape, (1, 1))
        self.assertEqual(distance_matrix.iloc[0, 0], 0)

    def test_case_6(self):
        # Test empty list
        input_data = []
        with self.assertRaises(IndexError):
            f_406(input_data)

    def test_case_7(self):
        # Test larger dataset
        input_data = [list(range(100)) for _ in range(50)]
        df, distance_matrix = f_406(input_data)
        self.assertEqual(df.shape, (50, 100))
        self.assertEqual(distance_matrix.shape, (50, 50))
        # No specific values check due to complexity

    def test_case_8(self):
        # Test single element list
        input_data = [[1]]
        df, distance_matrix = f_406(input_data)
        self.assertEqual(df.shape, (1, 1))
        self.assertEqual(distance_matrix.shape, (1, 1))
        self.assertEqual(distance_matrix.iloc[0, 0], 0)

    def test_case_9(self):
        # Test with different types in list
        input_data = [[1, 2, 3], ["a", "b", "c"]]
        with self.assertRaises(TypeError):
            f_406(input_data)

    def test_case_10(self):
        # Test with a more complex numerical list (including floats and negatives)
        input_data = [[-1.5, 2.3, 4.5], [0, 0, 0], [5.5, -2.3, 3.1]]
        df, distance_matrix = f_406(input_data)
        self.assertEqual(df.shape, (3, 3))
        self.assertEqual(distance_matrix.shape, (3, 3))

        # Define expected distances based on manual or precise calculation
        expected_distances = [
            [0.0, 5.27162, 8.49235],
            [5.27162, 0.0, 6.71937],
            [8.49235, 6.71937, 0.0],
        ]

        # Assert each calculated distance matches the expected value
        for i in range(len(expected_distances)):
            for j in range(len(expected_distances[i])):
                self.assertAlmostEqual(
                    distance_matrix.iloc[i, j], expected_distances[i][j], places=5
                )


if __name__ == "__main__":
    run_tests()
