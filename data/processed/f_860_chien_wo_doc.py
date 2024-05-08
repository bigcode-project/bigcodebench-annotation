import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


def f_881(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    """
    Processes a CSV file to train a Random Forest classifier and generates a formatted classification report.

    Parameters:
        csv_file_path (str): The path to the CSV file containing the data.
        target_column (str, optional): The name of the target variable column. Defaults to 'target'.
        test_size (float, optional): The proportion of the dataset to include in the test split. Defaults to 0.2.
        n_estimators (int, optional): The number of trees in the RandomForestClassifier. Defaults to 100.

    Returns:
        str: A formatted classification report. The report includes metrics such as precision, recall,
             f1-score for each class, as well as overall accuracy, macro average, and weighted average.

    Raises:
        ValueError: If the specified target_column is not found in the CSV file.

    Requirements:
        - pandas
        - sklearn

    Example:
    >>> report = f_881('/path/to/data.csv')
    >>> print(report)
    class 0        0.88       0.90       0.89          50
    class 1        0.89       0.87       0.88          48
    ...
    accuracy                           0.89         100
    macro avg       0.88       0.89       0.88         100
    weighted avg    0.89       0.89       0.89         100

    Note:
        The CSV file must have a column with the name specified by 'target_column', and it should be in a
        format readable by pandas.read_csv().
    """
    df = pd.read_csv(csv_file_path)
    if target_column not in df.columns:
        raise ValueError(f"'{target_column}' column not found in the CSV file.")
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)
    lines = report.split("\n")
    formatted_lines = []
    for line in lines:
        parts = line.split()
        if len(parts) == 5:  # Class-specific metrics
            formatted_line = f"{parts[0]:<15}{parts[1]:>10}{parts[2]:>10}{parts[3]:>10}{parts[4]:>10}"
        elif len(parts) == 4:  # Overall metrics
            formatted_line = f"{parts[0]:<15}{parts[1]:>10}{parts[2]:>10}{parts[3]:>10}"
        else:
            formatted_line = line  # Header or empty lines
        formatted_lines.append(formatted_line)
    formatted_report = "\n".join(formatted_lines)
    return formatted_report

import unittest
from unittest.mock import patch
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for f_881."""
    @patch("pandas.read_csv")
    def test_default_parameters(self, mock_read_csv):
        """
        Test f_881 with default parameters using an adequately sized mock dataset.
        """
        mock_data = {
            "feature1": range(100),
            "feature2": range(100, 200),
            "target": [0, 1] * 50,  # Alternating 0s and 1s
        }
        mock_read_csv.return_value = pd.DataFrame(mock_data)
        result = f_881("dummy_path.csv")
        self.assertIn("precision", result)
    @patch("pandas.read_csv")
    def test_non_default_target_column(self, mock_read_csv):
        """
        Test f_881 with a non-default target column using a larger mock dataset.
        """
        mock_data = {
            "feature1": range(100),
            "feature2": range(100, 200),
            "label": [1, 0] * 50,  # Alternating 1s and 0s
        }
        mock_read_csv.return_value = pd.DataFrame(mock_data)
        result = f_881("dummy_path.csv", target_column="label")
        self.assertIn("precision", result)
    @patch("pandas.read_csv")
    def test_different_test_size(self, mock_read_csv):
        """
        Test f_881 with a different test size and a larger dataset.
        """
        mock_data = {
            "feature1": range(100),
            "feature2": range(100, 200),
            "target": [0, 1, 1, 0] * 25,  # Repeated pattern
        }
        mock_read_csv.return_value = pd.DataFrame(mock_data)
        result = f_881("dummy_path.csv", test_size=0.5)
        self.assertIn("precision", result)
    @patch("pandas.read_csv")
    def test_different_n_estimators(self, mock_read_csv):
        """
        Test f_881 with a different number of estimators and an expanded dataset.
        """
        mock_data = {
            "feature1": range(100),
            "feature2": range(100, 200),
            "target": [1, 0] * 50,  # Alternating 1s and 0s
        }
        mock_read_csv.return_value = pd.DataFrame(mock_data)
        result = f_881("dummy_path.csv", n_estimators=50)
        self.assertIn("precision", result)
    @patch("pandas.read_csv")
    def test_missing_target_column(self, mock_read_csv):
        """
        Test f_881 with a missing target column.
        """
        mock_read_csv.return_value = pd.DataFrame(
            {"feature1": [1, 2], "feature2": [3, 4]}
        )
        with self.assertRaises(ValueError):
            f_881("dummy_path.csv", target_column="not_exist")
