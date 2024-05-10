import numpy as np
import matplotlib.pyplot as plt


# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def f_315(city_dict, max_range=1000000, seed=0):
    """
    Given a constant list of cities (CITIES) and a dictionary 'city_dict' of people's names and their favorite cities, 
    this function generates a dictionary of city populations for the cities in the list and plots the population 
    data using a bar chart. The population values are randomly generated integers between 1 and 'max_range' if 
    the city is in the list of cities, otherwise the population value is -1. The random number generator is seeded
    with the value 'seed' before generating the population values.

    Parameters:
    city_dict (dict): The dictionary with keys as people's names and values as city names. 
    max_range (int, Optional): The maximum population value for the randomly generated population. Defaults to 1000000.
    Must be greater than 1.
    seed (int, Optional): The seed for the random number generator. Defaults to 0.

    Returns:
    dict: A dictionary with city names as keys and randomly generated populations as values.
    matplotlib.axes.Axes: The Axes object of the plot for further manipulation or testing.

    Requirements:
    - numpy for random number generation
    - matplotlib for plotting

    Example:
    >>> city_dict = {'John': 'New York', 'Alice': 'London', 'Bob': 'Beijing', 'Charlie': 'Tokyo', 'David': 'Sydney'}
    >>> population_dict, plot_axes = f_315(city_dict)
    """
    if max_range < 1:
        raise ValueError("max_range must be a positive integer")

    np.random.seed(seed)
    city_population = {
        city: (np.random.randint(1, max_range) if city in CITIES else -1) 
        for _, city in city_dict.items() if isinstance(city, str)
    }

    # Plotting the bar chart
    plt.figure()
    ax = plt.bar(city_population.keys(), city_population.values())
    plt.xlabel('City')
    plt.ylabel('Population')
    plt.title('City Populations')

    return city_population, plt.gca()


import unittest
from matplotlib.axes import Axes
import doctest


class TestCases(unittest.TestCase):

    def test_case_1(self):
        """Test if the population dictionary has correct structure and values."""
        city_dict = {'John': 'New York', 'Alice': 'London', 'Bob': 'Beijing', 'Charlie': 'Tokyo', 'David': 'Mumbai'}
        population_dict, _ = f_315(city_dict, 250000, 56)
        self.assertSetEqual(set(population_dict.keys()), {'New York', 'London', 'Beijing', 'Tokyo', 'Mumbai'})
        for population in population_dict.values():
            self.assertTrue(-1 <= population <= 250000)

    def test_case_2(self):
        """Test if the bar chart plot has the correct attributes."""
        city_dict = {'Summer': 'New York', 'Alice': 'London', 'April': 'Beijing', 'Charlie': 'Tokyo', 'David': 'Sydney'}
        population_dict, ax = f_315(city_dict, seed=54)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), 'City Populations')
        self.assertEqual(ax.get_xlabel(), 'City')
        self.assertEqual(ax.get_ylabel(), 'Population')
        self.assertEqual(population_dict, {'New York': 72816, 'London': 367942, 'Beijing': 869251, 'Tokyo': 323344, 'Sydney': 267288})

        bars = [rect for rect in ax.get_children() if isinstance(rect, plt.Rectangle) and rect.get_width() > 0]
        bars = [bar for bar in bars if bar.get_xy()[0] != 0]  # Exclude the non-data bar
        self.assertEqual(len(bars), 5)

    def test_case_3(self):
        """Test the function with an empty input dictionary."""
        city_dict = {}
        population_dict, _ = f_315(city_dict)

        self.assertSetEqual(set(population_dict.keys()), set({}))
        self.assertTrue(all(1000000 <= pop <= 10000000 for pop in population_dict.values()))

    def test_case_4(self):
        """Test the function with a differently structured input dictionary."""
        city_dict = {'Person1': 'City1', 'Person2': 'City2'}
        population_dict, _ = f_315(city_dict)
        self.assertEqual(population_dict, {'City1': -1, 'City2': -1})

    def test_case_5(self):
        """Test if the population values are random with the same input and different seeds."""
        city_dict = {'John': 'New York', 'Alice': 'London'}
        population_dict1, _ = f_315(city_dict, seed=77)
        population_dict2, _ = f_315(city_dict, seed=42)
        self.assertNotEqual(population_dict1, population_dict2)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
