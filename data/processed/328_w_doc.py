import collections
import random
from queue import PriorityQueue


def task_func(number_teams=5):
    """
    Create a random sports ranking and sort it by points in descending order.
    
    Note:
    - Each team is assigned a name in the format "Team i" and a corresponding random number of points, where i ranges from 1 to the specified number of teams. 
    - The ranking is then sorted in descending order of points and returned as an OrderedDict.

    Parameters:
    number_teams (int, optional): The number of teams in the ranking. Default is 5.

    Returns:
    OrderedDict: Sorted dictionary where keys are team names and values are points.

    Requirements:
    - collections
    - random
    - queue.PriorityQueue


    Example:
    >>> random.seed(0)
    >>> ranking = task_func()
    >>> print(ranking)
    OrderedDict([('Team 4', 50), ('Team 5', 40), ('Team 1', 30), ('Team 2', 20), ('Team 3', 10)])
    """
    TEAMS = []
    POINTS = []
    for i in range(1, number_teams+1):
        TEAMS.append("Team "+str(i))
        POINTS.append(10*i)
    shuffled_points = POINTS.copy()
    random.shuffle(shuffled_points)
    ranking = dict(zip(TEAMS, shuffled_points))
    sorted_ranking = PriorityQueue()
    for team, points in ranking.items():
        sorted_ranking.put((-points, team))
    sorted_ranking_dict = collections.OrderedDict()
    while not sorted_ranking.empty():
        points, team = sorted_ranking.get()
        sorted_ranking_dict[team] = -points
    return sorted_ranking_dict

import unittest
import random
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test if the return type is OrderedDict."""
        random.seed(0)
        result = task_func()
        self.assertIsInstance(result, collections.OrderedDict, "Return type should be OrderedDict.")
    def test_length_of_return(self):
        """Test if the returned OrderedDict has the correct length."""
        random.seed(0)
        result = task_func(5)
        self.assertEqual(len(result), 5, "Returned OrderedDict should have the same length as TEAMS.")
    def test_inclusion_of_teams(self):
        """Test if all predefined teams are included."""
        random.seed(0)
        result = task_func(5)
        TEAMS = []
        for i in range(1, 5+1):
            TEAMS.append("Team "+str(i))
        self.assertTrue(all(team in result for team in TEAMS), "All predefined teams should be included in the result.")
    def test_ordering_of_points(self):
        """Test if points are in descending order."""
        random.seed(0)
        result = task_func()
        points = list(result.values())
        self.assertTrue(all(points[i] >= points[i + 1] for i in range(len(points) - 1)), "Points should be in descending order.")
    def test_data_types_in_return(self):
        """Test if keys and values in the returned OrderedDict are of correct data types."""
        random.seed(0)
        result = task_func()
        self.assertTrue(all(isinstance(team, str) for team in result.keys()), "All keys in the result should be strings.")
        self.assertTrue(all(isinstance(points, int) for points in result.values()), "All values in the result should be integers.")
