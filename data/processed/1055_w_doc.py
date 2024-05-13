import pandas as pd
import itertools
import random


def task_func(colors, states):
    """
    Generates a pandas DataFrame containing shuffled combinations of provided colors and states.
    The DataFrame is formatted so that each column represents a series of unique combinations,
    with each combination displayed as "Color:State".

    Parameters:
    - colors (list): A list of strings representing color names.
    - states (list): A list of strings representing state descriptions.

    Returns:
    - df (pandas.DataFrame): A DataFrame where each cell contains a string of the format "Color:State".
      The combinations are distributed across columns, with the number of columns being the lesser
      of the lengths of 'colors' and 'states'.

    Requirements:
    - pandas
    - itertools
    - random

    Note:
    - Cartesian product of 'colors' and 'states',
    - The number of columns in the resulting DataFrame is determined by the smaller number of elements
      in either the 'colors' or 'states' list, ensuring an even distribution without excess empty cells.
    - If the number of combinations is not evenly divisible by the number of columns, some columns
      will have fewer entries.

    Example:
    >>> colors = ['Red', 'Blue', 'Green']
    >>> states = ['Solid', 'Liquid']
    >>> color_state_table = task_func(colors, states)
    >>> print(color_state_table)
      Color:State 1 Color:State 2
    0   Blue:Liquid    Red:Liquid
    1    Blue:Solid   Green:Solid
    2     Red:Solid  Green:Liquid
    """

    combinations = list(itertools.product(colors, states))
    random.seed(42)
    random.shuffle(combinations)
    num_columns = min(len(colors), len(states))
    data = {
        f"Color:State {i+1}": [
            f"{comb[0]}:{comb[1]}" for comb in combinations[i::num_columns]
        ]
        for i in range(num_columns)
    }
    df = pd.DataFrame(data)
    return df

import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    def test_empty_lists(self):
        """Test with empty color and state lists."""
        self.assertEqual(task_func([], []).empty, True)
    def test_single_color_and_state(self):
        """Test with one color and one state."""
        random.seed(0)
        result = task_func(["Red"], ["Solid"])
        expected = pd.DataFrame({"Color:State 1": ["Red:Solid"]})
        pd.testing.assert_frame_equal(result, expected)
    def test_multiple_colors_single_state(self):
        """Test with multiple colors and a single state."""
        random.seed(1)
        result = task_func(["Red", "Blue", "Green"], ["Solid"])
        expected_combinations = set(["Red:Solid", "Blue:Solid", "Green:Solid"])
        result_combinations = set(result["Color:State 1"])
        self.assertEqual(result_combinations, expected_combinations)
    def test_single_color_multiple_states(self):
        """Test with a single color and multiple states."""
        random.seed(2)
        result = task_func(["Red"], ["Solid", "Liquid", "Gas"])
        expected_combinations = set(["Red:Solid", "Red:Liquid", "Red:Gas"])
        result_combinations = set(result["Color:State 1"])
        self.assertEqual(result_combinations, expected_combinations)
    def test_multiple_colors_and_states(self):
        """Test with multiple colors and states."""
        random.seed(3)
        colors = ["Red", "Blue"]
        states = ["Solid", "Liquid"]
        result = task_func(colors, states)
        expected_combinations = set(
            [f"{color}:{state}" for color in colors for state in states]
        )
        result_combinations = set(result.values.flatten())
        self.assertEqual(result_combinations, expected_combinations)
