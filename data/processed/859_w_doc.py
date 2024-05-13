import warnings
import sklearn.model_selection as model_selection
import sklearn.svm as svm
import sklearn.datasets as datasets
import sklearn.metrics as metrics

def task_func():
    """
    Perform an SVM classification of the iris dataset and warn if the accuracy is less than 0.9.
    The warning action is set to 'always'. The test size for the train-test split is 0.33.

    Parameters:
    - None

    Returns:
    tuple: A tuple containing:
        - accuracy (float): The accuracy of the SVM classification.
        - warning_msg (str or None): A warning message if the accuracy is below 0.9, None otherwise.

    Requirements:
    - warnings
    - sklearn

    Example:
    >>> task_func()
    (1.0, None)
    """

    warnings.simplefilter('always')
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        iris.data, iris.target, test_size=0.33, random_state=42)
    clf = svm.SVC(random_state=42)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, predictions)
    warning_msg = None
    if accuracy < 0.9:
        warning_msg = "The accuracy of the SVM classification is below 0.9."
        warnings.warn(warning_msg)
    return accuracy, warning_msg

import unittest
class TestCases(unittest.TestCase):
    def test_high_accuracy(self):
        accuracy, warning_msg = task_func()
        self.assertGreaterEqual(accuracy, 0.8)
        self.assertIsNone(warning_msg)
    def test_low_accuracy_warning(self):
        accuracy, warning_msg = task_func()
        if accuracy < 0.9:
            self.assertEqual(warning_msg, "The accuracy of the SVM classification is below 0.9.")
    def test_accuracy_range(self):
        accuracy, _ = task_func()
        self.assertGreaterEqual(accuracy, 0)
        self.assertLessEqual(accuracy, 1)
    def test_return_type(self):
        result = task_func()
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], float)
        self.assertIn(result[1], [None, "The accuracy of the SVM classification is below 0.9."])
    def test_warning_setting(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            _, _ = task_func()
            if w:
                self.assertEqual(str(w[-1].message), "The accuracy of the SVM classification is below 0.9.")
