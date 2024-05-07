import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt


def f_824(feature: pd.Series, target: pd.Series) -> (np.ndarray, plt.Axes):
    """
    Train a logistic regression model on one feature and evaluate its performance using a confusion matrix plot.
    The function takes a feature and a target series, splits them into training and testing sets, trains the logistic
    regression model, predicts the target for the test set, and plots the confusion matrix.

    Parameters:
    feature (pd.Series): Series representing the single feature for the logistic regression model.
    target (pd.Series): Series representing the target variable.

    Returns:
    (np.ndarray, plt.Axes): A tuple containing the confusion matrix and the matplotlib Axes object of the confusion matrix plot.

    Requirements:
    - pandas
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LogisticRegression
    - sklearn.metrics.confusion_matrix
    - numpy
    - matplotlib.pyplot

    Example:
    >>> feature = pd.Series(np.random.rand(1000)) # Feature data
    >>> target = pd.Series(np.random.randint(0, 2, size=1000)) # Target data (binary)
    >>> cm, ax = f_824(feature, target)
    >>> ax.get_title()
    'Confusion Matrix'
    """
    df = pd.DataFrame({"Feature": feature, "Target": target})
    X_train, X_test, y_train, y_test = train_test_split(
        df["Feature"], df["Target"], test_size=0.2, random_state=42
    )
    model = LogisticRegression()
    model.fit(X_train.values.reshape(-1, 1), y_train)
    y_pred = model.predict(X_test.values.reshape(-1, 1))
    cm = confusion_matrix(y_test, y_pred)
    _, ax = plt.subplots()
    cax = ax.matshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.colorbar(cax)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["No", "Yes"])
    ax.set_yticklabels(["No", "Yes"])
    return cm, ax

import unittest
import pandas as pd
import numpy as np
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    """Test cases for the function f_824."""
    def test_with_random_data(self):
        """
        Test the function with random data to ensure normal functionality.
        """
        np.random.seed(42)
        feature = pd.Series(np.random.rand(100))
        np.random.seed(42)
        target = pd.Series(np.random.randint(0, 2, size=100))
        cm, ax = f_824(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def test_with_all_zeroes(self):
        """
        Test the function with all zeroes in the feature set.
        """
        feature = pd.Series(np.zeros(100))
        np.random.seed(123)
        target = pd.Series(np.random.randint(0, 2, size=100))
        cm, ax = f_824(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def test_with_all_ones(self):
        """
        Test the function with all ones in the feature set.
        """
        feature = pd.Series(np.ones(100))
        np.random.seed(42)
        target = pd.Series(np.random.randint(0, 2, size=100))
        cm, ax = f_824(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def test_with_perfect_correlation(self):
        """
        Test the function when the feature perfectly predicts the target.
        """
        np.random.seed(123)
        feature = pd.Series(np.random.rand(100))
        target = feature.round()
        cm, ax = f_824(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def test_with_no_correlation(self):
        """
        Test the function when there is no correlation between feature and target.
        """
        np.random.seed(42)
        feature = pd.Series(np.random.rand(100))
        np.random.seed(42)
        target = pd.Series(np.random.choice([0, 1], size=100))
        cm, ax = f_824(feature, target)
        self.assertIsInstance(cm, np.ndarray)
        self.assertIsInstance(ax, Axes)
    def tearDown(self):
        plt.close()
