import pandas as pd
from collections import Counter

def f_744(d):
    """
    Count the occurrence of values with the keys "x," "y" and "z" from a list of dictionaries "d."

    Parameters:
    d (list): A list of dictionaries.

    Returns:
    dict: A dictionary with keys as 'x', 'y', and 'z' and values as Counter objects.

    Requirements:
    - pandas
    - collections.Counter

    Example:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 5}, {'x': 2, 'y': 1, 'z': 7}]
    >>> print(f_744(data))
    {'x': Counter({1: 1, 3: 1, 2: 1}), 'y': Counter({10: 1, 15: 1, 1: 1}), 'z': Counter({5: 2, 7: 1})}
    >>> data = [{'x': 2, 'y': 10}, {'y': 15, 'z': 5}, {'x': 2, 'z': 7}]
    >>> print(f_744(data))
    {'x': Counter({2.0: 2}), 'y': Counter({10.0: 1, 15.0: 1}), 'z': Counter({5.0: 1, 7.0: 1})}
    """
    df = pd.DataFrame(d)
    counts = {}

    for key in ['x', 'y', 'z']:
        if key in df.columns:
            counts[key] = Counter(df[key].dropna().tolist())
        else:
            counts[key] = Counter()

    return counts

import unittest

class TestCases(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(f_744([]), {'x': Counter(), 'y': Counter(), 'z': Counter()})

    def test_all_keys_present(self):
        data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 3, 'z': 2}]
        expected = {'x': Counter({1: 2}), 'y': Counter({2: 1, 3: 1}), 'z': Counter({3: 1, 2: 1})}
        self.assertEqual(f_744(data), expected)

    def test_missing_keys(self):
        data = [{'x': 1}, {'y': 2}, {'z': 3}]
        expected = {'x': Counter({1: 1}), 'y': Counter({2: 1}), 'z': Counter({3: 1})}
        self.assertEqual(f_744(data), expected)

    def test_duplicate_values(self):
        data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 2}]
        expected = {'x': Counter({1: 3}), 'y': Counter({2: 3}), 'z': Counter({3: 2})}
        self.assertEqual(f_744(data), expected)

    def test_mixed_data_types(self):
        data = [{'x': 1, 'y': 'a', 'z': 3.5}, {'x': '1', 'y': 'a', 'z': 3.5}]
        expected = {'x': Counter({1: 1, '1': 1}), 'y': Counter({'a': 2}), 'z': Counter({3.5: 2})}
        self.assertEqual(f_744(data), expected)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    unittest.main()
