import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


def f_103(json_data: str, data_key: str):
    """
    Processes a JSON string to extract numerical data, Min-Max normalize them,
    and generate a line plot.

    Parameters:
    - json_data (str): JSON formatted string containing the data.
    - data_key (str): Dot-separated full key path to access the numerical data within the JSON structure.

    Returns:
    - Tuple:
      - pd.Series: Original dataset in float64.
      - pd.Series or None: Dataset after Min-Max scaling in float64, or None if data is empty.
      - plt.Axes or None: Line plot of normalized data, or None if data is empty.

    Raises:
    - KeyError: if key path is not found in the given data.

    Requirements:
    - json
    - pandas
    - sklearn
    - matplotlib

    Notes:
    - The line plot includes labeled axes and a legend. It visualizes the original
      data with label "Original Data" and normalized ones as "Normalized Data".
      The function sets the plot title to "Comparison of Original and Normalized Data",
      with "Index" on the x-axis and "Value" on the y-axis.

    Example:
    >>> json_str = '{"data": {"values": [5, 10, 15, 20, 25]}}'
    >>> original_data, normalized_data, ax = f_103(json_str, 'data.values')
    >>> type(original_data), type(normalized_data), type(ax)
    (<class 'pandas.core.series.Series'>, <class 'pandas.core.series.Series'>, <class 'matplotlib.axes._axes.Axes'>)
    """
    data = json.loads(json_data)
    try:
        data = json.loads(json_data)
        for key in data_key.split("."):
            data = data[key]
        values = pd.Series(data, dtype=pd.Float64Dtype)
    except KeyError:
        raise KeyError(f"Key path '{data_key}' not found in the provided JSON data.")

    if values.empty:
        return values, None, None

    scaler = MinMaxScaler()
    normalized_values = pd.Series(
        scaler.fit_transform(values.values.reshape(-1, 1)).flatten(),
        dtype=pd.Float64Dtype,
    )

    fig, ax = plt.subplots()
    ax.plot(values, label="Original Data")
    ax.plot(normalized_values, label="Normalized Data")
    ax.set_title("Comparison of Original and Normalized Data")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.legend()

    return values, normalized_values, ax

import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_data_extraction(self):
        json_str = '{"data": {"values": [0.5, 10, 15, 20]}}'
        data_key = "data.values"
        original_data, _, _ = f_103(json_str, data_key)
        expected_series = pd.Series([0.5, 10, 15, 20], dtype=pd.Float64Dtype)
        pd.testing.assert_series_equal(original_data, expected_series)
    def test_data_normalization(self):
        json_str = '{"data": {"values": [0, 10, 20, 30, 40]}}'
        data_key = "data.values"
        _, normalized_data, _ = f_103(json_str, data_key)
        expected_normalized = pd.Series(
            [0.0, 0.25, 0.5, 0.75, 1.0], dtype=pd.Float64Dtype
        )
        pd.testing.assert_series_equal(normalized_data, expected_normalized)
    def test_plot_properties(self):
        json_str = '{"data": {"values": [1, 2, 3, 4, 5]}}'
        data_key = "data.values"
        _, _, ax = f_103(json_str, data_key)
        self.assertEqual(ax.get_title(), "Comparison of Original and Normalized Data")
        self.assertEqual(ax.get_xlabel(), "Index")
        self.assertEqual(ax.get_ylabel(), "Value")
        legend_texts = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertIn("Original Data", legend_texts)
        self.assertIn("Normalized Data", legend_texts)
    def test_empty_data(self):
        json_str = '{"data": {"values": []}}'
        data_key = "data.values"
        original_data, normalized_data, ax = f_103(json_str, data_key)
        self.assertTrue(original_data.empty)
        self.assertIsNone(normalized_data)
        self.assertIsNone(ax)
    def test_non_uniform_data_spacing(self):
        json_str = '{"data": {"values": [1, 1, 2, 3, 5, 8]}}'
        data_key = "data.values"
        _, normalized_data, _ = f_103(json_str, data_key)
        expected_normalized = pd.Series(
            [0.0, 0.0, 0.142857, 0.285714, 0.571429, 1.0], dtype=pd.Float64Dtype
        )
        pd.testing.assert_series_equal(normalized_data, expected_normalized, atol=1e-6)
    def test_negative_values(self):
        json_str = '{"data": {"values": [-50, -20, 0, 20, 50]}}'
        data_key = "data.values"
        _, normalized_data, _ = f_103(json_str, data_key)
        expected_normalized = pd.Series(
            [0.0, 0.3, 0.5, 0.7, 1.0], dtype=pd.Float64Dtype
        )
        pd.testing.assert_series_equal(normalized_data, expected_normalized, atol=1e-5)
    def test_nested_json_structure(self):
        json_str = '{"data": {"deep": {"deeper": {"values": [2, 4, 6, 8, 10]}}}}'
        data_key = "data.deep.deeper.values"
        original_data, _, _ = f_103(json_str, data_key)
        expected_series = pd.Series([2, 4, 6, 8, 10], dtype=pd.Float64Dtype)
        pd.testing.assert_series_equal(original_data, expected_series)
    def test_complex_json_structure(self):
        json_str = """
        {
            "metadata": {
                "source": "sensor_array",
                "timestamp": "2023-04-11"
            },
            "readings": {
                "temperature": [20, 22, 21, 23, 24],
                "humidity": [30, 32, 31, 33, 34],
                "data": {
                    "deep": {
                        "deeper": {
                            "values": [100, 200, 300, 400, 500]
                        },
                        "another_level": {
                            "info": "This should not be processed"
                        }
                    }
                }
            }
        }"""
        data_key = "readings.data.deep.deeper.values"
        original_data, normalized_data, ax = f_103(json_str, data_key)
        expected_series = pd.Series([100, 200, 300, 400, 500], dtype=pd.Float64Dtype)
        pd.testing.assert_series_equal(original_data, expected_series)
        expected_normalized = pd.Series(
            [0.0, 0.25, 0.5, 0.75, 1.0], dtype=pd.Float64Dtype
        )
        pd.testing.assert_series_equal(normalized_data, expected_normalized, atol=1e-5)
        self.assertIsInstance(ax, plt.Axes)
