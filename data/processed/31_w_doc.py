import random
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    """
    Draws a histogram of the "from_user" values in the provided result. The color of the histogram bars is selected at random from the provided colors list.

    Parameters:
    result (list): A list of dictionaries containing the key "from_user".
    colors (list, optional): A list of colors to choose from for the histogram bars. Defaults is ['b', 'g', 'r', 'c', 'm', 'y', 'k'].

    Returns:
    None: The function displays the histogram and does not return any value.

    Requirements:
    - random
    - matplotlib
    - seaborn

    Example:
    >>> result = [{"from_user": 0}, {"from_user": 0}, {"from_user": 1}]
    >>> task_func(result)
    """
    from_user_values = [d['from_user'] for d in result if 'from_user' in d]
    color = random.choice(colors)
    plt.figure()
    sns.histplot(from_user_values, color=color)
    plt.show()

import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        random.seed(42)
        result = [
            {"from_user": 0}, 
            {"from_user": 0}, 
            {"from_user": 1}
        ]
        with patch("matplotlib.pyplot.show") as mocked_show:
            task_func(result)
            mocked_show.assert_called_once()
    def test_case_2(self):
        random.seed(42)
        result = []
        with patch("matplotlib.pyplot.show") as mocked_show:
            task_func(result)
            mocked_show.assert_called_once()
    def test_case_3(self):
        random.seed(42)
        result = [
            {"hello": 0}, 
            {"world": 1}
        ]
        with patch("matplotlib.pyplot.show") as mocked_show:
            task_func(result)
            mocked_show.assert_called_once()
    def test_case_4(self):
        random.seed(42)
        result = [
            {"from_user": 0}, 
            {"from_user": 1}, 
            {"from_user": 2}
        ]
        colors = ["orange", "purple"]
        with patch("matplotlib.pyplot.show") as mocked_show, patch("random.choice", return_value="orange") as mocked_choice:
            task_func(result, colors)
            mocked_choice.assert_called_with(colors)
            mocked_show.assert_called_once()
    def test_case_5(self):
        random.seed(42)
        result = [
            {
                "hello": 0,
                "from_user": 1,
            },
            {
                "world": 1,
                "from_user": 1
            },
            {
                "love": 1,
                "from_user": 1
            }
        ]
        with patch("matplotlib.pyplot.show") as mocked_show:
            task_func(result)
            mocked_show.assert_called_once()
