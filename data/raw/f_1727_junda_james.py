import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def f_1727(data, n_components=2):
    """
    Perform Principal Component Analysis (PCA) on a dataset and record the result.
    Also, generates a scatter plot of the transformed data.

    Parameters:
    data (DataFrame): The dataset.
    n_components (int): The number of principal components to calculate. Default is 2.

    Returns:
    DataFrame: The transformed data with principal components.
    Axes: The matplotlib Axes object containing the scatter plot.

    Raises:
    ValueError: If n_components is not a positive integer.

    Requirements:
    - numpy
    - pandas
    - matplotlib.pyplot
    - sklearn.decomposition

    Example:
    >>> data = pd.DataFrame([[14, 25], [1, 22], [7, 8]], columns=['Column1', 'Column2'])
    >>> transformed_data, plot = f_1727(data)
    """
    np.random.seed(42)
    if not isinstance(n_components, int) or n_components <= 0:
        raise ValueError("n_components must be a positive integer")

    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    fig, ax = plt.subplots()
    ax.scatter(transformed_data[:, 0], transformed_data[:, 1])

    return pd.DataFrame(transformed_data, columns=[f'PC{i+1}' for i in range(n_components)]), ax

import unittest
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'Column1': np.random.rand(10),
            'Column2': np.random.rand(10)
        })

    def test_transformed_data_shape(self):
        transformed_data, _ = f_1727(self.data, 2)
        self.assertEqual(transformed_data.shape, (10, 2))

    def test_invalid_n_components(self):
        with self.assertRaises(ValueError):
            f_1727(self.data, 0)

    def test_invalid_n_components_type(self):
        with self.assertRaises(ValueError):
            f_1727(self.data, "two")

    def test_plot_axes(self):
        _, ax = f_1727(self.data, 2)
        self.assertEqual(len(ax.collections), 1)  # One scatter plot

    def test_values(self):
        np.random.seed(42)
        transformed_data, _ = f_1727(self.data, 2)
        df_list = transformed_data.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(df_list))

        # Convert string pairs to list of tuples of floats
        expect = ['-0.36270132751314693,-0.17330242962071069', '0.7073025303719391,0.12382897836601565', '0.45378164000836924,0.1734575007991456', '-0.06806713223200053,-0.18707071063291186', '-0.41150042971259093,0.09384691859758798', '-0.4104362188060755,0.09501439103733277', '-0.3990216926714853,0.2501208456858351', '0.34082913981297874,-0.14263963596803247', '0.08412503285413396,-0.028734567486117184', '0.06568845788787812,-0.20452129077814485']
        # self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")
        df_tuples = [tuple(map(float, item.split(','))) for item in df_list]
        expect_tuples = [tuple(map(float, item.split(','))) for item in expect]

        # Assert each pair of tuples is approximately equal
        for actual, expected in zip(df_tuples, expect_tuples):
            self.assertAlmostEqual(actual[0], expected[0], places=7, msg="DataFrame contents should match the expected output")
            self.assertAlmostEqual(actual[1], expected[1], places=7, msg="DataFrame contents should match the expected output")

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