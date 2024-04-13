import numpy as np
import pandas as pd
import collections
import matplotlib.pyplot as plt

# Constants
COUNTRIES = ['USA', 'Canada', 'UK', 'Germany', 'France', 'Australia']

def f_196(population_data):
    """
    Analyze a list of population data and return summary statistics and a pie chart of populations by country.

    Parameters:
    - population_data (list): A list of dictionaries where each dictionary represents population data for a country, e.g., [{'country': 'USA', 'population': 331002651}, {'country': 'UK', 'population': 67886011}]

    Returns:
    - dict: A dictionary with summary statistics (mean, median, mode) for the population data. Each key of the dictionary represents a product and the associated value is a dictionary with the keys 'mean', 'median' and 'mode'.
    - matplotlib.figure.Figure: A pie chart of populations by country.

    Requirements:
    - numpy
    - pandas
    - collections
    - matplotlib.pyplot

    Example:
    >>> population_data = [{'country': 'USA', 'population': 331002651}, {'country': 'UK', 'population': 67886011}]
    >>> stats, fig = f_196(population_data)
    >>> print(stats)
    >>> fig.show()
    """
    populations = collections.defaultdict(list)
    for data in population_data:
        populations[data['country']].append(data['population'])

    summary_stats = {}
    for country in populations:
        population_array = np.array(populations[country])
        summary_stats[country] = {
            'mean': np.mean(population_array),
            'median': np.median(population_array),
            'mode': collections.Counter(population_array).most_common(1)[0][0]
        }

    population_df = pd.DataFrame(population_data).set_index("country")
    fig = population_df['population'].plot.pie(autopct='%1.1f%%')
    fig.legend()
    plt.show()
    return summary_stats, fig

import unittest

class TestCases(unittest.TestCase):
    def test_case_1(self):
        """
        Test normal operation with valid input
        """
        population_data = [{'country': 'USA', 'population': 331002651}, {'country': 'UK', 'population': 67886011}]
        stats, ax = f_196(population_data)
        self.assertEqual(stats['USA']['mean'], 331002651.0)
        self.assertEqual(stats['UK']['mean'], 67886011.0)
        self.assertTrue('USA' in ax.get_legend().get_texts()[0].get_text())
        self.assertTrue('UK' in ax.get_legend().get_texts()[1].get_text())

    def test_case_2(self):
        """
        Test normal operation with valid input
        """
        population_data = [{'country': 'USA', 'population': 331002651}, {'country': 'Canada', 'population': 37664517}]
        stats, ax = f_196(population_data)
        self.assertEqual(stats['USA']['mean'], 331002651.0)
        self.assertEqual(stats['Canada']['mean'], 37664517.0)
        self.assertTrue('USA' in ax.get_legend().get_texts()[0].get_text())
        self.assertTrue('Canada' in ax.get_legend().get_texts()[1].get_text())

    def test_case_3(self):
        """
        Test normal operation with valid input
        """
        population_data = [{'country': 'Germany', 'population': 83166711}, {'country': 'France', 'population': 65273511}]
        stats, ax = f_196(population_data)
        self.assertEqual(stats['Germany']['mean'], 83166711.0)
        self.assertEqual(stats['France']['mean'], 65273511.0)
        self.assertTrue('Germany' in ax.get_legend().get_texts()[0].get_text())
        self.assertTrue('France' in ax.get_legend().get_texts()[1].get_text())

    def test_case_4(self):
        """
        Test normal operation with valid input
        """
        population_data = [{'country': 'Australia', 'population': 25499884}, {'country': 'UK', 'population': 67886011}]
        stats, ax = f_196(population_data)
        self.assertEqual(stats['Australia']['mean'], 25499884.0)
        self.assertEqual(stats['UK']['mean'], 67886011.0)
        self.assertTrue('Australia' in ax.get_legend().get_texts()[0].get_text())
        self.assertTrue('UK' in ax.get_legend().get_texts()[1].get_text())

    def test_case_5(self):
        """
        Test normal operation with valid input
        """
        population_data = [{'country': 'Canada', 'population': 37664517}, {'country': 'France', 'population': 65273511}]
        stats, ax = f_196(population_data)
        self.assertEqual(stats['Canada']['mean'], 37664517.0)
        self.assertEqual(stats['France']['mean'], 65273511.0)
        self.assertTrue('Canada' in ax.get_legend().get_texts()[0].get_text())
        self.assertTrue('France' in ax.get_legend().get_texts()[1].get_text())

    def test_case_6(self):
        """
        Test pie chart with valid input
        """
        population_data = [{'country': 'USA', 'population': 40000000}, {'country': 'UK', 'population': 10000000}]
        stats, ax = f_196(population_data)
        self.assertEqual(stats['USA']['mean'], 40000000)
        self.assertEqual(stats['UK']['mean'], 10000000)
        extracted_labels = [text.get_text() for text in ax.texts if "%" not in text.get_text()]
        expected_labels = ["USA", "UK"]
        extracted_sizes = [float(text.get_text().rstrip("%")) for text in ax.texts if "%" in text.get_text()]
        expected_sizes = [80.0, 20.0]
        self.assertListEqual(extracted_labels, expected_labels)
        self.assertListEqual(extracted_sizes, expected_sizes)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()