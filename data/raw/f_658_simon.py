import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def f_658(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    """
    Generate a dataset with a single feature and a target variable. The target
    is computed from the feature using a linear relation.
    In addition some gaussian noise (random samples from normal distributioin), scaled by
    noise_strength, is added to the target. The dataset is split into training
    and test sets. Then a linear regression model is adjusted to the training
    set and the R-squared score is calculated on the test set.

    Parameters:
    - num_samples (int): The number of samples to generate for the dataset.
                   Defaults to 500
    - noise_strength (float): The strength (magnitude) of the noise that is
                              added to the dataset. Defaults to 1
    - random_seed (int): The seed used in generating the dataset, in performing
                   the train test split and in generating the random noise.
                   Defaults to None
    - test_size (float): The fraction of the test split. Defaults to 0.2

    Returns:
    float: The R-squared score of the fitted model on the test set.
    LinearRegression: The trained linear regression model.

    Raises:
    - ValueError: If test set size is smaller than 2.

    Requirements:
    - numpy
    - pandas
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LinearRegression

    Example:
    >>> f_658(num_samples=10, noise_strength=23.5, random_seed=24, test_size=0.3)
    -0.4892453918038726
    >>> f_658(noise_strength=0.1)
    0.9720280466398104
    """

    if num_samples * test_size < 2:
        raise ValueError("Test set should contain at least 2 samples. num_samples * testsize >=2")

    if random_seed is not None:
        np.random.seed(random_seed)

    X = np.random.rand(num_samples, 1)
    y = 2*X.squeeze() + 1 + np.random.randn(num_samples) * noise_strength

    X_train, X_test, y_train, y_test = train_test_split(
                                            X, y,
                                            test_size=test_size,
                                            random_state=random_seed
                                            )

    model = LinearRegression()
    model.fit(X_train, y_train)

    r_squared = model.score(X_test, y_test)

    return r_squared, model


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_case_1(self):
        'rng reproducability'
        r_squared1, _ = f_658(random_seed=42)
        r_squared2, _ = f_658(random_seed=42)

        self.assertEqual(r_squared1, r_squared2)

    def test_case_2(self):
        'default params'
        r_squared, model = f_658(num_samples=1000)
        self.assertTrue(0 <= r_squared <= 1)
        self.assertTrue(isinstance(model, LinearRegression))
        
    def test_case_3(self):
        'noise strength'
        r_squared, model = f_658(noise_strength=0, random_seed=24)
        self.assertAlmostEqual(r_squared, 1)
        self.assertTrue(isinstance(model, LinearRegression))

    def test_case_4(self):
        'test set too small'
        self.assertRaises(Exception, f_658, {'num_samples': 10, 'test_size': 0.1})

    def test_case_5(self):
        r_squared, model = f_658(num_samples=1000, noise_strength=1000, random_seed=24, test_size=0.3)
        self.assertTrue(r_squared < 0.2)
        self.assertTrue(isinstance(model, LinearRegression))



if __name__ == "__main__":
    run_tests()