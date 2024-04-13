import matplotlib.pyplot as plt
import itertools
import numpy as np

# Constants
COLORS = ['r', 'g', 'b', 'y', 'm', 'c', 'k']
MARKERS = ['o', 's', '*', '+', 'x', 'D', '|', '_']

def f_181(T1):
    """
    This function takes as input T1 which is a tuple of tuples. Each tuple in T1 contains strings that can be converted into integers. For each tuple, you should draw a scatter plot with random x and y values.
    The number of point is each plot should be equal to the sum of the integers in the corresponding tuple.
    
    Steps:
    0. Create an empty that will contain all the scatter plots generated.
    1. Go through the list of tuple
    2. For each tuple, convert its element to integer and compute their sum.
    3. Create 2 random arrays with the same length equal to the sum computed above.
    4. Create a scatter plot with the array built previously.
        - The title is 'Graph' followed by the index of the tuple (starting from 1) e.g. 'Graph 1' for the first tuple, 'Graph 2' for the second tuple etc.
        - The color and marker of the scatter plot should be derived by taking the elements at the right index in the constants COLORS and MARKERS.
        - Append the current plot to the list of scatter plots.
    5. Return the list of scatter plots
    
    Parameters:
    T1 (tuple): A tuple of tuples, each containing string representations of integers.
    
    Returns:
    list of AxesSubplot: List of scatter plots generated for each tuple in 'T1'.
    
    Requirements:
    - matplotlib.pyplot
    - itertools
    - numpy
    
    Example:
    >>> T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
    >>> plots = f_181(T1)
    """
    color_marker = list(itertools.product(COLORS, MARKERS))
    plots = []

    for i, tup in enumerate(T1):
        int_list = list(map(int, tup))
        total_points = sum(int_list)

        x = np.random.rand(total_points)
        y = np.random.rand(total_points)
        color, marker = color_marker[i % len(color_marker)]
        
        fig, ax = plt.subplots()
        ax.scatter(x, y, color=color, marker=marker)
        ax.set_title(f'Graph {i+1}')
        plots.append(ax)
    
    return plots

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_181 function."""
    def test_case_1(self):
        T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
        plots = f_181(T1)
        self.assertEqual(len(plots), 3)  # Check if 3 plots are generated
        for i, ax in enumerate(plots):
            self.assertEqual(ax.get_title(), f"Graph {i+1}")  # Check the title of each plot
            self.assertEqual(len(ax.collections[0].get_offsets()), sum(map(int, T1[i])))  # Check the number of points in each plot

    def test_case_2(self):
        T1 = (('5', '7'), ('2', '3', '4'))
        plots = f_181(T1)
        self.assertEqual(len(plots), 2)
        for i, ax in enumerate(plots):
            self.assertEqual(ax.get_title(), f"Graph {i+1}")
            self.assertEqual(len(ax.collections[0].get_offsets()), sum(map(int, T1[i])))

    def test_case_3(self):
        T1 = (('1', '1', '1', '1'),)
        plots = f_181(T1)
        self.assertEqual(len(plots), 1)
        for i, ax in enumerate(plots):
            self.assertEqual(ax.get_title(), f"Graph {i+1}")
            self.assertEqual(len(ax.collections[0].get_offsets()), sum(map(int, T1[i])))
    
    def test_case_4(self):
        T1 = (('10',), ('5', '5'), ('2', '3', '5'))
        plots = f_181(T1)
        self.assertEqual(len(plots), 3)
        for i, ax in enumerate(plots):
            self.assertEqual(ax.get_title(), f"Graph {i+1}")
            self.assertEqual(len(ax.collections[0].get_offsets()), sum(map(int, T1[i])))
    
    def test_case_5(self):
        T1 = (('3', '2'), ('5',), ('1', '1', '1', '2'))
        plots = f_181(T1)
        self.assertEqual(len(plots), 3)
        for i, ax in enumerate(plots):
            self.assertEqual(ax.get_title(), f"Graph {i+1}")
            self.assertEqual(len(ax.collections[0].get_offsets()), sum(map(int, T1[i])))

if __name__ == "__main__" :
    run_tests()