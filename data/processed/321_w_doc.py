import pandas as pd
import re
from scipy import stats


def task_func(text):
    """
    Extracts all names from a given text string that are not surrounded by square brackets 
    and counts the frequency of each extracted name. It then creates a bar chart of the name frequencies and
    returns the name frequencies as a pandas Series and the bar chart plot's axes object along with the skewness 
    and kurtosis of the name frequencies. If the skewness and kurtosis are nan, they are returned as None.
    
    Parameters:
    text (str): The text from which to extract names. Each name should be separated by square brackets containing addresses.
    
    Returns:
    tuple: A tuple containing:
        - pd.Series: A pandas Series with the frequency of each name.
        - Axes: A bar chart plot showing the name frequencies. If no names are found, this will be None.
        - float: The skewness of the name frequencies.
        - float: The kurtosis of the name frequencies.
    
    Requirements:
    - re
    - pandas
    - matplotlib.pyplot
    - scipy.stats
    
    Example:
    >>> text_input = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
    >>> name_freqs, plot, skew, kurtosis = task_func(text_input)
    >>> print(list(name_freqs.items())[0])
    ('Josie Smith', 1)
    >>> type(plot)
    <class 'matplotlib.axes._axes.Axes'>
    >>> round(kurtosis, 2) is not None
    True
    """

    names = re.findall(r'(.*?)(?:\[.*?\]|$)', text)
    names = [name.strip() for name in names if name.strip()]  # Removing any empty or whitespace names
    name_freqs = pd.Series(names).value_counts()
    if not name_freqs.empty:
        ax = name_freqs.plot(kind='bar', title="Name Frequencies")
        skewness = stats.skew(name_freqs)
        kurtosis = stats.kurtosis(name_freqs)
    else:
        ax = skewness = kurtosis = None
    if skewness == float('nan'):
        skewness = None
    if kurtosis == float('nan'):
        kurtosis = None
    return name_freqs, ax, skewness, kurtosis

import unittest
import doctest
test_data = [
    # Test Case 1: Basic names separated by addresses in square brackets
    "John Doe [123 MAIN ST, TOWN, ST 12345]Jane Smith [456 OTHER ST, CITY, ST 67890]",
    
    # Test Case 2: Multiple occurrences of the same name
    "Alice [111 ALPHA ST, PLACE, ST 11111]Bob [222 BETA ST, LOCATION, ST 22222]Alice [333 GAMMA ST, REGION, ST 33333]",
    
    # Test Case 3: Names with special characters and different patterns
    "Mr. X [444 X ST, XPLACE, ST 44444]Dr. Y [555 Y ST, YCITY, ST 55555]Z [666 Z ST, ZTOWN, ST 66666]",
    
    # Test Case 4: Empty string
    "",
    
    # Test Case 5: Only addresses without names
    "[777 FIRST ST, APLACE, ST 77777][888 SECOND ST, BCITY, ST 88888][999 THIRD ST, CTOWN, ST 99999]",
    # Long test case with multiple names and addresses
    "John Doe [123 MAIN ST, TOWN, ST 12345]Jane Smith [456 OTHER ST, CITY, ST 67890]Alice [111 ALPHA ST, PLACE, ST 11111]Bob [222 BETA ST, LOCATION, ST 22222]Alice [333 GAMMA ST, REGION, ST 33333]Mr. X [444 X ST, XPLACE, ST 44444]Dr. Y [555 Y ST, YCITY, ST 55555]Z [666 Z ST, ZTOWN, ST 66666]"
]
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test Case 1: Basic names separated by addresses in square brackets
        input_text = test_data[0]
        name_freqs, plot, _, _ = task_func(input_text)
        self.assertEqual(name_freqs["John Doe"], 1)
        self.assertEqual(name_freqs["Jane Smith"], 1)
        self.assertTrue("Name Frequencies" in plot.get_title())
    
    def test_case_2(self):
        # Test Case 2: Multiple occurrences of the same name
        input_text = test_data[1]
        name_freqs, plot, _, _ = task_func(input_text)
        self.assertEqual(name_freqs["Alice"], 2)
        self.assertEqual(name_freqs["Bob"], 1)
    
    def test_case_3(self):
        # Test Case 3: Names with special characters and different patterns
        input_text = test_data[2]
        name_freqs, plot, _, _ = task_func(input_text)
        self.assertEqual(name_freqs["Mr. X"], 1)
        self.assertEqual(name_freqs["Dr. Y"], 1)
        self.assertEqual(name_freqs["Z"], 1)
    
    def test_case_4(self):
        # Test Case 4: Empty string
        input_text = test_data[3]
        name_freqs, plot, _, _ = task_func(input_text)
        self.assertTrue(name_freqs.empty)
    
    def test_case_5(self):
        # Test Case 5: Only addresses without names
        input_text = test_data[4]
        name_freqs, plot, _, _ = task_func(input_text)
        print(name_freqs)
        self.assertTrue(name_freqs.empty)
        # Long test case with multiple names and addresses
        input_text = test_data[5]
        name_freqs, plot, skewness, kurtosis = task_func(input_text)
        self.assertEqual(name_freqs["John Doe"], 1)
        # Test for skewness and kurtosis
        self.assertAlmostEqual(skewness, 2.04, places=2)
        self.assertAlmostEqual(kurtosis, 2.17, places=2)
