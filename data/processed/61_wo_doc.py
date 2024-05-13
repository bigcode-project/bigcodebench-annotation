import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    """
    Plots the square root function for values associated with the key 'from_user' from the input list of dictionaries. Annotates the graph with the current date and time.
    - Round each square root value to 2 decimals.

    Parameters:
    result (list): A list of dictionaries containing numeric values with the key 'from_user'.

    Returns:
    - numpy.ndarray: list of square values associated with the key 'from_user' from the input list of dictionaries.
    - matplotlib.axes.Axes: plot of square root values.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - datetime

    Constants:
    - PLOT_TITLE: Title of the plot (default is 'Square root plot').
    - X_LABEL: Label for the x-axis (default is 'x').
    - Y_LABEL: Label for the y-axis (default is 'sqrt(x)').
    - TIME_FORMAT: Format for displaying the current date and time (default is '%Y-%m-%d %H:%M:%S').

    Example:
    >>> result = [{"hi": 7, "bye": 4, "from_user": 16}, {"some_key": 2, "another_key": 4, "from_user": 9}]
    >>> square_roots, ax = task_func(result)
    >>> print(square_roots)
    [4. 3.]
    """

    from_user_values = [d['from_user'] for d in result if 'from_user' in d]
    square_roots = np.round(np.sqrt(from_user_values), 2)
    plt.figure()
    plt.plot(from_user_values, square_roots)
    plt.title(PLOT_TITLE)
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL)
    now = datetime.now()
    now_str = now.strftime(TIME_FORMAT)
    plt.annotate(now_str, (0.05, 0.95), xycoords='axes fraction')
    ax = plt.gca()
    return square_roots, ax

import unittest
import matplotlib
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        # Input 1: Normal case with 2 dictionaries with 'from_user' keys.
        data = [
            {"key_1": 7, "key_2": 4, "from_user": 16},
            {"key_1": 2, "key_2": 4, "from_user": 9},
        ]
        square_roots, ax = task_func(data)
        self.assertEqual(ax.get_title(), PLOT_TITLE)
        self.assertEqual(ax.get_xlabel(), X_LABEL)
        self.assertEqual(ax.get_ylabel(), Y_LABEL)
        np.testing.assert_array_equal(square_roots, np.array([4.0, 3.0]))
        annotations = [child for child in ax.get_children() if isinstance(child, matplotlib.text.Annotation)]
        try:
            datetime.strptime(annotations[0].get_text(), TIME_FORMAT)
        except:
            raise ValueError(f"The datetime in annotation ({annotations[0]}) does not have the right format ({TIME_FORMAT}).")
    def test_case_2(self):
        # Input 2: List with 1 dictionary without the 'from_user' key.
        data = [
            {
                "key_1": 7,
                "key_2": 4
            }
        ]
        square_roots, ax = task_func(data)
        self.assertEqual(len(square_roots), 0)
    def test_case_3(self):
        # Input 3: Empty list.
        data = []
        square_roots, ax = task_func(data)
        self.assertEqual(len(square_roots), 0)
    def test_case_4(self):
        # Input 4: Normal case with 5 dictionaries with 'from_user' keys.
        data = [
            {
                "from_user": 121,
                "unused_key": 45,
            },
            {
                "from_user": 169,
                "unused_key": -1,
            },
            {
                "from_user": 225,
            },
            {
                "from_user": 9,
            },
            {
                "from_user": 49,
            },
        ]
        square_roots, ax = task_func(data)
        np.testing.assert_array_equal(square_roots, np.array([11.0, 13.0, 15.0, 3.0, 7.0]))
    def test_case_5(self):
        # Input 5: List with 1 dictionary with the 'from_user' key.
        data = [{"from_user": 7, "bye": 4}]
        square_roots, ax = task_func(data)
        np.testing.assert_array_equal(square_roots, np.array([2.65]))
