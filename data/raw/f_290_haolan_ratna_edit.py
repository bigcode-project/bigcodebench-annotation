import collections
from random import shuffle
from queue import PriorityQueue


def f_290(number_teams=5):
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
    - queue


    Example:
    >>> ranking = f_290()
    >>> print(ranking)
    OrderedDict([('Team X', 50), ('Team Y', 40), ...])
    """

    # Constants
    
    TEAMS = []
    POINTS = []

    for i in range(1, number_teams+1):
        TEAMS.append("Team "+str(i))
        POINTS.append(10*i)
    
    shuffled_points = POINTS.copy()
    shuffle(shuffled_points)
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

class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test if the return type is OrderedDict."""
        result = f_290()
        self.assertIsInstance(result, collections.OrderedDict, "Return type should be OrderedDict.")

    def test_length_of_return(self):
        """Test if the returned OrderedDict has the correct length."""
        result = f_290(5)
        self.assertEqual(len(result), 5, "Returned OrderedDict should have the same length as TEAMS.")

    def test_inclusion_of_teams(self):
        """Test if all predefined teams are included."""
        result = f_290(5)
        TEAMS = []
        for i in range(1, 5+1):
            TEAMS.append("Team "+str(i))
        self.assertTrue(all(team in result for team in TEAMS), "All predefined teams should be included in the result.")

    def test_ordering_of_points(self):
        """Test if points are in descending order."""
        result = f_290()
        points = list(result.values())
        self.assertTrue(all(points[i] >= points[i + 1] for i in range(len(points) - 1)), "Points should be in descending order.")

    def test_data_types_in_return(self):
        """Test if keys and values in the returned OrderedDict are of correct data types."""
        result = f_290()
        self.assertTrue(all(isinstance(team, str) for team in result.keys()), "All keys in the result should be strings.")
        self.assertTrue(all(isinstance(points, int) for points in result.values()), "All values in the result should be integers.")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# Uncomment the line below to run tests when this script is executed directly
# run_tests()
if __name__ == "__main__":
    run_tests()